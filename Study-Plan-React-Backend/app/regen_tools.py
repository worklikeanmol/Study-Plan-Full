from langchain_core.tools import tool
import os
from supabase import create_client, Client
from dotenv import load_dotenv
from app.utils import get_logger
from typing import Dict, Any, Optional

load_dotenv()
logger = get_logger(__name__)

# Initialize Supabase client
supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")

if not supabase_url or not supabase_key:
    logger.warning("Supabase URL or Key not found. Using mock data for regeneration tools.")
    supabase = None
else:
    try:
        supabase: Client = create_client(supabase_url, supabase_key)
        logger.info("Supabase client initialized successfully for regeneration tools.")
    except Exception as e:
        logger.error(f"Failed to initialize Supabase client for regeneration: {e}", exc_info=True)
        supabase = None

@tool
def check_user_exists(user_id: str) -> Dict[str, Any]:
    """Check if user exists in User_Table and return their data if found."""
    if not supabase:
        logger.warning("Supabase not available. Using mock user check.")
        # Mock data for testing
        if user_id == "existing_user":
            return {
                "exists": True,
                "user_data": {
                    "user_id": "existing_user",
                    "state_msg": {"user_data": {"target_exam": "JEE Mains", "number_of_months": 8}},
                    "study_plan": {"insights": "Previous plan insights..."},
                    "created_at": "2024-01-01"
                }
            }
        return {"exists": False, "user_data": None}
    
    try:
        logger.info(f"Checking if user exists: {user_id}")
        response = supabase.table("User_Table").select("*").eq("user_id", user_id).execute()
        
        if response.data and len(response.data) > 0:
            logger.info(f"User {user_id} found in database")
            return {
                "exists": True,
                "user_data": response.data[0]
            }
        else:
            logger.info(f"User {user_id} not found in database")
            return {"exists": False, "user_data": None}
            
    except Exception as e:
        logger.error(f"Error checking user existence: {e}", exc_info=True)
        return {"exists": False, "user_data": None, "error": str(e)}

@tool
def get_user_performance(user_id: str) -> Dict[str, Any]:
    """Get user performance data from User_Performance table."""
    if not supabase:
        logger.warning("Supabase not available. Using mock performance data.")
        # Mock performance data for testing
        return {
            "found": True,
            "performance_data": {
                "user_id": user_id,
                "completed_topics": {
                    "physics": {
                        "Chapter_1": ["topic_1", "topic_2"],
                        "Chapter_2": ["topic_a"]
                    },
                    "chemistry": {
                        "Chapter_1": ["topic_x"]
                    },
                    "mathematics": {
                        "Chapter_1": ["topic_y"]
                    }
                },
                "not_completed_topics": {
                    "physics": {
                        "Chapter_1": ["topic_3"],
                        "Chapter_3": ["topic_1", "topic_2", "topic_3"]
                    },
                    "chemistry": {
                        "Chapter_2": ["topic_a", "topic_b"],
                        "Chapter_3": ["topic_1", "topic_2"]
                    },
                    "mathematics": {
                        "Chapter_2": ["topic_1", "topic_2"],
                        "Chapter_3": ["topic_1", "topic_2", "topic_3"]
                    }
                },
                "overall_progress_percentage": 35.5,
                "subject_wise_progress": {
                    "physics": 40.0,
                    "chemistry": 25.0,
                    "mathematics": 42.0
                },
                "performance_metrics": {
                    "total_study_days": 30,
                    "average_daily_hours": 5.5,
                    "consistency_score": 78.5,
                    "weak_areas": ["chemistry", "physics_chapter_3"],
                    "strong_areas": ["mathematics_chapter_1"]
                },
                "last_updated": "2024-01-30"
            }
        }
    
    try:
        logger.info(f"Fetching performance data for user: {user_id}")
        response = supabase.table("User_Performance").select("*").eq("user_id", user_id).execute()
        
        if response.data and len(response.data) > 0:
            logger.info(f"Performance data found for user {user_id}")
            return {
                "found": True,
                "performance_data": response.data[0]
            }
        else:
            logger.info(f"No performance data found for user {user_id}")
            return {"found": False, "performance_data": None}
            
    except Exception as e:
        logger.error(f"Error fetching user performance: {e}", exc_info=True)
        return {"found": False, "performance_data": None, "error": str(e)}

@tool
def analyze_topic_importance(exam: str, subject: str, topics: str) -> Dict[str, Any]:
    """Analyze the importance of not completed topics for exam preparation.
    
    Args:
        exam: The target exam name (e.g., 'JEE Mains')
        subject: The subject name (e.g., 'Physics')
        topics: Comma-separated string of topic names to analyze
    
    Returns:
        Dictionary containing analysis and summary of topic importance
    """
    if not supabase:
        logger.warning("Using mock topic importance analysis.")
        # Parse topics string into list
        topic_list = [t.strip() for t in topics.split(',') if t.strip()]
        # Mock analysis
        analysis = {}
        for topic in topic_list:
            # Simulate importance scoring
            if "topic_1" in topic or "Chapter_1" in topic:
                analysis[topic] = {
                    "importance_score": 9,
                    "importance_level": "Critical",
                    "exam_weightage": "High",
                    "dependency_impact": "High - Foundation topic",
                    "recommendation": "Must complete before proceeding"
                }
            elif "topic_2" in topic:
                analysis[topic] = {
                    "importance_score": 7,
                    "importance_level": "Important",
                    "exam_weightage": "Medium",
                    "dependency_impact": "Medium - Builds on other topics",
                    "recommendation": "Should complete in parallel"
                }
            else:
                analysis[topic] = {
                    "importance_score": 5,
                    "importance_level": "Moderate",
                    "exam_weightage": "Low",
                    "dependency_impact": "Low - Independent topic",
                    "recommendation": "Can be deferred if needed"
                }
        
        return {
            "analysis": analysis,
            "summary": {
                "critical_topics": len([t for t in topic_list if "topic_1" in t]),
                "important_topics": len([t for t in topic_list if "topic_2" in t]),
                "moderate_topics": len([t for t in topic_list if "topic_3" in t]),
                "overall_recommendation": "Focus on critical topics first, complete important ones in parallel"
            }
        }
    
    try:
        # Parse topics string into list
        topic_list = [t.strip() for t in topics.split(',') if t.strip()]
        logger.info(f"Analyzing topic importance for {exam} {subject}: {topic_list}")
        
        # This would typically involve complex analysis based on:
        # 1. Topic priority from database
        # 2. Chapter dependencies
        # 3. Exam weightage patterns
        # 4. Learning progression requirements
        
        # For now, implementing a simplified version
        analysis = {}
        for topic in topic_list:
            # Get topic priority from existing tools
            from app.tools import get_topic_priority
            topic_data = get_topic_priority.invoke({
                "exam": exam,
                "subject": subject,
                "chapter": topic.split("_")[0] if "_" in topic else "Chapter_1"
            })
            
            if topic_data:
                priority = topic_data[0].get("Topic Priority", "Medium") if topic_data else "Medium"
                if priority == "High":
                    importance_score = 9
                    importance_level = "Critical"
                    recommendation = "Must complete before proceeding"
                elif priority == "Medium":
                    importance_score = 7
                    importance_level = "Important"
                    recommendation = "Should complete in parallel"
                else:
                    importance_score = 5
                    importance_level = "Moderate"
                    recommendation = "Can be deferred if needed"
                
                analysis[topic] = {
                    "importance_score": importance_score,
                    "importance_level": importance_level,
                    "exam_weightage": priority,
                    "dependency_impact": f"{priority} - Based on topic priority",
                    "recommendation": recommendation
                }
            else:
                # Default analysis if no data found
                analysis[topic] = {
                    "importance_score": 6,
                    "importance_level": "Important",
                    "exam_weightage": "Medium",
                    "dependency_impact": "Medium - Standard topic",
                    "recommendation": "Include in regenerated plan"
                }
        
        # Generate summary
        critical_count = len([t for t, data in analysis.items() if data["importance_score"] >= 8])
        important_count = len([t for t, data in analysis.items() if 6 <= data["importance_score"] < 8])
        moderate_count = len([t for t, data in analysis.items() if data["importance_score"] < 6])
        
        return {
            "analysis": analysis,
            "summary": {
                "critical_topics": critical_count,
                "important_topics": important_count,
                "moderate_topics": moderate_count,
                "total_topics": len(topic_list),
                "overall_recommendation": "Prioritize critical topics, include important ones in parallel planning"
            }
        }
        
    except Exception as e:
        logger.error(f"Error analyzing topic importance: {e}", exc_info=True)
        return {"analysis": {}, "summary": {}, "error": str(e)}

@tool
def generate_progress_insights(performance_data: Dict[str, Any], previous_plan: Dict[str, Any]) -> str:
    """Generate detailed insights about user's progress and study plan effectiveness."""
    try:
        if not performance_data:
            return "No performance data available for analysis."
        
        # Extract key metrics
        overall_progress = performance_data.get("overall_progress_percentage", 0)
        subject_progress = performance_data.get("subject_wise_progress", {})
        completed_topics = performance_data.get("completed_topics", {})
        not_completed_topics = performance_data.get("not_completed_topics", {})
        performance_metrics = performance_data.get("performance_metrics", {})
        
        # Calculate completion statistics
        total_completed = sum(len(topics) for chapters in completed_topics.values() 
                            for topics in chapters.values())
        total_not_completed = sum(len(topics) for chapters in not_completed_topics.values() 
                                for topics in chapters.values())
        
        # Generate insights
        insights = f"""📊 **PROGRESS ANALYSIS & INSIGHTS**

**Overall Performance:**
• Progress: {overall_progress:.1f}% completed
• Topics Completed: {total_completed}
• Topics Pending: {total_not_completed}
• Study Consistency: {performance_metrics.get('consistency_score', 'N/A')}%

**Subject-wise Progress:**"""
        
        for subject, progress in subject_progress.items():
            insights += f"\n• {subject.title()}: {progress:.1f}%"
            
            # Add subject-specific insights
            if progress >= 70:
                insights += " ✅ Excellent progress!"
            elif progress >= 50:
                insights += " 🟡 Good progress, keep going"
            elif progress >= 30:
                insights += " 🟠 Needs more focus"
            else:
                insights += " 🔴 Requires immediate attention"
        
        insights += f"""

**Study Habits Analysis:**
• Average Daily Hours: {performance_metrics.get('average_daily_hours', 'N/A')} hours
• Total Study Days: {performance_metrics.get('total_study_days', 'N/A')} days
• Consistency Score: {performance_metrics.get('consistency_score', 'N/A')}%

**Strengths & Areas for Improvement:**"""
        
        strong_areas = performance_metrics.get('strong_areas', [])
        weak_areas = performance_metrics.get('weak_areas', [])
        
        if strong_areas:
            insights += f"\n✅ **Strong Areas:** {', '.join(strong_areas)}"
        if weak_areas:
            insights += f"\n⚠️ **Needs Attention:** {', '.join(weak_areas)}"
        
        # Add recommendations based on progress
        insights += f"""

**Key Recommendations:**"""
        
        if overall_progress < 30:
            insights += "\n• 🎯 Focus on building consistent study habits"
            insights += "\n• 📚 Prioritize foundational topics"
            insights += "\n• ⏰ Consider adjusting daily study hours"
        elif overall_progress < 60:
            insights += "\n• 🚀 Great momentum! Maintain consistency"
            insights += "\n• 🎯 Focus on weak subjects while maintaining strong ones"
            insights += "\n• 📈 Consider increasing difficulty level"
        else:
            insights += "\n• 🏆 Excellent progress! You're on track"
            insights += "\n• 🎯 Focus on advanced topics and practice"
            insights += "\n• 📝 Start intensive revision and mock tests"
        
        # Add specific topic recommendations
        if not_completed_topics:
            insights += f"\n\n**Pending Topics Analysis:**"
            for subject, chapters in not_completed_topics.items():
                total_pending = sum(len(topics) for topics in chapters.values())
                chapter_count = len(chapters)
                insights += f"\n• {subject.title()}: {total_pending} topics across {chapter_count} chapters pending"
        
        insights += f"""

**Next Steps:**
1. Review and prioritize pending critical topics
2. Decide on plan extension vs. new plan creation
3. Adjust study hours if needed
4. Set realistic goals for the next phase"""
        
        return insights
        
    except Exception as e:
        logger.error(f"Error generating progress insights: {e}", exc_info=True)
        return f"Error generating insights: {str(e)}"

@tool
def save_regenerated_plan(user_id: str, state_message: dict, study_plan: dict) -> str:
    """Save regenerated study plan and updated state to User_Table, overwriting previous plan."""
    if not supabase:
        logger.warning("Supabase not available. Cannot save regenerated plan to database.")
        return "Database not available - regenerated plan not saved"
    
    try:
        logger.info(f"Saving regenerated plan for user: {user_id}")
        
        # Prepare data for update (overwrite)
        plan_data = {
            "user_id": user_id,
            "state_msg": state_message,
            "study_plan": study_plan
        }
        
        # Use upsert to overwrite existing plan
        response = supabase.table("User_Table").upsert(plan_data).execute()
        
        if response.data:
            logger.info(f"Successfully saved regenerated plan for user: {user_id}")
            return f"Regenerated plan successfully saved for user {user_id}"
        else:
            logger.error(f"Failed to save regenerated plan for user {user_id}: No data returned")
            return f"Failed to save regenerated plan for user {user_id}"
            
    except Exception as e:
        logger.error(f"Error saving regenerated plan for user {user_id}: {e}", exc_info=True)
        return f"Error saving regenerated plan: {str(e)}"

@tool
def update_user_performance(user_id: str, performance_data: dict) -> str:
    """Update user performance data in User_Performance table."""
    if not supabase:
        logger.warning("Supabase not available. Cannot update user performance.")
        return "Database not available - performance not updated"
    
    try:
        logger.info(f"Updating performance data for user: {user_id}")
        
        # Use upsert to handle both insert and update cases
        response = supabase.table("User_Performance").upsert(performance_data).execute()
        
        if response.data:
            logger.info(f"Successfully updated performance for user: {user_id}")
            return f"Performance data successfully updated for user {user_id}"
        else:
            logger.error(f"Failed to update performance for user {user_id}: No data returned")
            return f"Failed to update performance for user {user_id}"
            
    except Exception as e:
        logger.error(f"Error updating performance for user {user_id}: {e}", exc_info=True)
        return f"Error updating performance: {str(e)}"