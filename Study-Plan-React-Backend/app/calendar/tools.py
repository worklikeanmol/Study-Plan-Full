"""
Enhanced Calendar Tools for Study Plan Generation
Features:
1. Calendar-based study plan starting from today
2. Monthly analysis with total_achievable_score and user_target
3. PYQ/DPP scheduling with proper tags
4. Weekend PYQ focus and daily DPP integration
"""

from langchain_core.tools import tool
from typing import Dict, List, Optional
from datetime import datetime, timedelta, date
# Note: These functions were moved from enhanced_new_score_oriented_tools during cleanup
# They should be implemented directly in this module or imported from appropriate location
# from app.enhanced_new_score_oriented_tools import (
#     calculate_monthly_target_scores,
#     generate_extended_months_plan,
#     create_comprehensive_weekend_schedule
# )
from app.core.tools import supabase
from app.core.utils import get_logger
import calendar

logger = get_logger(__name__)

@tool
def generate_calendar_based_study_plan(
    exam: str, 
    user_target_score: int, 
    total_months: int,
    start_date: Optional[str] = None,
    monthly_chapters: Optional[Dict[str, Dict[str, List[str]]]] = None
) -> Dict:
    """
    Generate a complete calendar-based study plan starting from today (or specified date).
    
    Args:
        exam: Target exam name
        user_target_score: User's target score out of 300
        total_months: Total months available for preparation
        start_date: Start date (YYYY-MM-DD format), defaults to today
        monthly_chapters: Pre-defined monthly chapter distribution
        
    Returns:
        Complete calendar-based study plan with monthly analysis
    """
    try:
        # Set start date
        if start_date:
            start_dt = datetime.strptime(start_date, "%Y-%m-%d").date()
        else:
            start_dt = date.today()
        
        logger.info(f"Generating calendar-based study plan starting from {start_dt}")
        
        # Generate monthly chapters if not provided
        if not monthly_chapters:
            monthly_chapters = generate_default_monthly_chapters(exam, total_months)
        
        # Calculate monthly targets using existing tool
        monthly_targets = calculate_monthly_target_scores.invoke({
            "exam": exam,
            "user_target_score": user_target_score,
            "monthly_chapters": monthly_chapters
        })
        
        # Generate calendar structure
        calendar_plan = {}
        current_date = start_dt
        
        for month_num in range(1, total_months + 1):
            month_key = f"month_{month_num}"
            
            # Calculate month boundaries
            month_start = current_date
            days_in_month = 30  # Approximate for planning
            month_end = month_start + timedelta(days=days_in_month - 1)
            
            # Get monthly target data
            month_target_data = monthly_targets.get("monthly_targets", {}).get(month_key, {})
            
            # Generate daily schedule for the month
            daily_schedule = generate_monthly_daily_schedule.invoke({
                "month_start": month_start.strftime("%Y-%m-%d"),
                "month_end": month_end.strftime("%Y-%m-%d"),
                "month_num": month_num,
                "total_months": total_months,
                "subjects_chapters": monthly_chapters.get(month_key, {}),
                "exam": exam
            })
            
            calendar_plan[month_key] = {
                "month_number": month_num,
                "month_name": month_start.strftime("%B %Y"),
                "start_date": month_start.strftime("%Y-%m-%d"),
                "end_date": month_end.strftime("%Y-%m-%d"),
                "total_days": days_in_month,
                "study_days": calculate_study_days(month_start, month_end),
                
                # Monthly Analysis Data
                "monthly_analysis": {
                    "total_achievable_score": month_target_data.get("total_achievable_score", 0),
                    "user_target_score": month_target_data.get("user_target_score", 0),
                    "efficiency_required": month_target_data.get("efficiency_required", 0),
                    "subject_breakdown": month_target_data.get("subject_breakdown", {}),
                    "target_ratio": month_target_data.get("target_ratio", 0)
                },
                
                # Daily Schedule
                "daily_schedule": daily_schedule,
                
                # Weekly Pattern
                "weekly_pattern": generate_weekly_pattern(month_num, total_months),
                
                # Tags and Focus
                "tags": generate_month_tags(month_num, total_months),
                "primary_focus": determine_month_focus(month_num, total_months)
            }
            
            # Move to next month
            current_date = month_end + timedelta(days=1)
        
        # Generate overall summary
        overall_summary = generate_overall_calendar_summary(
            calendar_plan=calendar_plan,
            monthly_targets=monthly_targets,
            start_date=start_dt,
            total_months=total_months
        )
        
        result = {
            "status": "success",
            "plan_type": "calendar_based",
            "start_date": start_dt.strftime("%Y-%m-%d"),
            "end_date": (start_dt + timedelta(days=total_months * 30)).strftime("%Y-%m-%d"),
            "total_months": total_months,
            "user_target_score": user_target_score,
            "exam": exam,
            "calendar_plan": calendar_plan,
            "overall_summary": overall_summary,
            "monthly_targets_data": monthly_targets
        }
        
        logger.info(f"Calendar-based study plan generated successfully for {total_months} months")
        return result
        
    except Exception as e:
        logger.error(f"Error generating calendar-based study plan: {e}")
        return {
            "status": "error",
            "error": str(e),
            "calendar_plan": {}
        }

@tool
def generate_monthly_daily_schedule(
    month_start: str,
    month_end: str,
    month_num: int,
    total_months: int,
    subjects_chapters: Dict[str, List[str]],
    exam: str
) -> Dict:
    """Generate daily schedule for a specific month"""
    try:
        # Convert string dates to date objects
        start_date = datetime.strptime(month_start, "%Y-%m-%d").date()
        end_date = datetime.strptime(month_end, "%Y-%m-%d").date()
        
        daily_schedule = {}
        current_date = start_date
        
        while current_date <= end_date:
            day_name = current_date.strftime("%A")
            day_key = current_date.strftime("%Y-%m-%d")
            
            if day_name in ["Saturday", "Sunday"]:
                # Weekend: PYQ Focus
                daily_schedule[day_key] = {
                    "date": day_key,
                    "day_name": day_name,
                    "type": "PYQ_PRACTICE",
                    "tag": "PYQ",
                    "primary_activity": "Previous Year Questions Practice",
                    "subjects": ["Physics", "Chemistry", "Mathematics"],
                    "duration_hours": 8,
                    "target_questions": 60 if month_num > 6 else 40,
                    "analysis_time": 2,
                    "schedule": {
                        "morning": "Physics PYQ (2.5 hours)",
                        "afternoon": "Chemistry PYQ (2.5 hours)", 
                        "evening": "Mathematics PYQ (2.5 hours)",
                        "night": "Analysis & Review (0.5 hours)"
                    }
                }
            else:
                # Weekday: Chapter Study + DPP
                subject_for_day = get_subject_for_weekday(day_name, subjects_chapters)
                
                daily_schedule[day_key] = {
                    "date": day_key,
                    "day_name": day_name,
                    "type": "STUDY_DPP",
                    "tag": "DPP",
                    "primary_activity": "Chapter Study + Daily Practice Paper",
                    "subject": subject_for_day,
                    "duration_hours": 6,
                    "schedule": {
                        "morning": f"{subject_for_day} Chapter Study (3 hours)",
                        "afternoon": f"{subject_for_day} DPP Practice (2 hours)",
                        "evening": "Review & Analysis (1 hour)"
                    },
                    "dpp_details": {
                        "subject": subject_for_day,
                        "target_questions": 25,
                        "difficulty_level": "mixed",
                        "time_limit": "2 hours"
                    }
                }
            
            current_date += timedelta(days=1)
        
        return daily_schedule
        
    except Exception as e:
        logger.error(f"Error generating daily schedule: {e}")
        return {}

@tool
def get_monthly_analysis_summary(exam: str, user_target_score: int, monthly_chapters: Dict) -> Dict:
    """
    Get detailed monthly analysis with achievable scores and targets for each month.
    """
    try:
        logger.info(f"Generating monthly analysis summary for {user_target_score} target score")
        
        # Calculate monthly targets
        monthly_targets = calculate_monthly_target_scores.invoke({
            "exam": exam,
            "user_target_score": user_target_score,
            "monthly_chapters": monthly_chapters
        })
        
        # Extract monthly analysis data
        monthly_analysis = {}
        total_achievable = 0
        total_user_target = 0
        
        for month_key, month_data in monthly_targets.get("monthly_targets", {}).items():
            achievable = month_data.get("total_achievable_score", 0)
            target = month_data.get("user_target_score", 0)
            
            total_achievable += achievable
            total_user_target += target
            
            monthly_analysis[month_key] = {
                "month_number": int(month_key.split("_")[1]),
                "total_achievable_score": round(achievable, 2),
                "user_target_score": round(target, 2),
                "efficiency_required": round((target / achievable * 100) if achievable > 0 else 0, 1),
                "subject_breakdown": month_data.get("subject_breakdown", {}),
                "target_ratio": round((target / user_target_score * 100) if user_target_score > 0 else 0, 1),
                "cumulative_achievable": round(total_achievable, 2),
                "cumulative_target": round(total_user_target, 2)
            }
        
        result = {
            "status": "success",
            "exam": exam,
            "user_target_score": user_target_score,
            "monthly_analysis": monthly_analysis,
            "overall_summary": {
                "total_achievable_score": round(total_achievable, 2),
                "total_user_target": round(total_user_target, 2),
                "overall_efficiency_required": round((total_user_target / total_achievable * 100) if total_achievable > 0 else 0, 1),
                "target_achievability": total_achievable >= user_target_score,
                "score_gap": max(0, user_target_score - total_achievable)
            }
        }
        
        logger.info(f"Monthly analysis completed: {len(monthly_analysis)} months analyzed")
        return result
        
    except Exception as e:
        logger.error(f"Error generating monthly analysis: {e}")
        return {
            "status": "error",
            "error": str(e),
            "monthly_analysis": {}
        }

# Helper functions

def generate_default_monthly_chapters(exam: str, total_months: int) -> Dict:
    """Generate default monthly chapter distribution"""
    # This is a simplified version - in practice, you'd use your existing chapter distribution logic
    subjects = ["Physics", "Chemistry", "Mathematics"]
    chapters_per_subject = 12  # Approximate
    
    monthly_chapters = {}
    
    for month_num in range(1, min(total_months + 1, 7)):  # First 6 months for syllabus
        month_key = f"month_{month_num}"
        monthly_chapters[month_key] = {}
        
        for subject in subjects:
            # Distribute chapters across months
            start_chapter = ((month_num - 1) * 2) + 1
            end_chapter = min(start_chapter + 2, chapters_per_subject + 1)
            
            chapters = [f"Chapter_{i}" for i in range(start_chapter, end_chapter)]
            monthly_chapters[month_key][subject] = chapters
    
    return monthly_chapters

def calculate_study_days(start_date: date, end_date: date) -> Dict:
    """Calculate study days breakdown for a month"""
    total_days = (end_date - start_date).days + 1
    weekdays = 0
    weekends = 0
    
    current = start_date
    while current <= end_date:
        if current.weekday() < 5:  # Monday = 0, Friday = 4
            weekdays += 1
        else:
            weekends += 1
        current += timedelta(days=1)
    
    return {
        "total_days": total_days,
        "weekdays": weekdays,
        "weekends": weekends,
        "study_days": weekdays,
        "practice_days": weekends
    }

def generate_weekly_pattern(month_num: int, total_months: int) -> Dict:
    """Generate weekly pattern for a month"""
    if month_num <= 6:
        return {
            "monday": {"type": "study", "subject": "Physics", "activity": "Chapter Study + DPP"},
            "tuesday": {"type": "study", "subject": "Chemistry", "activity": "Chapter Study + DPP"},
            "wednesday": {"type": "study", "subject": "Mathematics", "activity": "Chapter Study + DPP"},
            "thursday": {"type": "study", "subject": "Physics", "activity": "Chapter Study + DPP"},
            "friday": {"type": "study", "subject": "Chemistry", "activity": "Chapter Study + DPP"},
            "saturday": {"type": "practice", "activity": "PYQ Practice - All Subjects"},
            "sunday": {"type": "practice", "activity": "PYQ Practice - All Subjects"}
        }
    else:
        return {
            "monday": {"type": "practice", "subject": "Physics", "activity": "Intensive DPP"},
            "tuesday": {"type": "practice", "subject": "Chemistry", "activity": "Intensive DPP"},
            "wednesday": {"type": "practice", "subject": "Mathematics", "activity": "Intensive DPP"},
            "thursday": {"type": "practice", "subject": "Mixed", "activity": "All Subjects DPP"},
            "friday": {"type": "revision", "activity": "Weak Areas Revision"},
            "saturday": {"type": "practice", "activity": "Full Syllabus PYQ"},
            "sunday": {"type": "practice", "activity": "Mock Tests + Analysis"}
        }

def generate_month_tags(month_num: int, total_months: int) -> List[str]:
    """Generate tags for a month"""
    tags = []
    
    if month_num <= 6:
        tags.extend(["SYLLABUS", "CHAPTER_STUDY", "DPP", "PYQ"])
    else:
        tags.extend(["PRACTICE", "INTENSIVE_DPP", "PYQ", "MOCK_TESTS"])
    
    if month_num == total_months:
        tags.append("FINAL_REVISION")
    
    return tags

def determine_month_focus(month_num: int, total_months: int) -> str:
    """Determine primary focus for a month"""
    if month_num <= 6:
        return "Syllabus Completion with Daily Practice"
    elif month_num <= total_months - 1:
        return "Intensive Practice and PYQ Focus"
    else:
        return "Final Revision and Mock Tests"

def get_subject_for_weekday(day_name: str, subjects_chapters: Dict) -> str:
    """Get subject assignment for weekday"""
    day_to_subject = {
        "Monday": "Physics",
        "Tuesday": "Chemistry", 
        "Wednesday": "Mathematics",
        "Thursday": "Physics",
        "Friday": "Chemistry"
    }
    
    return day_to_subject.get(day_name, "Physics")

def generate_overall_calendar_summary(calendar_plan: Dict, monthly_targets: Dict, start_date: date, total_months: int) -> Dict:
    """Generate overall summary for the calendar plan"""
    total_study_days = sum(month["study_days"]["study_days"] for month in calendar_plan.values())
    total_practice_days = sum(month["study_days"]["practice_days"] for month in calendar_plan.values())
    
    return {
        "plan_duration": f"{total_months} months",
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date": (start_date + timedelta(days=total_months * 30)).strftime("%Y-%m-%d"),
        "total_study_days": total_study_days,
        "total_practice_days": total_practice_days,
        "syllabus_completion_months": min(6, total_months),
        "intensive_practice_months": max(0, total_months - 6),
        "weekend_pyq_sessions": total_practice_days,
        "daily_dpp_sessions": total_study_days,
        "overall_strategy": f"Complete syllabus in {min(6, total_months)} months with daily DPP practice, followed by intensive PYQ practice with weekend focus throughout the preparation."
    }