from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.graph import graph, StudyPlanState
from app.regen_graph import regen_graph, RegenerationState
from app.regen_tools import check_user_exists, get_user_performance
from app.tools import supabase
from app.utils import get_logger
from app.models import (
    UserData,
    ChatMessage,
    Validation,
    StudyPlan,
    WeeklySubjectPlan,
    PlanParameters,
)
from app.regen_models import (
    RegenerationUserData,
    RegenerationPreferences,
)
from typing import Dict, Optional

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger = get_logger(__name__)

# Global chat history storage - In production, use Redis or database
chat_history_storage = {}

class StudyPlanRequest(BaseModel):
    user_id: str
    target_exam: str
    study_plan_type: str
    preparation_type: str
    syllabus: Dict[str, list[str]]
    number_of_months: int
    hours_per_day: int
    user_message: str

class ChatRequest(BaseModel):
    user_id: str
    user_message: str
    # Required form data - provided by frontend form
    target_exam: str
    study_plan_type: str
    preparation_type: str
    syllabus: Dict[str, list[str]]
    number_of_months: int
    hours_per_day: int
    # Optional: Target score for generic study plans
    target_score: Optional[int] = None
    # Optional: Reset chat history (for new conversations)
    reset_chat: bool = False

class FormSaveRequest(BaseModel):
    user_id: str
    target_exam: str
    study_plan_type: str
    preparation_type: str
    syllabus: Dict[str, list[str]]
    number_of_months: int
    hours_per_day: int
    target_score: Optional[int] = None

class FormSaveResponse(BaseModel):
    success: bool
    message: str
    user_id: str

class ChatResponse(BaseModel):
    user_id: str
    assistant_message: str
    is_plan_generated: bool = False
    study_plan: StudyPlan | None = None
    chat_context: Dict[str, ChatMessage] = {}

@app.post("/save-form", response_model=FormSaveResponse)
async def save_form_data(request: FormSaveRequest):
    """Save form data to User_Table for later use in chat"""
    logger.info(f"Saving form data for user: {request.user_id}")
    
    try:
        # Prepare form content for database storage
        form_content = {
            "target_exam": request.target_exam,
            "study_plan_type": request.study_plan_type,
            "preparation_type": request.preparation_type,
            "syllabus": request.syllabus,
            "number_of_months": request.number_of_months,
            "hours_per_day": request.hours_per_day,
            "target_score": request.target_score
        }
        
        if not supabase:
            logger.warning("Supabase not available. Cannot save form data to database.")
            return FormSaveResponse(
                success=False,
                message="Database not available - form data not saved",
                user_id=request.user_id
            )
        
        # Check if user already exists
        existing_user = supabase.table("User_Table").select("*").eq("user_id", request.user_id).execute()
        
        if existing_user.data:
            # Update existing user's form content
            response = supabase.table("User_Table").update({
                "form_content": form_content
            }).eq("user_id", request.user_id).execute()
            logger.info(f"Updated form data for existing user: {request.user_id}")
        else:
            # Insert new user with form content
            response = supabase.table("User_Table").insert({
                "user_id": request.user_id,
                "state_msg": {},  # Empty state initially
                "form_content": form_content
            }).execute()
            logger.info(f"Created new user with form data: {request.user_id}")
        
        if response.data:
            return FormSaveResponse(
                success=True,
                message="Form data saved successfully",
                user_id=request.user_id
            )
        else:
            return FormSaveResponse(
                success=False,
                message="Failed to save form data",
                user_id=request.user_id
            )
            
    except Exception as e:
        logger.error(f"Error saving form data for user {request.user_id}: {e}", exc_info=True)
        return FormSaveResponse(
            success=False,
            message=f"Error saving form data: {str(e)}",
            user_id=request.user_id
        )

@app.post("/chat", response_model=ChatResponse)
async def chat_with_counsellor(request: ChatRequest):
    """Interactive chat endpoint for counsellor conversation with regeneration support"""
    logger.info(f"Received chat message from user: {request.user_id}")
    
    # STEP 1: Check if user exists (regeneration detection)
    try:
        user_check = check_user_exists.invoke({"user_id": request.user_id})
        is_existing_user = user_check.get("exists", False)
        user_data = user_check.get("user_data", {})
        
        # Only treat as existing user if they have a proper study plan
        has_study_plan = user_data and user_data.get("study_plan") is not None
        is_existing_user = is_existing_user and has_study_plan
        
        logger.info(f"User existence check for {request.user_id}: exists={user_check.get('exists', False)}, has_study_plan={has_study_plan}, treating_as_existing={is_existing_user}")
    except Exception as e:
        logger.error(f"Error checking user existence: {e}")
        is_existing_user = False
    
    # STEP 2: Route to appropriate flow
    if is_existing_user:
        logger.info(f"Existing user detected: {request.user_id} - routing to regeneration flow")
        return await handle_regeneration_chat(request)
    else:
        logger.info(f"New user detected: {request.user_id} - routing to normal flow")
        return await handle_normal_chat(request)

async def handle_normal_chat(request: ChatRequest):
    """Handle chat for new users (normal flow)"""
    
    # Try to get form data from database first
    stored_form_data = None
    if supabase:
        try:
            user_response = supabase.table("User_Table").select("form_content").eq("user_id", request.user_id).execute()
            if user_response.data and user_response.data[0].get("form_content"):
                stored_form_data = user_response.data[0]["form_content"]
                logger.info(f"Retrieved stored form data for user: {request.user_id}")
        except Exception as e:
            logger.warning(f"Could not retrieve stored form data for user {request.user_id}: {e}")
    
    # Use stored form data if available, otherwise use request data
    if stored_form_data:
        user_data = UserData(
            user_id=request.user_id,
            target_exam=stored_form_data.get("target_exam", request.target_exam),
            study_plan_type=stored_form_data.get("study_plan_type", request.study_plan_type),
            preparation_type=stored_form_data.get("preparation_type", request.preparation_type),
            syllabus=stored_form_data.get("syllabus", request.syllabus),
            number_of_months=stored_form_data.get("number_of_months", request.number_of_months),
            hours_per_day=stored_form_data.get("hours_per_day", request.hours_per_day),
            target_score=stored_form_data.get("target_score", request.target_score)
        )
        logger.info(f"Using stored form data for user: {request.user_id}")
    else:
        # Create user data from request (fallback)
        user_data = UserData(
            user_id=request.user_id,
            target_exam=request.target_exam,
            study_plan_type=request.study_plan_type,
            preparation_type=request.preparation_type,
            syllabus=request.syllabus,
            number_of_months=request.number_of_months,
            hours_per_day=request.hours_per_day,
            target_score=request.target_score
        )
        logger.info(f"Using request form data for user: {request.user_id}")
    
    # Auto-managed chat history storage
    chat_key = f"{request.user_id}_{request.target_exam}_{request.study_plan_type}"
    
    # Reset chat history if requested
    if request.reset_chat:
        chat_history_storage[chat_key] = {}
        logger.info(f"Reset chat history for user: {request.user_id}")
    
    # Get existing chat history from storage
    stored_chat_history = chat_history_storage.get(chat_key, {})
    
    # Build chat context from stored history
    chat_context = {}
    for turn_id, chat_msg in stored_chat_history.items():
        if isinstance(chat_msg, dict):
            chat_context[turn_id] = ChatMessage(**chat_msg)
        else:
            chat_context[turn_id] = chat_msg
    
    # Add current user message
    current_turn_id = str(len(chat_context) + 1)
    chat_context[current_turn_id] = ChatMessage(
        user_message=request.user_message,
        assistant_message=""
    )
    
    # Debug logging
    logger.info(f"Auto-managed chat history for {chat_key}")
    logger.info(f"Loaded {len(stored_chat_history)} previous turns from storage")
    logger.info(f"Built chat_context with {len(chat_context)} turns")
    for turn_id, turn in chat_context.items():
        logger.info(f"Turn {turn_id}: User='{turn.user_message[:50]}...' Assistant='{turn.assistant_message[:50]}...'")
    
    initial_state: StudyPlanState = {
        "user_data": user_data,
        "chat_context": chat_context,
        "plan_parameters": PlanParameters(),
        "monthly_coverage": {},
        "weekly_coverage": {},
        "validation_context": {},
        "study_plan": StudyPlan(),
        "plan_metadata": {},
        "regeneration_feedback": [],
        "feedback_requests": [],
        "supervisor_insights": [],
        "plan_finalized": False,
        "is_re_edit": False,
        "next_agent": ""
    }
    
    try:
        final_state = graph.invoke(initial_state)
        
        # Get the assistant's response from the latest chat context
        final_chat_context = final_state.get("chat_context", {})
        assistant_message = ""
        
        # Find the assistant's response in the latest turn
        if current_turn_id in final_chat_context:
            assistant_message = final_chat_context[current_turn_id].assistant_message
        
        # Check if a study plan was generated
        study_plan = final_state.get("study_plan")
        is_plan_generated = bool(study_plan and study_plan.monthly_plan)
        
        # CRITICAL FIX: Also check if plan was finalized
        plan_finalized = final_state.get("plan_finalized", False)
        
        if is_plan_generated:
            logger.info(f"Study plan generated for user: {request.user_id}")
            # Don't modify assistant_message here - let the feedback_counsellor handle the presentation
            
        # If plan is finalized, ensure we return it
        if plan_finalized:
            logger.info(f"Study plan finalized for user: {request.user_id}")
            is_plan_generated = True
        
        # Auto-save updated chat history to storage
        chat_history_storage[chat_key] = {
            turn_id: {
                "user_message": turn.user_message,
                "assistant_message": turn.assistant_message
            } for turn_id, turn in final_chat_context.items()
        }
        logger.info(f"Saved {len(final_chat_context)} turns to chat history storage")
        
        return ChatResponse(
            user_id=request.user_id,
            assistant_message=assistant_message or "I'm here to help you create a great study plan! Please tell me about your exam preparation needs.",
            is_plan_generated=is_plan_generated,
            study_plan=study_plan if is_plan_generated else None,
            chat_context=final_chat_context
        )
        
    except Exception as e:
        logger.error(f"Error in normal chat for user {request.user_id}: {e}", exc_info=True)
        # Save current context even on error
        chat_history_storage[chat_key] = {
            turn_id: {
                "user_message": turn.user_message,
                "assistant_message": turn.assistant_message
            } for turn_id, turn in chat_context.items()
        }
        
        return ChatResponse(
            user_id=request.user_id,
            assistant_message="I apologize, but I encountered an error. Please try again or contact support if the issue persists.",
            is_plan_generated=False,
            chat_context=chat_context
        )

async def handle_regeneration_chat(request: ChatRequest):
    """Handle chat for existing users (regeneration flow)"""
    logger.info(f"Handling regeneration chat for user: {request.user_id}")
    
    # Create regeneration user data
    regen_user_data = RegenerationUserData(
        user_id=request.user_id,
        target_exam=request.target_exam,
        study_plan_type=request.study_plan_type,
        preparation_type=request.preparation_type,
        syllabus=request.syllabus,
        number_of_months=request.number_of_months,
        hours_per_day=request.hours_per_day,
        target_score=request.target_score
    )
    
    # Auto-managed chat history storage (separate key for regeneration)
    chat_key = f"regen_{request.user_id}_{request.target_exam}_{request.study_plan_type}"
    
    # Reset chat history if requested
    if request.reset_chat:
        chat_history_storage[chat_key] = {}
        logger.info(f"Reset regeneration chat history for user: {request.user_id}")
    
    # Get existing chat history from storage
    stored_chat_history = chat_history_storage.get(chat_key, {})
    
    # Build chat context from stored history
    chat_context = {}
    for turn_id, chat_msg in stored_chat_history.items():
        if isinstance(chat_msg, dict):
            chat_context[turn_id] = ChatMessage(**chat_msg)
        else:
            chat_context[turn_id] = chat_msg
    
    # Add current user message
    current_turn_id = str(len(chat_context) + 1)
    chat_context[current_turn_id] = ChatMessage(
        user_message=request.user_message,
        assistant_message=""
    )
    
    logger.info(f"Regeneration chat context built with {len(chat_context)} turns")
    
    # Create regeneration state
    initial_regen_state: RegenerationState = {
        "user_id": request.user_id,
        "is_existing_user": True,
        "previous_plan": None,
        "performance_data": None,
        "regeneration_preferences": RegenerationPreferences(),
        "regeneration_insights": None,
        "chat_context": chat_context,
        "plan_parameters": PlanParameters(),
        "monthly_coverage": {},
        "weekly_coverage": {},
        "validation_context": {},
        "study_plan": None,
        "plan_metadata": {},
        "regen_feedback": [],
        "regen_supervisor_insights": [],
        "plan_finalized": False,
        "is_re_edit": False,
        "next_agent": "regen_counsellor"
    }
    
    try:
        final_regen_state = regen_graph.invoke(initial_regen_state)
        
        # Get the assistant's response from the latest chat context
        final_chat_context = final_regen_state.get("chat_context", {})
        assistant_message = ""
        
        # Find the assistant's response in the latest turn
        if current_turn_id in final_chat_context:
            assistant_message = final_chat_context[current_turn_id].assistant_message
        
        # Check if a regenerated study plan was generated
        study_plan = final_regen_state.get("study_plan")
        is_plan_generated = bool(study_plan and hasattr(study_plan, 'monthly_plan') and study_plan.monthly_plan)
        
        # Check if plan was finalized
        plan_finalized = final_regen_state.get("plan_finalized", False)
        
        if is_plan_generated:
            logger.info(f"Regenerated study plan generated for user: {request.user_id}")
            
        # If plan is finalized, ensure we return it
        if plan_finalized:
            logger.info(f"Regenerated study plan finalized for user: {request.user_id}")
            is_plan_generated = True
        
        # Auto-save updated chat history to storage
        chat_history_storage[chat_key] = {
            turn_id: {
                "user_message": turn.user_message,
                "assistant_message": turn.assistant_message
            } for turn_id, turn in final_chat_context.items()
        }
        logger.info(f"Saved {len(final_chat_context)} regeneration turns to chat history storage")
        
        return ChatResponse(
            user_id=request.user_id,
            assistant_message=assistant_message or "Welcome back! I'm here to help you regenerate your study plan based on your progress. Let me analyze your performance and guide you through the next phase.",
            is_plan_generated=is_plan_generated,
            study_plan=study_plan if is_plan_generated else None,
            chat_context=final_chat_context
        )
        
    except Exception as e:
        logger.error(f"Error in regeneration chat for user {request.user_id}: {e}", exc_info=True)
        # Save current context even on error
        chat_history_storage[chat_key] = {
            turn_id: {
                "user_message": turn.user_message,
                "assistant_message": turn.assistant_message
            } for turn_id, turn in chat_context.items()
        }
        
        return ChatResponse(
            user_id=request.user_id,
            assistant_message="I apologize, but I encountered an error in the regeneration process. Please try again or contact support if the issue persists.",
            is_plan_generated=False,
            chat_context=chat_context
        )

@app.post("/generate-study-plan", response_model=StudyPlan)
async def generate_study_plan(request: StudyPlanRequest):
    """Legacy endpoint for direct study plan generation"""
    logger.info(f"Received legacy request for user: {request.user_id}")
    
    user_data = UserData(**request.model_dump())
    
    initial_state: StudyPlanState = {
        "user_data": user_data,
        "chat_context": {"1": ChatMessage(user_message=request.user_message, assistant_message="")},
        "plan_parameters": PlanParameters(),
        "monthly_coverage": {},
        "weekly_coverage": {},
        "validation_context": {},
        "study_plan": StudyPlan(),
        "plan_metadata": {},
        "regeneration_feedback": [],
        "feedback_requests": [],
        "supervisor_insights": [],
        "plan_finalized": False,
        "next_agent": ""
    }
    
    try:
        final_state = graph.invoke(initial_state)
        logger.info(f"Successfully generated study plan for user: {request.user_id}")
        return final_state.get("study_plan", StudyPlan())
    except Exception as e:
        logger.error(f"Error generating study plan for user {request.user_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/chat-history/{user_id}")
async def get_chat_history(user_id: str, target_exam: str = "JEE Mains", study_plan_type: str = "Custom"):
    """Get stored chat history for a user"""
    chat_key = f"{user_id}_{target_exam}_{study_plan_type}"
    stored_history = chat_history_storage.get(chat_key, {})
    return {
        "user_id": user_id,
        "chat_key": chat_key,
        "total_turns": len(stored_history),
        "chat_history": stored_history
    }

@app.delete("/chat-history/{user_id}")
async def clear_chat_history(user_id: str, target_exam: str = "JEE Mains", study_plan_type: str = "Custom"):
    """Clear stored chat history for a user"""
    chat_key = f"{user_id}_{target_exam}_{study_plan_type}"
    if chat_key in chat_history_storage:
        del chat_history_storage[chat_key]
        return {"message": f"Chat history cleared for {chat_key}"}
    else:
        return {"message": f"No chat history found for {chat_key}"}

@app.get("/chat-storage-status")
async def get_chat_storage_status():
    """Get overview of all stored chat histories"""
    normal_chats = [k for k in chat_history_storage.keys() if not k.startswith("regen_")]
    regen_chats = [k for k in chat_history_storage.keys() if k.startswith("regen_")]
    
    return {
        "total_users": len(chat_history_storage),
        "normal_conversations": len(normal_chats),
        "regeneration_conversations": len(regen_chats),
        "storage_keys": list(chat_history_storage.keys()),
        "total_conversations": sum(len(history) for history in chat_history_storage.values())
    }

@app.post("/check-user-status")
async def check_user_status(user_id: str):
    """Check if user is new or existing (for regeneration routing)"""
    try:
        user_check = check_user_exists.invoke({"user_id": user_id})
        is_existing = user_check.get("exists", False)
        user_data = user_check.get("user_data", None)
        
        return {
            "user_id": user_id,
            "is_existing_user": is_existing,
            "flow_type": "regeneration" if is_existing else "normal",
            "has_previous_plan": bool(user_data and user_data.get("study_plan")),
            "created_at": user_data.get("created_at") if user_data else None
        }
    except Exception as e:
        logger.error(f"Error checking user status: {e}")
        return {
            "user_id": user_id,
            "is_existing_user": False,
            "flow_type": "normal",
            "error": str(e)
        }

@app.get("/chapters/{exam}")
async def get_chapters_by_exam(exam: str):
    """Get chapters from Chapter_Metadata table for a specific exam"""
    logger.info(f"Fetching chapters for exam: {exam}")
    
    if not supabase:
        logger.warning("Supabase not available. Using fallback chapter data.")
        # Fallback data structure
        fallback_chapters = {
            "mathematics": ["Algebra", "Calculus", "Coordinate Geometry", "Trigonometry", "Statistics", "Probability", "Vectors", "Complex Numbers", "Matrices", "Sequences and Series"],
            "physics": ["Mechanics", "Thermodynamics", "Waves and Oscillations", "Electrostatics", "Current Electricity", "Magnetism", "Electromagnetic Induction", "Optics", "Modern Physics", "Atomic Structure"],
            "chemistry": ["Atomic Structure", "Chemical Bonding", "Thermodynamics", "Chemical Equilibrium", "Ionic Equilibrium", "Electrochemistry", "Chemical Kinetics", "Organic Chemistry", "Coordination Compounds", "Biomolecules"]
        }
        return {
            "exam": exam,
            "subjects": fallback_chapters,
            "total_chapters": sum(len(chapters) for chapters in fallback_chapters.values()),
            "source": "fallback"
        }
    
    try:
        # Fetch chapters from Chapter_Metadata table
        response = supabase.table("Chapter_Metadata").select("*").eq("Exam", exam).execute()
        
        if not response.data:
            logger.warning(f"No chapters found for exam: {exam}")
            return {
                "exam": exam,
                "subjects": {},
                "total_chapters": 0,
                "source": "database",
                "message": f"No chapters found for exam: {exam}"
            }
        
        # Group chapters by subject
        subjects = {}
        for row in response.data:
            subject = row.get("Subject", "").lower()
            chapter = row.get("Chapter", "")
            
            if subject and chapter:
                if subject not in subjects:
                    subjects[subject] = []
                subjects[subject].append(chapter)
        
        # Sort chapters within each subject
        for subject in subjects:
            subjects[subject].sort()
        
        logger.info(f"Retrieved {len(response.data)} chapters for {exam} across {len(subjects)} subjects")
        
        return {
            "exam": exam,
            "subjects": subjects,
            "total_chapters": len(response.data),
            "source": "database"
        }
        
    except Exception as e:
        logger.error(f"Error fetching chapters for exam {exam}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error fetching chapters: {str(e)}")

@app.get("/regeneration-info/{user_id}")
async def get_regeneration_info(user_id: str):
    """Get regeneration information for existing users"""
    try:
        # Check user exists
        user_check = check_user_exists.invoke({"user_id": user_id})
        if not user_check.get("exists", False):
            raise HTTPException(status_code=404, detail="User not found")
        
        # Get performance data
        performance_result = get_user_performance.invoke({"user_id": user_id})
        
        user_data = user_check.get("user_data", {})
        performance_data = performance_result.get("performance_data", {}) if performance_result.get("found") else {}
        
        return {
            "user_id": user_id,
            "previous_plan": user_data.get("study_plan", {}),
            "performance_data": performance_data,
            "plan_created_at": user_data.get("created_at"),
            "last_performance_update": performance_data.get("last_updated"),
            "overall_progress": performance_data.get("overall_progress_percentage", 0),
            "subject_progress": performance_data.get("subject_wise_progress", {}),
            "completed_topics_count": sum(
                len(chapters.values()) if isinstance(chapters, dict) else 0 
                for chapters in performance_data.get("completed_topics", {}).values()
            ),
            "pending_topics_count": sum(
                len(chapters.values()) if isinstance(chapters, dict) else 0 
                for chapters in performance_data.get("not_completed_topics", {}).values()
            )
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting regeneration info: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 