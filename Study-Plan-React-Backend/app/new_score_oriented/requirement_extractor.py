"""
New Score-Oriented Requirement Extractor
Extracts user preferences and requirements for new_score_oriented study plans
"""

import json
import logging
from typing import Dict, List, Any, Optional
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
import os

logger = logging.getLogger(__name__)

@tool
def extract_new_score_oriented_requirements(chat_context: Dict[str, Any], user_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract user requirements and preferences for new_score_oriented study plans
    
    Args:
        chat_context: Complete chat conversation context
        user_data: User's basic information (target_score, exam, duration, etc.)
    
    Returns:
        Dict containing extracted requirements
    """
    logger.info("Extracting requirements for new_score_oriented plan")
    
    try:
        # Combine all user messages from chat context
        all_user_messages = []
        for turn_key, turn_data in chat_context.items():
            if hasattr(turn_data, 'user_message') and turn_data.user_message:
                all_user_messages.append(turn_data.user_message)
            elif isinstance(turn_data, dict) and 'user_message' in turn_data:
                all_user_messages.append(turn_data['user_message'])
        
        combined_user_input = " ".join(all_user_messages)
        logger.info(f"Combined user input: {combined_user_input}")
        
        # Create LLM for requirement extraction
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=os.getenv("GOOGLE_API_KEY"),
            temperature=0.1
        )
        
        # Create comprehensive extraction prompt
        extraction_prompt = f"""
You are an expert study plan analyzer. Extract user preferences and requirements from their conversation for a New Score-Oriented study plan.

**USER INFORMATION:**
- Target Exam: {user_data.get('target_exam', 'Not specified')}
- Current Target Score: {user_data.get('target_score', 'Not specified')}/300
- Duration: {user_data.get('number_of_months', 'Not specified')} months
- Study Hours: {user_data.get('hours_per_day', 'Not specified')} hours/day

**USER CONVERSATION:**
"{combined_user_input}"

**EXTRACTION REQUIREMENTS:**
Analyze the conversation and extract the following preferences. Pay special attention to target score changes and subject priorities. Return ONLY a valid JSON object with these exact keys:

{{
    "target_score_update": "number if user wants to change target score (e.g., 'change target to 218' → 218)",
    "subject_priority": ["subject1", "subject2", "subject3"],
    "subject_wise_targets": {{
        "physics": "target score for physics if specified",
        "chemistry": "target score for chemistry if specified",
        "mathematics": "target score for mathematics if specified"
    }},
    "chapter_priority": {{
        "physics": ["chapter1", "chapter2"],
        "chemistry": ["chapter1", "chapter2"], 
        "mathematics": ["chapter1", "chapter2"]
    }},
    "time_allocation_preferences": {{
        "physics": "more/less/standard",
        "chemistry": "more/less/standard",
        "mathematics": "more/less/standard"
    }},
    "chapter_coverage_preferences": {{
        "chapters_per_month": "number if specified (e.g., '3 chapters per month' → 3)",
        "focus_areas": ["area1", "area2"],
        "difficulty_preference": "high/medium/low priority chapters first"
    }},
    "study_style_preferences": {{
        "revision_intensity": "high/medium/low",
        "practice_focus": "pyq/dpp/both",
        "weekend_preference": "study/practice/mixed"
    }},
    "specific_requests": [
        "any specific requests like 'change target score to 218', '3 chapters per month', 'more time for physics', etc."
    ],
    "weak_areas": ["subject or chapter areas mentioned as weak"],
    "strong_areas": ["subject or chapter areas mentioned as strong"],
    "exam_strategy": {{
        "target_breakdown": "if user mentions subject-wise targets",
        "preparation_approach": "intensive/balanced/focused"
    }},
    "regeneration_reason": "why user wants changes (e.g., 'target_score_change', 'chapter_coverage_change', 'subject_priority_change')"
}}

**EXTRACTION GUIDELINES:**
1. **Target Score Update**: Look for phrases like "change target to 218", "update score to 240", "target score 218"
2. **Subject Priority**: Order subjects by user's stated preference or focus
3. **Subject-wise Targets**: If user mentions specific scores for subjects
4. **Chapter Priority**: Specific chapters mentioned as important/priority
5. **Time Allocation**: Any mentions of wanting more/less time for subjects
6. **Chapter Coverage**: Requests like "3 chapters per month", "2 chapters per month"
7. **Study Style**: Preferences for revision intensity, practice focus
8. **Specific Requests**: Direct requests for modifications or preferences
9. **Weak/Strong Areas**: Subjects or topics mentioned as strengths/weaknesses
10. **Exam Strategy**: Overall approach or target breakdown preferences
11. **Regeneration Reason**: Why the user wants changes

**IMPORTANT:**
- If no preference is mentioned for a field, use empty array [] or empty object {{}} or null
- Extract only what is explicitly mentioned or clearly implied
- For subject_priority, use: ["physics", "chemistry", "mathematics"]
- For chapters, use format: "Chapter_1", "Chapter_2", etc.
- For target_score_update, extract the NUMBER only (e.g., 218, 240, 200)
- Return ONLY the JSON object, no additional text

**EXAMPLES:**
- "change my target score to 218" → target_score_update: 218, specific_requests: ["change target score to 218"]
- "I want to focus more on Physics" → subject_priority: ["physics", "chemistry", "mathematics"]
- "3 chapters per month" → chapter_coverage_preferences: {{"chapters_per_month": 3}}
- "I'm weak in Organic Chemistry" → weak_areas: ["organic chemistry"]
- "More time for Mathematics" → time_allocation_preferences: {{"mathematics": "more"}}
- "I want 80 marks in Physics" → subject_wise_targets: {{"physics": 80}}
"""
        
        # Get LLM response
        response = llm.invoke(extraction_prompt)
        response_text = response.content if hasattr(response, 'content') else str(response)
        
        logger.info(f"LLM raw response: {response_text}")
        
        # Parse JSON response
        try:
            # Clean the response to extract JSON
            json_start = response_text.find('{')
            json_end = response_text.rfind('}') + 1
            
            if json_start != -1 and json_end != -1:
                json_text = response_text[json_start:json_end]
                parsed_data = json.loads(json_text)
                logger.info(f"Parsed JSON data: {parsed_data}")
            else:
                raise ValueError("No JSON found in response")
                
        except (json.JSONDecodeError, ValueError) as e:
            logger.error(f"Error parsing JSON response: {e}")
            # Return default structure
            parsed_data = {
                "subject_priority": [],
                "chapter_priority": {},
                "time_allocation_preferences": {},
                "chapter_coverage_preferences": {},
                "study_style_preferences": {},
                "specific_requests": [],
                "weak_areas": [],
                "strong_areas": [],
                "exam_strategy": {}
            }
        
        # Validate and clean the extracted data
        validated_requirements = _validate_requirements(parsed_data, user_data)
        
        # Calculate subject-wise targets if target score update is provided
        if validated_requirements.get("target_score_update"):
            target_calculation = calculate_subject_wise_targets.invoke({
                "total_target": validated_requirements["target_score_update"],
                "subject_priority": validated_requirements.get("subject_priority", ["physics", "chemistry", "mathematics"]),
                "user_preferences": validated_requirements
            })
            
            if target_calculation.get("status") == "success":
                validated_requirements["calculated_subject_targets"] = target_calculation["subject_targets"]
                logger.info(f"Calculated subject targets: {target_calculation['subject_targets']}")
        
        logger.info(f"Final extracted requirements: {validated_requirements}")
        
        return {
            "status": "success",
            "requirements": validated_requirements,
            "extraction_source": "llm_analysis",
            "user_input_analyzed": combined_user_input
        }
        
    except Exception as e:
        logger.error(f"Error extracting requirements: {e}")
        return {
            "status": "error",
            "message": str(e),
            "requirements": _get_default_requirements(),
            "extraction_source": "fallback"
        }


def _validate_requirements(parsed_data: Dict[str, Any], user_data: Dict[str, Any]) -> Dict[str, Any]:
    """Validate and clean extracted requirements"""
    
    # Ensure all required keys exist
    default_structure = {
        "subject_priority": [],
        "chapter_priority": {},
        "time_allocation_preferences": {},
        "chapter_coverage_preferences": {},
        "study_style_preferences": {},
        "specific_requests": [],
        "weak_areas": [],
        "strong_areas": [],
        "exam_strategy": {}
    }
    
    # Merge with defaults
    for key, default_value in default_structure.items():
        if key not in parsed_data:
            parsed_data[key] = default_value
    
    # Validate subject_priority
    valid_subjects = ["physics", "chemistry", "mathematics"]
    if parsed_data["subject_priority"]:
        parsed_data["subject_priority"] = [
            subj.lower() for subj in parsed_data["subject_priority"] 
            if subj.lower() in valid_subjects
        ]
    
    # If no subject priority specified, use default order
    if not parsed_data["subject_priority"]:
        parsed_data["subject_priority"] = valid_subjects
    
    # Validate chapter_priority structure
    if parsed_data["chapter_priority"]:
        validated_chapters = {}
        for subject, chapters in parsed_data["chapter_priority"].items():
            if subject.lower() in valid_subjects and isinstance(chapters, list):
                validated_chapters[subject.lower()] = chapters
        parsed_data["chapter_priority"] = validated_chapters
    
    # Add user_data context
    parsed_data["user_context"] = {
        "target_score": user_data.get("target_score"),
        "target_exam": user_data.get("target_exam"),
        "duration_months": user_data.get("number_of_months"),
        "hours_per_day": user_data.get("hours_per_day")
    }
    
    return parsed_data


@tool
def calculate_subject_wise_targets(total_target: int, subject_priority: List[str], user_preferences: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculate subject-wise target score distribution
    
    Args:
        total_target: Total target score (e.g., 218)
        subject_priority: Priority order of subjects
        user_preferences: User preferences for subject allocation
    
    Returns:
        Dict with subject-wise target distribution
    """
    logger.info(f"Calculating subject-wise targets for total: {total_target}")
    
    try:
        # Default equal distribution
        base_score_per_subject = total_target // 3
        remainder = total_target % 3
        
        # Initialize with equal distribution
        subject_targets = {
            "physics": base_score_per_subject,
            "chemistry": base_score_per_subject,
            "mathematics": base_score_per_subject
        }
        
        # Distribute remainder based on priority
        if remainder > 0:
            for i in range(remainder):
                if i < len(subject_priority):
                    subject_targets[subject_priority[i]] += 1
        
        # Apply user preferences for time allocation
        time_preferences = user_preferences.get("time_allocation_preferences", {})
        
        if time_preferences:
            # Adjust based on "more" or "less" preferences
            adjustments = {}
            total_adjustment = 0
            
            for subject, preference in time_preferences.items():
                if preference == "more":
                    adjustment = min(8, total_target // 20)  # Up to 8 marks more
                    adjustments[subject] = adjustment
                    total_adjustment += adjustment
                elif preference == "less":
                    adjustment = min(6, total_target // 25)  # Up to 6 marks less
                    adjustments[subject] = -adjustment
                    total_adjustment -= adjustment
            
            # Apply adjustments
            for subject, adjustment in adjustments.items():
                subject_targets[subject] += adjustment
            
            # Redistribute any imbalance
            if total_adjustment != 0:
                # Find subjects without explicit preferences to balance
                neutral_subjects = [s for s in subject_targets.keys() if s not in time_preferences]
                if neutral_subjects:
                    balance_per_subject = -total_adjustment // len(neutral_subjects)
                    for subject in neutral_subjects:
                        subject_targets[subject] += balance_per_subject
        
        # Ensure no negative scores and total matches
        for subject in subject_targets:
            subject_targets[subject] = max(20, subject_targets[subject])  # Minimum 20 marks per subject
        
        # Final adjustment to match total
        current_total = sum(subject_targets.values())
        if current_total != total_target:
            diff = total_target - current_total
            # Adjust the highest priority subject
            if subject_priority:
                subject_targets[subject_priority[0]] += diff
        
        logger.info(f"Subject-wise targets calculated: {subject_targets}")
        
        return {
            "status": "success",
            "subject_targets": subject_targets,
            "total_target": total_target,
            "distribution_method": "priority_based" if time_preferences else "equal"
        }
        
    except Exception as e:
        logger.error(f"Error calculating subject targets: {e}")
        # Fallback to equal distribution
        equal_score = total_target // 3
        return {
            "status": "error",
            "message": str(e),
            "subject_targets": {
                "physics": equal_score,
                "chemistry": equal_score,
                "mathematics": total_target - (2 * equal_score)
            },
            "total_target": total_target,
            "distribution_method": "equal_fallback"
        }


def _get_default_requirements() -> Dict[str, Any]:
    """Return default requirements structure"""
    return {
        "target_score_update": None,
        "subject_priority": ["physics", "chemistry", "mathematics"],
        "subject_wise_targets": {},
        "chapter_priority": {},
        "time_allocation_preferences": {},
        "chapter_coverage_preferences": {},
        "study_style_preferences": {},
        "specific_requests": [],
        "weak_areas": [],
        "strong_areas": [],
        "exam_strategy": {},
        "regeneration_reason": None,
        "user_context": {}
    }


@tool
def apply_requirements_to_plan(requirements: Dict[str, Any], base_plan: Dict[str, Any]) -> Dict[str, Any]:
    """
    Apply extracted requirements to modify the base study plan
    
    Args:
        requirements: Extracted user requirements
        base_plan: Base study plan to modify
    
    Returns:
        Modified plan with user requirements applied
    """
    logger.info("Applying user requirements to new_score_oriented plan")
    
    try:
        modified_plan = base_plan.copy()
        user_requirements = requirements.get("requirements", {})
        
        # Apply subject priority
        subject_priority = user_requirements.get("subject_priority", [])
        if subject_priority:
            logger.info(f"Applying subject priority: {subject_priority}")
            modified_plan["subject_priority_order"] = subject_priority
        
        # Apply chapter coverage preferences
        coverage_prefs = user_requirements.get("chapter_coverage_preferences", {})
        if coverage_prefs.get("chapters_per_month"):
            chapters_per_month = coverage_prefs["chapters_per_month"]
            logger.info(f"Applying chapters per month preference: {chapters_per_month}")
            modified_plan["chapters_per_month_preference"] = chapters_per_month
        
        # Apply time allocation preferences
        time_prefs = user_requirements.get("time_allocation_preferences", {})
        if time_prefs:
            logger.info(f"Applying time allocation preferences: {time_prefs}")
            modified_plan["time_allocation_preferences"] = time_prefs
        
        # Apply specific requests
        specific_requests = user_requirements.get("specific_requests", [])
        if specific_requests:
            logger.info(f"Applying specific requests: {specific_requests}")
            modified_plan["user_specific_requests"] = specific_requests
        
        # Apply weak/strong areas
        weak_areas = user_requirements.get("weak_areas", [])
        strong_areas = user_requirements.get("strong_areas", [])
        if weak_areas or strong_areas:
            modified_plan["focus_areas"] = {
                "weak_areas": weak_areas,
                "strong_areas": strong_areas
            }
        
        # Store complete requirements for reference
        modified_plan["user_requirements"] = user_requirements
        
        return {
            "status": "success",
            "modified_plan": modified_plan,
            "applied_preferences": {
                "subject_priority": bool(subject_priority),
                "chapter_coverage": bool(coverage_prefs),
                "time_allocation": bool(time_prefs),
                "specific_requests": bool(specific_requests),
                "focus_areas": bool(weak_areas or strong_areas)
            }
        }
        
    except Exception as e:
        logger.error(f"Error applying requirements to plan: {e}")
        return {
            "status": "error",
            "message": str(e),
            "modified_plan": base_plan
        }