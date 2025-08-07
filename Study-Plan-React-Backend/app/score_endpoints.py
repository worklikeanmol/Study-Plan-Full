from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, List, Optional
from app.score_oriented_tools import (
    validate_exam_date,
    calculate_target_score_progress,
    get_weightage_optimized_chapter_sequence,
    save_score_progress,
)
from app.utils import get_logger

logger = get_logger(__name__)

# Create router for score-oriented endpoints
score_router = APIRouter(prefix="/score", tags=["score-oriented"])

class ExamDateValidationRequest(BaseModel):
    exam_date: str

class ScoreProgressRequest(BaseModel):
    user_id: str
    exam: str
    target_score: int
    completed_chapters: Dict[str, List[str]]

class OptimizedSequenceRequest(BaseModel):
    exam: str
    target_score: int
    available_months: int

@score_router.post("/validate-exam-date")
async def validate_exam_date_endpoint(request: ExamDateValidationRequest):
    """Validate if exam date is at least 5 months from today"""
    try:
        result = validate_exam_date.invoke({"exam_date": request.exam_date})
        return result
    except Exception as e:
        logger.error(f"Error validating exam date: {e}")
        raise HTTPException(status_code=400, detail=str(e))

@score_router.post("/calculate-progress")
async def calculate_score_progress_endpoint(request: ScoreProgressRequest):
    """Calculate current score progress based on completed chapters"""
    try:
        result = calculate_target_score_progress.invoke({
            "exam": request.exam,
            "target_score": request.target_score,
            "completed_chapters": request.completed_chapters
        })
        
        # Save progress to database
        if not result.get("error"):
            save_result = save_score_progress.invoke({
                "user_id": request.user_id,
                "progress_data": result
            })
            result["save_status"] = save_result
        
        return result
    except Exception as e:
        logger.error(f"Error calculating score progress: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@score_router.post("/optimized-sequence")
async def get_optimized_sequence_endpoint(request: OptimizedSequenceRequest):
    """Get weightage-optimized chapter sequence for score-oriented plans"""
    try:
        result = get_weightage_optimized_chapter_sequence.invoke({
            "exam": request.exam,
            "target_score": request.target_score,
            "available_months": request.available_months
        })
        return result
    except Exception as e:
        logger.error(f"Error generating optimized sequence: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@score_router.get("/progress/{user_id}")
async def get_user_score_progress(user_id: str):
    """Get saved score progress for a user"""
    try:
        from app.tools import supabase
        
        if not supabase:
            raise HTTPException(status_code=503, detail="Database not available")
        
        response = supabase.table("Score_Progress").select("*").eq("user_id", user_id).execute()
        
        if response.data:
            return {
                "found": True,
                "progress_data": response.data[0]
            }
        else:
            return {
                "found": False,
                "message": "No score progress found for user"
            }
            
    except Exception as e:
        logger.error(f"Error retrieving score progress: {e}")
        raise HTTPException(status_code=500, detail=str(e))