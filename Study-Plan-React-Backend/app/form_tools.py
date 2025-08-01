"""
Tools for handling form data storage and retrieval
"""
from langchain_core.tools import tool
import os
from supabase import create_client, Client
from dotenv import load_dotenv
from app.utils import get_logger
from typing import Dict, Optional, Any

load_dotenv()
logger = get_logger(__name__)

# Initialize Supabase client
supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")

if not supabase_url or not supabase_key:
    logger.warning("Supabase URL or Key not found. Form storage will not work.")
    supabase = None
else:
    try:
        supabase: Client = create_client(supabase_url, supabase_key)
        logger.info("Supabase client initialized successfully for form tools.")
    except Exception as e:
        logger.error(f"Failed to initialize Supabase client for form tools: {e}", exc_info=True)
        supabase = None

@tool
def save_user_form_data(user_id: str, form_data: Dict[str, Any]) -> str:
    """Save user form data to User_Table for later retrieval during chat"""
    if not supabase:
        logger.warning("Supabase not available. Cannot save form data.")
        return "Database not available - form data not saved"
    
    try:
        logger.info(f"Saving form data for user: {user_id}")
        
        # Check if user already exists
        existing_user = supabase.table("User_Table").select("*").eq("user_id", user_id).execute()
        
        if existing_user.data:
            # Update existing user's form content
            response = supabase.table("User_Table").update({
                "form_content": form_data
            }).eq("user_id", user_id).execute()
            logger.info(f"Updated form data for existing user: {user_id}")
        else:
            # Insert new user with form content
            response = supabase.table("User_Table").insert({
                "user_id": user_id,
                "state_msg": {},  # Empty state initially
                "form_content": form_data
            }).execute()
            logger.info(f"Created new user with form data: {user_id}")
        
        if response.data:
            return f"Form data successfully saved for user {user_id}"
        else:
            return f"Failed to save form data for user {user_id}"
            
    except Exception as e:
        logger.error(f"Error saving form data for user {user_id}: {e}", exc_info=True)
        return f"Error saving form data: {str(e)}"

@tool
def get_user_form_data(user_id: str) -> Dict[str, Any]:
    """Retrieve user form data from User_Table"""
    if not supabase:
        logger.warning("Supabase not available. Cannot retrieve form data.")
        return {}
    
    try:
        logger.info(f"Retrieving form data for user: {user_id}")
        
        response = supabase.table("User_Table").select("form_content").eq("user_id", user_id).execute()
        
        if response.data and response.data[0].get("form_content"):
            form_data = response.data[0]["form_content"]
            logger.info(f"Retrieved form data for user: {user_id}")
            return form_data
        else:
            logger.info(f"No form data found for user: {user_id}")
            return {}
            
    except Exception as e:
        logger.error(f"Error retrieving form data for user {user_id}: {e}", exc_info=True)
        return {}

@tool
def update_user_state_message(user_id: str, state_message: Dict[str, Any]) -> str:
    """Update user state message in User_Table"""
    if not supabase:
        logger.warning("Supabase not available. Cannot update state message.")
        return "Database not available - state not updated"
    
    try:
        logger.info(f"Updating state message for user: {user_id}")
        
        response = supabase.table("User_Table").update({
            "state_msg": state_message
        }).eq("user_id", user_id).execute()
        
        if response.data:
            logger.info(f"Successfully updated state message for user: {user_id}")
            return f"State message updated for user {user_id}"
        else:
            logger.error(f"Failed to update state message for user {user_id}")
            return f"Failed to update state message for user {user_id}"
            
    except Exception as e:
        logger.error(f"Error updating state message for user {user_id}: {e}", exc_info=True)
        return f"Error updating state message: {str(e)}"

@tool
def validate_form_data(form_data: Dict[str, Any]) -> Dict[str, Any]:
    """Validate form data according to business rules"""
    validation_result = {
        "is_valid": True,
        "errors": [],
        "warnings": []
    }
    
    try:
        # Check required fields
        required_fields = ["target_exam", "study_plan_type", "preparation_type", "syllabus", "number_of_months", "hours_per_day"]
        for field in required_fields:
            if field not in form_data or form_data[field] is None:
                validation_result["errors"].append(f"Missing required field: {field}")
                validation_result["is_valid"] = False
        
        # Validate study plan type and target score
        if form_data.get("study_plan_type") == "Generic":
            if not form_data.get("target_score"):
                validation_result["errors"].append("Target score is required for Generic study plans")
                validation_result["is_valid"] = False
            elif form_data.get("target_score") and (form_data["target_score"] < 1 or form_data["target_score"] > 300):
                validation_result["errors"].append("Target score must be between 1 and 300")
                validation_result["is_valid"] = False
        
        # Validate preparation type and months
        if form_data.get("preparation_type") == "Syllabus Coverage":
            if form_data.get("number_of_months") and form_data["number_of_months"] < 3:
                validation_result["errors"].append("Minimum 3 months required for Syllabus Coverage")
                validation_result["is_valid"] = False
        
        # Validate syllabus
        syllabus = form_data.get("syllabus", {})
        required_subjects = ["mathematics", "physics", "chemistry"]
        for subject in required_subjects:
            if subject not in syllabus or not syllabus[subject] or len(syllabus[subject]) == 0:
                validation_result["errors"].append(f"At least one chapter required for {subject}")
                validation_result["is_valid"] = False
        
        # Validate numeric ranges
        if form_data.get("number_of_months") and (form_data["number_of_months"] < 1 or form_data["number_of_months"] > 24):
            validation_result["warnings"].append("Number of months should be between 1 and 24")
        
        if form_data.get("hours_per_day") and (form_data["hours_per_day"] < 1 or form_data["hours_per_day"] > 16):
            validation_result["warnings"].append("Hours per day should be between 1 and 16")
        
        logger.info(f"Form validation completed. Valid: {validation_result['is_valid']}")
        return validation_result
        
    except Exception as e:
        logger.error(f"Error validating form data: {e}", exc_info=True)
        validation_result["is_valid"] = False
        validation_result["errors"].append(f"Validation error: {str(e)}")
        return validation_result