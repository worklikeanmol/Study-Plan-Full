from langchain_core.tools import tool
import os
from supabase import create_client, Client
from dotenv import load_dotenv
from app.utils import get_logger
from typing import Dict, Any, List, Optional
import json

load_dotenv()
logger = get_logger(__name__)

# Initialize Supabase client
supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")

if not supabase_url or not supabase_key:
    logger.warning("Supabase URL or Key not found. Using mock data for score tools.")
    supabase = None
else:
    try:
        supabase: Client = create_client(supabase_url, supabase_key)
        logger.info("Supabase client initialized successfully for score tools.")
    except Exception as e:
        logger.error(f"Failed to initialize Supabase client for score tools: {e}", exc_info=True)
        supabase = None

# Mock data for testing
mock_exam_weightage = [
    {
        "exam_id": 1,
        "chapter_id": 1,
        "marks_history": [8, 10, 12, 9, 11],
        "marks_min": 8.0,
        "marks_max": 12.0,
        "marks_avg": 10.0,
        "marks_sd": 1.5,
        "insights": "High-scoring chapter with consistent marks",
        "prerequisites": "Basic algebra"
    },
    {
        "exam_id": 1,
        "chapter_id": 2,
        "marks_history": [4, 6, 5, 7, 5],
        "marks_min": 4.0,
        "marks_max": 7.0,
        "marks_avg": 5.4,
        "marks_sd": 1.1,
        "insights": "Medium-scoring chapter",
        "prerequisites": "Chapter 1"
    }
]

@tool
def get_exam_weightage_data(exam: str, subject: str = None) -> List[Dict[str, Any]]:
    """Get exam weightage data including marks history for chapters.
    
    Args:
        exam: The target exam name (e.g., 'JEE Mains')
        subject: Optional subject filter (e.g., 'Physics')
    
    Returns:
        List of weightage data with marks history, averages, and insights
    """
    if not supabase:
        logger.warning("Using mock exam weightage data.")
        return mock_exam_weightage
    
    try:
        logger.info(f"Fetching exam weightage data for {exam}, subject: {subject}")
        
        # This would typically join with exam and chapter tables
        # For now, using simplified query
        query = supabase.table("data_exam_weightage").select("*")
        
        # Add filters based on exam and subject if available
        # Note: This would need proper joins with exam and chapter tables
        response = query.execute()
        
        return response.data if response.data else []
        
    except Exception as e:
        logger.error(f"Error fetching exam weightage data: {e}", exc_info=True)
        return []

@tool
def calculate_expected_score(coverage_plan: str, target_score: int) -> Dict[str, Any]:
    """Calculate expected score based on planned chapter coverage.
    
    Args:
        coverage_plan: JSON string of planned coverage {subject: {chapter: coverage_percentage}}
        target_score: User's target score (e.g., 252 out of 300)
    
    Returns:
        Dictionary with score analysis, achievability, and recommendations
    """
    try:
        # Parse coverage plan
        coverage_data = json.loads(coverage_plan)
        logger.info(f"Calculating expected score for target: {target_score}")
        
        # Get weightage data (using existing tools for now)
        from app.tools import get_chapter_weightage
        
        total_expected_score = 0.0
        total_possible_score = 300.0  # JEE Mains maximum
        chapter_scores = {}
        
        for subject, chapters in coverage_data.items():
            subject_score = 0.0
            
            # Get chapter weightage for this subject
            weightage_data = get_chapter_weightage.invoke({
                "exam": "JEE Mains",
                "subject": subject
            })
            
            for chapter, coverage_percentage in chapters.items():
                # Find weightage for this chapter
                chapter_weightage = 0.0
                for weight_info in weightage_data:
                    if weight_info.get("Chapter") == chapter:
                        chapter_weightage = weight_info.get("Average Weightage", 0.0)
                        break
                
                # Calculate expected score for this chapter
                chapter_expected_score = chapter_weightage * (coverage_percentage / 100.0)
                chapter_scores[f"{subject}_{chapter}"] = {
                    "weightage": chapter_weightage,
                    "coverage": coverage_percentage,
                    "expected_score": chapter_expected_score
                }
                
                subject_score += chapter_expected_score
            
            total_expected_score += subject_score
        
        # Calculate achievability
        achievability_percentage = (total_expected_score / target_score) * 100 if target_score > 0 else 0
        score_gap = target_score - total_expected_score
        
        # Generate recommendations
        recommendations = []
        if total_expected_score >= target_score:
            recommendations.append("✅ Your plan can achieve the target score!")
            recommendations.append(f"Expected score: {total_expected_score:.1f}/{total_possible_score}")
        else:
            recommendations.append(f"⚠️ Score gap: {score_gap:.1f} marks short of target")
            recommendations.append("💡 Consider focusing on high-weightage chapters")
            recommendations.append("🕒 Or extend study time for better coverage")
        
        return {
            "expected_score": round(total_expected_score, 1),
            "target_score": target_score,
            "max_possible_score": total_possible_score,
            "achievability_percentage": round(achievability_percentage, 1),
            "score_gap": round(score_gap, 1),
            "is_achievable": total_expected_score >= target_score,
            "chapter_scores": chapter_scores,
            "recommendations": recommendations,
            "analysis": f"Based on your coverage plan, you can expect to score {total_expected_score:.1f} out of {total_possible_score}. Target: {target_score}"
        }
        
    except Exception as e:
        logger.error(f"Error calculating expected score: {e}", exc_info=True)
        return {
            "expected_score": 0,
            "target_score": target_score,
            "error": str(e),
            "recommendations": ["Error in score calculation. Please check your coverage plan."]
        }

@tool
def optimize_for_target_score(target_score: int, available_hours: int, syllabus: str) -> Dict[str, Any]:
    """Optimize study plan to achieve target score with available time.
    
    Args:
        target_score: User's target score (e.g., 252)
        available_hours: Total available study hours
        syllabus: JSON string of complete syllabus {subject: [chapters]}
    
    Returns:
        Optimized plan with high-priority chapters and score predictions
    """
    try:
        syllabus_data = json.loads(syllabus)
        logger.info(f"Optimizing plan for target score: {target_score} with {available_hours} hours")
        
        # Get weightage data for all subjects
        from app.tools import get_chapter_weightage, get_chapter_flow
        
        all_chapters = []
        
        for subject, chapters in syllabus_data.items():
            # Get weightage data
            weightage_data = get_chapter_weightage.invoke({
                "exam": "JEE Mains",
                "subject": subject
            })
            
            # Get flow data for required hours
            flow_data = get_chapter_flow.invoke({
                "exam": "JEE Mains", 
                "subject": subject
            })
            
            for chapter in chapters:
                chapter_info = {
                    "subject": subject,
                    "chapter": chapter,
                    "weightage": 0.0,
                    "category": "Medium",
                    "required_hours": 10,  # Default
                    "priority_score": 0.0
                }
                
                # Find weightage info
                for weight_info in weightage_data:
                    if weight_info.get("Chapter") == chapter:
                        chapter_info["weightage"] = weight_info.get("Average Weightage", 0.0)
                        chapter_info["category"] = weight_info.get("Chapter Category", "Medium")
                        break
                
                # Find required hours
                for flow_info in flow_data:
                    if flow_info.get("Chapter") == chapter:
                        chapter_info["required_hours"] = flow_info.get("Required Hours", 10)
                        break
                
                # Calculate priority score (Weightage > Category > efficiency)
                category_multiplier = {"High": 3, "Medium": 2, "Low": 1}.get(chapter_info["category"], 2)
                efficiency = chapter_info["weightage"] / max(chapter_info["required_hours"], 1)  # marks per hour
                
                chapter_info["priority_score"] = (
                    chapter_info["weightage"] * 0.5 +  # 50% weightage
                    category_multiplier * 5 * 0.3 +    # 30% category  
                    efficiency * 10 * 0.2               # 20% efficiency
                )
                
                all_chapters.append(chapter_info)
        
        # Sort by priority score (highest first)
        all_chapters.sort(key=lambda x: x["priority_score"], reverse=True)
        
        # Select chapters that fit within available hours and achieve target
        selected_chapters = []
        total_hours_used = 0
        total_expected_score = 0
        
        for chapter in all_chapters:
            if total_hours_used + chapter["required_hours"] <= available_hours:
                selected_chapters.append(chapter)
                total_hours_used += chapter["required_hours"]
                total_expected_score += chapter["weightage"]
                
                # Stop if we've achieved target score
                if total_expected_score >= target_score:
                    break
        
        # Calculate time needed for target score if not achieved
        time_needed_for_target = available_hours
        if total_expected_score < target_score:
            # Estimate additional time needed
            remaining_score = target_score - total_expected_score
            remaining_chapters = [ch for ch in all_chapters if ch not in selected_chapters]
            
            additional_hours = 0
            for chapter in remaining_chapters[:5]:  # Check next 5 best chapters
                additional_hours += chapter["required_hours"]
                if chapter["weightage"] >= remaining_score:
                    break
            
            time_needed_for_target = total_hours_used + additional_hours
        
        # Generate recommendations
        recommendations = []
        if total_expected_score >= target_score:
            recommendations.append(f"✅ Target achievable! Expected score: {total_expected_score:.1f}")
            recommendations.append(f"📚 Focus on {len(selected_chapters)} high-priority chapters")
            recommendations.append(f"⏰ Time utilization: {total_hours_used}/{available_hours} hours")
        else:
            score_gap = target_score - total_expected_score
            recommendations.append(f"⚠️ Target challenging with current time")
            recommendations.append(f"📊 Expected score: {total_expected_score:.1f} (Gap: {score_gap:.1f})")
            recommendations.append(f"⏰ Need ~{time_needed_for_target} hours for target score")
            recommendations.append("💡 Consider: Extend study time OR adjust target score")
        
        return {
            "optimized_plan": {
                subject: [ch["chapter"] for ch in selected_chapters if ch["subject"] == subject]
                for subject in syllabus_data.keys()
            },
            "selected_chapters": selected_chapters,
            "total_expected_score": round(total_expected_score, 1),
            "target_score": target_score,
            "hours_used": total_hours_used,
            "hours_available": available_hours,
            "time_needed_for_target": time_needed_for_target,
            "is_target_achievable": total_expected_score >= target_score,
            "recommendations": recommendations,
            "priority_analysis": f"Selected {len(selected_chapters)} chapters based on weightage and efficiency"
        }
        
    except Exception as e:
        logger.error(f"Error optimizing for target score: {e}", exc_info=True)
        return {
            "error": str(e),
            "recommendations": ["Error in optimization. Please check your inputs."]
        }

@tool
def analyze_score_progress(completed_topics: str, not_completed_topics: str, target_score: int) -> Dict[str, Any]:
    """Analyze current score progress based on completed and pending topics.
    
    Args:
        completed_topics: JSON string of completed topics {subject: {chapter: [topics]}}
        not_completed_topics: JSON string of pending topics {subject: {chapter: [topics]}}
        target_score: User's target score
    
    Returns:
        Score progress analysis with current achievement and remaining potential
    """
    try:
        completed_data = json.loads(completed_topics)
        not_completed_data = json.loads(not_completed_topics)
        
        logger.info(f"Analyzing score progress for target: {target_score}")
        
        # Get weightage data
        from app.tools import get_chapter_weightage, get_topic_priority
        
        current_score = 0.0
        potential_remaining_score = 0.0
        chapter_analysis = {}
        
        # Analyze completed topics
        for subject, chapters in completed_data.items():
            weightage_data = get_chapter_weightage.invoke({
                "exam": "JEE Mains",
                "subject": subject
            })
            
            for chapter, topics in chapters.items():
                # Get total topics for this chapter
                all_topics = get_topic_priority.invoke({
                    "exam": "JEE Mains",
                    "subject": subject,
                    "chapter": chapter
                })
                
                total_topics_in_chapter = len(all_topics) if all_topics else 1
                completed_topics_count = len(topics) if isinstance(topics, list) else 0
                completion_percentage = (completed_topics_count / total_topics_in_chapter) * 100
                
                # Find chapter weightage
                chapter_weightage = 0.0
                for weight_info in weightage_data:
                    if weight_info.get("Chapter") == chapter:
                        chapter_weightage = weight_info.get("Average Weightage", 0.0)
                        break
                
                # Calculate score from this chapter
                chapter_score = chapter_weightage * (completion_percentage / 100.0)
                current_score += chapter_score
                
                chapter_analysis[f"{subject}_{chapter}"] = {
                    "status": "completed",
                    "completion_percentage": completion_percentage,
                    "weightage": chapter_weightage,
                    "score_contribution": chapter_score
                }
        
        # Analyze not completed topics
        for subject, chapters in not_completed_data.items():
            weightage_data = get_chapter_weightage.invoke({
                "exam": "JEE Mains",
                "subject": subject
            })
            
            for chapter, topics in chapters.items():
                # Find chapter weightage
                chapter_weightage = 0.0
                for weight_info in weightage_data:
                    if weight_info.get("Chapter") == chapter:
                        chapter_weightage = weight_info.get("Average Weightage", 0.0)
                        break
                
                potential_remaining_score += chapter_weightage
                
                chapter_analysis[f"{subject}_{chapter}"] = {
                    "status": "pending",
                    "completion_percentage": 0,
                    "weightage": chapter_weightage,
                    "potential_score": chapter_weightage
                }
        
        # Calculate progress metrics
        total_possible_score = current_score + potential_remaining_score
        progress_percentage = (current_score / target_score) * 100 if target_score > 0 else 0
        remaining_score_needed = max(0, target_score - current_score)
        
        # Generate insights
        insights = []
        if current_score >= target_score:
            insights.append(f"🎉 Target achieved! Current score: {current_score:.1f}")
        else:
            insights.append(f"📊 Current progress: {current_score:.1f}/{target_score} ({progress_percentage:.1f}%)")
            insights.append(f"🎯 Remaining needed: {remaining_score_needed:.1f} marks")
            
            if potential_remaining_score >= remaining_score_needed:
                insights.append("✅ Target is still achievable with remaining topics")
            else:
                insights.append("⚠️ Target may be challenging with remaining topics")
                insights.append("💡 Consider focusing on high-weightage pending chapters")
        
        return {
            "current_score": round(current_score, 1),
            "target_score": target_score,
            "progress_percentage": round(progress_percentage, 1),
            "remaining_score_needed": round(remaining_score_needed, 1),
            "potential_remaining_score": round(potential_remaining_score, 1),
            "total_possible_score": round(total_possible_score, 1),
            "is_target_achievable": potential_remaining_score >= remaining_score_needed,
            "chapter_analysis": chapter_analysis,
            "insights": insights,
            "summary": f"You've achieved {current_score:.1f} marks so far. Need {remaining_score_needed:.1f} more for your target of {target_score}."
        }
        
    except Exception as e:
        logger.error(f"Error analyzing score progress: {e}", exc_info=True)
        return {
            "error": str(e),
            "current_score": 0,
            "target_score": target_score,
            "insights": ["Error in score analysis. Please check your data."]
        }