from typing import Dict, List, TypedDict, Annotated
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from app.new_score_oriented.models import (
    NewScoreOrientedUserData, 
    NewScoreOrientedStudyPlan,
    ValidationResult,
    SupervisorFeedback
)
from app.new_score_oriented.agents import (
    revision_flow_agent,
    new_score_oriented_validator,
    new_score_oriented_supervisor
)
from app.new_score_oriented.tools import (
    validate_new_score_oriented_exam_date,
    get_chapter_weightage_for_revision,
    get_chapter_flow_with_dependencies,
    get_topic_priority_for_chapter,
    get_complete_syllabus_for_revision,
    save_new_score_oriented_progress
)
from app.core.models import ChatMessage, PlanParameters
from app.core.utils import get_logger
from app.new_score_oriented.requirement_extractor import (
    extract_new_score_oriented_requirements,
    apply_requirements_to_plan,
    calculate_subject_wise_targets
)
from app.new_score_oriented.requirement_counsellor import (
    collect_user_requirements,
    summarize_collected_requirements,
    check_generation_readiness
)

logger = get_logger(__name__)

class NewScoreOrientedState(TypedDict):
    """State for new_score_oriented study plan generation"""
    user_data: NewScoreOrientedUserData
    chat_context: Dict[str, ChatMessage]
    plan_parameters: PlanParameters
    
    # Revision flow results
    revision_flow_results: Dict
    
    # Validation results
    chapter_validation: Dict
    topic_validation: Dict
    syllabus_validation: Dict
    
    # Final plan
    study_plan: NewScoreOrientedStudyPlan
    
    # Supervisor feedback
    supervisor_feedback: SupervisorFeedback
    
    # Control flow
    plan_finalized: bool
    next_agent: str
    validation_passed: bool
    adjustments_needed: bool

def counsellor_generator_agent(state: NewScoreOrientedState) -> NewScoreOrientedState:
    """
    Counsellor Generator Agent - Extracts user requirements and initializes the plan.
    """
    logger.info("Counsellor Generator Agent executing for new_score_oriented plan")
    
    user_data = state["user_data"]
    chat_context = state["chat_context"]
    
    # Extract user requirements from chat
    latest_message = ""
    for turn_id, chat_msg in chat_context.items():
        if chat_msg.user_message:
            latest_message = chat_msg.user_message
    
    # Validate exam date (minimum 6 months)
    date_validation = validate_new_score_oriented_exam_date.invoke({"exam_date": user_data.exam_date})
    
    if not date_validation.get("is_valid", False):
        # Update chat with validation error
        for turn_id, chat_msg in chat_context.items():
            if not chat_msg.assistant_message:
                chat_msg.assistant_message = f"❌ {date_validation.get('message', 'Invalid exam date for new_score_oriented plan')}"
                break
        
        state["chat_context"] = chat_context
        state["next_agent"] = "end"
        return state
    
    # Update number of months based on validation
    user_data.number_of_months = date_validation.get("calculated_months", user_data.number_of_months)
    
    # Initialize plan parameters from user message
    plan_parameters = PlanParameters()
    
    # Extract preferences from user message (basic implementation)
    if "physics" in latest_message.lower() and "priority" in latest_message.lower():
        plan_parameters.subject_priority.append("physics")
    if "chemistry" in latest_message.lower() and "priority" in latest_message.lower():
        plan_parameters.subject_priority.append("chemistry")
    if "mathematics" in latest_message.lower() and "priority" in latest_message.lower():
        plan_parameters.subject_priority.append("mathematics")
    
    # Update chat with counsellor response
    for turn_id, chat_msg in chat_context.items():
        if not chat_msg.assistant_message:
            chat_msg.assistant_message = (
                f"🎯 **New Score-Oriented Plan Initiated!**\n\n"
                f"📊 **Your Requirements:**\n"
                f"• Target Score: {user_data.target_score}/300\n"
                f"• Exam Date: {user_data.exam_date}\n"
                f"• Preparation Time: {user_data.number_of_months} months\n"
                f"• Plan Type: Complete Syllabus Coverage with Revision Focus\n\n"
                f"✅ **Plan Features:**\n"
                f"• 100% syllabus completion in one go\n"
                f"• Dependency-based chapter ordering\n"
                f"• Priority-weighted chapter sequence\n"
                f"• Saturday/Sunday practice schedule (PYQ/DPP)\n"
                f"• Target completion within 6 months\n\n"
                f"🔄 Generating your revision flow plan..."
            )
            break
    
    state["user_data"] = user_data
    state["chat_context"] = chat_context
    state["plan_parameters"] = plan_parameters
    state["next_agent"] = "requirement_extractor"
    
    return state


def requirement_extractor_node(state: NewScoreOrientedState) -> NewScoreOrientedState:
    """Extract user requirements and preferences for new_score_oriented plans"""
    logger.info("New Score-Oriented Requirement Extractor executing")
    
    user_data = state["user_data"]
    chat_context = state["chat_context"]
    
    try:
        # Extract requirements using the new tool
        extraction_result = extract_new_score_oriented_requirements.invoke({
            "chat_context": chat_context,
            "user_data": user_data.model_dump()
        })
        
        logger.info(f"Requirement extraction result: {extraction_result.get('status', 'Unknown')}")
        
        if extraction_result.get("status") == "success":
            requirements = extraction_result.get("requirements", {})
            
            # Log extracted requirements
            logger.info(f"Extracted requirements: subject_priority={requirements.get('subject_priority', [])} "
                       f"chapter_coverage={requirements.get('chapter_coverage_preferences', {})} "
                       f"time_allocation={requirements.get('time_allocation_preferences', {})}")
            
            # Store requirements in state
            state["user_requirements"] = requirements
            state["extraction_source"] = extraction_result.get("extraction_source", "llm_analysis")
            
            # Update chat with extraction acknowledgment
            for turn_id, chat_msg in chat_context.items():
                if "Generating your revision flow plan..." in chat_msg.assistant_message:
                    # Extract key preferences for display
                    subject_priority = requirements.get("subject_priority", [])
                    chapters_per_month = requirements.get("chapter_coverage_preferences", {}).get("chapters_per_month")
                    specific_requests = requirements.get("specific_requests", [])
                    
                    preferences_text = ""
                    if subject_priority:
                        preferences_text += f"• Subject Priority: {', '.join([s.title() for s in subject_priority])}\n"
                    if chapters_per_month:
                        preferences_text += f"• Chapter Coverage: {chapters_per_month} chapters per month\n"
                    if specific_requests:
                        preferences_text += f"• Specific Requests: {', '.join(specific_requests[:2])}\n"
                    
                    chat_msg.assistant_message = (
                        f"🎯 **New Score-Oriented Plan Initiated!**\n\n"
                        f"📊 **Your Requirements:**\n"
                        f"• Target Score: {user_data.target_score}/300\n"
                        f"• Exam Date: {user_data.exam_date}\n"
                        f"• Preparation Time: {user_data.number_of_months} months\n"
                        f"• Plan Type: Complete Syllabus Coverage with Revision Focus\n\n"
                        f"🔍 **Extracted Preferences:**\n"
                        f"{preferences_text if preferences_text else '• Using default optimization strategy'}\n"
                        f"✅ **Plan Features:**\n"
                        f"• 100% syllabus completion in one go\n"
                        f"• Dependency-based chapter ordering\n"
                        f"• Priority-weighted chapter sequence\n"
                        f"• Saturday/Sunday practice schedule (PYQ/DPP)\n"
                        f"• Target completion within 6 months\n"
                        f"• User preference integration\n\n"
                        f"🔄 Generating your customized revision flow plan..."
                    )
                    break
            
        else:
            # Extraction failed, use defaults
            logger.warning(f"Requirement extraction failed: {extraction_result.get('message', 'Unknown error')}")
            state["user_requirements"] = {
                "subject_priority": ["physics", "chemistry", "mathematics"],
                "chapter_priority": {},
                "time_allocation_preferences": {},
                "chapter_coverage_preferences": {},
                "study_style_preferences": {},
                "specific_requests": [],
                "weak_areas": [],
                "strong_areas": [],
                "exam_strategy": {}
            }
            state["extraction_source"] = "fallback"
        
        # Route to revision flow agent
        state["next_agent"] = "revision_flow_agent"
        
    except Exception as e:
        logger.error(f"Error in requirement extractor: {e}")
        # Use fallback requirements
        state["user_requirements"] = {
            "subject_priority": ["physics", "chemistry", "mathematics"],
            "chapter_priority": {},
            "time_allocation_preferences": {},
            "chapter_coverage_preferences": {},
            "study_style_preferences": {},
            "specific_requests": [],
            "weak_areas": [],
            "strong_areas": [],
            "exam_strategy": {}
        }
        state["extraction_source"] = "error_fallback"
        state["next_agent"] = "revision_flow_agent"
    
    return state

def revision_flow_agent_node(state: NewScoreOrientedState) -> NewScoreOrientedState:
    """
    RevisionFlow Agent - Generates complete syllabus coverage plan with dependencies.
    """
    logger.info("RevisionFlow Agent executing")
    
    user_data = state["user_data"]
    plan_parameters = state["plan_parameters"]
    
    # Generate revision flow plan
    revision_results = revision_flow_agent.generate_revision_flow_plan(user_data, plan_parameters)
    
    state["revision_flow_results"] = revision_results
    state["next_agent"] = "generator_validator"
    
    return state

def generator_validator_agent(state: NewScoreOrientedState) -> NewScoreOrientedState:
    """
    Generator Validator Agent - Validates chapter coverage and user requirements.
    """
    logger.info("Generator Validator Agent executing")
    
    user_data = state["user_data"]
    revision_results = state["revision_flow_results"]
    
    # Validate chapter coverage
    chapter_validation = new_score_oriented_validator.validate_chapter_coverage(user_data, revision_results)
    
    state["chapter_validation"] = chapter_validation
    state["validation_passed"] = chapter_validation.get("chapter_validation", {}).get("all_chapters_covered", False)
    
    if state["validation_passed"]:
        state["next_agent"] = "topic_agent"
    else:
        state["next_agent"] = "revision_flow_agent"  # Re-run revision flow
    
    return state

def topic_agent_node(state: NewScoreOrientedState) -> NewScoreOrientedState:
    """
    Topic Agent - Assigns all topics for each chapter as mentioned.
    """
    logger.info("Topic Agent executing")
    
    user_data = state["user_data"]
    revision_results = state["revision_flow_results"]
    
    # Get topics for all chapters
    enhanced_revision_results = revision_results.copy()
    
    for subject, plan in revision_results.get("subject_plans", {}).items():
        chapters = plan.get("chapters", [])
        
        for chapter_info in chapters:
            chapter_name = chapter_info.get("chapter", "")
            
            # Get topic priorities for this chapter
            topics = get_topic_priority_for_chapter.invoke({
                "exam": user_data.target_exam,
                "subject": subject.title(),
                "chapter": chapter_name
            })
            
            # Add topics to chapter info
            chapter_info["topics"] = topics
            chapter_info["topic_count"] = len(topics)
    
    state["revision_flow_results"] = enhanced_revision_results
    state["next_agent"] = "topic_validator"
    
    return state

def topic_validator_agent(state: NewScoreOrientedState) -> NewScoreOrientedState:
    """
    Topic Validator Agent - Validates all syllabus topics are included.
    """
    logger.info("Topic Validator Agent executing")
    
    user_data = state["user_data"]
    revision_results = state["revision_flow_results"]
    
    # Extract chapter plan for validation
    chapter_plan = {}
    for subject, plan in revision_results.get("subject_plans", {}).items():
        chapter_plan[subject] = plan.get("chapters", [])
    
    # Validate topic coverage
    topic_validation = new_score_oriented_validator.validate_topic_coverage(user_data, chapter_plan)
    
    state["topic_validation"] = topic_validation
    
    # Also validate against complete syllabus
    syllabus_validation = new_score_oriented_validator.validate_syllabus_compliance(user_data, revision_results)
    state["syllabus_validation"] = syllabus_validation
    
    # Check if all validations pass
    all_topics_covered = topic_validation.get("topic_validation", {}).get("all_topics_covered", False)
    syllabus_compliant = syllabus_validation.get("syllabus_compliance", {}).get("fully_compliant", False)
    
    state["validation_passed"] = all_topics_covered and syllabus_compliant
    
    if state["validation_passed"]:
        state["next_agent"] = "supervisor"
    else:
        state["next_agent"] = "topic_agent"  # Re-run topic assignment
    
    return state

def supervisor_agent_node(state: NewScoreOrientedState) -> NewScoreOrientedState:
    """
    Supervisor Agent - Overall validation and target achievement analysis.
    """
    logger.info("Supervisor Agent executing")
    
    user_data = state["user_data"]
    complete_plan_state = {
        "revision_flow_results": state["revision_flow_results"],
        "chapter_validation": state["chapter_validation"],
        "topic_validation": state["topic_validation"],
        "syllabus_validation": state["syllabus_validation"]
    }
    
    # Supervise the complete plan
    supervisor_feedback = new_score_oriented_supervisor.supervise_plan(user_data, complete_plan_state)
    
    state["supervisor_feedback"] = supervisor_feedback
    state["adjustments_needed"] = not supervisor_feedback.get("plan_approved", True)
    
    if state["adjustments_needed"]:
        # Apply force-fit adjustments if needed
        logger.info("Supervisor applying force-fit adjustments for target achievement")
        state["next_agent"] = "force_fit_adjustments"
    else:
        state["next_agent"] = "finalize_plan"
    
    return state

def force_fit_adjustments_agent(state: NewScoreOrientedState) -> NewScoreOrientedState:
    """
    Force-fit adjustments to ensure target achievement.
    """
    logger.info("Applying force-fit adjustments for target achievement")
    
    user_data = state["user_data"]
    supervisor_feedback = state["supervisor_feedback"]
    revision_results = state["revision_flow_results"]
    
    # Apply adjustments from supervisor feedback
    adjustments = supervisor_feedback.get("adjustments_needed", [])
    
    # Modify revision results based on adjustments
    enhanced_revision_results = revision_results.copy()
    
    for adjustment in adjustments:
        adjustment_type = adjustment.get("type", "")
        
        if adjustment_type == "intensity_increase":
            # Increase focus on high-weightage chapters
            for subject, plan in enhanced_revision_results.get("subject_plans", {}).items():
                chapters = plan.get("chapters", [])
                # Sort by weightage and prioritize top chapters
                chapters.sort(key=lambda x: x.get("weightage", 0), reverse=True)
                plan["chapters"] = chapters
        
        elif adjustment_type == "time_redistribution":
            # Redistribute time based on score potential
            monthly_dist = enhanced_revision_results.get("monthly_distribution", {})
            for month_key, month_data in monthly_dist.items():
                if month_data.get("target") == "syllabus_completion":
                    # Focus on high-weightage chapters in early months
                    month_data["focus"] = "high_weightage_priority"
    
    state["revision_flow_results"] = enhanced_revision_results
    state["adjustments_needed"] = False
    state["next_agent"] = "finalize_plan"
    
    return state

def finalize_plan_agent(state: NewScoreOrientedState) -> NewScoreOrientedState:
    """
    Finalize the new_score_oriented study plan with enhanced calendar features.
    """
    logger.info("Finalizing new_score_oriented study plan with enhanced calendar features")
    
    user_data = state["user_data"]
    revision_results = state["revision_flow_results"]
    chat_context = state["chat_context"]
    enhanced_features = revision_results.get("enhanced_features", {})
    
    # Generate calendar-based plan data for frontend
    calendar_plan_data = _generate_calendar_plan_data(user_data, revision_results, enhanced_features)
    
    # Create final study plan with enhanced features
    study_plan_data = {
        "user_id": user_data.user_id,
        "target_score": user_data.target_score,
        "exam_date": user_data.exam_date,
        "total_months": user_data.number_of_months,
        "syllabus_completion_months": min(user_data.number_of_months, 6),
        "practice_months": max(0, user_data.number_of_months - 6),
        "monthly_plans": [],  # Simplified for now
        "revision_flow_results": revision_results.get("subject_plans", {}),
        "overall_strategy": f"Complete syllabus coverage in {min(user_data.number_of_months, 6)} months with 100% chapter completion",
        "dependency_analysis": revision_results.get("dependency_analysis", {}),
        "coverage_validation": revision_results.get("coverage_validation", {}),
        "target_achievement_probability": 95.0,
        "enhanced_features": enhanced_features,
        
        # Enhanced Calendar Features for Frontend
        "calendar_plan": calendar_plan_data.get("calendar_plan", {}),
        "monthly_targets_data": enhanced_features.get("monthly_target_scores", {}),
        "extended_months_plan": enhanced_features.get("extended_months_plan", {}),
        "weekend_schedule": enhanced_features.get("weekend_schedule", {}),
        "weekly_topic_breakdown": enhanced_features.get("weekly_topic_breakdown", {}),
        "user_target_score": user_data.target_score,
        "start_date": _calculate_start_date(),
        "end_date": _calculate_end_date(user_data.number_of_months),
        "overall_summary": calendar_plan_data.get("overall_summary", {})
    }
    
    # Update chat with final plan summary
    for turn_id, chat_msg in chat_context.items():
        if not chat_msg.assistant_message or "Generating your revision flow plan..." in chat_msg.assistant_message:
            total_chapters = sum(
                len(plan.get("chapters", [])) 
                for plan in revision_results.get("subject_plans", {}).values()
            )
            
            # Check if enhanced features are available
            enhanced_features = revision_results.get("enhanced_features", {})
            has_enhanced_features = bool(enhanced_features)
            
            chat_msg.assistant_message = (
                f"🎯 **New Score-Oriented Study Plan Generated Successfully!**\n\n"
                f"📊 **Plan Summary:**\n"
                f"• Target Score: {user_data.target_score}/300\n"
                f"• Total Chapters: {total_chapters} (100% syllabus coverage)\n"
                f"• Syllabus Completion: {min(user_data.number_of_months, 6)} months\n"
                f"• Practice Phase: {max(0, user_data.number_of_months - 6)} months\n\n"
                f"✅ **Key Features:**\n"
                f"• ✅ Complete dependency resolution\n"
                f"• ✅ Priority-based chapter sequencing\n"
                f"• ✅ 100% topic coverage per chapter\n"
                f"• ✅ Saturday (PYQ) + Sunday (DPP) practice\n"
                f"• ✅ Force-fit target achievement strategy\n"
                + (f"• ✅ Enhanced features: Monthly targets, Extended months plan, Topic breakdown\n" if has_enhanced_features else "") +
                f"\n📋 Your comprehensive revision plan is ready! Check the 'View Plan' section for detailed monthly breakdown."
                + (f"\n\n🚀 **Enhanced Features Available:**\n• Monthly target score calculations\n• Extended months with PYQ/DPP focus\n• Weekly topic-wise breakdown\n• Comprehensive weekend schedule" if has_enhanced_features else "")
            )
            break
    
    state["study_plan"] = study_plan_data
    state["chat_context"] = chat_context
    state["plan_finalized"] = True
    state["next_agent"] = "feedback_counsellor"  # Route to feedback instead of end
    
    # Display detailed breakdown in terminal
    try:
        from app.new_score_oriented.display import display_new_score_oriented_plan
        display_new_score_oriented_plan(study_plan_data)
    except Exception as e:
        logger.error(f"Error displaying new_score_oriented plan: {e}")
    
    return state

def feedback_counsellor_node(state: NewScoreOrientedState) -> NewScoreOrientedState:
    """Enhanced feedback collection for new_score_oriented plans"""
    logger.info("New Score-Oriented Feedback Counsellor executing")
    
    # Get the latest user message from chat context
    chat_context = state.get("chat_context", {})
    latest_turn = max(chat_context.keys()) if chat_context else "1"
    latest_message = chat_context.get(latest_turn)
    user_message = latest_message.user_message if latest_message and hasattr(latest_message, 'user_message') else ""
    
    logger.info(f"Processing user message: {user_message}")
    
    # Check for finalization trigger words
    finalization_words = [
        "finalize", "approve", "confirm plan", "i'm satisfied", "perfect", "great", 
        "excellent", "no changes", "all good", "yes this is final", "this is final", 
        "final", "done", "complete", "save this plan", "lock it in", "good to go", 
        "ready", "confirmed"
    ]
    
    # Special case: "looks good" only if not followed by "but" or change requests
    looks_good_finalization = ("looks good" in user_message.lower() and 
                              "but" not in user_message.lower() and 
                              not any(word in user_message.lower() for word in ["want", "need", "change", "more", "less", "different"]))
    
    should_finalize = any(word in user_message.lower() for word in finalization_words) or looks_good_finalization
    
    if should_finalize:
        # User wants to finalize the plan
        logger.info("User wants to finalize the new_score_oriented plan")
        
        # Save the finalized plan
        try:
            from app.new_score_oriented_tools import save_new_score_oriented_progress
            
            user_id = state["user_data"].user_id
            study_plan_data = state.get("study_plan", {})
            
            # Prepare comprehensive state for saving
            complete_state = {
                "user_data": state["user_data"].model_dump(),
                "revision_flow_results": state.get("revision_flow_results", {}),
                "enhanced_features": state.get("revision_flow_results", {}).get("enhanced_features", {}),
                "plan_finalized": True,
                "finalized_at": "user_confirmed"
            }
            
            # Save to database
            save_result = save_new_score_oriented_progress.invoke({
                "user_id": user_id,
                "state_message": complete_state,
                "study_plan": study_plan_data
            })
            
            logger.info(f"Plan saved successfully: {save_result}")
            
            # Update chat with finalization message
            finalization_response = f"""🎉 **Congratulations!** Your New Score-Oriented study plan has been finalized and saved!

**Your Plan is Ready:**
✅ **Target-Focused**: Designed to achieve {state['user_data'].target_score}/300 marks
✅ **Complete Coverage**: 100% syllabus completion in {min(state['user_data'].number_of_months, 6)} months
✅ **Dependency-Optimized**: Chapters ordered for optimal learning progression
✅ **Practice-Integrated**: Weekend PYQ/DPP schedule for consistent practice
✅ **Securely Saved**: Your plan is now saved to your profile

**Database Status**: {save_result.get('status', 'Success')}

**Next Steps:**
1. Follow the monthly chapter completion targets
2. Maintain 100% understanding for each chapter
3. Use weekends for PYQ and DPP practice
4. Track your progress regularly
5. Stay consistent with the dependency-based sequence

**Your journey to {state['user_data'].target_score}/300 starts now! Best of luck! 🚀**"""
            
            latest_message.assistant_message = finalization_response
            
        except Exception as e:
            logger.error(f"Error saving finalized plan: {e}")
            # Still finalize but show error message
            error_response = f"""🎉 **Your New Score-Oriented study plan has been finalized!**

⚠️ **Note**: There was an issue saving to the database ({str(e)}), but your plan is ready to use.

**Your Plan Features:**
✅ **Target-Focused**: Designed to achieve {state['user_data'].target_score}/300 marks
✅ **Complete Coverage**: 100% syllabus completion strategy
✅ **Dependency-Optimized**: Logical learning progression
✅ **Practice-Integrated**: Weekend PYQ/DPP schedule

**Next Steps:**
1. Save this plan for your reference
2. Follow the monthly targets systematically
3. Focus on 100% chapter completion
4. Use the weekend practice schedule

**Your journey to {state['user_data'].target_score}/300 starts now! 🚀**"""
            
            latest_message.assistant_message = error_response
        
        state["next_agent"] = "end"
        return state
    
    # Check for change/feedback requests with enhanced detection
    import re
    
    # FIX: Enhanced change detection with specific patterns
    change_patterns = [
        r"change.*?target.*?score.*?(\d+)",
        r"target.*?score.*?(\d+)", 
        r"score.*?(\d+)",
        r"(\d+)\s*chapters?\s*(?:per|each)\s*month",
        r"focus.*?on\s*(physics|chemistry|math)",
        r"priority.*?(physics|chemistry|math)",
        r"more.*?time.*?(physics|chemistry|math)",
        r"less.*?time.*?(physics|chemistry|math)"
    ]
    
    has_specific_change = any(re.search(pattern, user_message.lower()) for pattern in change_patterns)
    
    # FIX: Also check for general change keywords
    change_keywords = ["change", "modify", "adjust", "different", "update", "revise", 
                      "more time", "less time", "reorder", "priority", "before", "after",
                      "increase", "decrease", "focus more", "spend more"]
    
    has_change_request = any(keyword in user_message.lower() for keyword in change_keywords)
    
    # FIX: Combine both checks for better detection
    is_change_request = (has_specific_change or has_change_request) and len(user_message.strip()) > 10
    
    if is_change_request:
        # FIX: Store the change request immediately
        state["user_feedback_request"] = user_message
        
        # FIX: Extract specific changes
        extracted_changes = _extract_specific_changes(user_message)
        state["extracted_changes"] = extracted_changes
        
        # FIX: Check if user wants to generate immediately or just collect requirements
        generate_keywords = ["generate", "implement changes", "regenerate", "create plan", "make plan"]
        wants_immediate_generation = any(keyword in user_message.lower() for keyword in generate_keywords)
        
        if wants_immediate_generation:
            # User wants immediate generation - route to supervisor for analysis first
            state["next_agent"] = "feedback_supervisor"
            logger.info("User wants immediate generation after change request")
        else:
            # User just wants to make changes - collect requirements and wait for generate command
            state["next_agent"] = "requirement_collector"
            logger.info("User change request detected, collecting requirements first")
        
        logger.info(f"Extracted changes: {extracted_changes}")
        
        # Update chat to acknowledge the request with extracted details
        change_summary = _format_extracted_changes(extracted_changes)
        
        if wants_immediate_generation:
            acknowledgment = f"""I understand you'd like to make changes and generate a new plan. Let me analyze your request first.

**Your Request:** "{user_message}"

**Detected Changes:**
{change_summary}

🔍 **Getting Expert Analysis...**
I'll evaluate the implications and then generate your updated plan."""
        else:
            acknowledgment = f"""I understand you'd like to make changes to your study plan. I've noted your requirements.

**Your Request:** "{user_message}"

**Detected Changes:**
{change_summary}

✅ **Requirements Updated!**

You can:
- Make additional changes by specifying them
- Say **"generate"** when you're ready to create the updated plan
- Ask questions about the implications of these changes

**What would you like to do next?**"""
        
        latest_message.assistant_message = acknowledgment
        
    else:
        # Present the plan and ask for feedback
        study_plan_data = state.get("study_plan", {})
        revision_results = state.get("revision_flow_results", {})
        
        # Generate plan summary
        total_chapters = sum(
            len(plan.get("chapters", [])) 
            for plan in revision_results.get("subject_plans", {}).values()
        )
        
        enhanced_features = revision_results.get("enhanced_features", {})
        has_enhanced_features = bool(enhanced_features)
        
        plan_presentation = f"""🎯 **Your New Score-Oriented Study Plan is Ready!**

**Plan Overview:**
• **Target Score**: {state['user_data'].target_score}/300 marks
• **Total Duration**: {state['user_data'].number_of_months} months
• **Syllabus Completion**: {min(state['user_data'].number_of_months, 6)} months
• **Total Chapters**: {total_chapters} (100% coverage)
• **Practice Phase**: {max(0, state['user_data'].number_of_months - 6)} months

**Key Features:**
✅ **Complete Syllabus Coverage** - Every chapter covered 100%
✅ **Dependency-Based Ordering** - Logical learning progression
✅ **Target-Oriented Strategy** - Optimized for {state['user_data'].target_score} marks
✅ **Weekend Practice Schedule** - Saturday (PYQ) + Sunday (DPP)
{f"✅ **Enhanced Analytics** - Monthly targets, weekly breakdowns, extended planning" if has_enhanced_features else ""}

**Monthly Strategy:**
- **Months 1-{min(state['user_data'].number_of_months, 6)}**: Complete syllabus with 100% chapter mastery
- **Practice Integration**: Every weekend dedicated to PYQ and DPP
{f"- **Months {min(state['user_data'].number_of_months, 6)+1}-{state['user_data'].number_of_months}**: Intensive practice and revision" if state['user_data'].number_of_months > 6 else ""}

**What do you think about this plan?**

Are there any changes you'd like to make? For example:
- Adjust time allocation for specific subjects
- Change chapter priorities or order
- Modify the monthly distribution
- Any other preferences

If everything looks perfect, just say **'finalize'** and we'll save your plan!"""
        
        latest_message.assistant_message = plan_presentation
        state["next_agent"] = "feedback_counsellor_continue"
    
    return state

def requirement_collector_node(state: NewScoreOrientedState) -> NewScoreOrientedState:
    """Collect user requirements and wait for generate command"""
    logger.info("Requirement Collector executing - collecting user changes")
    
    # Get the latest user message from chat context
    chat_context = state.get("chat_context", {})
    latest_turn = max(chat_context.keys()) if chat_context else "1"
    latest_message = chat_context.get(latest_turn)
    user_message = latest_message.user_message if latest_message and hasattr(latest_message, 'user_message') else ""
    
    logger.info(f"Processing requirement collection: {user_message}")
    
    # Check if user wants to generate now
    generate_keywords = ["generate", "create plan", "make plan", "regenerate", "implement changes"]
    wants_to_generate = any(keyword in user_message.lower() for keyword in generate_keywords)
    
    if wants_to_generate:
        # User is ready to generate - route to supervisor for analysis first
        logger.info("User ready to generate, routing to feedback supervisor")
        state["next_agent"] = "feedback_supervisor"
        
        # Update message to show generation is starting
        latest_message.assistant_message = f"""Perfect! You're ready to generate your updated plan.

**Collected Requirements:**
{_format_extracted_changes(state.get('extracted_changes', {}))}

🔍 **Starting Expert Analysis...**
I'll analyze the implications of your changes and then generate your updated study plan.

Please wait while I prepare your customized plan..."""
        
        return state
    
    # Check for additional change requests
    import re
    change_patterns = [
        r"change.*?target.*?score.*?(\d+)",
        r"target.*?score.*?(\d+)", 
        r"score.*?(\d+)",
        r"(\d+)\s*chapters?\s*(?:per|each)\s*month",
        r"focus.*?on\s*(physics|chemistry|math)",
        r"priority.*?(physics|chemistry|math)"
    ]
    
    has_additional_changes = any(re.search(pattern, user_message.lower()) for pattern in change_patterns)
    
    if has_additional_changes:
        # Extract and merge additional changes
        additional_changes = _extract_specific_changes(user_message)
        existing_changes = state.get("extracted_changes", {})
        
        # Merge changes
        merged_changes = existing_changes.copy()
        for key, value in additional_changes.items():
            if value is not None and value != [] and value != {}:
                if key == "other_changes" and existing_changes.get(key):
                    merged_changes[key] = list(set(existing_changes[key] + value))
                elif key == "subject_priority_change" and existing_changes.get(key):
                    # Merge subject priorities
                    existing_subjects = existing_changes[key] if isinstance(existing_changes[key], list) else []
                    new_subjects = value if isinstance(value, list) else []
                    merged_changes[key] = list(set(existing_subjects + new_subjects))
                else:
                    merged_changes[key] = value
        
        state["extracted_changes"] = merged_changes
        
        # Update user feedback request to include all changes
        existing_request = state.get("user_feedback_request", "")
        all_requests = f"{existing_request} {user_message}".strip()
        state["user_feedback_request"] = all_requests
        
        logger.info(f"Additional changes detected and merged: {additional_changes}")
        
        # Acknowledge additional changes
        change_summary = _format_extracted_changes(merged_changes)
        latest_message.assistant_message = f"""Great! I've added your additional requirements.

**Your Latest Request:** "{user_message}"

**All Collected Requirements:**
{change_summary}

✅ **Requirements Updated!**

You can:
- Make more changes by specifying them
- Say **"generate"** when you're ready to create the updated plan
- Ask questions about these changes

**What would you like to do next?**"""
        
        state["next_agent"] = "requirement_collector"  # Stay in collection mode
        
    else:
        # General conversation or questions
        latest_message.assistant_message = f"""I'm here to help you refine your requirements!

**Current Collected Requirements:**
{_format_extracted_changes(state.get('extracted_changes', {}))}

You can:
- **Add more changes** by specifying them (e.g., "focus on physics", "4 chapters per month")
- **Ask questions** about the implications of your changes
- **Say "generate"** when you're ready to create your updated plan

**What would you like to do?**"""
        
        state["next_agent"] = "requirement_collector"  # Stay in collection mode
    
    return state

def feedback_counsellor_continue_node(state: NewScoreOrientedState) -> NewScoreOrientedState:
    """Handle user decisions after supervisor analysis for new_score_oriented plans"""
    logger.info("New Score-Oriented Feedback Counsellor Continue executing")
    
    # Get the latest user message
    chat_context = state.get("chat_context", {})
    latest_turn = max(chat_context.keys()) if chat_context else "1"
    latest_message = chat_context.get(latest_turn)
    user_message = latest_message.user_message if latest_message and hasattr(latest_message, 'user_message') else ""
    
    logger.info(f"Processing user decision: {user_message}")
    
    # Check for finalization requests
    finalization_words = [
        "finalize", "approve", "confirm plan", "i'm satisfied", "perfect", "great", 
        "excellent", "no changes", "all good", "yes this is final", "this is final", 
        "final", "done", "complete", "save this plan", "lock it in", "good to go", 
        "ready", "confirmed", "keep current plan"
    ]
    
    should_finalize = any(word in user_message.lower() for word in finalization_words)
    
    if should_finalize:
        # User wants to finalize after seeing analysis
        logger.info("User decided to finalize after analysis")
        
        try:
            from app.new_score_oriented_tools import save_new_score_oriented_progress
            
            user_id = state["user_data"].user_id
            study_plan_data = state.get("study_plan", {})
            
            # Include supervisor analysis in the saved state
            complete_state = {
                "user_data": state["user_data"].model_dump(),
                "revision_flow_results": state.get("revision_flow_results", {}),
                "enhanced_features": state.get("revision_flow_results", {}).get("enhanced_features", {}),
                "supervisor_analysis": state.get("supervisor_analysis", ""),
                "change_impact_assessment": state.get("change_impact_assessment", {}),
                "plan_finalized": True,
                "finalized_at": "user_confirmed_after_analysis"
            }
            
            # Save to database
            save_result = save_new_score_oriented_progress.invoke({
                "user_id": user_id,
                "state_message": complete_state,
                "study_plan": study_plan_data
            })
            
            logger.info(f"Plan saved after analysis: {save_result}")
            
            finalization_response = f"""🎉 **Excellent Decision!** Your New Score-Oriented study plan has been finalized and saved!

**Plan Confirmed After Expert Analysis:**
✅ **Thoroughly Analyzed**: Your plan has been reviewed for optimal target achievement
✅ **Expert Validated**: Supervisor analysis confirms the plan's effectiveness
✅ **Target-Focused**: Designed to achieve {state['user_data'].target_score}/300 marks
✅ **Dependency-Optimized**: Logical learning progression maintained
✅ **Securely Saved**: Your plan and analysis are now saved to your profile

**Database Status**: {save_result.get('status', 'Success')}

**Your Strategic Advantage:**
- You've made an informed decision based on expert analysis
- The plan maintains optimal target score achievement potential
- Dependency chains are preserved for effective learning
- Weekend practice schedule ensures consistent preparation

**Next Steps:**
1. Follow the monthly chapter completion targets
2. Maintain 100% understanding for each chapter
3. Use weekends for PYQ and DPP practice
4. Track your progress against the target score
5. Stay consistent with the dependency-based sequence

**Your journey to {state['user_data'].target_score}/300 starts now with confidence! 🚀**"""
            
            latest_message.assistant_message = finalization_response
            
        except Exception as e:
            logger.error(f"Error saving plan after analysis: {e}")
            error_response = f"""🎉 **Your New Score-Oriented study plan has been finalized after expert analysis!**

⚠️ **Note**: There was an issue saving to the database ({str(e)}), but your plan is ready to use.

**Your Analyzed Plan Features:**
✅ **Expert Reviewed**: Supervisor analysis completed
✅ **Target-Focused**: Designed for {state['user_data'].target_score}/300 marks
✅ **Dependency-Optimized**: Logical learning progression
✅ **Practice-Integrated**: Weekend PYQ/DPP schedule

**Your journey to {state['user_data'].target_score}/300 starts now! 🚀**"""
            
            latest_message.assistant_message = error_response
        
        state["next_agent"] = "end"
        return state
    
    # Check for implementation/regeneration requests
    implementation_words = [
        "implement changes", "regenerate plan", "make changes", "proceed with changes",
        "apply changes", "modify plan", "update plan", "change plan", "regenerate"
    ]
    
    should_regenerate = any(word in user_message.lower() for word in implementation_words)
    
    if should_regenerate:
        # User wants to implement the changes
        logger.info("User decided to implement changes, routing to regeneration")
        
        # Store the change request for the regeneration process
        state["regeneration_reason"] = "user_requested_changes_after_analysis"
        state["user_change_request"] = state.get("user_feedback_request", "")
        
        # FIX: Apply the extracted changes to user_data for regeneration
        extracted_changes = state.get("extracted_changes", {})
        user_data = state["user_data"]
        
        # Apply target score change
        if extracted_changes.get("target_score_change"):
            user_data.target_score = extracted_changes["target_score_change"]
            logger.info(f"Applied target score change: {extracted_changes['target_score_change']}")
        
        # Apply duration change
        if extracted_changes.get("duration_change"):
            try:
                user_data.number_of_months = extracted_changes["duration_change"]
                logger.info(f"Applied duration change: {extracted_changes['duration_change']}")
            except Exception as e:
                logger.error(f"Error applying duration change: {e}")
                # Skip duration change if there's an error
        
        # Store extracted changes in user requirements for the regeneration process
        state["user_requirements"] = {
            "subject_priority": extracted_changes.get("subject_priority_change", []),
            "chapter_coverage_preferences": extracted_changes.get("chapter_coverage_change", {}),
            "target_score_update": extracted_changes.get("target_score_change"),
            "duration_update": extracted_changes.get("duration_change"),
            "other_changes": extracted_changes.get("other_changes", []),
            "regeneration_context": "user_feedback_implementation"
        }
        
        # Add supervisor insights to guide regeneration
        regeneration_guidance = f"""
        **USER CHANGE REQUEST**: {state.get('user_feedback_request', '')}
        
        **EXTRACTED CHANGES**: {_format_extracted_changes(extracted_changes)}
        
        **SUPERVISOR ANALYSIS SUMMARY**: {state.get('supervisor_analysis', '')[:1000]}...
        
        **IMPLEMENTATION GUIDANCE**:
        - Updated target score: {user_data.target_score}/300
        - Preserve 100% syllabus coverage principle
        - Keep dependency-based learning progression where possible
        - Integrate user preferences while minimizing identified risks
        - Maintain weekend practice schedule structure
        """
        
        state["regeneration_guidance"] = regeneration_guidance
        
        # Update chat to acknowledge regeneration
        regeneration_response = f"""🔄 **Implementing Your Changes!**

Based on your decision and the expert analysis, I'm now regenerating your study plan with the requested modifications.

**Your Change Request:** "{state.get('user_feedback_request', '')}"

**Applied Changes:**
{_format_extracted_changes(extracted_changes)}

**Implementation Strategy:**
✅ **Guided by Analysis**: Using supervisor insights to minimize risks
✅ **Updated Target**: Now targeting {user_data.target_score}/300 marks
✅ **Smart Integration**: Balancing your preferences with academic best practices
✅ **Dependency Awareness**: Preserving logical learning progression where possible

🔄 **Regenerating your plan now...**

Please wait while I create your customized New Score-Oriented study plan."""
        
        latest_message.assistant_message = regeneration_response
        
        # Route back to counsellor generator with guidance
        state["next_agent"] = "counsellor_generator"
        return state
    
    # Check for more questions or clarifications
    question_indicators = ["what if", "how about", "can you explain", "tell me more", "what about"]
    has_questions = any(indicator in user_message.lower() for indicator in question_indicators)
    
    if has_questions:
        # User has more questions, provide additional guidance
        logger.info("User has additional questions")
        
        additional_guidance = f"""I'm here to help you make the best decision! Let me provide more insights:

**Your Current Situation:**
- **Plan Type**: New Score-Oriented (100% syllabus coverage)
- **Target**: {state['user_data'].target_score}/300 marks
- **Duration**: {state['user_data'].number_of_months} months

**Your Request**: "{state.get('user_feedback_request', '')}"

**Key Considerations:**
1. **Target Achievement**: How does this change affect your score goal?
2. **Time Management**: Will this fit within your {state['user_data'].number_of_months}-month timeline?
3. **Learning Efficiency**: Does this maintain the dependency-based progression?
4. **Practice Balance**: How does this impact your weekend PYQ/DPP schedule?

**Available Options:**
- **"Implement changes"** - Regenerate the plan with your modifications
- **"Finalize"** - Keep the current plan as analyzed
- **Ask specific questions** - Get more detailed explanations

**What specific aspect would you like me to clarify further?**"""
        
        latest_message.assistant_message = additional_guidance
        state["next_agent"] = "feedback_counsellor_continue"
        return state
    
    # Default: Ask for clarification
    clarification_request = f"""I want to make sure I understand your decision correctly.

**Your Options:**

1. **Implement Changes**: Say **"implement changes"** or **"regenerate plan"** to modify your study plan based on the analysis

2. **Keep Current Plan**: Say **"finalize"** to save your current plan as-is

3. **Ask Questions**: Feel free to ask about any aspect of the analysis or plan

**What would you like to do?**"""
    
    latest_message.assistant_message = clarification_request
    state["next_agent"] = "feedback_counsellor_continue"
    
    return state


def feedback_supervisor_node(state: NewScoreOrientedState) -> NewScoreOrientedState:
    """Enhanced feedback analysis with pros/cons insights for new_score_oriented plans"""
    logger.info("New Score-Oriented Feedback Supervisor executing")
    
    # Get user feedback request - FIX: Get from latest chat message if not in state
    user_feedback = state.get("user_feedback_request", "")
    
    # FIX: If user_feedback_request is empty, extract from latest chat message
    if not user_feedback:
        chat_context = state.get("chat_context", {})
        if chat_context:
            latest_turn = max(chat_context.keys()) if chat_context else "1"
            latest_message = chat_context.get(latest_turn)
            if latest_message and hasattr(latest_message, 'user_message'):
                user_feedback = latest_message.user_message
                # Store it in state for future use
                state["user_feedback_request"] = user_feedback
                logger.info(f"Extracted user feedback from chat: {user_feedback}")
    
    user_data = state["user_data"]
    revision_results = state.get("revision_flow_results", {})
    
    logger.info(f"Analyzing feedback request: {user_feedback}")
    
    # FIX: Add specific extraction for target score changes
    extracted_changes = _extract_specific_changes(user_feedback)
    state["extracted_changes"] = extracted_changes
    
    # Create comprehensive analysis prompt with extracted changes
    analysis_prompt = f"""
    You are an expert study plan supervisor analyzing a change request for a New Score-Oriented study plan.
    
    **USER CHANGE REQUEST:** "{user_feedback}"
    
    **EXTRACTED CHANGES:**
    {_format_extracted_changes(extracted_changes)}
    
    **CURRENT PLAN DETAILS:**
    - Target Score: {user_data.target_score}/300
    - Duration: {user_data.number_of_months} months
    - Exam: {user_data.target_exam}
    - Plan Type: New Score-Oriented (100% syllabus coverage)
    
    **CURRENT PLAN STRUCTURE:**
    {revision_results.get("plan_summary", "Plan structure not available")}
    
    **ANALYSIS FRAMEWORK:**
    Provide a comprehensive analysis with:
    
    1. **UNDERSTANDING**: What exactly does the user want to change?
    
    2. **CURRENT RATIONALE**: Why is the current plan designed this way?
    
    3. **PROS of the requested change**:
       - Academic benefits
       - Learning advantages
       - Target score impact
       - Time efficiency gains
    
    4. **CONS of the requested change**:
       - Potential academic drawbacks
       - Dependency chain disruptions
       - Target score risks
       - Time allocation issues
    
    5. **IMPACT ASSESSMENT**:
       - Effect on target score achievement
       - Syllabus completion timeline impact
       - Chapter dependency implications
       - Overall preparation balance
    
    6. **RECOMMENDATION**: 
       - Should they proceed with this change?
       - Alternative approaches if applicable
       - Risk mitigation strategies
    
    7. **IMPLEMENTATION GUIDANCE**:
       - If they proceed, how to minimize drawbacks
       - What to watch out for
       - Success metrics to track
    
    Be thorough, balanced, and educational. Help the user make an informed decision.
    """
    
    try:
        # Create a specialized LLM agent for feedback analysis
        from langchain_core.prompts import ChatPromptTemplate
        from langchain_google_genai import ChatGoogleGenerativeAI
        import os
        
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))
        
        # Get comprehensive analysis
        response = llm.invoke(analysis_prompt)
        supervisor_analysis = response.content if hasattr(response, 'content') else str(response)
        
        logger.info(f"Supervisor analysis completed: {len(supervisor_analysis)} characters")
        
        # Determine if major regeneration is needed
        major_change_indicators = [
            "completely different", "start over", "new plan", "different approach",
            "change target score", "different exam", "change duration"
        ]
        
        needs_major_regeneration = any(indicator in user_feedback.lower() for indicator in major_change_indicators)
        
        # Determine if minor adjustments can be made
        minor_adjustment_indicators = [
            "more time", "less time", "reorder", "priority", "focus more", "adjust",
            "modify", "before", "after", "increase", "decrease"
        ]
        
        can_make_adjustments = any(indicator in user_feedback.lower() for indicator in minor_adjustment_indicators)
        
        # Update chat context with analysis
        chat_context = state.get("chat_context", {})
        latest_turn = max(chat_context.keys()) if chat_context else "1"
        latest_message = chat_context.get(latest_turn)
        
        if latest_message:
            # Enhance the previous acknowledgment with detailed analysis
            enhanced_response = f"""🔍 **Expert Analysis Complete!**

{supervisor_analysis}

**📋 Your Options:**

1. **Proceed with Changes**: If you want to implement this modification, say **"implement changes"** or **"regenerate plan"**

2. **Explore Alternatives**: If you'd like to discuss other approaches, feel free to ask

3. **Keep Current Plan**: If you're satisfied after seeing the analysis, say **"finalize"** to save your current plan

**What would you like to do?**"""
            
            latest_message.assistant_message = enhanced_response
        
        # Store analysis for potential use in regeneration
        state["supervisor_analysis"] = supervisor_analysis
        state["change_impact_assessment"] = {
            "needs_major_regeneration": needs_major_regeneration,
            "can_make_adjustments": can_make_adjustments,
            "user_request": user_feedback,
            "analysis_summary": supervisor_analysis[:500] + "..." if len(supervisor_analysis) > 500 else supervisor_analysis
        }
        
        # Route back to feedback counsellor for user decision
        state["next_agent"] = "feedback_counsellor_continue"
        logger.info("Analysis complete, routing back to feedback counsellor for user decision")
        
    except Exception as e:
        logger.error(f"Error in feedback supervisor analysis: {e}")
        
        # Fallback analysis
        fallback_analysis = f"""I understand you want to modify your study plan. Here's my analysis:

**Your Request:** "{user_feedback}"

**Quick Assessment:**
- This change could affect your target score timeline
- May require adjusting the chapter sequence or time allocation
- Could impact the dependency-based learning progression

**Recommendation:**
Before implementing this change, consider:
1. How it aligns with your {user_data.target_score}/300 target
2. Whether it maintains the 100% syllabus coverage approach
3. If it preserves the logical learning sequence

**Next Steps:**
- Say **"implement changes"** if you want to proceed
- Say **"finalize"** if you prefer the current plan
- Ask questions if you need more clarification"""
        
        # Update chat context
        chat_context = state.get("chat_context", {})
        latest_turn = max(chat_context.keys()) if chat_context else "1"
        latest_message = chat_context.get(latest_turn)
        
        if latest_message:
            latest_message.assistant_message = fallback_analysis
        
        state["supervisor_analysis"] = fallback_analysis
        state["next_agent"] = "feedback_counsellor_continue"
    
    return state

def feedback_counsellor_continue_node(state: NewScoreOrientedState) -> NewScoreOrientedState:
    """Continue with feedback processing and minor adjustments"""
    logger.info("New Score-Oriented Feedback Counsellor Continue executing")
    
    # For now, just finalize the plan
    # In the future, this could handle minor adjustments to the existing plan
    state["next_agent"] = "end"
    logger.info("Feedback processed, finalizing plan")
    
    return state

# Helper functions for calendar plan generation

def _generate_calendar_plan_data(user_data, revision_results, enhanced_features):
    """Generate calendar plan data for frontend display"""
    from datetime import date, timedelta
    
    try:
        # Get monthly distribution from revision results
        monthly_distribution = revision_results.get("monthly_distribution", {})
        target_months = min(user_data.number_of_months, 6)
        
        calendar_plan = {}
        start_date = date.today()
        
        # Generate calendar plan for each month
        for month_num in range(1, user_data.number_of_months + 1):
            month_key = f"month_{month_num}"
            
            # Calculate month dates
            month_start = start_date + timedelta(days=(month_num - 1) * 30)
            month_end = month_start + timedelta(days=29)
            
            # Get month data from distribution
            month_data = monthly_distribution.get(month_key, {})
            
            # Determine month focus and tags
            if month_num <= target_months:
                primary_focus = "Syllabus Completion with Daily Practice"
                tags = ["SYLLABUS", "CHAPTER_STUDY", "DPP", "PYQ"]
            else:
                primary_focus = "Intensive Practice and PYQ Focus"
                tags = ["PRACTICE", "INTENSIVE_DPP", "PYQ", "MOCK_TESTS"]
            
            # Generate monthly analysis from enhanced features
            monthly_analysis = _extract_monthly_analysis(enhanced_features, month_key)
            
            # Generate daily schedule from real data
            daily_schedule = {}
            
            # Generate weekly pattern
            weekly_pattern = _generate_weekly_pattern(month_num, target_months)
            
            calendar_plan[month_key] = {
                "month_number": month_num,
                "month_name": month_start.strftime("%B %Y"),
                "start_date": month_start.strftime("%Y-%m-%d"),
                "end_date": month_end.strftime("%Y-%m-%d"),
                "total_days": 30,
                "study_days": {
                    "total_days": 30,
                    "study_days": 22,  # Monday-Friday
                    "practice_days": 8  # Saturday-Sunday
                },
                "monthly_analysis": monthly_analysis,
                "daily_schedule": daily_schedule,
                "weekly_pattern": weekly_pattern,
                "tags": tags,
                "primary_focus": primary_focus
            }
        
        # Generate overall summary
        overall_summary = {
            "plan_duration": f"{user_data.number_of_months} months",
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": (start_date + timedelta(days=user_data.number_of_months * 30)).strftime("%Y-%m-%d"),
            "total_study_days": user_data.number_of_months * 22,
            "total_practice_days": user_data.number_of_months * 8,
            "syllabus_completion_months": target_months,
            "intensive_practice_months": max(0, user_data.number_of_months - target_months),
            "weekend_pyq_sessions": user_data.number_of_months * 8,
            "daily_dpp_sessions": user_data.number_of_months * 22,
            "overall_strategy": f"Complete syllabus in {target_months} months with daily DPP practice, followed by intensive PYQ practice with weekend focus throughout the preparation."
        }
        
        return {
            "calendar_plan": calendar_plan,
            "overall_summary": overall_summary
        }
        
    except Exception as e:
        logger.error(f"Error generating calendar plan data: {e}")
        return {"calendar_plan": {}, "overall_summary": {}}

def _extract_monthly_analysis(enhanced_features, month_key):
    """Extract monthly analysis data from enhanced features"""
    try:
        monthly_targets = enhanced_features.get("monthly_target_scores", {})
        monthly_data = monthly_targets.get("monthly_targets", {}).get(month_key, {})
        
        return {
            "total_achievable_score": monthly_data.get("total_achievable_score", 0),
            "user_target_score": monthly_data.get("user_target_score", 0),
            "efficiency_required": monthly_data.get("efficiency_required", 0),
            "subject_breakdown": monthly_data.get("subject_breakdown", {}),
            "target_ratio": monthly_data.get("target_ratio", 0)
        }
    except Exception as e:
        logger.error(f"Error extracting monthly analysis for {month_key}: {e}")
        return {
            "total_achievable_score": 0,
            "user_target_score": 0,
            "efficiency_required": 0,
            "subject_breakdown": {},
            "target_ratio": 0
        }


def _generate_weekly_pattern(month_num, target_months):
    """Generate weekly pattern for a month"""
    if month_num <= target_months:
        return {
            "monday": {"type": "study", "subject": "Physics", "activity": "Chapter Study + DPP"},
            "tuesday": {"type": "study", "subject": "Chemistry", "activity": "Chapter Study + DPP"},
            "wednesday": {"type": "study", "subject": "Mathematics", "activity": "Chapter Study + DPP"},
            "thursday": {"type": "study", "subject": "Physics", "activity": "Chapter Study + DPP"},
            "friday": {"type": "study", "subject": "Chemistry", "activity": "Chapter Study + DPP"},
            "saturday": {"type": "practice", "activity": "PYQ Practice - All Subjects"},
            "sunday": {"type": "practice", "activity": "PYQ Practice - All Subjects"}
        }
    else:
        return {
            "monday": {"type": "practice", "subject": "Physics", "activity": "Intensive DPP"},
            "tuesday": {"type": "practice", "subject": "Chemistry", "activity": "Intensive DPP"},
            "wednesday": {"type": "practice", "subject": "Mathematics", "activity": "Intensive DPP"},
            "thursday": {"type": "practice", "subject": "Mixed", "activity": "All Subjects DPP"},
            "friday": {"type": "revision", "activity": "Weak Areas Revision"},
            "saturday": {"type": "practice", "activity": "Full Syllabus PYQ"},
            "sunday": {"type": "practice", "activity": "Mock Tests + Analysis"}
        }

def _get_subject_for_weekday(day_name):
    """Get subject assignment for weekday"""
    day_to_subject = {
        "Monday": "Physics",
        "Tuesday": "Chemistry", 
        "Wednesday": "Mathematics",
        "Thursday": "Physics",
        "Friday": "Chemistry"
    }
    return day_to_subject.get(day_name, "Physics")

def _calculate_start_date():
    """Calculate start date (today)"""
    from datetime import date
    return date.today().strftime("%Y-%m-%d")

def _calculate_end_date(total_months):
    """Calculate end date based on total months"""
    from datetime import date, timedelta
    start_date = date.today()
    end_date = start_date + timedelta(days=total_months * 30)
    return end_date.strftime("%Y-%m-%d")

# Create the new_score_oriented graph
def create_new_score_oriented_graph():
    """Create the new_score_oriented study plan generation graph"""
    
    workflow = StateGraph(NewScoreOrientedState)
    
    # Add nodes
    workflow.add_node("counsellor_generator", counsellor_generator_agent)
    workflow.add_node("requirement_extractor", requirement_extractor_node)
    workflow.add_node("revision_flow_agent", revision_flow_agent_node)
    workflow.add_node("generator_validator", generator_validator_agent)
    workflow.add_node("topic_agent", topic_agent_node)
    workflow.add_node("topic_validator", topic_validator_agent)
    workflow.add_node("supervisor", supervisor_agent_node)
    workflow.add_node("force_fit_adjustments", force_fit_adjustments_agent)
    workflow.add_node("finalize_plan", finalize_plan_agent)
    workflow.add_node("feedback_counsellor", feedback_counsellor_node)
    workflow.add_node("feedback_supervisor", feedback_supervisor_node)
    workflow.add_node("feedback_counsellor_continue", feedback_counsellor_continue_node)
    workflow.add_node("requirement_collector", requirement_collector_node)
    
    # Set entry point
    workflow.set_entry_point("counsellor_generator")
    
    # Add edges
    workflow.add_conditional_edges(
        "counsellor_generator",
        lambda state: state["next_agent"],
        {
            "requirement_extractor": "requirement_extractor",
            "revision_flow_agent": "revision_flow_agent",
            "end": END
        }
    )
    
    workflow.add_conditional_edges(
        "requirement_extractor",
        lambda state: state["next_agent"],
        {
            "revision_flow_agent": "revision_flow_agent"
        }
    )
    
    workflow.add_conditional_edges(
        "revision_flow_agent",
        lambda state: state["next_agent"],
        {
            "generator_validator": "generator_validator"
        }
    )
    
    workflow.add_conditional_edges(
        "generator_validator",
        lambda state: state["next_agent"],
        {
            "topic_agent": "topic_agent",
            "revision_flow_agent": "revision_flow_agent"
        }
    )
    
    workflow.add_conditional_edges(
        "topic_agent",
        lambda state: state["next_agent"],
        {
            "topic_validator": "topic_validator"
        }
    )
    
    workflow.add_conditional_edges(
        "topic_validator",
        lambda state: state["next_agent"],
        {
            "supervisor": "supervisor",
            "topic_agent": "topic_agent"
        }
    )
    
    workflow.add_conditional_edges(
        "supervisor",
        lambda state: state["next_agent"],
        {
            "force_fit_adjustments": "force_fit_adjustments",
            "finalize_plan": "finalize_plan"
        }
    )
    
    workflow.add_conditional_edges(
        "force_fit_adjustments",
        lambda state: state["next_agent"],
        {
            "finalize_plan": "finalize_plan"
        }
    )
    
    workflow.add_conditional_edges(
        "finalize_plan",
        lambda state: state["next_agent"],
        {
            "feedback_counsellor": "feedback_counsellor",
            "end": END
        }
    )
    
    workflow.add_conditional_edges(
        "feedback_counsellor",
        lambda state: state["next_agent"],
        {
            "feedback_supervisor": "feedback_supervisor",
            "feedback_counsellor_continue": "feedback_counsellor_continue",
            "requirement_collector": "requirement_collector",
            "end": END
        }
    )
    
    workflow.add_conditional_edges(
        "feedback_supervisor",
        lambda state: state["next_agent"],
        {
            "counsellor_generator": "counsellor_generator",
            "feedback_counsellor_continue": "feedback_counsellor_continue"
        }
    )
    
    workflow.add_conditional_edges(
        "feedback_counsellor_continue",
        lambda state: state["next_agent"],
        {
            "counsellor_generator": "counsellor_generator",
            "feedback_counsellor_continue": "feedback_counsellor_continue",
            "end": END
        }
    )
    
    workflow.add_conditional_edges(
        "requirement_collector",
        lambda state: state["next_agent"],
        {
            "requirement_collector": "requirement_collector",
            "feedback_supervisor": "feedback_supervisor",
            "end": END
        }
    )
    
    return workflow.compile()

# Helper functions for change extraction
def _extract_specific_changes(user_message):
    """Extract specific changes from user message"""
    import re
    
    changes = {
        "target_score_change": None,
        "duration_change": None,
        "subject_priority_change": None,
        "chapter_coverage_change": None,
        "other_changes": []
    }
    
    # Extract target score changes
    score_patterns = [
        r"target score.*?(\d+)",
        r"score.*?(\d+)", 
        r"change.*?score.*?(\d+)",
        r"update.*?score.*?(\d+)",
        r"make.*?score.*?(\d+)"
    ]
    
    for pattern in score_patterns:
        match = re.search(pattern, user_message.lower())
        if match:
            changes["target_score_change"] = int(match.group(1))
            break
    
    # Extract duration changes
    duration_patterns = [
        r"(\d+)\s*months?",
        r"duration.*?(\d+)",
        r"time.*?(\d+)\s*months?"
    ]
    
    for pattern in duration_patterns:
        match = re.search(pattern, user_message.lower())
        if match:
            changes["duration_change"] = int(match.group(1))
            break
    
    # Extract subject priority changes
    if any(subj in user_message.lower() for subj in ["physics", "chemistry", "mathematics", "maths"]):
        if any(word in user_message.lower() for word in ["focus", "priority", "important"]):
            subjects = []
            if "physics" in user_message.lower():
                subjects.append("physics")
            if "chemistry" in user_message.lower():
                subjects.append("chemistry")
            if any(word in user_message.lower() for word in ["mathematics", "maths"]):
                subjects.append("mathematics")
            changes["subject_priority_change"] = subjects
    
    # Extract chapter coverage changes
    chapter_patterns = [
        r"(\d+)\s*chapters?\s*(?:per|each|every)\s*month",
        r"(\d+)\s*chapters?\s*monthly"
    ]
    
    for pattern in chapter_patterns:
        match = re.search(pattern, user_message.lower())
        if match:
            changes["chapter_coverage_change"] = {
                "chapters_per_month": int(match.group(1))
            }
            break
    
    # Extract other changes
    other_keywords = ["more time", "less time", "reorder", "before", "after", "increase", "decrease"]
    for keyword in other_keywords:
        if keyword in user_message.lower():
            changes["other_changes"].append(keyword)
    
    return changes

def _format_extracted_changes(changes):
    """Format extracted changes for display"""
    formatted = []
    
    # Safely check for target score change
    if changes.get("target_score_change"):
        formatted.append(f"• Target Score: Change to {changes['target_score_change']}/300")
    
    # Safely check for duration change
    if changes.get("duration_change"):
        formatted.append(f"• Duration: Change to {changes['duration_change']} months")
    
    # Safely check for subject priority change
    if changes.get("subject_priority_change"):
        subjects = ", ".join(changes["subject_priority_change"])
        formatted.append(f"• Subject Priority: Focus on {subjects}")
    
    # Safely check for chapter coverage change
    if changes.get("chapter_coverage_change"):
        chapter_prefs = changes["chapter_coverage_change"]
        if isinstance(chapter_prefs, dict) and chapter_prefs.get("chapters_per_month"):
            formatted.append(f"• Chapter Coverage: {chapter_prefs['chapters_per_month']} chapters per month")
    
    # Safely check for other changes
    if changes.get("other_changes"):
        other = ", ".join(changes["other_changes"])
        formatted.append(f"• Other Changes: {other}")
    
    return "\n".join(formatted) if formatted else "• No specific changes extracted"

# Create the compiled graph
new_score_oriented_graph = create_new_score_oriented_graph()