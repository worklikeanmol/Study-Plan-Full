from langchain_core.tools import tool
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from supabase import create_client, Client
from dotenv import load_dotenv
from app.utils import get_logger
from app.tools import get_chapter_weightage

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

def validate_exam_date_logic(exam_date: str) -> dict:
    """
    Validates if the exam date is at least 5 months from today.
    Returns validation result and calculated months.
    """
    try:
        # Parse the exam date
        exam_datetime = datetime.strptime(exam_date, "%Y-%m-%d")
        today = datetime.now()
        
        # Calculate the difference
        time_diff = exam_datetime - today
        months_available = time_diff.days / 30.44  # Average days per month
        
        logger.info(f"Exam date: {exam_date}, Today: {today.strftime('%Y-%m-%d')}, Months available: {months_available:.1f}")
        
        if months_available < 5:
            return {
                "is_valid": False,
                "months_available": round(months_available, 1),
                "minimum_required": 5,
                "message": f"Exam date is only {months_available:.1f} months away. Minimum 5 months required for Score-Oriented plans. Please choose Custom plan type for shorter durations.",
                "suggested_action": "switch_to_custom"
            }
        else:
            return {
                "is_valid": True,
                "months_available": round(months_available, 1),
                "message": f"Exam date is {months_available:.1f} months away. Sufficient time for Score-Oriented preparation.",
                "calculated_months": min(int(months_available), 12)  # Cap at 12 months
            }
            
    except ValueError as e:
        logger.error(f"Invalid date format: {exam_date}. Expected YYYY-MM-DD")
        return {
            "is_valid": False,
            "message": "Invalid date format. Please use YYYY-MM-DD format.",
            "error": str(e)
        }
    except Exception as e:
        logger.error(f"Error validating exam date: {e}", exc_info=True)
        return {
            "is_valid": False,
            "message": f"Error validating exam date: {str(e)}",
            "error": str(e)
        }

@tool
def validate_exam_date(exam_date: str) -> dict:
    """
    Validates if the exam date is at least 5 months from today.
    Returns validation result and calculated months.
    """
    return validate_exam_date_logic(exam_date)

@tool
def calculate_target_score_progress(exam: str, target_score: int, completed_chapters: Dict[str, List[str]]) -> dict:
    """
    Calculates current score progress based on completed chapters and their weightages.
    Returns current score, remaining score needed, and probability analysis.
    """
    try:
        current_score = 0.0
        total_possible_score = 0.0
        
        # Get all subjects for the exam
        subjects = ["Physics", "Chemistry", "Mathematics"]  # Standard for JEE Mains
        
        for subject in subjects:
            # Get chapter weightages for this subject
            weightage_data = get_chapter_weightage.invoke({"exam": exam, "subject": subject})
            
            for chapter_info in weightage_data:
                chapter_name = chapter_info.get("Chapter", "")
                chapter_weightage = chapter_info.get("Average Weightage", 0)
                
                total_possible_score += chapter_weightage
                
                # Check if this chapter is completed
                subject_lower = subject.lower()
                if subject_lower in completed_chapters:
                    if chapter_name in completed_chapters[subject_lower]:
                        current_score += chapter_weightage
                        logger.info(f"Chapter {chapter_name} in {subject} completed: +{chapter_weightage} marks")
        
        # Calculate progress metrics
        score_percentage = (current_score / total_possible_score * 100) if total_possible_score > 0 else 0
        remaining_score_needed = max(0, target_score - current_score)
        remaining_possible_score = total_possible_score - current_score
        
        # Calculate probability of achieving target
        if remaining_score_needed <= 0:
            probability = 100.0
            status = "target_achieved"
        elif remaining_score_needed <= remaining_possible_score:
            probability = ((remaining_possible_score - remaining_score_needed) / remaining_possible_score) * 100
            if probability >= 80:
                status = "highly_achievable"
            elif probability >= 60:
                status = "achievable"
            elif probability >= 40:
                status = "challenging"
            else:
                status = "very_challenging"
        else:
            probability = 0.0
            status = "not_achievable"
        
        result = {
            "current_score": round(current_score, 1),
            "target_score": target_score,
            "total_possible_score": round(total_possible_score, 1),
            "score_percentage": round(score_percentage, 1),
            "remaining_score_needed": round(remaining_score_needed, 1),
            "remaining_possible_score": round(remaining_possible_score, 1),
            "achievement_probability": round(probability, 1),
            "status": status,
            "completed_chapters_count": sum(len(chapters) for chapters in completed_chapters.values()),
            "analysis": _generate_score_analysis(current_score, target_score, probability, status)
        }
        
        logger.info(f"Score progress calculated: {result}")
        return result
        
    except Exception as e:
        logger.error(f"Error calculating target score progress: {e}", exc_info=True)
        return {
            "error": str(e),
            "current_score": 0,
            "target_score": target_score,
            "achievement_probability": 0,
            "status": "error"
        }

def _generate_score_analysis(current_score: float, target_score: int, probability: float, status: str) -> str:
    """Generate human-readable analysis of score progress"""
    
    if status == "target_achieved":
        return f"🎉 Congratulations! You've already achieved your target score of {target_score}. Current score: {current_score:.1f}/300"
    
    elif status == "highly_achievable":
        return f"✅ Excellent progress! You're at {current_score:.1f}/300 with {probability:.1f}% probability of achieving {target_score}. Stay consistent!"
    
    elif status == "achievable":
        return f"👍 Good progress! You're at {current_score:.1f}/300 with {probability:.1f}% probability of achieving {target_score}. Focus on high-weightage chapters."
    
    elif status == "challenging":
        return f"⚠️ Challenging but possible! You're at {current_score:.1f}/300 with {probability:.1f}% probability of achieving {target_score}. Prioritize high-weightage chapters immediately."
    
    elif status == "very_challenging":
        return f"🚨 Very challenging! You're at {current_score:.1f}/300 with only {probability:.1f}% probability of achieving {target_score}. Consider revising your target or focusing on highest-weightage chapters only."
    
    elif status == "not_achievable":
        return f"❌ Target not achievable with remaining syllabus. Current: {current_score:.1f}/300, Target: {target_score}. Consider adjusting your target score."
    
    else:
        return f"Current score: {current_score:.1f}/300, Target: {target_score}"

@tool
def get_weightage_optimized_chapter_sequence(exam: str, target_score: int, available_months: int) -> dict:
    """
    Returns an optimized chapter sequence based on weightage and dependencies for score-oriented plans.
    Prioritizes high-weightage chapters while respecting dependencies.
    """
    try:
        subjects = ["Physics", "Chemistry", "Mathematics"]
        optimized_sequence = {}
        total_expected_score = 0
        
        for subject in subjects:
            # Get chapter weightages and dependencies
            weightage_data = get_chapter_weightage.invoke({"exam": exam, "subject": subject})
            
            # Sort chapters by weightage (descending) while respecting dependencies
            chapters_with_weightage = []
            for chapter_info in weightage_data:
                chapters_with_weightage.append({
                    "chapter": chapter_info.get("Chapter", ""),
                    "weightage": chapter_info.get("Average Weightage", 0),
                    "category": chapter_info.get("Chapter Category", "Medium"),
                    "priority_score": _calculate_priority_score(chapter_info)
                })
            
            # Sort by priority score (weightage + category bonus)
            chapters_with_weightage.sort(key=lambda x: x["priority_score"], reverse=True)
            
            # Create optimized sequence for this subject
            subject_sequence = []
            subject_expected_score = 0
            
            for chapter_data in chapters_with_weightage:
                subject_sequence.append({
                    "chapter": chapter_data["chapter"],
                    "weightage": chapter_data["weightage"],
                    "category": chapter_data["category"],
                    "priority_score": chapter_data["priority_score"]
                })
                subject_expected_score += chapter_data["weightage"]
            
            optimized_sequence[subject.lower()] = subject_sequence
            total_expected_score += subject_expected_score
        
        # Calculate if target is achievable
        achievement_analysis = {
            "total_expected_score": round(total_expected_score, 1),
            "target_score": target_score,
            "is_achievable": total_expected_score >= target_score,
            "score_gap": max(0, target_score - total_expected_score),
            "efficiency_rating": min(100, (target_score / total_expected_score) * 100) if total_expected_score > 0 else 0
        }
        
        result = {
            "optimized_sequence": optimized_sequence,
            "achievement_analysis": achievement_analysis,
            "recommendation": _generate_sequence_recommendation(achievement_analysis, available_months)
        }
        
        logger.info(f"Generated weightage-optimized sequence for target {target_score}: Expected score {total_expected_score}")
        return result
        
    except Exception as e:
        logger.error(f"Error generating optimized chapter sequence: {e}", exc_info=True)
        return {
            "error": str(e),
            "optimized_sequence": {},
            "achievement_analysis": {"is_achievable": False}
        }

def _calculate_priority_score(chapter_info: dict) -> float:
    """Calculate priority score for chapter based on weightage and category"""
    weightage = chapter_info.get("Average Weightage", 0)
    category = chapter_info.get("Chapter Category", "Medium")
    
    # Category multipliers for score optimization
    category_multiplier = {
        "High": 1.5,
        "Medium": 1.2,
        "Low": 1.0
    }.get(category, 1.0)
    
    return weightage * category_multiplier

def _generate_sequence_recommendation(analysis: dict, available_months: int) -> str:
    """Generate recommendation based on achievement analysis"""
    
    if analysis["is_achievable"]:
        efficiency = analysis["efficiency_rating"]
        if efficiency >= 90:
            return f"🎯 Perfect! Your target is highly achievable with {available_months} months. Follow the optimized sequence for maximum efficiency."
        elif efficiency >= 75:
            return f"✅ Great! Your target is achievable with focused study. Prioritize high-weightage chapters in the given sequence."
        else:
            return f"👍 Your target is achievable but requires consistent effort. Stick to the weightage-based sequence for best results."
    else:
        gap = analysis["score_gap"]
        return f"⚠️ Target is challenging with current syllabus. Consider focusing on top {int(analysis['efficiency_rating'])}% highest-weightage chapters or adjusting target by {gap:.1f} marks."

@tool
def save_score_progress(user_id: str, progress_data: dict) -> str:
    """Save user's score progress to database for tracking"""
    if not supabase:
        logger.warning("Supabase not available. Cannot save score progress.")
        return "Database not available - progress not saved"
    
    try:
        # Prepare progress data for insertion/upsert
        progress_record = {
            "user_id": user_id,
            "current_score": progress_data.get("current_score", 0),
            "target_score": progress_data.get("target_score", 0),
            "completed_chapters": progress_data.get("completed_chapters", {}),
            "achievement_probability": progress_data.get("achievement_probability", 0),
            "status": progress_data.get("status", "unknown"),
            "last_updated": datetime.now().isoformat()
        }
        
        # Use upsert to handle both insert and update cases
        response = supabase.table("Score_Progress").upsert(progress_record).execute()
        
        if response.data:
            logger.info(f"Successfully saved score progress for user: {user_id}")
            return f"Score progress saved for user {user_id}"
        else:
            logger.error(f"Failed to save score progress for user {user_id}: No data returned")
            return f"Failed to save score progress for user {user_id}"
            
    except Exception as e:
        logger.error(f"Error saving score progress for user {user_id}: {e}", exc_info=True)
        return f"Error saving progress: {str(e)}"