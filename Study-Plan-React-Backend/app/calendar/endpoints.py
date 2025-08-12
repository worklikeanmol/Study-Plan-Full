"""
Enhanced Calendar Endpoints for Study Plan Generation
Supports calendar-based planning with monthly analysis and PYQ/DPP scheduling
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, List, Optional
from datetime import date
from app.enhanced_calendar_tools import (
    generate_calendar_based_study_plan,
    get_monthly_analysis_summary
)
from app.enhanced_new_score_oriented_tools import (
    calculate_monthly_target_scores,
    generate_extended_months_plan,
    create_comprehensive_weekend_schedule,
    generate_weekly_topic_breakdown
)
from app.core.utils import get_logger

logger = get_logger(__name__)

# Create router for enhanced calendar endpoints
enhanced_calendar_router = APIRouter(prefix="/enhanced_calendar", tags=["enhanced-calendar"])

class CalendarStudyPlanRequest(BaseModel):
    exam: str
    user_target_score: int
    total_months: int
    start_date: Optional[str] = None  # YYYY-MM-DD format
    monthly_chapters: Optional[Dict[str, Dict[str, List[str]]]] = None

class MonthlyAnalysisRequest(BaseModel):
    exam: str
    user_target_score: int
    monthly_chapters: Dict[str, Dict[str, List[str]]]

class ExtendedPlanRequest(BaseModel):
    total_months: int
    syllabus_completion_months: int = 6

class WeeklyTopicRequest(BaseModel):
    exam: str
    monthly_chapters: Dict[str, Dict[str, List[str]]]

@enhanced_calendar_router.post("/generate-calendar-plan")
async def generate_calendar_study_plan_endpoint(request: CalendarStudyPlanRequest):
    """
    Generate a complete calendar-based study plan starting from today or specified date.
    Includes monthly analysis, daily scheduling, and PYQ/DPP integration.
    """
    try:
        logger.info(f"Generating calendar-based study plan for {request.exam}")
        
        result = generate_calendar_based_study_plan.invoke({
            "exam": request.exam,
            "user_target_score": request.user_target_score,
            "total_months": request.total_months,
            "start_date": request.start_date,
            "monthly_chapters": request.monthly_chapters
        })
        
        if result.get("status") == "error":
            raise HTTPException(status_code=400, detail=result.get("error"))
        
        return result
        
    except Exception as e:
        logger.error(f"Error generating calendar study plan: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@enhanced_calendar_router.post("/monthly-analysis")
async def get_monthly_analysis_endpoint(request: MonthlyAnalysisRequest):
    """
    Get detailed monthly analysis with total_achievable_score and user_target for each month.
    """
    try:
        logger.info(f"Generating monthly analysis for target score: {request.user_target_score}")
        
        result = get_monthly_analysis_summary.invoke({
            "exam": request.exam,
            "user_target_score": request.user_target_score,
            "monthly_chapters": request.monthly_chapters
        })
        
        if result.get("status") == "error":
            raise HTTPException(status_code=400, detail=result.get("error"))
        
        return result
        
    except Exception as e:
        logger.error(f"Error generating monthly analysis: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@enhanced_calendar_router.post("/calculate-monthly-targets")
async def calculate_monthly_targets_endpoint(request: MonthlyAnalysisRequest):
    """
    Calculate monthly target scores based on user's target and chapter weightages.
    """
    try:
        logger.info(f"Calculating monthly targets for {request.exam}")
        
        result = calculate_monthly_target_scores.invoke({
            "exam": request.exam,
            "user_target_score": request.user_target_score,
            "monthly_chapters": request.monthly_chapters
        })
        
        return result
        
    except Exception as e:
        logger.error(f"Error calculating monthly targets: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@enhanced_calendar_router.post("/extended-months-plan")
async def generate_extended_plan_endpoint(request: ExtendedPlanRequest):
    """
    Generate plan for extended months (beyond 6 months) with PYQ/DPP focus.
    """
    try:
        logger.info(f"Generating extended plan for {request.total_months} months")
        
        result = generate_extended_months_plan(
            total_months=request.total_months,
            syllabus_completion_months=request.syllabus_completion_months
        )
        
        return result
        
    except Exception as e:
        logger.error(f"Error generating extended plan: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@enhanced_calendar_router.post("/weekend-schedule")
async def create_weekend_schedule_endpoint(request: ExtendedPlanRequest):
    """
    Create comprehensive weekend schedule with Saturday & Sunday PYQ focus.
    """
    try:
        logger.info(f"Creating weekend schedule for {request.total_months} months")
        
        result = create_comprehensive_weekend_schedule(
            total_months=request.total_months,
            syllabus_completion_months=request.syllabus_completion_months
        )
        
        return result
        
    except Exception as e:
        logger.error(f"Error creating weekend schedule: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@enhanced_calendar_router.post("/weekly-topic-breakdown")
async def generate_weekly_topics_endpoint(request: WeeklyTopicRequest):
    """
    Generate weekly topic-wise breakdown for all months using Topic_Priority table.
    """
    try:
        logger.info(f"Generating weekly topic breakdown for {request.exam}")
        
        result = generate_weekly_topic_breakdown(
            exam=request.exam,
            monthly_chapters=request.monthly_chapters
        )
        
        return result
        
    except Exception as e:
        logger.error(f"Error generating weekly topic breakdown: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@enhanced_calendar_router.get("/current-date")
async def get_current_date():
    """Get current date for calendar planning"""
    try:
        current_date = date.today()
        return {
            "current_date": current_date.strftime("%Y-%m-%d"),
            "formatted_date": current_date.strftime("%B %d, %Y"),
            "day_of_week": current_date.strftime("%A")
        }
    except Exception as e:
        logger.error(f"Error getting current date: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@enhanced_calendar_router.post("/validate-dates")
async def validate_study_dates(start_date: str, total_months: int):
    """Validate study plan dates and calculate end date"""
    try:
        from datetime import datetime, timedelta
        
        # Parse start date
        start_dt = datetime.strptime(start_date, "%Y-%m-%d").date()
        
        # Calculate end date (approximate)
        end_dt = start_dt + timedelta(days=total_months * 30)
        
        # Validate that start date is not in the past
        today = date.today()
        if start_dt < today:
            return {
                "valid": False,
                "error": "Start date cannot be in the past",
                "suggested_start_date": today.strftime("%Y-%m-%d")
            }
        
        return {
            "valid": True,
            "start_date": start_dt.strftime("%Y-%m-%d"),
            "end_date": end_dt.strftime("%Y-%m-%d"),
            "total_days": (end_dt - start_dt).days,
            "formatted_duration": f"{total_months} months ({(end_dt - start_dt).days} days)"
        }
        
    except ValueError as e:
        return {
            "valid": False,
            "error": f"Invalid date format. Use YYYY-MM-DD format. Error: {str(e)}"
        }
    except Exception as e:
        logger.error(f"Error validating dates: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@enhanced_calendar_router.get("/sample-monthly-chapters/{exam}")
async def get_sample_monthly_chapters(exam: str, total_months: int = 6):
    """Get sample monthly chapter distribution for testing"""
    try:
        # Generate sample data for testing
        subjects = ["Physics", "Chemistry", "Mathematics"]
        sample_chapters = {}
        
        for month_num in range(1, total_months + 1):
            month_key = f"month_{month_num}"
            sample_chapters[month_key] = {}
            
            for subject in subjects:
                # Generate sample chapters
                start_chapter = ((month_num - 1) * 2) + 1
                end_chapter = min(start_chapter + 2, 13)  # Max 12 chapters per subject
                
                chapters = [f"Chapter_{i}" for i in range(start_chapter, end_chapter)]
                sample_chapters[month_key][subject] = chapters
        
        return {
            "exam": exam,
            "total_months": total_months,
            "sample_monthly_chapters": sample_chapters,
            "note": "This is sample data for testing. Replace with actual chapter distribution."
        }
        
    except Exception as e:
        logger.error(f"Error generating sample chapters: {e}")
        raise HTTPException(status_code=500, detail=str(e))