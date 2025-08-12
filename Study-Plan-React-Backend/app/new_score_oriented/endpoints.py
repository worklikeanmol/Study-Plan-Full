from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, List, Optional
from app.new_score_oriented.tools import (
    validate_new_score_oriented_exam_date,
    get_chapter_weightage_for_revision,
    get_chapter_flow_with_dependencies,
    get_topic_priority_for_chapter,
    get_complete_syllabus_for_revision,
    save_new_score_oriented_progress,
    validate_syllabus_coverage
)
from app.core.utils import get_logger
# Note: enhanced_score_oriented_json_generator was removed during cleanup
# This import needs to be updated or the functionality moved to this module

logger = get_logger(__name__)

# Create router for new_score_oriented endpoints
new_score_oriented_router = APIRouter(prefix="/new_score_oriented", tags=["new-score-oriented"])

class NewScoreOrientedExamDateValidationRequest(BaseModel):
    exam_date: str

class NewScoreOrientedProgressRequest(BaseModel):
    user_id: str
    exam: str
    target_score: int
    completed_chapters: Dict[str, List[str]]

class RevisionFlowRequest(BaseModel):
    exam: str
    target_score: int
    available_months: int

class SyllabusValidationRequest(BaseModel):
    exam: str
    planned_chapters: Dict[str, List[str]]

@new_score_oriented_router.post("/validate-exam-date")
async def validate_new_score_oriented_exam_date_endpoint(request: NewScoreOrientedExamDateValidationRequest):
    """Validate if exam date is at least 6 months from today for new_score_oriented plans"""
    try:
        result = validate_new_score_oriented_exam_date.invoke({"exam_date": request.exam_date})
        return result
    except Exception as e:
        logger.error(f"Error validating exam date: {e}")
        raise HTTPException(status_code=400, detail=str(e))

@new_score_oriented_router.post("/calculate-progress")
async def calculate_new_score_oriented_progress_endpoint(request: NewScoreOrientedProgressRequest):
    """Calculate current progress for new_score_oriented plan"""
    try:
        # Calculate progress based on completed chapters
        progress_data = {
            "user_id": request.user_id,
            "exam": request.exam,
            "target_score": request.target_score,
            "completed_chapters": request.completed_chapters,
            "completion_percentage": 0.0,
            "expected_score": 0.0
        }
        
        # Get weightage data for progress calculation
        total_weightage = 0
        completed_weightage = 0
        
        for subject, chapters in request.completed_chapters.items():
            subject_weightage = get_chapter_weightage_for_revision.invoke({
                "exam": request.exam,
                "subject": subject
            })
            
            for weightage_item in subject_weightage:
                chapter_weight = weightage_item.get("Average Weightage", 0)
                total_weightage += chapter_weight
                
                if weightage_item.get("Chapter") in chapters:
                    completed_weightage += chapter_weight
        
        if total_weightage > 0:
            progress_data["completion_percentage"] = (completed_weightage / total_weightage) * 100
            progress_data["expected_score"] = completed_weightage
        
        # Save progress
        save_result = save_new_score_oriented_progress.invoke({
            "user_id": request.user_id,
            "progress_data": progress_data
        })
        
        progress_data["save_status"] = save_result
        return progress_data
        
    except Exception as e:
        logger.error(f"Error calculating new_score_oriented progress: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@new_score_oriented_router.post("/revision-flow")
async def get_revision_flow_endpoint(request: RevisionFlowRequest):
    """Get revision flow data for new_score_oriented plans"""
    try:
        # Get chapter weightage and flow data
        subjects = ["Physics", "Chemistry", "Mathematics"]
        revision_flow_data = {
            "exam": request.exam,
            "target_score": request.target_score,
            "available_months": request.available_months,
            "subjects": {}
        }
        
        for subject in subjects:
            # Get weightage data
            weightage_data = get_chapter_weightage_for_revision.invoke({
                "exam": request.exam,
                "subject": subject
            })
            
            # Get flow/dependency data
            flow_data = get_chapter_flow_with_dependencies.invoke({
                "exam": request.exam,
                "subject": subject
            })
            
            revision_flow_data["subjects"][subject.lower()] = {
                "weightage_data": weightage_data,
                "flow_data": flow_data,
                "total_chapters": len(weightage_data)
            }
        
        return revision_flow_data
        
    except Exception as e:
        logger.error(f"Error generating revision flow: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@new_score_oriented_router.post("/validate-syllabus")
async def validate_syllabus_coverage_endpoint(request: SyllabusValidationRequest):
    """Validate syllabus coverage for new_score_oriented plans"""
    try:
        result = validate_syllabus_coverage.invoke({
            "exam": request.exam,
            "planned_chapters": request.planned_chapters
        })
        return result
    except Exception as e:
        logger.error(f"Error validating syllabus coverage: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@new_score_oriented_router.get("/syllabus/{exam}")
async def get_complete_syllabus_endpoint(exam: str):
    """Get complete syllabus for new_score_oriented validation"""
    try:
        syllabus_data = get_complete_syllabus_for_revision.invoke({"exam": exam})
        
        # Group by subject and chapter
        grouped_syllabus = {}
        for item in syllabus_data:
            subject = item.get("Subject", "")
            chapter = item.get("Chapter", "")
            topic = item.get("Topic", "")
            
            if subject not in grouped_syllabus:
                grouped_syllabus[subject] = {}
            if chapter not in grouped_syllabus[subject]:
                grouped_syllabus[subject][chapter] = []
            grouped_syllabus[subject][chapter].append(topic)
        
        return {
            "exam": exam,
            "syllabus": grouped_syllabus,
            "total_items": len(syllabus_data)
        }
        
    except Exception as e:
        logger.error(f"Error fetching complete syllabus: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@new_score_oriented_router.get("/progress/{user_id}")
async def get_new_score_oriented_progress(user_id: str):
    """Get saved new_score_oriented progress for a user"""
    try:
        from app.core.tools import supabase
        
        if not supabase:
            raise HTTPException(status_code=503, detail="Database not available")
        
        response = supabase.table("New_Score_Oriented_Progress").select("*").eq("user_id", user_id).execute()
        
        if response.data:
            return {
                "found": True,
                "progress_data": response.data[0]
            }
        else:
            return {
                "found": False,
                "message": "No new_score_oriented progress found for user"
            }
            
    except Exception as e:
        logger.error(f"Error retrieving new_score_oriented progress: {e}")
        raise HTTPException(status_code=500, detail=str(e))

class EnhancedScoreOrientedPlanRequest(BaseModel):
    """Request model for enhanced score-oriented plan generation"""
    exam: str
    target_score: str  # Format: "240/300"
    exam_date: str     # Format: "YYYY-MM-DD"
    start_date: Optional[str] = None  # Format: "YYYY-MM-DD", defaults to today

@new_score_oriented_router.post("/generate_enhanced_plan")
async def generate_enhanced_score_oriented_plan(request: EnhancedScoreOrientedPlanRequest):
    """
    Generate enhanced score-oriented study plan with comprehensive JSON structure
    
    This endpoint creates a detailed study plan including:
    - Plan info with calculated parameters
    - Monthly breakdown with score targets
    - Chapter distribution across months
    - Weekly breakdown with topics and DPP/PYQ schedules
    """
    try:
        logger.info(f"Generating enhanced score-oriented plan for exam: {request.exam}")
        
        # Generate the enhanced JSON structure
        enhanced_plan = generate_enhanced_score_oriented_json.invoke({
            "exam": request.exam,
            "target_score": request.target_score,
            "exam_date": request.exam_date,
            "start_date": request.start_date
        })
        
        logger.info("Successfully generated enhanced score-oriented plan")
        
        return {
            "status": "success",
            "message": "Enhanced score-oriented plan generated successfully",
            "data": enhanced_plan
        }
        
    except ValueError as e:
        logger.error(f"Validation error in enhanced plan generation: {e}")
        return {"status": "error", "message": str(e)}
    except Exception as e:
        logger.error(f"Unexpected error in enhanced plan generation: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))