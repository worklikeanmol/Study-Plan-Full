"""
New Score-Oriented Requirement Counsellor
Collects user requirements without auto-generating plans
"""

import logging
from typing import Dict, List, Any, Optional
from langchain_core.tools import tool

logger = logging.getLogger(__name__)

@tool
def collect_user_requirements(user_message: str, existing_requirements: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Collect and acknowledge user requirements without generating plans
    
    Args:
        user_message: Latest user message
        existing_requirements: Previously collected requirements
    
    Returns:
        Dict containing updated requirements and response
    """
    logger.info(f"Collecting requirements from user message: {user_message}")
    
    try:
        # Initialize requirements if not provided
        if existing_requirements is None:
            existing_requirements = {}
        
        # Check if user wants to generate
        generate_triggers = ["generate", "create plan", "make plan", "start planning"]
        wants_to_generate = any(trigger in user_message.lower() for trigger in generate_triggers)
        
        if wants_to_generate:
            return {
                "status": "generate_requested",
                "action": "proceed_to_generation",
                "message": "🔄 **Generating your New Score-Oriented study plan with all requirements...**",
                "requirements": existing_requirements
            }
        
        # Detect requirement types
        requirement_detected = False
        response_parts = []
        
        # Target score changes
        if any(phrase in user_message.lower() for phrase in ["target score", "change target", "score to", "target to"]):
            requirement_detected = True
            response_parts.append("✅ **Target score update** noted")
        
        # Subject priority
        if any(phrase in user_message.lower() for phrase in ["focus on", "priority", "more time for", "emphasize"]):
            requirement_detected = True
            response_parts.append("✅ **Subject priority** preferences noted")
        
        # Chapter coverage
        if any(phrase in user_message.lower() for phrase in ["chapters per month", "chapter coverage", "chapters each month"]):
            requirement_detected = True
            response_parts.append("✅ **Chapter coverage** preferences noted")
        
        # Time allocation
        if any(phrase in user_message.lower() for phrase in ["more time", "less time", "time allocation", "hours for"]):
            requirement_detected = True
            response_parts.append("✅ **Time allocation** preferences noted")
        
        # Weak/Strong areas
        if any(phrase in user_message.lower() for phrase in ["weak in", "strong in", "good at", "bad at", "struggle with"]):
            requirement_detected = True
            response_parts.append("✅ **Strength/Weakness** areas noted")
        
        # Study style preferences
        if any(phrase in user_message.lower() for phrase in ["study style", "revision", "practice", "weekend"]):
            requirement_detected = True
            response_parts.append("✅ **Study style** preferences noted")
        
        # Generate response based on detected requirements
        if requirement_detected:
            response = f"""📋 **Requirements Updated!**

{chr(10).join(response_parts)}

**Current Status:**
- All your preferences are being collected
- No plan generated yet (waiting for your confirmation)

**Next Steps:**
- Add more preferences if needed
- Say **"generate"** when you're ready to create your study plan
- Or ask questions about the planning process

**Ready to generate your plan?** Just say **"generate"**!"""
        
        else:
            # General conversation or clarification
            response = f"""I understand you're interested in creating a New Score-Oriented study plan! 

**To get started, you can tell me:**
- Your target score (e.g., "I want to score 218/300")
- Subject priorities (e.g., "Focus more on Physics")
- Chapter preferences (e.g., "3 chapters per month")
- Time allocation (e.g., "More time for Mathematics")
- Weak/strong areas (e.g., "I'm weak in Organic Chemistry")

**When you're ready:** Say **"generate"** to create your personalized study plan!

**What would you like to specify for your study plan?**"""
        
        return {
            "status": "requirements_collected",
            "action": "wait_for_more_or_generate",
            "message": response,
            "requirements": existing_requirements,
            "requirement_detected": requirement_detected
        }
        
    except Exception as e:
        logger.error(f"Error collecting requirements: {e}")
        return {
            "status": "error",
            "action": "retry",
            "message": f"I encountered an error processing your request: {str(e)}. Please try again.",
            "requirements": existing_requirements or {}
        }


@tool
def summarize_collected_requirements(requirements: Dict[str, Any]) -> Dict[str, Any]:
    """
    Summarize all collected requirements for user confirmation
    
    Args:
        requirements: All collected requirements
    
    Returns:
        Dict containing formatted summary
    """
    logger.info("Summarizing collected requirements")
    
    try:
        if not requirements:
            return {
                "status": "no_requirements",
                "summary": "No specific requirements collected yet.",
                "formatted_summary": "**No specific preferences set.** Using default optimization strategy."
            }
        
        summary_parts = []
        
        # Target score
        if requirements.get("target_score_update"):
            summary_parts.append(f"🎯 **Target Score:** {requirements['target_score_update']}/300")
        
        # Subject priority
        if requirements.get("subject_priority"):
            priority_list = ", ".join([s.title() for s in requirements["subject_priority"]])
            summary_parts.append(f"📊 **Subject Priority:** {priority_list}")
        
        # Subject-wise targets
        if requirements.get("calculated_subject_targets"):
            targets = requirements["calculated_subject_targets"]
            target_text = ", ".join([f"{s.title()}: {score}" for s, score in targets.items()])
            summary_parts.append(f"📈 **Subject Targets:** {target_text}")
        
        # Chapter coverage
        coverage_prefs = requirements.get("chapter_coverage_preferences", {})
        if coverage_prefs.get("chapters_per_month"):
            summary_parts.append(f"📚 **Chapter Coverage:** {coverage_prefs['chapters_per_month']} chapters per month")
        
        # Time allocation
        time_prefs = requirements.get("time_allocation_preferences", {})
        if time_prefs:
            time_text = ", ".join([f"{s.title()}: {pref}" for s, pref in time_prefs.items() if pref])
            summary_parts.append(f"⏰ **Time Allocation:** {time_text}")
        
        # Weak areas
        if requirements.get("weak_areas"):
            weak_text = ", ".join(requirements["weak_areas"])
            summary_parts.append(f"⚠️ **Focus Areas (Weak):** {weak_text}")
        
        # Strong areas
        if requirements.get("strong_areas"):
            strong_text = ", ".join(requirements["strong_areas"])
            summary_parts.append(f"💪 **Strong Areas:** {strong_text}")
        
        # Specific requests
        if requirements.get("specific_requests"):
            requests_text = ", ".join(requirements["specific_requests"][:3])  # Show first 3
            summary_parts.append(f"📝 **Specific Requests:** {requests_text}")
        
        formatted_summary = "\n".join(summary_parts) if summary_parts else "**Using default optimization strategy**"
        
        return {
            "status": "success",
            "summary": summary_parts,
            "formatted_summary": formatted_summary,
            "requirement_count": len([p for p in summary_parts if p])
        }
        
    except Exception as e:
        logger.error(f"Error summarizing requirements: {e}")
        return {
            "status": "error",
            "summary": [],
            "formatted_summary": "Error summarizing requirements",
            "requirement_count": 0
        }


@tool
def check_generation_readiness(user_message: str, requirements: Dict[str, Any]) -> Dict[str, Any]:
    """
    Check if user is ready to generate plan or wants to add more requirements
    
    Args:
        user_message: Latest user message
        requirements: Current requirements
    
    Returns:
        Dict indicating readiness status
    """
    logger.info(f"Checking generation readiness for: {user_message}")
    
    try:
        # Check for explicit generation requests
        generate_triggers = [
            "generate", "create plan", "make plan", "start planning", 
            "build plan", "generate plan", "create my plan", "let's start"
        ]
        
        wants_to_generate = any(trigger in user_message.lower() for trigger in generate_triggers)
        
        if wants_to_generate:
            # Check if we have minimum requirements
            has_basic_info = bool(requirements)
            
            return {
                "status": "ready_to_generate",
                "action": "proceed_to_generation",
                "has_requirements": has_basic_info,
                "message": "🔄 **Proceeding to plan generation with your requirements...**"
            }
        
        # Check for requirement additions
        requirement_keywords = [
            "target", "score", "focus", "priority", "chapters", "time", 
            "weak", "strong", "prefer", "want", "need", "change"
        ]
        
        adding_requirements = any(keyword in user_message.lower() for keyword in requirement_keywords)
        
        if adding_requirements:
            return {
                "status": "adding_requirements",
                "action": "collect_more_requirements",
                "message": "📝 **Adding to your requirements...**"
            }
        
        # General conversation
        return {
            "status": "conversing",
            "action": "provide_guidance",
            "message": "💬 **I'm here to help! Tell me your preferences or say 'generate' when ready.**"
        }
        
    except Exception as e:
        logger.error(f"Error checking generation readiness: {e}")
        return {
            "status": "error",
            "action": "retry",
            "message": "Error processing your request. Please try again."
        }