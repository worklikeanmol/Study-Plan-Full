"""
New Score Oriented Display Module
Handles detailed terminal output for new_score_oriented study plans
"""

from typing import Dict, Any
from datetime import date, timedelta
import json
from app.core.utils import get_logger

logger = get_logger(__name__)

def display_new_score_oriented_plan(study_plan_data: Dict[str, Any]) -> None:
    """
    Display detailed new_score_oriented plan breakdown in terminal
    Shows monthly targets, chapter breakdown, and weekly schedules
    """
    try:
        print("\n" + "="*80)
        print("🎯 NEW SCORE-ORIENTED STUDY PLAN - DETAILED BREAKDOWN")
        print("="*80)
        
        # Extract plan data
        user_target = study_plan_data.get("user_target_score", study_plan_data.get("target_score", 250))
        total_months = study_plan_data.get("total_months", 6)
        syllabus_months = min(study_plan_data.get("syllabus_completion_months", 6), 6)
        
        enhanced_features = study_plan_data.get("enhanced_features", {})
        
        # Also check if data is in new_score_oriented_data
        new_score_data = study_plan_data.get("new_score_oriented_data", {})
        if not enhanced_features and new_score_data:
            enhanced_features = new_score_data.get("enhanced_features", {})
        
        # Calculate dates
        start_date_obj = date.today()
        end_date_obj = start_date_obj + timedelta(days=total_months * 30)
        start_date = start_date_obj.strftime("%Y-%m-%d")
        end_date = end_date_obj.strftime("%Y-%m-%d")
        
        # Calculate study statistics according to documentation
        study_days = syllabus_months * 22  # 22 weekdays per month for syllabus completion
        pyq_days = (syllabus_months * 8) + ((total_months - syllabus_months) * 8)  # Weekend days + extended months
        weekend_sessions = pyq_days
        dpp_sessions = (syllabus_months * 22) * 3  # Each study day * 3 subjects
        
        # Display header info exactly as requested
        print(f"{start_date} to {end_date} | Target: {user_target}/300")
        print(f"\n{total_months}")
        print("Months")
        print(f"{study_days}")
        print("Study Days")
        print(f"{pyq_days}")
        print("PYQ Days")
        print(f"{weekend_sessions}")
        print("Weekend Sessions")
        print(f"{dpp_sessions}")
        print("DPP Sessions")
        
        # Display monthly breakdown
        _display_monthly_breakdown(study_plan_data)
        
        # Display chapter breakdown
        _display_chapter_breakdown(study_plan_data)
        
        # Display weekly breakdown
        _display_weekly_breakdown(study_plan_data)
        
        # Generate and display JSON output
        try:
            json_output = generate_plan_json(study_plan_data)
            print("\n" + "="*80)
            print("📋 JSON OUTPUT:")
            print("="*80)
            print(json.dumps(json_output, indent=2))
        except Exception as json_error:
            print(f"❌ Error generating JSON: {json_error}")
        
        print("\n" + "="*80)
        print("✅ NEW SCORE-ORIENTED PLAN DISPLAY COMPLETE")
        print("="*80 + "\n")
        
    except Exception as e:
        logger.error(f"Error displaying new_score_oriented plan: {e}")
        print(f"❌ Error displaying plan: {e}")

def generate_plan_json(study_plan_data: Dict[str, Any]) -> Dict[str, Any]:
    """Generate JSON output for the new_score_oriented plan"""
    try:
        # Extract plan data
        user_target = study_plan_data.get("user_target_score", study_plan_data.get("target_score", 250))
        total_months = study_plan_data.get("total_months", 6)
        syllabus_months = min(study_plan_data.get("syllabus_completion_months", 6), 6)
        
        # Calculate dates
        start_date_obj = date.today()
        end_date_obj = start_date_obj + timedelta(days=total_months * 30)
        start_date = start_date_obj.strftime("%Y-%m-%d")
        end_date = end_date_obj.strftime("%Y-%m-%d")
        
        # Get enhanced features data - check multiple locations
        enhanced_features = study_plan_data.get("enhanced_features", {})
        
        # Also check in new_score_oriented_data
        new_score_data = study_plan_data.get("new_score_oriented_data", {})
        if not enhanced_features and new_score_data:
            enhanced_features = new_score_data.get("enhanced_features", {})
        
        monthly_targets = enhanced_features.get("monthly_target_scores", {})
        monthly_data = monthly_targets.get("monthly_targets", {})
        monthly_chapters_data = monthly_targets.get("monthly_chapters", {})
        weekly_breakdown = enhanced_features.get("weekly_topic_breakdown", {})
        
        # Build JSON structure
        json_output = {
            "plan_info": {
                "start_date": start_date,
                "end_date": end_date,
                "target_score": f"{user_target}/300",
                "total_months": total_months,
                "syllabus_completion_months": syllabus_months,
                "study_days": syllabus_months * 22,
                "pyq_days": (syllabus_months * 8) + ((total_months - syllabus_months) * 8),
                "weekend_sessions": (syllabus_months * 8) + ((total_months - syllabus_months) * 8),
                "dpp_sessions": (syllabus_months * 22) * 3,
                "Full_month_revision": total_months - syllabus_months
            },
            "monthly_breakdown": {},
            "chapter_breakdown": {},
            "weekly_breakdown": {}
        }
        
        # Add monthly breakdown
        dpp_schedule = ["Morning", "Evening", "Night"]
        for month_num in range(1, syllabus_months + 1):
            month_key = f"month_{month_num}"
            month_info = monthly_data.get(month_key, {})
            
            if month_info:
                # Add DPP schedule to subject breakdown
                subject_breakdown = month_info.get("subject_breakdown", {})
                enhanced_subject_breakdown = {}
                
                for i, (subject, data) in enumerate(subject_breakdown.items()):
                    enhanced_data = data.copy() if isinstance(data, dict) else {}
                    enhanced_data["Dpp"] = dpp_schedule[i % 3]
                    enhanced_subject_breakdown[subject] = enhanced_data
                
                json_output["monthly_breakdown"][f"Month {month_num}"] = {
                    "target_ratio": f"{month_info.get('target_ratio', 0.0):.1f}% of target",
                    "total_achievable_score": month_info.get("total_achievable_score", 0.0),
                    "user_target_score": month_info.get("user_target_score", 0.0),
                    "efficiency_required": f"{month_info.get('efficiency_required', 0.0):.1f}%",
                    "subject_breakdown": enhanced_subject_breakdown
                }
        
        # Add revision months (Month 7 and beyond) if total months > 6
        total_months = study_plan_data.get("total_months", 6)
        if total_months > 6:
            for month_num in range(7, total_months + 1):
                # Calculate PYQ targets based on proximity to exam
                months_remaining = total_months - month_num + 1
                if months_remaining <= 1:
                    pyq_target = 60  # Final month intensive
                elif months_remaining <= 2:
                    pyq_target = 50  # Second last month
                else:
                    pyq_target = 40  # Earlier revision months
                
                json_output["monthly_breakdown"][f"Month {month_num}"] = {
                    "Total_PYQs_in_this_Month": pyq_target
                }
        
        # Add chapter breakdown
        for month_num in range(1, syllabus_months + 1):
            month_key = f"month_{month_num}"
            month_data = monthly_data.get(month_key, {})
            subject_breakdown = month_data.get("subject_breakdown", {})
            
            json_output["chapter_breakdown"][f"month_{month_num}"] = {}
            
            for subject in ["mathematics", "physics", "chemistry"]:
                chapters_list = []
                if subject in subject_breakdown:
                    chapters = subject_breakdown[subject].get("chapters", [])
                    chapters_list = chapters if chapters else []
                
                json_output["chapter_breakdown"][f"month_{month_num}"][subject] = chapters_list
        
        # Add weekly breakdown
        for month_num in range(1, syllabus_months + 1):
            month_key = f"month_{month_num}"
            month_data = monthly_data.get(month_key, {})
            subject_breakdown = month_data.get("subject_breakdown", {})
            
            json_output["weekly_breakdown"][f"month_{month_num}"] = {}
            
            for week_num in range(1, 5):
                # Calculate weekly targets based on month position
                weekly_pyq = 2 if month_num <= 6 else 4
                weekly_dpp = 15 if month_num <= 6 else 20
                
                json_output["weekly_breakdown"][f"month_{month_num}"][f"week {week_num}"] = {
                    "total_pyq": weekly_pyq,
                    "total_dpp": weekly_dpp,
                    "subject_breakdown": {}
                }
                
                for subject in ["mathematics", "physics", "chemistry"]:
                    if subject in subject_breakdown:
                        chapters = subject_breakdown[subject].get("chapters", [])
                        chapter_names = ", ".join(chapters) if chapters else "No chapter assigned"
                        
                        # Get topics from weekly breakdown data organized by chapter
                        chapter_topics_dict = {}
                        total_topic_count = 0
                        
                        # Try to get topics from enhanced features
                        weekly_breakdown_data = enhanced_features.get("weekly_topic_breakdown", {})
                        monthly_topic_data = weekly_breakdown_data.get("monthly_topic_breakdown", {})
                        month_data = monthly_topic_data.get(month_key, {})
                        subject_wise_topics = month_data.get("subject_wise_topics", {})
                        subject_topics = subject_wise_topics.get(subject, {})
                        
                        # Organize topics by chapter
                        for chapter in chapters:
                            chapter_data = subject_topics.get(chapter, {})
                            high_priority = chapter_data.get("high_priority", [])
                            medium_priority = chapter_data.get("medium_priority", [])
                            low_priority = chapter_data.get("low_priority", [])
                            chapter_topics = high_priority + medium_priority + low_priority
                            
                            if chapter_topics:
                                chapter_topics_dict[chapter] = chapter_topics
                                total_topic_count += len(chapter_topics)
                        
                        json_output["weekly_breakdown"][f"month_{month_num}"][f"week {week_num}"]["subject_breakdown"][subject] = {
                            "chapters": chapter_topics_dict,
                            "total_topic_count": total_topic_count
                        }
                    else:
                        json_output["weekly_breakdown"][f"month_{month_num}"][f"week {week_num}"]["subject_breakdown"][subject] = {
                            "chapters": {},
                            "total_topic_count": 0
                        }
        
        return json_output
        
    except Exception as e:
        logger.error(f"Error generating plan JSON: {e}")
        return {"error": f"Failed to generate JSON: {str(e)}"}

def _display_monthly_breakdown(study_plan_data: Dict[str, Any]) -> None:
    """Display monthly target breakdown"""
    print("\n📊 MONTHLY TARGET BREAKDOWN:")
    print("-" * 50)
    
    # Get enhanced features data - check multiple locations
    enhanced_features = study_plan_data.get("enhanced_features", {})
    
    # Also check in new_score_oriented_data
    new_score_data = study_plan_data.get("new_score_oriented_data", {})
    if not enhanced_features and new_score_data:
        enhanced_features = new_score_data.get("enhanced_features", {})
    
    monthly_targets = enhanced_features.get("monthly_target_scores", {})
    monthly_data = monthly_targets.get("monthly_targets", {})
    
    
    # Limit to syllabus completion months (max 6)
    syllabus_months = min(study_plan_data.get("syllabus_completion_months", 6), 6)
    
    for month_num in range(1, syllabus_months + 1):
        month_key = f"month_{month_num}"
        month_info = monthly_data.get(month_key, {})
        
        if month_info:
            # Use real data from enhanced features
            target_ratio = month_info.get("target_ratio", 0.0)
            total_achievable = month_info.get("total_achievable_score", 0.0)
            user_target = month_info.get("user_target_score", 0.0)
            efficiency = month_info.get("efficiency_required", 0.0)
            subject_breakdown = month_info.get("subject_breakdown", {})
            
            if target_ratio > 0 and total_achievable > 0:
                print(f"\nMonth {month_num}")
                print(f"{target_ratio:.1f}% of target")
                print(f"{total_achievable:.1f}")
                print("Total Achievable Score")
                print(f"{user_target:.1f}")
                print("Your Target Score")
                print("Efficiency Required")
                print(f"{efficiency:.1f}%")
                print("Subject Breakdown:")
                
                for subject, score in subject_breakdown.items():
                    print(f"{subject.title()}:")
                    if isinstance(score, dict):
                        print(str(score))
                    elif isinstance(score, (int, float)):
                        print(f"{score:.1f}")
                    else:
                        print(str(score))
            else:
                print(f"\nMonth {month_num}")
                print("❌ No valid monthly target data available for this month")
        else:
            print(f"\nMonth {month_num}")
            print("❌ No monthly target data available for this month")

def _display_chapter_breakdown(study_plan_data: Dict[str, Any]) -> None:
    """Display chapter breakdown by month"""
    # Skip chapter breakdown for new_score_oriented as mentioned in your note
    return
    
    # Get enhanced features data for monthly distribution - check multiple locations
    enhanced_features = study_plan_data.get("enhanced_features", {})
    
    # Also check in new_score_oriented_data
    new_score_data = study_plan_data.get("new_score_oriented_data", {})
    if not enhanced_features and new_score_data:
        enhanced_features = new_score_data.get("enhanced_features", {})
    
    monthly_targets = enhanced_features.get("monthly_target_scores", {})
    monthly_data = monthly_targets.get("monthly_targets", {})
    
    # Extract chapters from monthly_data instead of looking for monthly_chapters
    monthly_chapters_data = {}
    for month_key, month_info in monthly_data.items():
        subject_breakdown = month_info.get("subject_breakdown", {})
        monthly_chapters_data[month_key] = {}
        for subject, data in subject_breakdown.items():
            if isinstance(data, dict) and "chapters" in data:
                monthly_chapters_data[month_key][subject] = data["chapters"]
    
    
    # Limit to syllabus completion months (max 6)
    syllabus_months = min(study_plan_data.get("syllabus_completion_months", 6), 6)
    
    for month_num in range(1, syllabus_months + 1):
        month_key = f"month_{month_num}"
        print(f"\nmonth_{month_num}")
        
        # Get month chapters data
        month_chapters = monthly_chapters_data.get(month_key, {})
        
        # Display each subject's chapters
        for subject in ["mathematics", "physics", "chemistry"]:
            print(f"{subject}")
            print()
            
            subject_chapters = month_chapters.get(subject, [])
            
            if subject_chapters:
                for chapter_name in subject_chapters:
                    print(f"{chapter_name}")
                    print("100%")  # Always 100% for new_score_oriented
            else:
                print("❌ No chapters assigned for this month")

def _display_weekly_breakdown(study_plan_data: Dict[str, Any]) -> None:
    """Display weekly topic breakdown for each month"""
    print("\nWeekly Breakdown")
    print("-" * 50)
    
    # Get weekly breakdown data from enhanced features - check multiple locations
    enhanced_features = study_plan_data.get("enhanced_features", {})
    
    # Also check in new_score_oriented_data
    new_score_data = study_plan_data.get("new_score_oriented_data", {})
    if not enhanced_features and new_score_data:
        enhanced_features = new_score_data.get("enhanced_features", {})
    
    weekly_breakdown = enhanced_features.get("weekly_topic_breakdown", {})
    monthly_topic_breakdown = weekly_breakdown.get("monthly_topic_breakdown", {})
    
    # Limit to syllabus completion months (max 6)
    syllabus_months = min(study_plan_data.get("syllabus_completion_months", 6), 6)
    
    # Display weekly breakdown for each month
    for month_num in range(1, syllabus_months + 1):
        month_key = f"month_{month_num}"
        # Get weekly data from monthly_topic_breakdown
        month_data = monthly_topic_breakdown.get(month_key, {})
        subject_wise_topics = month_data.get("subject_wise_topics", {})
        weekly_schedule = month_data.get("weekly_schedule", {})
        
        if subject_wise_topics:
            print(f"\n--- Month {month_num} Weekly Breakdown ---")
            
            # Display topics for each subject
            for subject in ["mathematics", "physics", "chemistry"]:
                subject_data = subject_wise_topics.get(subject, {})
                
                if subject_data:
                    print(f"\n{subject}")
                    
                    # Display chapters and their topics
                    for chapter, chapter_data in subject_data.items():
                        print(f"{chapter}")
                        
                        # Get topics by priority
                        high_priority = chapter_data.get("high_priority", [])
                        medium_priority = chapter_data.get("medium_priority", [])
                        low_priority = chapter_data.get("low_priority", [])
                        
                        all_topics = high_priority + medium_priority + low_priority
                        
                        for topic in all_topics:
                            print(f"  {topic}")
                        
                        print(f"{len(all_topics)} topic{'s' if len(all_topics) != 1 else ''}")
                else:
                    print(f"\n{subject}")
                    print("❌ No topics assigned")
                    print("0 topics")
        else:
            print(f"\n--- Month {month_num} ---")
            print("❌ No weekly breakdown available for this month")

