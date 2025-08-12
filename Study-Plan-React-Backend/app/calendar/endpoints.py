"""
Enhanced Calendar Endpoints for Study Plan Generation
Supports calendar-based planning with monthly analysis and PYQ/DPP scheduling
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, List, Optional
from datetime import date
from app.calendar.tools import (
    generate_calendar_based_study_plan,
    get_monthly_analysis_summary
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

@enhanced_calendar_router.get("/status")
async def calendar_status():
    """Get calendar module status"""
    return {
        "status": "active",
        "message": "Calendar module is running. Some enhanced features are temporarily disabled during cleanup.",
        "available_endpoints": [
            "/generate-calendar-plan",
            "/monthly-analysis"
        ],
        "disabled_endpoints": [
            "/calculate-monthly-targets",
            "/extended-months-plan", 
            "/weekend-schedule",
            "/weekly-topic-breakdown"
        ]
    }

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

# Note: Additional enhanced endpoints are temporarily disabled during cleanup
# They require functions that were removed and need to be reimplemented:
# - /calculate-monthly-targets
# - /extended-months-plan
# - /weekend-schedule  
# - /weekly-topic-breakdown