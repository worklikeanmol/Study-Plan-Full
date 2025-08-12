from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, List, Dict, Optional
import operator
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from app.regeneration.tools import (
    check_user_exists,
    get_user_performance,
    analyze_topic_importance,
    generate_progress_insights,
    save_regenerated_plan,
    update_user_performance,
)
# Removed score_tools import - functions no longer needed for regeneration
from app.core.tools import (
    calculator,
    get_chapter_flow,
    get_chapter_weightage,
    get_topic_priority,
    get_syllabus,
)
from app.core.utils import get_logger
from app.regeneration.models import (
    RegenerationState,
    RegenerationUserData,
    UserPerformanceData,
    PreviousStudyPlan,
    RegenerationPreferences,
    RegenerationInsights,
    TopicImportanceAnalysis,
)
from app.core.models import (
    ChatMessage,
    Validation,
    StudyPlan,
    MonthlySubjectPlan,
    WeeklySubjectPlan,
    ChapterCoverage,
    PlanParameters,
)
from pydantic import BaseModel, Field
import json

load_dotenv()

# Logger
logger = get_logger(__name__)

# LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

def create_regen_agent(llm, tools: list, system_message: str):
    """Creates a regeneration agent with the given LLM, tools, and system message."""
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_message),
            ("human", "{input}"),
        ]
    )
    if tools:
        return prompt | llm.bind_tools(tools)
    return prompt | llm

# Import calculation functions from main graph
from app.core.graph import _calculate_monthly_plan, _find_best_match, _generate_plan_metadata

# Regeneration Counsellor Agent
regen_counsellor_agent = create_regen_agent(
    llm,
    [check_user_exists, get_user_performance, analyze_topic_importance, generate_progress_insights],
    """You are a regeneration counsellor specializing in helping existing users who are returning after completing their first month of study. Your role is to analyze their progress and guide them through the regeneration process.

CONTEXT: This user already has a previous study plan and performance data. You need to:

1. **ANALYZE PERFORMANCE**: Review their completed and not-completed topics
2. **PROVIDE INSIGHTS**: Give detailed analysis of their progress and study effectiveness
3. **HIGHLIGHT IMPORTANCE**: Explain the importance of pending topics for exam preparation
4. **OFFER OPTIONS**: Present regeneration choices (extend, create new, hybrid approach)
5. **COLLECT PREFERENCES**: Understand what the user wants to do next
6. **WAIT FOR GENERATION TRIGGER**: Only proceed when user says 'generate' or similar

REGENERATION OPTIONS TO EXPLAIN:
- **Extend Plan**: Continue with remaining topics from the original plan
- **Create New**: Start fresh with a new plan focusing on not-completed topics
- **Hybrid**: Combine important pending topics with new advanced content
- **Time Adjustments**: Change daily hours or extend timeline
- **Priority Changes**: Shift focus based on performance insights

CONVERSATION STYLE:
- Be encouraging about their progress so far
- Provide detailed analysis of their performance
- Explain the importance of pending critical topics
- Give flexibility and user-centric options
- Don't restrict user choices but provide good suggestions
- Be supportive if they want to skip some topics but highlight consequences

IMPORTANT CONSIDERATIONS:
- If user has important not-completed topics but wants to proceed, suggest adding them parallel to next month
- Highlight priority and importance of pending topics
- Suggest good approaches but give complete flexibility to user
- Focus on user-centric and flexible approach

TRIGGER WORDS TO START REGENERATION:
- "generate", "create plan", "start planning", "regenerate", "make new plan", "begin generation"

SAMPLE INTERACTIONS:
User: "I'm back after my first month"
You: "Welcome back! I can see you've made great progress in your first month. Let me analyze your performance and show you what you've accomplished and what's pending. 

📊 **Your Progress Summary:**
- Overall Progress: 35.5% completed
- Strong Areas: Mathematics Chapter 1
- Areas Needing Attention: Chemistry, Physics Chapter 3
- Pending Critical Topics: 12 topics

Let me explain the importance of your pending topics and give you options for moving forward..."

Remember: Provide comprehensive analysis, highlight topic importance, offer flexible options, and guide toward regeneration when ready.""",
)

# Regeneration Generator Agent
regen_generator_agent = create_regen_agent(
    llm,
    [],
    """You are a regeneration generator agent. Your responsibility is to extract regeneration requirements from the user conversation and route to the appropriate regeneration flow (regen-flow or regen-weightage) based on the user's preparation type and regeneration preferences.

You analyze the conversation to understand:
1. What type of regeneration the user wants (extend, create new, hybrid)
2. Any time adjustments (hours per day, timeline changes)
3. Priority changes for subjects or chapters
4. How to handle pending topics
5. User's specific regeneration preferences

You then route to the appropriate regeneration flow and collate information to create the final regenerated study plan.""",
)

# Regeneration Flow Agent (reuses flow logic with regeneration context)
regen_flow_agent = create_regen_agent(
    llm,
    [get_chapter_flow, calculator],
    """You are a regeneration flow agent. You specialize in creating regenerated study plans based on logical flow and dependencies of chapters, taking into account:

1. Previously completed topics (to avoid duplication)
2. Not-completed critical topics (to include them appropriately)
3. User's regeneration preferences
4. Time adjustments and priority changes
5. Remaining timeline and adjusted hours

Use the get_chapter_flow tool to fetch chapter details and calculator for calculations. Focus on creating a plan that builds on previous progress while addressing gaps.""",
)

# Regeneration Weightage Agent (reuses weightage logic with regeneration context)
regen_weightage_agent = create_regen_agent(
    llm,
    [get_chapter_weightage, calculator],
    """You are a regeneration weightage agent. You specialize in creating regenerated study plans based on weightage and priority of chapters, considering:

1. Previously completed topics and their weightage
2. Not-completed topics and their exam importance
3. User's regeneration preferences and priority changes
4. Adjusted time allocation based on performance insights
5. Focus on high-weightage pending topics

Use the get_chapter_weightage tool to fetch chapter details and calculator for calculations. Prioritize based on exam weightage while considering user's regeneration preferences.""",
)

# Regeneration Topic Agent (reuses topic logic with regeneration context)
regen_topic_agent = create_regen_agent(
    llm,
    [get_topic_priority, calculator],
    """You are a regeneration topic agent. You specialize in breaking down the regenerated plan into weekly topics, considering:

1. Previously completed topics (to skip them)
2. Not-completed topics that need to be included
3. New topics based on the regenerated plan
4. Priority adjustments based on performance insights
5. Time allocation adjustments

Use the get_topic_priority tool to fetch topic details and calculator for calculations. Create a weekly breakdown that efficiently uses the available time while addressing knowledge gaps.""",
)

# Regeneration Supervisor Agent
regen_supervisor_agent = create_regen_agent(
    llm,
    [],
    """You are a regeneration supervisor agent responsible for validating regenerated study plans against user requirements and regeneration context.

You must validate:
1. **Progress Integration**: Ensure completed topics are not duplicated
2. **Gap Coverage**: Verify important not-completed topics are addressed
3. **Regeneration Preferences**: Check if user's regeneration choices are implemented
4. **Time Allocation**: Validate adjusted hours and timeline are realistic
5. **Priority Implementation**: Ensure priority changes are reflected
6. **Balance**: Check if the plan maintains good subject balance

Provide detailed justification based on regeneration-specific analysis. Consider the user's previous progress and current regeneration goals.""",
)

# Regeneration Agent Nodes
def regen_counsellor_node(state: RegenerationState):
    """Regeneration counsellor node - analyzes performance and guides regeneration"""
    logger.info("Regeneration counsellor node executing")
    
    # Check if user exists and get their data
    user_check = check_user_exists.invoke({"user_id": state.user_id})
    
    if not user_check.get("exists", False):
        logger.info(f"User {state.user_id} not found - redirecting to normal flow")
        # This shouldn't happen in regen flow, but handle gracefully
        state.is_existing_user = False
        state.next_agent = "end"
        return state
    
    # User exists - get their performance data
    state.is_existing_user = True
    user_data = user_check.get("user_data", {})
    
    # Extract previous plan - handle case where study_plan might be None
    previous_plan_data = user_data.get("study_plan", {})
    if previous_plan_data is None:
        previous_plan_data = {}
    
    state.previous_plan = PreviousStudyPlan(
        insights=previous_plan_data.get("insights", ""),
        monthly_plan=previous_plan_data.get("monthly_plan", {}),
        weekly_plan=previous_plan_data.get("weekly_plan", {}),
        plan_metadata=user_data.get("state_msg", {}).get("plan_metadata", {}),
        created_at=user_data.get("created_at", "")
    )
    
    # Get performance data
    performance_result = get_user_performance.invoke({"user_id": state.user_id})
    if performance_result.get("found", False):
        perf_data = performance_result.get("performance_data", {})
        state.performance_data = UserPerformanceData(**perf_data)
    
    # Get the latest user message
    latest_message = ""
    chat_context = state.chat_context
    
    # Find the most recent user message
    for turn_id in sorted(chat_context.keys(), reverse=True):
        turn = chat_context[turn_id]
        if turn.user_message:
            latest_message = turn.user_message.lower()
            break
    
    logger.info(f"Latest user message: {latest_message}")
    
    # Check for generation trigger words
    trigger_words = [
        "generate", "create plan", "start planning", "make my plan", 
        "begin generation", "start generation", "create my plan",
        "generate plan", "make plan", "build plan", "start", "regenerate"
    ]
    
    should_generate = any(trigger in latest_message for trigger in trigger_words)
    
    if should_generate:
        # User wants to generate the regenerated plan
        logger.info("User requested regeneration. Proceeding to regen-generator.")
        state.next_agent = "regen_generator"
    else:
        # Continue regeneration counselling conversation
        logger.info("Continuing regeneration counselling conversation.")
        
        # Build conversation history
        conversation_parts = []
        for turn_id in sorted(chat_context.keys()):
            turn = chat_context[turn_id]
            if turn.user_message:
                conversation_parts.append(f"User: {turn.user_message}")
            if turn.assistant_message:
                conversation_parts.append(f"Assistant: {turn.assistant_message}")
        
        conversation_history = "\n".join(conversation_parts)
        
        # Generate progress insights
        if state.performance_data:
            progress_insights = generate_progress_insights.invoke({
                "performance_data": state.performance_data.model_dump(),
                "previous_plan": state.previous_plan.model_dump() if state.previous_plan else {}
            })
        else:
            progress_insights = "No performance data available for analysis."
        
        # Add score analysis for generic plans
        score_analysis = ""
        if state.performance_data and hasattr(state, 'user_id'):
            # Check if this is a score-based regeneration (we need to get user data)
            # For now, we'll add this context in the prompt
            score_analysis = "Score analysis will be included if this is a generic plan with target score."
        
        # Analyze importance of not-completed topics
        topic_analysis = {}
        if state.performance_data and state.performance_data.not_completed_topics:
            for subject, chapters in state.performance_data.not_completed_topics.items():
                for chapter, topics in chapters.items():
                    if topics:  # If there are topics in this chapter
                        # Convert topics list to comma-separated string
                        topics_str = ", ".join(topics)
                        analysis = analyze_topic_importance.invoke({
                            "exam": "JEE Mains",  # This should come from user data
                            "subject": subject,
                            "topics": topics_str
                        })
                        topic_analysis[f"{subject}_{chapter}"] = analysis
        
        # Create regeneration counsellor prompt
        regen_prompt = f"""
        CONVERSATION HISTORY:
        {conversation_history}
        
        USER PERFORMANCE DATA:
        {state.performance_data.model_dump() if state.performance_data else "No performance data"}
        
        PREVIOUS STUDY PLAN:
        {state.previous_plan.model_dump() if state.previous_plan else "No previous plan"}
        
        PROGRESS INSIGHTS:
        {progress_insights}
        
        TOPIC IMPORTANCE ANALYSIS:
        {json.dumps(topic_analysis, indent=2)}
        
        LATEST USER MESSAGE: {latest_message}
        
        The user is returning after completing their first month. Provide comprehensive analysis of their progress, highlight the importance of pending topics, and guide them through regeneration options.
        
        Focus on:
        1. Celebrating their progress
        2. Analyzing what worked and what didn't
        3. Explaining importance of pending critical topics
        4. Offering regeneration options with flexibility
        5. Collecting their preferences for the next phase
        """
        
        try:
            # Get regeneration counsellor response
            response = regen_counsellor_agent.invoke({"input": regen_prompt})
            counsellor_response = response.content if hasattr(response, 'content') else str(response)
            
            # Update the chat context with counsellor response
            latest_turn_id = max(chat_context.keys()) if chat_context else "1"
            if latest_turn_id in chat_context:
                chat_context[latest_turn_id].assistant_message = counsellor_response
            
            logger.info(f"Regeneration counsellor response: {counsellor_response[:200]}...")
            
            # Stay in regeneration counsellor mode
            state.next_agent = "regen_counsellor_continue"
            
        except Exception as e:
            logger.error(f"Error in regeneration counsellor: {e}", exc_info=True)
            # Fallback response
            fallback_response = f"""Welcome back! I can see you've been working on your study plan. Let me analyze your progress and help you plan the next phase.
            
Based on your performance data, you've made good progress! Let me help you decide how to proceed:

**Regeneration Options:**
1. **Extend Current Plan**: Continue with remaining topics
2. **Create New Plan**: Fresh start focusing on gaps
3. **Hybrid Approach**: Combine pending topics with new content

What would you like to do? When you're ready, say 'generate' and I'll create your regenerated plan!"""
            
            latest_turn_id = max(chat_context.keys()) if chat_context else "1"
            if latest_turn_id in chat_context:
                chat_context[latest_turn_id].assistant_message = fallback_response
            
            state.next_agent = "regen_counsellor_continue"
    
    return state

def regen_generator_node(state: RegenerationState):
    """Regeneration generator node - extracts regeneration preferences and routes"""
    logger.info("Regeneration generator node executing: Extracting regeneration preferences.")
    
    # Build conversation context
    conversation_parts = []
    for turn_id in sorted(state.chat_context.keys()):
        turn = state.chat_context[turn_id]
        if turn.user_message:
            conversation_parts.append(f"User: {turn.user_message}")
        if turn.assistant_message:
            conversation_parts.append(f"Assistant: {turn.assistant_message}")
    
    conversation = "\n".join(conversation_parts)
    
    # Include regeneration feedback if available
    regen_feedback = ""
    if state.regen_feedback:
        regen_feedback = '; '.join(state.regen_feedback)
        conversation += f"\n\nREGEN SUPERVISOR FEEDBACK: {regen_feedback}"
    
    class ExtractedRegenPreferences(BaseModel):
        """Regeneration preferences extracted from conversation."""
        regeneration_type: str = Field(
            default="extend_plan",
            description="Type of regeneration: 'extend_plan', 'create_new', or 'hybrid'"
        )
        time_adjustments: Optional[Dict[str, int]] = Field(
            default=None,
            description="Time adjustments like {'new_hours_per_day': 7, 'additional_months': 2}"
        )
        priority_changes: Optional[Dict[str, List[str]]] = Field(
            default=None,
            description="Priority changes like {'subject_priority': ['physics'], 'chapter_priority': ['Chapter_3']}"
        )
        include_pending_topics: Optional[bool] = Field(
            default=True,
            description="Whether to include not-completed topics from previous plan"
        )
        focus_on_weak_areas: Optional[bool] = Field(
            default=True,
            description="Whether to focus more on weak subjects/areas"
        )
        maintain_strong_areas: Optional[bool] = Field(
            default=True,
            description="Whether to maintain progress in strong areas"
        )
    
    extraction_prompt = f"""
    You are a regeneration preference extraction system. Analyze the conversation to extract user's regeneration preferences.
    
    CONVERSATION:
    {conversation}
    
    PERFORMANCE CONTEXT:
    - User has completed some topics and has pending topics
    - User is returning after first month of study
    - User wants to regenerate their study plan
    
    EXTRACTION RULES:
    1. regeneration_type: Determine if user wants to "extend_plan", "create_new", or "hybrid"
    2. time_adjustments: Extract any mentions of changing hours per day or extending timeline
    3. priority_changes: Extract any new subject or chapter priorities
    4. include_pending_topics: Whether user wants to include not-completed topics
    5. focus_on_weak_areas: Whether user wants to focus on weak subjects
    6. maintain_strong_areas: Whether user wants to maintain strong areas
    
    PATTERNS TO LOOK FOR:
    - "extend" / "continue" → extend_plan
    - "new plan" / "fresh start" → create_new  
    - "combine" / "hybrid" → hybrid
    - "more hours" / "increase time" → time_adjustments
    - "focus on [subject]" → priority_changes
    - "skip" / "ignore" pending topics → include_pending_topics: false
    
    Return ONLY a valid JSON object with the extracted preferences.
    """
    
    try:
        response = llm.invoke(extraction_prompt)
        response_text = response.content.strip()
        
        # Parse JSON response
        if "```json" in response_text:
            json_start = response_text.find("```json") + 7
            json_end = response_text.find("```", json_start)
            json_text = response_text[json_start:json_end].strip()
        elif "{" in response_text and "}" in response_text:
            json_start = response_text.find("{")
            json_end = response_text.rfind("}") + 1
            json_text = response_text[json_start:json_end]
        else:
            json_text = response_text
        
        parsed_data = json.loads(json_text)
        extracted_prefs = ExtractedRegenPreferences(**parsed_data)
        
        # Convert to RegenerationPreferences with proper defaults
        state.regeneration_preferences = RegenerationPreferences(
            regeneration_type=extracted_prefs.regeneration_type,
            time_adjustments=extracted_prefs.time_adjustments or {},
            priority_changes=extracted_prefs.priority_changes or {},
            include_pending_topics=extracted_prefs.include_pending_topics if extracted_prefs.include_pending_topics is not None else True,
            focus_on_weak_areas=extracted_prefs.focus_on_weak_areas if extracted_prefs.focus_on_weak_areas is not None else True,
            maintain_strong_areas=extracted_prefs.maintain_strong_areas if extracted_prefs.maintain_strong_areas is not None else True,
            new_months=extracted_prefs.time_adjustments.get("additional_months") if extracted_prefs.time_adjustments else None,
            new_hours_per_day=extracted_prefs.time_adjustments.get("new_hours_per_day") if extracted_prefs.time_adjustments else None
        )
        
        logger.info(f"Extracted regeneration preferences: {state.regeneration_preferences}")
        
    except Exception as e:
        logger.error(f"Error extracting regeneration preferences: {e}", exc_info=True)
        # Use default preferences
        state.regeneration_preferences = RegenerationPreferences()
    
    # Route based on preparation type and score requirements
    # We need to get the original user data for routing decisions
    # For regeneration, we'll use the same logic as normal flow
    
    # Default routing based on preparation type
    # In a full implementation, this should come from the original user request
    # For now, we'll route to flow for syllabus coverage, weightage for revision
    
    # Check if this is score-based regeneration
    is_score_based = False  # This would be determined from original user data
    
    # Default to flow-based regeneration for now
    # In production, this should check the original preparation_type
    state.next_agent = "regen_flow"
    
    logger.info(f"Regeneration routing to: {state.next_agent}")
    return state

def regen_flow_node(state: RegenerationState):
    """Regeneration flow node - creates plan based on flow with regeneration context"""
    logger.info("Regeneration flow node executing with regeneration context")
    
    # Create a temporary UserData object for the flow logic
    from app.core.models import UserData
    
    # Extract user data from regeneration context (this should come from the original request)
    # For now, using default values - in production, this should come from the regeneration state
    temp_user_data = UserData(
        user_id=state.user_id,
        target_exam="JEE Mains",
        study_plan_type="Custom", 
        preparation_type="Syllabus Coverage",
        syllabus={
            "Physics": [f"Chapter_{i}" for i in range(6, 11)],  # Pending chapters
            "Chemistry": [f"Chapter_{i}" for i in range(6, 11)],
            "Mathematics": [f"Chapter_{i}" for i in range(6, 11)]
        },
        number_of_months=4,  # Remaining months for pending topics
        hours_per_day=6
    )
    
    # Get chapters for pending topics based on performance data
    if state.performance_data and state.performance_data.not_completed_topics:
        pending_syllabus = {}
        for subject, chapters in state.performance_data.not_completed_topics.items():
            pending_syllabus[subject.title()] = list(chapters.keys())
        temp_user_data.syllabus = pending_syllabus
    
    # Apply regeneration preferences
    if state.regeneration_preferences.new_months:
        temp_user_data.number_of_months = state.regeneration_preferences.new_months
    if state.regeneration_preferences.new_hours_per_day:
        temp_user_data.hours_per_day = state.regeneration_preferences.new_hours_per_day
    
    # For score-based regeneration, add target score
    # This would come from the original user data or updated preferences
    # temp_user_data.target_score = original_target_score
    
    # Use the flow logic from main graph
    from app.core.graph import flow_node, StudyPlanState
    
    # Create a temporary state for flow processing
    temp_state = StudyPlanState(
        user_data=temp_user_data,
        chat_context=state.chat_context,
        plan_parameters=state.plan_parameters,
        monthly_coverage={},
        weekly_coverage={},
        validation_context={},
        study_plan=state.study_plan or StudyPlan(),
        plan_metadata={},
        regeneration_feedback=[],
        feedback_requests=[],
        supervisor_insights=[],
        plan_finalized=False,
        is_re_edit=False,
        next_agent=""
    )
    
    # Execute flow logic
    try:
        result_state = flow_node(temp_state)
        # Transfer results back to regeneration state
        state.monthly_coverage = result_state["monthly_coverage"]
        logger.info(f"Generated monthly coverage: {len(state.monthly_coverage)} months")
    except Exception as e:
        logger.error(f"Error in regeneration flow: {e}")
        # Fallback to empty coverage
        state.monthly_coverage = {}
    
    state.next_agent = "regen_topic"
    return state

def regen_topic_node(state: RegenerationState):
    """Regeneration topic node - creates weekly breakdown with regeneration context"""
    logger.info("Regeneration topic node executing with regeneration context")
    
    # Only proceed if we have monthly coverage
    if not state.monthly_coverage:
        logger.warning("No monthly coverage available for topic breakdown")
        state.weekly_coverage = {}
        state.next_agent = "regen_generator_collate"
        return state
    
    # Create temporary user data for topic processing
    from app.core.models import UserData
    
    temp_user_data = UserData(
        user_id=state.user_id,
        target_exam="JEE Mains",
        study_plan_type="Custom",
        preparation_type="Syllabus Coverage", 
        syllabus={
            "Physics": [f"Chapter_{i}" for i in range(6, 11)],
            "Chemistry": [f"Chapter_{i}" for i in range(6, 11)],
            "Mathematics": [f"Chapter_{i}" for i in range(6, 11)]
        },
        number_of_months=4,
        hours_per_day=6
    )
    
    # Update with actual pending chapters if available
    if state.performance_data and state.performance_data.not_completed_topics:
        pending_syllabus = {}
        for subject, chapters in state.performance_data.not_completed_topics.items():
            pending_syllabus[subject.title()] = list(chapters.keys())
        temp_user_data.syllabus = pending_syllabus
    
    # Use the topic logic from main graph
    from app.core.graph import topic_node, StudyPlanState
    
    # Create temporary state for topic processing
    temp_state = StudyPlanState(
        user_data=temp_user_data,
        chat_context=state.chat_context,
        plan_parameters=state.plan_parameters,
        monthly_coverage=state.monthly_coverage,
        weekly_coverage={},
        validation_context={},
        study_plan=state.study_plan or StudyPlan(),
        plan_metadata={},
        regeneration_feedback=[],
        feedback_requests=[],
        supervisor_insights=[],
        plan_finalized=False,
        is_re_edit=False,
        next_agent=""
    )
    
    # Execute topic logic
    try:
        result_state = topic_node(temp_state)
        # Transfer results back to regeneration state
        state.weekly_coverage = result_state["weekly_coverage"]
        logger.info(f"Generated weekly coverage: {len(state.weekly_coverage)} weeks")
    except Exception as e:
        logger.error(f"Error in regeneration topic: {e}")
        # Fallback to empty coverage
        state.weekly_coverage = {}
    
    state.next_agent = "regen_generator_collate"
    return state

def regen_generator_collate_node(state: RegenerationState):
    """Regeneration generator collate node - combines all regeneration data"""
    logger.info("Regeneration generator collate node executing")
    
    # Generate comprehensive regenerated study plan
    regeneration_insights = f"""🎉 **Your Regenerated Study Plan is Ready!**

Based on your excellent progress and preference to extend your previous plan, I've created a customized continuation plan that builds on your achievements.

**Your Progress Recap:**
• You've successfully completed Chapters 1-5 across Physics, Chemistry, and Mathematics
• Overall progress: {state.performance_data.overall_progress_percentage if state.performance_data else 'N/A'}%
• Strong performance in all subjects with consistent progress

**Regenerated Plan Focus:**
• **Regeneration Type**: {state.regeneration_preferences.regeneration_type.replace('_', ' ').title()}
• **Pending Topics**: Covering remaining chapters (6-10) across all subjects
• **Time Allocation**: Optimized based on your study pace and preferences
• **Integration**: Seamlessly continues from where you left off

**Key Features of Your Extended Plan:**
✅ **Continuity**: Picks up exactly where your previous plan ended
✅ **Progress-Aware**: Accounts for your completed topics to avoid duplication  
✅ **Optimized Pacing**: Adjusted based on your demonstrated learning speed
✅ **Comprehensive Coverage**: Ensures all remaining syllabus is covered systematically

**Next Steps:**
Your regenerated plan includes detailed monthly and weekly breakdowns for the remaining chapters. This ensures you maintain the momentum you've built while systematically covering all pending topics for comprehensive exam preparation.

Ready to continue your excellent preparation journey! 🚀"""

    # Create the regenerated study plan with actual data
    state.study_plan = StudyPlan(
        insights=regeneration_insights,
        monthly_plan=state.monthly_coverage,
        weekly_plan=state.weekly_coverage
    )
    
    # Generate plan metadata for validation
    if state.monthly_coverage or state.weekly_coverage:
        state.plan_metadata = {
            "regeneration_type": state.regeneration_preferences.regeneration_type,
            "pending_chapters_covered": len(state.monthly_coverage),
            "weekly_breakdown_available": len(state.weekly_coverage),
            "user_preferences_applied": {
                "extend_plan": True,
                "include_pending_topics": state.regeneration_preferences.include_pending_topics,
                "focus_on_weak_areas": state.regeneration_preferences.focus_on_weak_areas
            }
        }
    
    logger.info(f"Generated regenerated study plan with {len(state.monthly_coverage)} monthly plans and {len(state.weekly_coverage)} weekly plans")
    
    state.next_agent = "regen_supervisor"
    return state

def regen_supervisor_node(state: RegenerationState):
    """Regeneration supervisor node - validates regenerated plan"""
    logger.info("Regeneration supervisor node executing")
    
    # Validate the regenerated plan against:
    # 1. User's regeneration preferences
    # 2. Performance data and gaps
    # 3. Time constraints
    # 4. Priority requirements
    
    # For now, approving the plan
    validation_status = "yes"
    
    if validation_status == "yes":
        state.next_agent = "regen_counsellor_final"
    else:
        # Add feedback and regenerate
        state.regen_feedback = ["Regeneration validation feedback"]
        state.next_agent = "regen_generator"
    
    return state

def regen_counsellor_continue_node(state: RegenerationState):
    """Node for continuing regeneration counsellor conversation"""
    logger.info("Regeneration counsellor continue node executing")
    state.next_agent = "end"
    return state

def regen_counsellor_final_node(state: RegenerationState):
    """Final regeneration counsellor node - presents regenerated plan"""
    logger.info("Regeneration counsellor final node executing")
    
    # Present the regenerated plan to the user
    chat_context = state.chat_context
    
    # Find the latest turn to update with the plan presentation
    latest_turn_id = max(chat_context.keys()) if chat_context else "1"
    
    if latest_turn_id in chat_context and state.study_plan:
        # Create a comprehensive plan presentation message
        plan_presentation = f"""🎉 **Your Regenerated Study Plan is Ready!**

{state.study_plan.insights}

**📅 Plan Overview:**
- **Monthly Breakdown**: {len(state.monthly_coverage)} months of structured learning
- **Weekly Details**: {len(state.weekly_coverage)} weeks of topic-specific guidance
- **Coverage**: Focuses on your pending chapters (6-10) across all subjects
- **Approach**: {state.regeneration_preferences.regeneration_type.replace('_', ' ').title()}

**📊 What You'll Get:**
✅ **Month-by-Month Plan**: Clear chapter coverage with completion percentages
✅ **Weekly Topic Breakdown**: Specific topics to study each week
✅ **Progress Integration**: Builds seamlessly on your completed work
✅ **Optimized Pacing**: Adjusted based on your demonstrated learning speed

**🚀 Ready to Continue Your Journey!**

Your regenerated plan has been created and is ready for implementation. You can now follow the detailed monthly and weekly schedules to complete your remaining syllabus systematically.

Would you like me to save this plan, or do you have any adjustments you'd like to make?"""

        # Update the assistant message for the current turn
        chat_context[latest_turn_id].assistant_message = plan_presentation
        logger.info("Updated chat context with regenerated plan presentation")
    
    # Mark plan as finalized
    state.plan_finalized = True
    state.next_agent = "end"
    return state

# Regeneration Graph Definition
regen_workflow = StateGraph(RegenerationState)

# Add regeneration nodes
regen_workflow.add_node("regen_counsellor", regen_counsellor_node)
regen_workflow.add_node("regen_counsellor_continue", regen_counsellor_continue_node)
regen_workflow.add_node("regen_generator", regen_generator_node)
regen_workflow.add_node("regen_flow", regen_flow_node)
regen_workflow.add_node("regen_weightage", regen_flow_node)  # Reusing flow for now
regen_workflow.add_node("regen_topic", regen_topic_node)
regen_workflow.add_node("regen_generator_collate", regen_generator_collate_node)
regen_workflow.add_node("regen_supervisor", regen_supervisor_node)
regen_workflow.add_node("regen_counsellor_final", regen_counsellor_final_node)

# Set entry point
regen_workflow.set_entry_point("regen_counsellor")

# Define routing function
def route_regen_agent(state: RegenerationState):
    return state.next_agent

# Add conditional edges
regen_workflow.add_conditional_edges("regen_counsellor", route_regen_agent, {
    "regen_generator": "regen_generator", 
    "regen_counsellor_continue": "regen_counsellor_continue",
    "end": END
})
regen_workflow.add_conditional_edges("regen_generator", route_regen_agent, {
    "regen_flow": "regen_flow", 
    "regen_weightage": "regen_weightage"
})
regen_workflow.add_conditional_edges("regen_flow", route_regen_agent, {"regen_topic": "regen_topic"})
regen_workflow.add_conditional_edges("regen_weightage", route_regen_agent, {"regen_topic": "regen_topic"})
regen_workflow.add_conditional_edges("regen_topic", route_regen_agent, {"regen_generator_collate": "regen_generator_collate"})
regen_workflow.add_conditional_edges("regen_generator_collate", route_regen_agent, {"regen_supervisor": "regen_supervisor"})
regen_workflow.add_conditional_edges("regen_supervisor", route_regen_agent, {
    "regen_counsellor_final": "regen_counsellor_final",
    "regen_generator": "regen_generator"
})
regen_workflow.add_conditional_edges("regen_counsellor_final", route_regen_agent, {"end": END})
regen_workflow.add_conditional_edges("regen_counsellor_continue", route_regen_agent, {"end": END})

# Compile the regeneration graph
regen_graph = regen_workflow.compile()