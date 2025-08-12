from langchain_core.tools import tool
import os
from supabase import create_client, Client
from dotenv import load_dotenv
from app.core.utils import get_logger

load_dotenv()
logger = get_logger(__name__)

# Initialize Supabase client
supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")

if not supabase_url or not supabase_key:
    logger.warning("Supabase URL or Key not found. Using mock data.")
    supabase = None
else:
    try:
        supabase: Client = create_client(supabase_url, supabase_key)
        logger.info("Supabase client initialized successfully.")
    except Exception as e:
        logger.error(f"Failed to initialize Supabase client: {e}", exc_info=True)
        supabase = None

# Mock Supabase data (as a fallback)
mock_chapter_flow = [
    {"Exam": "JEE Mains", "Subject": "Physics", "Chapter": "Chapter_1", "Dependencies": None, "Required Hours": 10},
    {"Exam": "JEE Mains", "Subject": "Physics", "Chapter": "Chapter_2", "Dependencies": "Chapter_1", "Required Hours": 12},
    {"Exam": "JEE Mains", "Subject": "Physics", "Chapter": "Chapter_3", "Dependencies": "Chapter_1", "Required Hours": 8},
]

mock_chapter_weightage = [
    {"Exam": "JEE Mains", "Subject": "Physics", "Chapter": "Chapter_1", "Average Weightage": 5.0, "Chapter Category": "High"},
    {"Exam": "JEE Mains", "Subject": "Physics", "Chapter": "Chapter_2", "Average Weightage": 3.0, "Chapter Category": "Medium"},
    {"Exam": "JEE Mains", "Subject": "Physics", "Chapter": "Chapter_3", "Average Weightage": 2.0, "Chapter Category": "Low"},
]

mock_topic_priority = [
    {"Exam": "JEE Mains", "Subject": "Physics", "Chapter": "Chapter_1", "Topic": "topic_1", "Topic Priority": "High"},
    {"Exam": "JEE Mains", "Subject": "Physics", "Chapter": "Chapter_1", "Topic": "topic_2", "Topic Priority": "Medium"},
    {"Exam": "JEE Mains", "Subject": "Physics", "Chapter": "Chapter_1", "Topic": "topic_3", "Topic Priority": "Low"},
]

# Add mock data for the new syllabus tool
mock_syllabus = [
    {"Exam": "JEE Mains", "Subject": "Physics", "Chapter": "Chapter_1", "Topic": "topic_1"},
    {"Exam": "JEE Mains", "Subject": "Physics", "Chapter": "Chapter_1", "Topic": "topic_2"},
    {"Exam": "JEE Mains", "Subject": "Physics", "Chapter": "Chapter_2", "Topic": "topic_a"},
    {"Exam": "JEE Mains", "Subject": "Chemistry", "Chapter": "Chapter_1", "Topic": "topic_x"},
    {"Exam": "JEE Mains", "Subject": "Maths", "Chapter": "Chapter_1", "Topic": "topic_y"},
]

@tool
def calculator(query: str) -> str:
    """A simple calculator tool."""
    try:
        return eval(query)
    except Exception as e:
        return str(e)

@tool
def get_syllabus(exam: str) -> list:
    """Fetches the complete syllabus (subjects, chapters, topics) for a given exam."""
    if not supabase:
        logger.info(f"Using mock syllabus data for exam: {exam}")
        return [item for item in mock_syllabus if item["Exam"] == exam]
    try:
        logger.info(f"Fetching syllabus for exam: {exam}")
        response = supabase.table("Syllabus").select("*").eq("Exam", exam).execute()
        return response.data
    except Exception as e:
        logger.error(f"Error fetching syllabus from Supabase: {e}", exc_info=True)
        return []

@tool
def get_chapter_flow(exam: str, subject: str) -> list:
    """Fetch chapter flow from Supabase. If Supabase is unavailable, uses mock data."""
    if not supabase:
        logger.info("Using mock chapter flow data.")
        return [item for item in mock_chapter_flow if item["Exam"] == exam and item["Subject"] == subject]
    try:
        logger.info(f"Fetching chapter flow for exam: {exam}, subject: {subject}")
        response = supabase.table("Chapter_Flow").select("*").eq("Exam", exam).eq("Subject", subject.capitalize()).execute()
        return response.data
    except Exception as e:
        logger.error(f"Error fetching chapter flow from Supabase: {e}", exc_info=True)
        return [] # Return empty list on error

@tool
def get_chapter_weightage(exam: str, subject: str) -> list:
    """Fetch chapter weightage from Supabase. If Supabase is unavailable, uses mock data."""
    if not supabase:
        logger.info("Using mock chapter weightage data.")
        return [item for item in mock_chapter_weightage if item["Exam"] == exam and item["Subject"] == subject]
    try:
        logger.info(f"Fetching chapter weightage for exam: {exam}, subject: {subject}")
        response = supabase.table("Chapter_Weightage").select("*").eq("Exam", exam).eq("Subject", subject.capitalize()).execute()
        return response.data
    except Exception as e:
        logger.error(f"Error fetching chapter weightage from Supabase: {e}", exc_info=True)
        return []

@tool
def get_topic_priority(exam: str, subject: str, chapter: str) -> list:
    """Fetch topic priority from Supabase. If Supabase is unavailable, uses mock data."""
    if not supabase:
        logger.info(f"Using mock topic priority data for chapter: {chapter}")
        return [item for item in mock_topic_priority if item["Exam"] == exam and item["Subject"] == subject and item["Chapter"] == chapter]
    try:
        logger.info(f"Fetching topic priority for exam: {exam}, subject: {subject}, chapter: {chapter}")
        response = supabase.table("Topic_Priority").select("*").eq("Exam", exam).eq("Subject", subject.capitalize()).eq("Chapter", chapter).execute()
        return response.data
    except Exception as e:
        logger.error(f"Error fetching topic priority from Supabase: {e}", exc_info=True)
        return []

@tool
def save_finalized_plan(user_id: str, state_message: dict, study_plan: dict) -> str:
    """Save finalized study plan and state to User_Table in Supabase."""
    if not supabase:
        logger.warning("Supabase not available. Cannot save finalized plan to database.")
        return "Database not available - plan not saved"
    
    try:
        logger.info(f"Saving finalized plan for user: {user_id}")
        
        # Prepare data for insertion/upsert
        plan_data = {
            "user_id": user_id,
            "state_msg": state_message,
            "study_plan": study_plan
        }
        
        # Use upsert to handle both insert and update cases
        response = supabase.table("User_Table").upsert(plan_data).execute()
        
        if response.data:
            logger.info(f"Successfully saved finalized plan for user: {user_id}")
            return f"Plan successfully saved for user {user_id}"
        else:
            logger.error(f"Failed to save plan for user {user_id}: No data returned")
            return f"Failed to save plan for user {user_id}"
            
    except Exception as e:
        logger.error(f"Error saving finalized plan for user {user_id}: {e}", exc_info=True)
        return f"Error saving plan: {str(e)}" 