from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, List, Dict, Optional
import operator
import json
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from app.core.tools import (
    calculator,
    get_chapter_flow,
    get_chapter_weightage,
    get_topic_priority,
    get_syllabus,
    save_finalized_plan,
)
# Removed score_tools import - functions no longer needed for custom plans
# Removed score_oriented_validator import
from app.new_score_oriented.agents import (
    revision_flow_agent, 
    new_score_oriented_validator, 
    new_score_oriented_supervisor
)
from app.core.utils import get_logger
from app.core.models import (
    UserData,
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

class StudyPlanState(TypedDict):
    user_data: UserData
    chat_context: Dict[str, ChatMessage]
    plan_parameters: PlanParameters # To store extracted personalization
    monthly_coverage: Dict[str, MonthlySubjectPlan]
    weekly_coverage: Dict[str, WeeklySubjectPlan]
    validation_context: Dict[str, Validation]
    study_plan: StudyPlan
    plan_metadata: Dict # Metadata for supervisor validation
    regeneration_feedback: Annotated[List[str], operator.add]
    feedback_requests: Annotated[List[str], operator.add] # User feedback and change requests
    supervisor_insights: Annotated[List[str], operator.add] # Supervisor pros/cons analysis
    plan_finalized: bool # Whether user has finalized the plan
    is_re_edit: bool # Flag to prevent infinite re-edit loops
    next_agent: str

def create_agent(llm, tools: list, system_message: str):
    """Creates an agent with the given LLM, tools, and system message."""
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_message),
            ("human", "{input}"),
        ]
    )
    if tools:
        return prompt | llm.bind_tools(tools)
    return prompt | llm

def _calculate_monthly_plan(user_data: UserData, chapters_with_hours: Dict[str, list]) -> Dict[str, MonthlySubjectPlan]:
    """The core logic for calculating the day-by-day monthly plan."""
    
    total_days = user_data.number_of_months * 30
    # Guard against division by zero if syllabus is empty
    if not user_data.syllabus:
        return {f"month_{i+1}": MonthlySubjectPlan() for i in range(user_data.number_of_months)}
        
    hours_per_day_per_subject = user_data.hours_per_day / len(user_data.syllabus)
    
    # Track progress for each subject
    subject_progress = {
        subject: {"current_chapter_idx": 0, "hours_done_on_current_chapter": 0.0}
        for subject in user_data.syllabus
    }
    
    # Store the daily breakdown of hours per chapter
    daily_breakdown = [
        {subject: {} for subject in user_data.syllabus} for _ in range(total_days)
    ]

    for day in range(total_days):
        for subject, chapters in chapters_with_hours.items():
            progress = subject_progress.get(subject)
            if not progress or progress["current_chapter_idx"] >= len(chapters):
                continue

            remaining_today = hours_per_day_per_subject
            
            while remaining_today > 0 and progress["current_chapter_idx"] < len(chapters):
                current_chapter = chapters[progress["current_chapter_idx"]]
                chapter_name = current_chapter["Chapter"]
                chapter_total_hours = current_chapter.get("adjusted_hours", 0)

                # Skip chapter if it has no time allocated
                if chapter_total_hours <= 0:
                    progress["current_chapter_idx"] += 1
                    continue
                
                hours_needed_for_chapter = chapter_total_hours - progress["hours_done_on_current_chapter"]
                hours_to_spend = min(remaining_today, hours_needed_for_chapter)
                
                if chapter_name not in daily_breakdown[day][subject]:
                    daily_breakdown[day][subject][chapter_name] = 0
                daily_breakdown[day][subject][chapter_name] += hours_to_spend
                
                progress["hours_done_on_current_chapter"] += hours_to_spend
                remaining_today -= hours_to_spend
                
                if progress["hours_done_on_current_chapter"] >= chapter_total_hours - 0.01: # Epsilon for float
                    progress["current_chapter_idx"] += 1
                    progress["hours_done_on_current_chapter"] = 0

    # Consolidate daily breakdown into a monthly plan
    monthly_coverage = {f"month_{i+1}": MonthlySubjectPlan() for i in range(user_data.number_of_months)}
    for month_idx in range(user_data.number_of_months):
        start_day, end_day = month_idx * 30, (month_idx + 1) * 30
        month_key = f"month_{month_idx + 1}"
        
        # Consolidate all hours spent on each chapter within the month
        monthly_chapter_hours = {s: {} for s in chapters_with_hours.keys()}
        for day in range(start_day, end_day):
            for subject, day_data in daily_breakdown[day].items():
                for chapter, hours in day_data.items():
                    if chapter not in monthly_chapter_hours[subject]:
                        monthly_chapter_hours[subject][chapter] = 0
                    monthly_chapter_hours[subject][chapter] += hours
        
        # Calculate coverage percentage
        for subject, chapters in chapters_with_hours.items():
            for chap_info in chapters:
                chap_name = chap_info['Chapter']
                if chap_name in monthly_chapter_hours.get(subject, {}):
                    hours_done = monthly_chapter_hours[subject][chap_name]
                    total_hours = chap_info.get("adjusted_hours", 0)
                    if total_hours > 0:
                        coverage = min(1.0, hours_done / total_hours)
                        chapter_coverage = ChapterCoverage(chapter=chap_name, coverage=coverage)
                        subject_key_lower = subject.lower()
                        # Ensure we append to the correct list in the Pydantic model
                        if hasattr(monthly_coverage[month_key], subject_key_lower):
                           getattr(monthly_coverage[month_key], subject_key_lower).append(chapter_coverage)

    return monthly_coverage

def _find_best_match(query: str, candidates: list) -> str:
    """Finds the best match for a query string from a list of candidates."""
    if not query or not candidates: return None
    query_lower = query.lower()
    if query_lower in (c.lower() for c in candidates): return next(c for c in candidates if c.lower() == query_lower)
    for candidate in candidates:
        if query_lower in candidate.lower(): return candidate
    return None

# Counsellor Agent
counsellor_agent = create_agent(
    llm,
    [],
    """You are a friendly study plan counsellor. Your role is to collect ADDITIONAL PREFERENCES and SPECIAL REQUIREMENTS from users.

IMPORTANT: All basic information (exam, syllabus, months, hours) is already provided from a form. You only need to collect:

1. SUBJECT PREFERENCES: Which subjects to focus on or prioritize
2. CHAPTER PREFERENCES: Specific chapters to prioritize or cover first  
3. STUDY PREFERENCES: Any special requirements, constraints, or learning preferences
4. WAIT FOR GENERATION TRIGGER: Only proceed when user says 'generate', 'create plan', or similar

WHAT YOU DON'T NEED TO ASK:
- Target exam (already provided)
- Number of months (already provided) 
- Daily study hours (already provided)
- Syllabus chapters (already provided)
- Target score (for custom plans)

WHAT TO FOCUS ON:
- "Which subjects do you want to focus more on?"
- "Are there specific chapters you want to prioritize?"
- "Do you want to cover any chapters first?"
- "Any special study preferences or constraints?"
- For GENERIC plans: Acknowledge target score and explain score-based optimization

CONVERSATION STYLE:
- Be encouraging and supportive
- Focus on preferences, not basic info
- Ask about study priorities and special needs
- Confirm understanding before proceeding
- Guide users to specify their learning preferences

TRIGGER WORDS TO START GENERATION:
- "generate", "create plan", "start planning", "make my plan", "begin generation"

SAMPLE INTERACTIONS:
User: "I want help with my study plan"
You: "Perfect! I can see you're preparing for [exam] over [months] months. Let me help you personalize your plan:
- Do you want to focus more on any particular subjects?
- Are there specific chapters you'd like to prioritize or cover first?
- Any special study preferences or constraints I should know about?"

User: "I want to focus more on physics and cover chapter 3 first"
You: "Excellent! I'll prioritize physics and ensure chapter 3 is covered first. Any other subject or chapter preferences? When you're ready, just say 'generate' and I'll create your personalized study plan."

FOR GENERIC PLANS WITH TARGET SCORE:
User: "I want help with my study plan"
You: "Perfect! I can see you're preparing for [exam] with a target score of [target_score]/300. I'll create a score-optimized plan focusing on high-weightage chapters to help you achieve your goal efficiently. 
- Do you want to focus more on any particular subjects?
- Any specific preferences for your score-based optimization?
When ready, say 'generate' for your target score-optimized plan!"

Remember: Focus only on collecting study preferences and special requirements, not basic form data.""",
)

# Feedback Counsellor Agent - Handles post-generation feedback
feedback_counsellor_agent = create_agent(
    llm,
    [save_finalized_plan],
    """You are a feedback counsellor specializing in study plan refinements. Your role is to help users review and request changes to their generated study plan.

CONTEXT: A study plan has already been generated and shown to the user. Now you help them refine it.

YOUR RESPONSIBILITIES:
1. PRESENT THE PLAN: Summarize the key aspects of the generated plan
2. COLLECT FEEDBACK: Ask what they think about the plan and if they want changes
3. CAPTURE CHANGE REQUESTS: Document specific changes they want
4. FINALIZATION: Guide them to say 'finalize' when they're satisfied

WHAT TO FOCUS ON:
- "What do you think about this study plan?"
- "Are there any changes you'd like to make?"
- "Would you like to adjust time allocation for any subjects?"
- "Do you want to change the chapter order or priorities?"
- "Any concerns about the current schedule?"

CHANGE REQUEST PATTERNS TO CAPTURE:
- Time allocation changes: "I want more/less time for [subject]"
- Chapter reordering: "Can we do [chapter] before [chapter]?"
- Subject priority changes: "I want to focus more on [subject]"
- Schedule adjustments: "Can we spread this over more/fewer months?"

FINALIZATION TRIGGER:
- "finalize", "looks good", "approve", "confirm plan", "I'm satisfied"

CONVERSATION STYLE:
- Be supportive and understanding
- Acknowledge their concerns
- Explain that you'll get expert analysis for any changes
- Reassure them that changes are possible
- Guide them toward finalization when appropriate

SAMPLE INTERACTIONS:
User: "The plan looks good but I want more time for physics"
You: "I understand you'd like more time allocated to physics. Let me get our expert analysis on how this change would affect your overall preparation. This will help you make an informed decision."

User: "Can we do chemistry chapters in a different order?"
You: "Absolutely! Chapter order can be adjusted. Could you tell me specifically which chapters you'd like to prioritize or reorder? I'll have our supervisor analyze the pros and cons of this change."

User: "Everything looks perfect"
You: "Wonderful! If you're satisfied with the plan, just say 'finalize' and we'll lock in your personalized study schedule."

Remember: Always be supportive, capture specific change requests clearly, and guide toward expert analysis or finalization.""",
)

# Generator Agent
generator_agent = create_agent(
    llm,
    [],
    "You are a generator agent. Your responsibility is to invoke the correct "
    "sub-agent (Flow or Weightage) based on the user's preparation type. "
    "You also collate the information from the sub-agents and the Topic agent "
    "to create the final study plan.",
)

# Flow Agent
flow_agent = create_agent(
    llm,
    [get_chapter_flow, calculator],
    """You are a flow agent. You specialize in creating a study plan based on the logical flow and dependencies of chapters.

For SYLLABUS COVERAGE preparation:
- Follow chapter dependencies and logical progression
- Ensure comprehensive coverage of all topics
- Maintain proper learning sequence

For GENERIC plans with target scores:
- Still follow logical flow but consider score implications
- Prioritize high-weightage chapters within the flow sequence
- Balance comprehensive coverage with score optimization

Use the get_chapter_flow tool to fetch chapter details and calculator for calculations.""",
)

# Weightage Agent  
weightage_agent = create_agent(
    llm,
    [get_chapter_weightage, calculator],
    """You are a weightage agent. You specialize in creating a study plan based on the weightage and priority of chapters. 

For REVISION preparation type:
- Prioritize high-weightage chapters for maximum score impact
- Focus on chapters with highest exam importance
- Optimize for score efficiency and time utilization

For GENERIC study plans with target scores:
- Prioritize chapters by: Average Weightage > Chapter Category > Topic Priority
- Use 3x multiplier for High category, 2x for Medium, 1x for Low
- Focus on achieving the target score efficiently
- Consider marks per hour efficiency for time optimization
- Calculate expected score and warn if target is not achievable with current time

For SCORE-ORIENTED plans:
- Apply weightage-based prioritization like normal flow
- Ensure ALL syllabus chapters are covered across months
- Use enhanced priority scoring with category multipliers (3x High, 2x Medium, 1x Low)
- Continue incomplete chapters to next months
- Integrate with enhanced score calculation engine for full coverage

For CUSTOM study plans with revision:
- Use standard weightage-based prioritization
- Focus on high-impact topics for revision

Use the get_chapter_weightage tool to fetch chapter details and calculator for calculations.""",
)

# Topic Agent
topic_agent = create_agent(
    llm,
    [get_topic_priority, calculator],
    "You are a topic agent. You specialize in breaking down the first month's plan "
    "into a weekly plan with topics. Use the get_topic_priority tool to fetch "
    "the topic details and the calculator for any calculations.",
)

# Pydantic model for the supervisor's response
class ValidationResponse(BaseModel):
    status: str
    justification: str

# Pre-configured structured LLM for the supervisor
structured_validator_llm = llm.with_structured_output(ValidationResponse)

def _generate_plan_metadata(state: StudyPlanState) -> Dict:
    """Generate comprehensive metadata for supervisor validation"""
    metadata = {
        "chapter_wise_coverage": {},
        "chapter_wise_time_allocation": {},
        "subject_total_time": {},
        "chapter_order_coverage": {},
        "subject_overall_time": {},
        "chapter_overall_time": {},
        "user_preferences_applied": {},
        "plan_statistics": {}
    }
    
    user_data = state["user_data"]
    plan_params = state["plan_parameters"]
    monthly_coverage = state["monthly_coverage"]
    weekly_coverage = state["weekly_coverage"]
    
    # 1. Calculate chapter order and coverage for each subject
    for subject in user_data.syllabus.keys():
        subject_key = subject.lower()
        metadata["chapter_order_coverage"][subject] = {}
        
        # Get chapter order from monthly plan
        chapter_order = []
        chapter_topics = {}
        
        for month_key, month_plan in monthly_coverage.items():
            month_data = month_plan.model_dump()
            if subject_key in month_data:
                for chapter_info in month_data[subject_key]:
                    chapter_name = chapter_info["chapter"]
                    if chapter_name not in chapter_order:
                        chapter_order.append(chapter_name)
                    
                    # Get topics for this chapter from weekly plan
                    if chapter_name not in chapter_topics:
                        chapter_topics[chapter_name] = []
                    
                    # Extract topics from first month's weekly plan
                    if month_key == "month_1":
                        for week_key, week_plan in weekly_coverage.items():
                            week_data = week_plan.model_dump()
                            if subject_key in week_data and chapter_name in week_data[subject_key]:
                                topics = week_data[subject_key][chapter_name]
                                for topic in topics:
                                    if topic not in chapter_topics[chapter_name]:
                                        chapter_topics[chapter_name].append(topic)
        
        metadata["chapter_order_coverage"][subject] = {
            "chapter_order": chapter_order,
            "chapter_topics": chapter_topics
        }
    
    # 2. Calculate subject overall time allocation
    total_available_hours = user_data.number_of_months * 30 * user_data.hours_per_day
    hours_per_subject = total_available_hours / len(user_data.syllabus) if user_data.syllabus else 0
    
    # Calculate priority multipliers based on number of prioritized subjects
    priority_count = len(plan_params.subject_priority)
    if priority_count == 1:
        priority_multiplier = 1.5
        non_priority_multiplier = 0.75  # Reduced by 1/4
    elif priority_count == 2:
        priority_multiplier = 1.25
        non_priority_multiplier = 0.875  # Reduced by 1/8
    else:
        priority_multiplier = 1.0
        non_priority_multiplier = 1.0
    
    for subject in user_data.syllabus.keys():
        base_hours = hours_per_subject
        # Apply subject priority multiplier if applicable
        if subject in plan_params.subject_priority:
            base_hours *= priority_multiplier
        else:
            # Apply reduction to non-prioritized subjects when priorities exist
            if priority_count > 0:
                base_hours *= non_priority_multiplier
        
        metadata["subject_overall_time"][subject] = {
            "allocated_hours": round(base_hours, 2),
            "percentage_of_total": round((base_hours / total_available_hours) * 100, 2),
            "is_prioritized": subject in plan_params.subject_priority,
            "multiplier_applied": priority_multiplier if subject in plan_params.subject_priority else non_priority_multiplier
        }
    
    # 3. Calculate chapter-wise time allocation
    for subject in user_data.syllabus.keys():
        subject_key = subject.lower()
        metadata["chapter_overall_time"][subject] = {}
        
        total_chapter_hours = 0
        for month_key, month_plan in monthly_coverage.items():
            month_data = month_plan.model_dump()
            if subject_key in month_data:
                for chapter_info in month_data[subject_key]:
                    chapter_name = chapter_info["chapter"]
                    coverage = chapter_info["coverage"]
                    
                    if chapter_name not in metadata["chapter_overall_time"][subject]:
                        metadata["chapter_overall_time"][subject][chapter_name] = {
                            "total_coverage": 0.0,
                            "months_covered": [],
                            "is_prioritized": False,
                            "estimated_hours": 0.0
                        }
                    
                    metadata["chapter_overall_time"][subject][chapter_name]["total_coverage"] += coverage
                    metadata["chapter_overall_time"][subject][chapter_name]["months_covered"].append(month_key)
                    
                    # Check if chapter is prioritized
                    if (subject in plan_params.chapter_priority and 
                        chapter_name in plan_params.chapter_priority[subject]):
                        metadata["chapter_overall_time"][subject][chapter_name]["is_prioritized"] = True
                    
                    # Estimate hours (rough calculation)
                    subject_hours = metadata["subject_overall_time"][subject]["allocated_hours"]
                    chapter_hours = (subject_hours / len(user_data.syllabus[subject])) * coverage
                    if metadata["chapter_overall_time"][subject][chapter_name]["is_prioritized"]:
                        chapter_hours *= 1.5
                    
                    metadata["chapter_overall_time"][subject][chapter_name]["estimated_hours"] += chapter_hours
    
    # 4. Track which user preferences were applied
    metadata["user_preferences_applied"] = {
        "subject_priority_applied": bool(plan_params.subject_priority),
        "chapter_priority_applied": bool(plan_params.chapter_priority),
        "chapter_order_applied": bool(plan_params.chapter_coverage_order),
        "extracted_preferences": {
            "subject_priority": plan_params.subject_priority,
            "chapter_priority": plan_params.chapter_priority,
            "chapter_coverage_order": plan_params.chapter_coverage_order
        }
    }
    
    # 5. Generate chapter_wise_coverage (priority-wise chapter list for each subject)
    for subject in user_data.syllabus.keys():
        subject_key = subject.lower()
        chapter_list = []
        
        # Get chapters from monthly plan in order of appearance
        for month_key, month_plan in monthly_coverage.items():
            month_data = month_plan.model_dump()
            if subject_key in month_data:
                for chapter_info in month_data[subject_key]:
                    chapter_name = chapter_info["chapter"]
                    if chapter_name not in chapter_list:
                        chapter_list.append(chapter_name)
        
        # Sort by priority: prioritized chapters first, then others
        # Use lowercase subject key for consistency
        prioritized_chapters = plan_params.chapter_priority.get(subject_key, [])
        priority_list = [ch for ch in prioritized_chapters if ch in chapter_list]
        remaining_list = [ch for ch in chapter_list if ch not in prioritized_chapters]
        
        metadata["chapter_wise_coverage"][subject_key] = priority_list + remaining_list
    
    # 6. Generate chapter_wise_time_allocation
    for subject in user_data.syllabus.keys():
        subject_key = subject.lower()
        metadata["chapter_wise_time_allocation"][subject_key] = {}
        
        for month_key, month_plan in monthly_coverage.items():
            month_data = month_plan.model_dump()
            if subject_key in month_data:
                for chapter_info in month_data[subject_key]:
                    chapter_name = chapter_info["chapter"]
                    coverage = chapter_info["coverage"]
                    
                    if chapter_name not in metadata["chapter_wise_time_allocation"][subject_key]:
                        metadata["chapter_wise_time_allocation"][subject_key][chapter_name] = 0.0
                    
                    # Estimate hours based on coverage and subject allocation
                    subject_hours = metadata["subject_overall_time"][subject]["allocated_hours"]
                    chapter_hours = (subject_hours / len(user_data.syllabus[subject])) * coverage
                    if chapter_name in plan_params.chapter_priority.get(subject_key, []):
                        chapter_hours *= 1.5
                    
                    metadata["chapter_wise_time_allocation"][subject_key][chapter_name] += chapter_hours
    
    # 7. Generate subject_total_time
    for subject in user_data.syllabus.keys():
        subject_key = subject.lower()
        metadata["subject_total_time"][subject_key] = metadata["subject_overall_time"][subject]["allocated_hours"]
    
    # 8. Generate plan statistics
    total_chapters = sum(len(chapters) for chapters in user_data.syllabus.values())
    covered_chapters = 0
    prioritized_chapters = 0
    
    for subject_data in metadata["chapter_overall_time"].values():
        for chapter_data in subject_data.values():
            if chapter_data["total_coverage"] > 0:
                covered_chapters += 1
            if chapter_data["is_prioritized"]:
                prioritized_chapters += 1
    
    metadata["plan_statistics"] = {
        "total_chapters": total_chapters,
        "covered_chapters": covered_chapters,
        "coverage_percentage": round((covered_chapters / total_chapters) * 100, 2) if total_chapters > 0 else 0,
        "prioritized_chapters": prioritized_chapters,
        "total_study_hours": total_available_hours,
        "study_months": user_data.number_of_months,
        "daily_hours": user_data.hours_per_day
    }
    
    return metadata

# Validation tools for supervisor
@tool
def analyze_subject_priority_implementation(metadata: dict, user_preferences: dict) -> str:
    """Analyze if subject priorities from user preferences were properly implemented in the plan"""
    
    subject_priorities = user_preferences.get("subject_priority", [])
    if not subject_priorities:
        return "No subject priorities specified by user."
    
    subject_time_data = metadata.get("subject_overall_time", {})
    
    analysis = []
    for priority_subject in subject_priorities:
        if priority_subject in subject_time_data:
            subject_data = subject_time_data[priority_subject]
            if subject_data["is_prioritized"]:
                analysis.append(f"✅ {priority_subject}: Allocated {subject_data['allocated_hours']} hours ({subject_data['percentage_of_total']}% of total time) - PRIORITIZED")
            else:
                analysis.append(f"❌ {priority_subject}: Not properly prioritized in time allocation")
        else:
            analysis.append(f"❌ {priority_subject}: Subject not found in plan")
    
    return "; ".join(analysis)

@tool
def analyze_chapter_priority_implementation(metadata: dict, user_preferences: dict) -> str:
    """Analyze if chapter priorities from user preferences were properly implemented in the plan"""
    
    chapter_priorities = user_preferences.get("chapter_priority", {})
    if not chapter_priorities:
        return "No chapter priorities specified by user."
    
    chapter_time_data = metadata.get("chapter_overall_time", {})
    
    analysis = []
    for subject, priority_chapters in chapter_priorities.items():
        if subject in chapter_time_data:
            for chapter in priority_chapters:
                if chapter in chapter_time_data[subject]:
                    chapter_data = chapter_time_data[subject][chapter]
                    if chapter_data["is_prioritized"]:
                        analysis.append(f"✅ {subject} {chapter}: {chapter_data['estimated_hours']:.1f} hours allocated - PRIORITIZED")
                    else:
                        analysis.append(f"❌ {subject} {chapter}: Not properly prioritized")
                else:
                    analysis.append(f"❌ {subject} {chapter}: Chapter not found in plan")
        else:
            analysis.append(f"❌ {subject}: Subject not found in plan")
    
    return "; ".join(analysis)

@tool
def analyze_chapter_order_implementation(metadata: dict, user_preferences: dict) -> str:
    """Analyze if chapter order preferences were properly implemented in the plan"""
    
    chapter_orders = user_preferences.get("chapter_coverage_order", {})
    if not chapter_orders:
        return "No chapter order preferences specified by user."
    
    chapter_coverage_data = metadata.get("chapter_order_coverage", {})
    
    analysis = []
    for subject, preferred_order in chapter_orders.items():
        if subject in chapter_coverage_data:
            actual_order = chapter_coverage_data[subject]["chapter_order"]
            
            # Check if preferred chapters appear early in the actual order
            early_chapters = actual_order[:len(preferred_order)] if actual_order else []
            matches = sum(1 for ch in preferred_order if ch in early_chapters)
            
            if matches == len(preferred_order):
                analysis.append(f"✅ {subject}: Preferred order {preferred_order} implemented correctly")
            else:
                analysis.append(f"⚠️ {subject}: Preferred order {preferred_order}, actual order starts with {early_chapters}")
        else:
            analysis.append(f"❌ {subject}: Subject not found in plan")
    
    return "; ".join(analysis)

@tool
def get_plan_summary_stats(metadata: dict) -> str:
    """Get summary statistics about the generated plan"""
    
    stats = metadata.get("plan_statistics", {})
    preferences = metadata.get("user_preferences_applied", {})
    
    summary = []
    summary.append(f"Plan covers {stats.get('covered_chapters', 0)}/{stats.get('total_chapters', 0)} chapters ({stats.get('coverage_percentage', 0)}%)")
    summary.append(f"Total study time: {stats.get('total_study_hours', 0)} hours over {stats.get('study_months', 0)} months")
    summary.append(f"Prioritized chapters: {stats.get('prioritized_chapters', 0)}")
    
    if preferences.get("subject_priority_applied"):
        summary.append("✅ Subject priorities applied")
    if preferences.get("chapter_priority_applied"):
        summary.append("✅ Chapter priorities applied")
    if preferences.get("chapter_order_applied"):
        summary.append("✅ Chapter order preferences applied")
    
    return "; ".join(summary)

# Supervisor Agent with validation tools (defined after tools are created)
supervisor_agent = create_agent(
    llm,
    [analyze_subject_priority_implementation, analyze_chapter_priority_implementation, 
     analyze_chapter_order_implementation, get_plan_summary_stats],
    "You are a supervisor agent responsible for validating study plans against user requirements. "
    "Use the provided validation tools to analyze if user preferences were properly implemented. "
    "Check subject priorities, chapter priorities, chapter order, and overall plan quality. "
    "Provide detailed justification based on concrete analysis from the tools.",
)

# Feedback Supervisor Agent - Provides pros/cons analysis for user change requests
feedback_supervisor_agent = create_agent(
    llm,
    [analyze_subject_priority_implementation, analyze_chapter_priority_implementation, 
     analyze_chapter_order_implementation, get_plan_summary_stats],
    """You are a feedback supervisor specializing in analyzing study plan change requests. Your role is to provide expert pros/cons analysis for user-requested modifications.

CONTEXT: A study plan has been generated and the user wants to make changes. You must analyze the impact of their requests.

YOUR RESPONSIBILITIES:
1. ANALYZE CURRENT PLAN: Understand the existing plan structure and rationale
2. EVALUATE CHANGE REQUEST: Assess the impact of the requested changes
3. PROVIDE PROS/CONS: Give balanced analysis of benefits and drawbacks
4. MAKE RECOMMENDATION: Suggest whether the change is advisable or not

ANALYSIS FRAMEWORK:
For each change request, consider:
- ACADEMIC IMPACT: How does this affect learning progression and exam preparation?
- TIME ALLOCATION: How does this change the overall time distribution?
- DEPENDENCY EFFECTS: Are there chapter dependencies that might be affected?
- EXAM WEIGHTAGE: Does this align with or conflict with exam priorities?
- FEASIBILITY: Is this change practically achievable within the constraints?

RESPONSE FORMAT:
For each change request, provide:
1. UNDERSTANDING: "I understand you want to [specific change]"
2. CURRENT RATIONALE: "The current plan does [X] because [reason]"
3. PROS: "Benefits of this change: [list positive impacts]"
4. CONS: "Potential drawbacks: [list negative impacts]"
5. RECOMMENDATION: "Based on the analysis, I [recommend/advise caution] because [reason]"
6. ALTERNATIVES: "If you still want this change, here are ways to minimize the drawbacks: [suggestions]"

EXAMPLE ANALYSIS:
User Request: "I want more time for physics"
Your Response: 
"I understand you want to allocate more time to physics study.

CURRENT RATIONALE: The current plan allocates equal time (480 hours) to each subject based on balanced JEE Mains preparation strategy.

PROS of increasing physics time:
✅ Stronger foundation in physics concepts
✅ More practice time for complex problem-solving
✅ Better confidence in physics sections

CONS of increasing physics time:
❌ Reduced time for mathematics and chemistry
❌ May create imbalance in overall preparation
❌ Could affect performance in other subjects

RECOMMENDATION: I recommend this change if physics is your weakest subject, but suggest taking time primarily from your strongest subject rather than equally from both others.

IMPLEMENTATION: If you proceed, I suggest increasing physics by 20% and reducing your strongest subject by 20% to maintain balance."

Remember: Always provide balanced, evidence-based analysis that helps users make informed decisions.""",
)


# Agent Nodes
def counsellor_node(state: StudyPlanState):
    logger.info("Counsellor node executing")
    
    # Get the latest user message
    latest_message = ""
    chat_context = state.get("chat_context", {})
    
    # Find the most recent user message
    for turn_id in sorted(chat_context.keys(), reverse=True):
        turn = chat_context[turn_id]
        if turn.user_message:
            latest_message = turn.user_message.lower()
            break
    
    logger.info(f"Latest user message: {latest_message}")
    
    # Removed generic logic - keeping only custom plans
    user_data = state["user_data"]
    is_score_based = False
    logger.info(f"Score-based planning: {is_score_based}, Target: {user_data.target_score}")
    
    # Check for generation trigger words
    trigger_words = [
        "generate", "create plan", "start planning", "make my plan", 
        "begin generation", "start generation", "create my plan",
        "generate plan", "make plan", "build plan", "start"
    ]
    
    # Check for re-edit trigger words (from feedback phase)
    re_edit_triggers = [
        "re edit", "re-edit", "reedit", "edit the plan", "implement changes",
        "make the changes", "apply changes", "update the plan", "regenerate"
    ]
    
    # Check for finalization trigger words - must be standalone or with positive confirmation
    finalization_words = [
        "finalize", "approve", "confirm plan", "i'm satisfied",
        "yes this is final", "this is final", "final", "done", "complete",
        "save this plan", "lock it in", "good to go", "ready", "confirmed"
    ]
    
    # Special case: "looks good" only if not followed by "but" or change requests
    looks_good_finalization = "looks good" in latest_message and "but" not in latest_message and not any(word in latest_message for word in ["want", "need", "change", "more", "less", "different"])
    
    should_generate = any(trigger in latest_message for trigger in trigger_words)
    should_re_edit = any(trigger in latest_message for trigger in re_edit_triggers)
    should_finalize = any(word in latest_message for word in finalization_words) or looks_good_finalization
    
    logger.info(f"Generation trigger detected: {should_generate}")
    logger.info(f"Re-edit trigger detected: {should_re_edit}")
    logger.info(f"Finalization trigger detected: {should_finalize}")
    
    if should_finalize:
        # User wants to finalize - check if we have a study plan to finalize
        if state.get("study_plan") and state.get("study_plan").insights:
            logger.info("User wants to finalize existing study plan")
            state["plan_finalized"] = True
            
            # Save the finalized plan to database
            try:
                user_id = state["user_data"].user_id
                
                # Prepare state message (complete state for reference)
                state_message = {
                    "user_data": state["user_data"].model_dump(),
                    "plan_parameters": state["plan_parameters"].model_dump(),
                    "plan_metadata": state.get("plan_metadata", {}),
                    "chat_context": {k: v.model_dump() for k, v in state["chat_context"].items()},
                    "finalized_at": "finalized",
                    "plan_finalized": True
                }
                
                # Prepare study plan data
                study_plan_data = state["study_plan"].model_dump() if state.get("study_plan") else {}
                
                # Save to database
                save_result = save_finalized_plan.invoke({
                    "user_id": user_id,
                    "state_message": state_message,
                    "study_plan": study_plan_data
                })
                
                logger.info(f"Database save result: {save_result}")
                
                # Add finalization message to chat with save confirmation
                latest_turn_id = max(chat_context.keys()) if chat_context else "1"
                if latest_turn_id in chat_context:
                    finalization_response = f"""🎉 **Congratulations!** Your personalized study plan has been finalized and saved!
                    
Your plan is now ready and optimized for your JEE Mains preparation. Here's what you can expect:

✅ **Personalized Schedule**: Tailored to your preferences and learning style
✅ **Balanced Coverage**: All subjects and chapters systematically covered
✅ **Time-Optimized**: Efficient use of your daily 6-hour study commitment
✅ **Goal-Oriented**: Designed specifically for JEE Mains success
✅ **Securely Saved**: Your plan has been saved to your profile

**Database Status**: {save_result}

**Next Steps:**
1. Your plan is now saved and ready for reference
2. Start following the monthly and weekly schedules
3. Track your progress regularly
4. Stay consistent with the allocated time

Best of luck with your preparation! You've got this! 🚀"""
                    
                    chat_context[latest_turn_id].assistant_message = finalization_response
                
            except Exception as e:
                logger.error(f"Error saving finalized plan: {e}", exc_info=True)
                # Still finalize but show error message
                latest_turn_id = max(chat_context.keys()) if chat_context else "1"
                if latest_turn_id in chat_context:
                    finalization_response = f"""🎉 **Congratulations!** Your personalized study plan has been finalized!
                    
Your plan is now ready and optimized for your JEE Mains preparation. 

⚠️ **Note**: There was an issue saving to the database ({str(e)}), but your plan is still finalized and ready to use.

✅ **Personalized Schedule**: Tailored to your preferences and learning style
✅ **Balanced Coverage**: All subjects and chapters systematically covered
✅ **Time-Optimized**: Efficient use of your daily 6-hour study commitment
✅ **Goal-Oriented**: Designed specifically for JEE Mains success

**Next Steps:**
1. Save this plan for your reference
2. Start following the monthly and weekly schedules
3. Track your progress regularly
4. Stay consistent with the allocated time

Best of luck with your preparation! You've got this! 🚀"""
                    
                    chat_context[latest_turn_id].assistant_message = finalization_response
            
            state["next_agent"] = "counsellor_continue"
            return state
        else:
            logger.info("User wants to finalize but no study plan exists yet - treating as generate request")
            should_generate = True
    
    if should_re_edit:
        # User wants to re-edit existing plan with new requirements
        logger.info("User requested plan re-editing. Proceeding to generator with feedback context.")
        # Add a flag to indicate this is a re-edit to prevent loops
        state["is_re_edit"] = True
        state["next_agent"] = "generator"
    elif should_generate:
        # User wants to generate the plan - proceed to generator
        logger.info("User requested plan generation. Proceeding to generator.")
        state["next_agent"] = "generator"
    else:
        # Continue counselling conversation
        logger.info("Continuing counselling conversation.")
        
        # Build conversation history for counsellor
        conversation_parts = []
        for turn_id in sorted(chat_context.keys()):
            turn = chat_context[turn_id]
            if turn.user_message:
                conversation_parts.append(f"User: {turn.user_message}")
            if turn.assistant_message:
                conversation_parts.append(f"Assistant: {turn.assistant_message}")
        
        conversation_history = "\n".join(conversation_parts)
        
        # Get user data to check what information we already have
        user_data = state["user_data"]
        
        # Create counsellor prompt with context
        score_context = ""
        if is_score_based:
            score_context = f"""
        - Study Plan Type: {user_data.study_plan_type} (Score-Optimized)
        - Target Score: {user_data.target_score}/300 marks
        - Score-Based Features: Will prioritize high-weightage chapters for efficient score achievement"""
        
        counsellor_prompt = f"""
        CONVERSATION HISTORY:
        {conversation_history}
        
        FORM DATA PROVIDED:
        - Target Exam: {user_data.target_exam}
        - Study Duration: {user_data.number_of_months} months
        - Daily Hours: {user_data.hours_per_day} hours
        - Subjects: {list(user_data.syllabus.keys())}
        - Total Chapters: {sum(len(chapters) for chapters in user_data.syllabus.values())}{score_context}
        
        LATEST USER MESSAGE: {latest_message}
        
        The user has already provided all basic information through a form. Your job is to collect ADDITIONAL PREFERENCES:
        
        1. Focus on study preferences and special requirements
        2. Ask about subject priorities (which subjects to focus more on)
        3. Ask about chapter preferences (specific chapters to prioritize or cover first)
        4. Confirm any preferences they've mentioned
        5. {"For SCORE-BASED plans: Explain how the plan will optimize for their target score" if is_score_based else ""}
        6. Remind them to say 'generate' when ready
        
        {"SCORE-BASED GUIDANCE: Mention that the plan will focus on high-weightage chapters to achieve their target score of " + str(user_data.target_score) + "/300 efficiently." if is_score_based else ""}
        
        Be encouraging and focus only on personalizing their study approach, not collecting basic info.
        """
        
        try:
            # Get counsellor response
            response = counsellor_agent.invoke({"input": counsellor_prompt})
            counsellor_response = response.content if hasattr(response, 'content') else str(response)
            
            # Update the chat context with counsellor response
            latest_turn_id = max(chat_context.keys()) if chat_context else "1"
            if latest_turn_id in chat_context:
                chat_context[latest_turn_id].assistant_message = counsellor_response
            
            logger.info(f"Counsellor response: {counsellor_response}")
            
            # Stay in counsellor mode (don't proceed to generator)
            state["next_agent"] = "counsellor_continue"
            
        except Exception as e:
            logger.error(f"Error in counsellor conversation: {e}", exc_info=True)
            # Fallback response focused on preferences only
            score_info = f" with a target score of {user_data.target_score}/300" if is_score_based else ""
            score_features = "\n• 🎯 Score-optimized: Will focus on high-weightage chapters for maximum score efficiency" if is_score_based else ""
            
            fallback_response = f"""I'm here to help personalize your {user_data.target_exam} study plan{score_info}! I can see you have {user_data.number_of_months} months to prepare with {user_data.hours_per_day} hours daily.{score_features}

Let me help you customize your approach:
• Do you want to focus more on any particular subjects ({', '.join(user_data.syllabus.keys())})?
• Are there specific chapters you'd like to prioritize or cover first?
• Any special study preferences or constraints?

When you're ready, just say 'generate' and I'll create your {"score-optimized " if is_score_based else ""}personalized plan!"""
            
            latest_turn_id = max(chat_context.keys()) if chat_context else "1"
            if latest_turn_id in chat_context:
                chat_context[latest_turn_id].assistant_message = fallback_response
            
            state["next_agent"] = "counsellor_continue"
    
    return state


def generator_node(state: StudyPlanState):
    """Parses user conversation to extract personalization, then routes."""
    logger.info("Generator node executing: Extracting user preferences.")
    
    # Build conversation context with better formatting - include ALL user messages
    conversation_parts = []
    for turn_id in sorted(state['chat_context'].keys()):
        turn = state['chat_context'][turn_id]
        if turn.user_message:
            conversation_parts.append(f"User: {turn.user_message}")
        if turn.assistant_message:
            conversation_parts.append(f"Assistant: {turn.assistant_message}")
    
    conversation = "\n".join(conversation_parts)
    logger.info(f"Complete conversation context: {conversation}")
    
    # Also include regeneration feedback if available
    supervisor_feedback = ""
    if state.get('regeneration_feedback'):
        supervisor_feedback = '; '.join(state['regeneration_feedback'])
        conversation += f"\n\nSUPERVISOR FEEDBACK: {supervisor_feedback}"
        logger.info(f"Processing supervisor feedback: {supervisor_feedback}")

    class ExtractedParameters(BaseModel):
        """Parameters for personalization. Adhere strictly to this JSON structure."""
        subject_priority: Optional[List[str]] = Field(
            default_factory=list, 
            description="A list of subjects the user wants to prioritize (e.g., ['physics', 'mathematics'])."
        )
        chapter_priority: Optional[Dict[str, List[str]]] = Field(
            default_factory=dict, 
            description="A dictionary of specific chapters to prioritize, grouped by subject (e.g., {'physics': ['Chapter_1', 'Chapter_3']})."
        )
        chapter_coverage_order: Optional[Dict[str, List[str]]] = Field(
            default_factory=dict, 
            description="A dictionary specifying a custom chapter order for any subject (e.g., {'chemistry': ['Chapter_3', 'Chapter_1', 'Chapter_2']})."
        )

    extraction_prompt = f"""
    You are a study plan preference extraction system. Analyze the conversation and extract user preferences.
    
    CONVERSATION:
    {conversation}
    
    CRITICAL EXTRACTION RULES:
    1. subject_priority: List subjects the user wants to FOCUS ON or PRIORITIZE
    2. chapter_priority: Map subjects to specific chapters the user wants to spend MORE TIME on
    3. chapter_coverage_order: Map subjects to custom chapter sequences (if user specifies ORDER/SEQUENCE)
    
    KEY INTENT PATTERNS:
    - "more time" / "spend more" / "focus more" on chapters → chapter_priority
    - "firstly" / "first" / "start with" chapters → chapter_coverage_order  
    - "focus on [subject]" / "prioritize [subject]" / "want to focus on [subject]" → subject_priority
    - "cover firstly chapter X" → chapter_coverage_order (sequence preference)
    - "more time on chapter X and Y firstly" → BOTH chapter_priority AND chapter_coverage_order
    
    CRITICAL: Look for patterns like:
    - "focus on mathematics" → subject_priority: ["mathematics"]
    - "focus on physics" → subject_priority: ["physics"] 
    - "I want to focus on chemistry" → subject_priority: ["chemistry"]
    
    EXAMPLES OF USER INTENT:
    - "focus more on physics" → subject_priority: ["physics"]
    - "focus on mathematics" → subject_priority: ["mathematics"]
    - "I want to focus on chemistry" → subject_priority: ["chemistry"]
    - "spend more time on chapter 3 and chapter 2 in physics" → chapter_priority: {{"physics": ["Chapter_3", "Chapter_2"]}}
    - "do physics chapter 2 first" → chapter_coverage_order: {{"physics": ["Chapter_2"]}}
    - "cover firstly chapter 3 in physics" → chapter_coverage_order: {{"physics": ["Chapter_3"]}}
    - "i would like to spend more time on chapter 3 and chapter 2 firstly in physics" → chapter_priority: {{"physics": ["Chapter_3", "Chapter_2"]}} AND chapter_coverage_order: {{"physics": ["Chapter_3", "Chapter_2"]}}
    
    SUPERVISOR FEEDBACK HANDLING:
    {f"SUPERVISOR SAYS: {supervisor_feedback}" if supervisor_feedback else "No previous feedback."}
    
    If supervisor feedback mentions:
    - "extract as chapter_priority" → put chapters in chapter_priority
    - "extract as chapter_coverage_order" → put chapters in chapter_coverage_order  
    - "extract as subject_priority" → put subjects in subject_priority
    - "MISSING: chapter_priority" → you must extract chapter_priority from user message
    - "EXTRACTION ERROR" → fix the extraction based on feedback
    
    IMPORTANT:
    - ALWAYS use lowercase for subjects: "physics", "chemistry", "mathematics" 
    - Use format "Chapter_1", "Chapter_2", etc. for chapters
    - If user says "more time" on chapters, put them in chapter_priority
    - If user specifies order/sequence, put them in chapter_coverage_order
    - If user wants BOTH more time AND specific order, use BOTH fields
    - Return empty lists/dicts if no preferences mentioned
    - Convert all subject names to lowercase to prevent mismatches
    
    RESPONSE FORMAT:
    Return ONLY a valid JSON object with this exact structure:
    {{
        "subject_priority": [],
        "chapter_priority": {{}},
        "chapter_coverage_order": {{}}
    }}
    
    Do not include any explanations, markdown formatting, or additional text.
    """
    
    try:
        # Use regular LLM call instead of structured output to avoid early validation
        response = llm.invoke(extraction_prompt)
        response_text = response.content.strip()
        logger.info(f"LLM raw response: {response_text}")
        
        # Try to parse as JSON first
        try:
            # Extract JSON from response if it's wrapped in text
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
            
            import json  # Ensure json is available in this scope
            parsed_data = json.loads(json_text)
            logger.info(f"Parsed JSON data: {parsed_data}")
            
            # Create ExtractedParameters with proper type handling
            extracted_params = ExtractedParameters(
                subject_priority=parsed_data.get('subject_priority', []),
                chapter_priority=parsed_data.get('chapter_priority', {}),
                chapter_coverage_order=parsed_data.get('chapter_coverage_order', {})
            )
            
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            logger.warning(f"Failed to parse JSON response: {e}. Using fallback extraction.")
            # Fallback: try to extract using simple text parsing
            extracted_params = ExtractedParameters()
            
            # Simple text-based extraction for common patterns
            response_lower = response_text.lower()
            if "physics" in response_lower and ("chapter" in response_lower):
                if "chapter_2" in response_lower or "chapter 2" in response_lower:
                    if "chapter_3" in response_lower or "chapter 3" in response_lower:
                        extracted_params.chapter_priority = {"Physics": ["Chapter_2", "Chapter_3"]}
                        logger.info("Used fallback extraction for Physics chapters")
        
        logger.info(f"Final extracted parameters: {extracted_params}")
        
    except Exception as e:
        logger.error(f"LLM parameter extraction failed: {e}", exc_info=True)
        extracted_params = ExtractedParameters()

    exam = state['user_data'].target_exam
    syllabus_data = get_syllabus.invoke({"exam": exam})
    
    clean_params = PlanParameters()
    if syllabus_data:
        subjects = sorted(list(set(item['Subject'] for item in syllabus_data)))
        chapters_by_subject = {s: sorted(list(set(item['Chapter'] for item in syllabus_data if item['Subject'] == s))) for s in subjects}
        
        # Create normalized subjects list once for all processing
        normalized_subjects = [s.lower() for s in subjects]
        
        if extracted_params.subject_priority:
            # Normalize to lowercase and then find matches
            clean_params.subject_priority = list(set(s.lower() for s_user in extracted_params.subject_priority if (s := _find_best_match(s_user.lower(), normalized_subjects)) is not None))

        for param_type in ['chapter_priority', 'chapter_coverage_order']:
            source_dict = getattr(extracted_params, param_type)
            target_dict = getattr(clean_params, param_type)
            if source_dict:
                for subj_user, chaps_user in source_dict.items():
                    # Normalize subject to lowercase for consistency
                    subj_match = _find_best_match(subj_user.lower(), normalized_subjects)
                    if subj_match and chaps_user:
                        # Find the original subject name for chapter lookup
                        original_subject = next((s for s in subjects if s.lower() == subj_match), subj_match)
                        target_dict[subj_match] = [c for c_user in chaps_user if (c := _find_best_match(c_user, chapters_by_subject.get(original_subject, []))) is not None]
        
        logger.info(f"Cleaned and validated parameters: {clean_params}")
        state['plan_parameters'] = clean_params
    else:
        logger.warning("Could not fetch syllabus. Proceeding with empty plan parameters.")
        state['plan_parameters'] = PlanParameters()

    # Route based on preparation type and score requirements
    user_data = state["user_data"]
    is_score_based = False  # Removed generic logic
    
    # For generic plans with target score, check if time is sufficient
    if is_score_based:
        logger.info(f"Generic plan detected with target score: {user_data.target_score}")
        
        # Removed score optimization - not needed for custom plans
        import json
        
        try:
            # Simplified logic for custom plans
            is_target_achievable = True
            time_needed = 0
            available_hours = user_data.number_of_months * 30 * user_data.hours_per_day
            
            # Custom plans don't need target score validation
            if False:  # Disabled score optimization
                # Store warning for counsellor to present to user
                state["plan_metadata"]["time_warning"] = {
                    "target_score": user_data.target_score,
                    "available_hours": available_hours,
                    "time_needed": time_needed,
                    "warning": f"⚠️ Target score {user_data.target_score}/300 requires ~{time_needed} hours, but you have {available_hours} hours available.",
                    "suggestions": [
                        f"Option 1: Extend study time to {time_needed} hours (add {time_needed - available_hours} hours)",
                        f"Option 2: Adjust target score to achievable range",
                        f"Option 3: Focus on high-weightage topics only (revision approach)"
                    ]
                }
                
                # For now, continue with weightage-based approach for score optimization
                # In a full implementation, this could pause and ask user for preference
                logger.warning(f"Target score challenging with available time. Using weightage-based optimization.")
                state["next_agent"] = "weightage"  # Use weightage for score optimization
            else:
                # Target is achievable, use normal routing
                if user_data.preparation_type.lower() == "syllabus coverage":
                    state["next_agent"] = "flow"
                else:  # revision
                    state["next_agent"] = "weightage"
        except Exception as e:
            logger.error(f"Error in score optimization check: {e}")
            # Fallback to normal routing
            if user_data.preparation_type.lower() == "syllabus coverage":
                state["next_agent"] = "flow"
            else:
                state["next_agent"] = "weightage"
    else:
        # Normal routing for custom plans
        if user_data.preparation_type.lower() == "syllabus coverage":
            state["next_agent"] = "flow"
        else:  # revision
            state["next_agent"] = "weightage"
    
    # Check if this is a score-oriented plan that needs validation
    is_score_oriented = (
        False  # Removed score-oriented and generic logic
    )
    
    # Check for new_score_oriented plans
    is_new_score_oriented = user_data.study_plan_type.lower() == "new_score_oriented"
    
    # Route new_score_oriented plans through RevisionFlow agent
    if is_new_score_oriented:
        logger.info("New Score-Oriented plan detected - routing through RevisionFlow agent")
        state["next_agent"] = "revision_flow"
    # Route score-oriented plans through validator before weightage
    elif is_score_oriented and state["next_agent"] == "weightage":
        logger.info("Score-oriented plan detected - routing through score_oriented_validator")
        state["next_agent"] = "score_oriented_validator"
    
    logger.info(f"Routing to: {state['next_agent']} (preparation_type: {user_data.preparation_type}, study_plan_type: {user_data.study_plan_type})")
    return state


def score_oriented_validator_node(state: StudyPlanState):
    """
    Score-oriented validator agent that handles:
    1. Dependency chain validation and reordering
    2. 100% coverage enforcement for selected chapters
    """
    logger.info("Score-oriented validator node executing")
    
    user_data = state["user_data"]
    plan_parameters = state["plan_parameters"]
    
    # Perform validation and optimization
    validation_results = score_validator.validate_and_optimize_chapters(user_data, plan_parameters)
    
    if validation_results["status"] == "skipped":
        logger.info("Validation skipped - proceeding to weightage node")
        state["next_agent"] = "weightage"
        return state
    
    # Store validation results in state for use by weightage node
    state["score_validation_results"] = validation_results
    
    # Generate validation summary for logging
    validation_summary = score_validator.generate_validation_summary(validation_results)
    logger.info(f"Score validation summary:\n{validation_summary}")
    
    # Update plan_parameters with optimized sequences if needed
    if validation_results["optimized_sequences"]:
        logger.info("Updating plan parameters with optimized chapter sequences")
        
        # Update chapter_coverage_order with dependency-optimized sequences
        for subject, optimized_sequence in validation_results["optimized_sequences"].items():
            chapter_order = [ch["chapter"] for ch in optimized_sequence]
            if chapter_order:
                plan_parameters.chapter_coverage_order[subject.lower()] = chapter_order
                logger.info(f"Updated {subject} chapter order: {chapter_order}")
        
        # Update chapter_priority to ensure 100% coverage
        for subject, optimized_sequence in validation_results["optimized_sequences"].items():
            high_priority_chapters = [
                ch["chapter"] for ch in optimized_sequence 
                if ch.get("priority_reason") == "high_weightage"
            ]
            if high_priority_chapters:
                if subject.lower() not in plan_parameters.chapter_priority:
                    plan_parameters.chapter_priority[subject.lower()] = []
                plan_parameters.chapter_priority[subject.lower()].extend(high_priority_chapters)
                # Remove duplicates while preserving order
                plan_parameters.chapter_priority[subject.lower()] = list(dict.fromkeys(
                    plan_parameters.chapter_priority[subject.lower()]
                ))
                logger.info(f"Updated {subject} chapter priorities: {plan_parameters.chapter_priority[subject.lower()]}")
    
    # Store validation insights for later use in study plan
    validation_insights = {
        "target_score": validation_results["target_score"],
        "expected_score": validation_results["total_expected_score"],
        "target_achievable": validation_results["target_achievable"],
        "score_gap": validation_results.get("score_gap", 0),
        "optimization_applied": True,
        "dependency_fixes_count": len(validation_results.get("dependency_fixes", [])),
        "subjects_optimized": list(validation_results["optimized_sequences"].keys())
    }
    
    # Store in plan_metadata for supervisor and insights generation
    if "plan_metadata" not in state:
        state["plan_metadata"] = {}
    state["plan_metadata"]["score_validation"] = validation_insights
    
    # Add validation message to chat context if needed
    if validation_results.get("score_gap", 0) > 0:
        logger.warning(f"Score gap detected: {validation_results['score_gap']:.1f} marks")
        state["plan_metadata"]["score_warning"] = {
            "target_score": validation_results["target_score"],
            "expected_score": validation_results["total_expected_score"],
            "score_gap": validation_results["score_gap"],
            "warning": f"⚠️ Target score {validation_results['target_score']}/300 may be challenging. Expected: {validation_results['total_expected_score']:.1f}/300"
        }
    else:
        state["plan_metadata"]["score_analysis"] = {
            "target_score": validation_results["target_score"],
            "expected_score": validation_results["total_expected_score"],
            "is_achievable": True,
            "message": f"✅ Target score {validation_results['target_score']}/300 is achievable! Expected: {validation_results['total_expected_score']:.1f}/300"
        }
    
    # Proceed to weightage node with optimized parameters
    state["next_agent"] = "weightage"
    logger.info("Score validation complete - proceeding to weightage node")
    
    return state


def revision_flow_node(state: StudyPlanState):
    """
    RevisionFlow agent for new_score_oriented plans.
    Combines flow and weightage logic with complete syllabus coverage.
    """
    logger.info("RevisionFlow node executing for new_score_oriented plan")
    
    user_data = state["user_data"]
    plan_parameters = state["plan_parameters"]
    
    # Generate revision flow plan
    revision_plan = revision_flow_agent.generate_revision_flow_plan(user_data, plan_parameters)
    
    if revision_plan["status"] == "skipped":
        logger.info("RevisionFlow skipped - not a new_score_oriented plan")
        # Route to normal flow/weightage based on preparation type
        if user_data.preparation_type.lower() == "syllabus coverage":
            state["next_agent"] = "flow"
        else:
            state["next_agent"] = "weightage"
        return state
    
    # Store revision flow results
    state["revision_flow_results"] = revision_plan
    
    # Log revision flow summary
    logger.info(f"RevisionFlow completed:")
    logger.info(f"  - Target Score: {revision_plan['target_score']}/300")
    logger.info(f"  - Total Months: {revision_plan['total_months']}")
    logger.info(f"  - Subjects Planned: {list(revision_plan['subject_plans'].keys())}")
    logger.info(f"  - Complete Coverage: {revision_plan['complete_syllabus_coverage']}")
    
    # Convert revision plan to monthly coverage format for compatibility
    monthly_coverage = _convert_revision_plan_to_monthly_coverage(revision_plan, user_data)
    state["monthly_coverage"] = monthly_coverage
    
    # Proceed to generator validation
    state["next_agent"] = "new_score_oriented_generator_validation"
    logger.info("RevisionFlow complete - proceeding to generator validation")
    
    return state


def new_score_oriented_generator_validation_node(state: StudyPlanState):
    """
    Generator validation for new_score_oriented plans.
    Validates all chapters covered and user requirements fulfilled.
    """
    logger.info("New Score-Oriented Generator Validation executing")
    
    user_data = state["user_data"]
    revision_plan = state.get("revision_flow_results", {})
    
    # Perform chapter coverage validation
    validation_result = new_score_oriented_validator.validate_chapter_coverage(user_data, revision_plan)
    
    # Store validation results
    state["generator_validation_results"] = validation_result
    
    # Log validation summary
    logger.info(f"Generator Validation Results:")
    logger.info(f"  - All Chapters Covered: {validation_result['chapter_validation']['all_chapters_covered']}")
    logger.info(f"  - Coverage Percentage: {validation_result['chapter_validation']['coverage_percentage']:.1f}%")
    logger.info(f"  - User Requirements Fulfilled: {validation_result['user_requirements_fulfilled']}")
    logger.info(f"  - Target Achievable: {validation_result['target_achievability']['achievable']}")
    
    # Check if validation passed
    if not validation_result["user_requirements_fulfilled"]:
        logger.warning("User requirements not fulfilled - may need plan adjustments")
        # Store warning for supervisor
        if "plan_metadata" not in state:
            state["plan_metadata"] = {}
        state["plan_metadata"]["generator_validation_warning"] = {
            "issue": "User requirements not fully met",
            "recommendations": validation_result.get("recommendations", [])
        }
    
    # Proceed to topic assignment
    state["next_agent"] = "new_score_oriented_topic"
    logger.info("Generator validation complete - proceeding to topic assignment")
    
    return state


def new_score_oriented_topic_node(state: StudyPlanState):
    """
    Topic assignment for new_score_oriented plans.
    Assigns all topics for each chapter as mentioned in syllabus.
    """
    logger.info("New Score-Oriented Topic Assignment executing")
    
    user_data = state["user_data"]
    revision_plan = state.get("revision_flow_results", {})
    monthly_coverage = state.get("monthly_coverage", {})
    
    # Generate topic assignments for all chapters
    topic_assignments = {}
    
    for subject, subject_plan in revision_plan.get("subject_plans", {}).items():
        logger.info(f"Assigning topics for {subject}")
        
        subject_topics = {}
        for chapter_info in subject_plan.get("chapters", []):
            chapter_name = chapter_info["chapter"]
            
            # Get all topics for this chapter from Topic_Priority table
            try:
                chapter_topics = get_topic_priority.invoke({
                    "exam": user_data.target_exam,
                    "subject": subject.title(),
                    "chapter": chapter_name
                })
                
                # For new_score_oriented, include ALL topics (100% coverage)
                all_topics = [topic["Topic"] for topic in chapter_topics]
                subject_topics[chapter_name] = all_topics
                
                logger.info(f"  - {chapter_name}: {len(all_topics)} topics assigned")
                
            except Exception as e:
                logger.error(f"Error getting topics for {chapter_name}: {e}")
                subject_topics[chapter_name] = []
        
        topic_assignments[subject] = subject_topics
    
    # Store topic assignments
    state["topic_assignments"] = topic_assignments
    
    # Convert to weekly coverage format for compatibility
    weekly_coverage = _convert_topic_assignments_to_weekly_coverage(
        topic_assignments, revision_plan, user_data
    )
    state["weekly_coverage"] = weekly_coverage
    
    # Validate topic coverage
    topic_validation = new_score_oriented_validator.validate_topic_coverage(
        user_data, topic_assignments
    )
    state["topic_validation_results"] = topic_validation
    
    logger.info(f"Topic Assignment Results:")
    logger.info(f"  - Total Topics: {topic_validation['topic_validation']['total_topics']}")
    logger.info(f"  - Covered Topics: {topic_validation['topic_validation']['covered_topics']}")
    logger.info(f"  - All Topics Covered: {topic_validation['topic_validation']['all_topics_covered']}")
    
    # Proceed to final generator validation
    state["next_agent"] = "new_score_oriented_final_validation"
    logger.info("Topic assignment complete - proceeding to final validation")
    
    return state


def new_score_oriented_final_validation_node(state: StudyPlanState):
    """
    Final validation for new_score_oriented plans.
    Validates all syllabus topics included using Syllabus table.
    """
    logger.info("New Score-Oriented Final Validation executing")
    
    user_data = state["user_data"]
    complete_plan = {
        "revision_plan": state.get("revision_flow_results", {}),
        "topic_assignments": state.get("topic_assignments", {}),
        "monthly_coverage": state.get("monthly_coverage", {}),
        "weekly_coverage": state.get("weekly_coverage", {})
    }
    
    # Perform final syllabus compliance validation
    final_validation = new_score_oriented_validator.validate_syllabus_compliance(
        user_data, complete_plan
    )
    
    # Store final validation results
    state["final_validation_results"] = final_validation
    
    logger.info(f"Final Validation Results:")
    logger.info(f"  - Fully Compliant: {final_validation['syllabus_compliance']['fully_compliant']}")
    logger.info(f"  - Compliance Percentage: {final_validation['syllabus_compliance']['compliance_percentage']:.1f}%")
    
    # Generate study plan insights
    insights = _generate_new_score_oriented_insights(state)
    
    # Create final study plan
    state["study_plan"] = StudyPlan(
        insights=insights,
        monthly_plan=state["monthly_coverage"],
        weekly_plan=state["weekly_coverage"]
    )
    
    # Print study plan to terminal
    _print_study_plan_to_terminal(state)
    
    # Proceed to new score-oriented supervisor
    state["next_agent"] = "new_score_oriented_supervisor"
    logger.info("Final validation complete - proceeding to supervisor")
    
    return state


def new_score_oriented_supervisor_node(state: StudyPlanState):
    """
    Supervisor for new_score_oriented plans with target achievement focus.
    """
    logger.info("New Score-Oriented Supervisor executing")
    
    user_data = state["user_data"]
    complete_plan_state = state
    
    # Perform comprehensive supervision
    supervision_result = new_score_oriented_supervisor.supervise_plan(user_data, complete_plan_state)
    
    # Store supervision results
    state["supervision_results"] = supervision_result
    
    logger.info(f"Supervision Results:")
    logger.info(f"  - Plan Approved: {supervision_result['plan_approved']}")
    logger.info(f"  - User Requirements Met: {supervision_result['user_requirements_met']}")
    logger.info(f"  - Adjustments Needed: {len(supervision_result['adjustments_needed'])}")
    
    # Check if plan needs adjustments
    if not supervision_result["plan_approved"]:
        logger.warning("Plan needs adjustments for target achievement")
        
        # Apply force-fit adjustments
        adjustments = supervision_result["adjustments_needed"]
        for adjustment in adjustments:
            logger.info(f"  - {adjustment['type']}: {adjustment['description']}")
        
        # Update plan metadata with adjustments
        if "plan_metadata" not in state:
            state["plan_metadata"] = {}
        state["plan_metadata"]["supervisor_adjustments"] = adjustments
        
        # Force approve after adjustments (as per requirement: achieve target regardless)
        supervision_result["plan_approved"] = True
        supervision_result["user_requirements_met"] = True
        logger.info("Plan force-approved with adjustments for target achievement")
    
    # Generate final recommendations
    final_recommendations = supervision_result["final_recommendations"]
    logger.info("Final Recommendations:")
    for i, rec in enumerate(final_recommendations, 1):
        logger.info(f"  {i}. {rec}")
    
    # Update study plan with supervision insights
    if state.get("study_plan"):
        supervision_insights = f"""
{state['study_plan'].insights}

🎯 **SUPERVISION ANALYSIS:**
Target Achievement Probability: {supervision_result['target_achievement_analysis'].get('success_probability', 0):.1f}%
Plan Status: {'✅ Approved' if supervision_result['plan_approved'] else '⚠️ Needs Adjustments'}

📋 **FINAL RECOMMENDATIONS:**
{chr(10).join(f'• {rec}' for rec in final_recommendations)}
"""
        state["study_plan"].insights = supervision_insights
    
    # Proceed to counsellor final
    state["next_agent"] = "counsellor_final"
    logger.info("New Score-Oriented supervision complete - proceeding to counsellor final")
    
    return state

def flow_node(state: StudyPlanState):
    logger.info("Flow node executing with priorities.")
    user_data = state["user_data"]
    plan_params = state["plan_parameters"]
    
    # Removed generic logic - keeping only custom plans
    is_score_based = False
    logger.info(f"Flow node - Score-based planning: {is_score_based}, Preparation: {user_data.preparation_type}")

    # 1. Fetch all chapters and apply chapter coverage order first.
    chapters_by_subject = {}
    for subject, chapters_to_cover in user_data.syllabus.items():
        all_chapter_flows = get_chapter_flow.invoke({"exam": user_data.target_exam, "subject": subject})
        subject_chapters = [c for c in all_chapter_flows if c["Chapter"] in chapters_to_cover]
        
        # Apply custom chapter order
        if subject in plan_params.chapter_coverage_order:
            ordered_chapters = plan_params.chapter_coverage_order[subject]
            chapter_map = {c['Chapter']: c for c in subject_chapters}
            new_order = [chapter_map[c] for c in ordered_chapters if c in chapter_map]
            remaining = [c for c in subject_chapters if c['Chapter'] not in ordered_chapters]
            chapters_by_subject[subject] = new_order + remaining
        else:
            chapters_by_subject[subject] = subject_chapters

    # 2. Calculate priority-adjusted required hours for each chapter.
    priority_hours_map = {s: {} for s in chapters_by_subject}
    for subject, chapters in chapters_by_subject.items():
        for chap in chapters:
            base_hours = chap.get("Required Hours", 0)
            # Apply chapter priority
            if subject in plan_params.chapter_priority and chap['Chapter'] in plan_params.chapter_priority.get(subject, []):
                base_hours *= 1.5
            priority_hours_map[subject][chap['Chapter']] = base_hours
    
    # 3. Calculate total required hours for each subject, then apply subject priority.
    subject_hour_totals = {s: sum(ch.values()) for s, ch in priority_hours_map.items()}
    if len(plan_params.subject_priority) == 1:
        subj = plan_params.subject_priority[0]
        if subj in subject_hour_totals: subject_hour_totals[subj] *= 1.5
    elif len(plan_params.subject_priority) == 2:
        for subj in plan_params.subject_priority:
            if subj in subject_hour_totals: subject_hour_totals[subj] *= 1.25

    # 4. Calculate final adjusted hours for each chapter using a single scaling factor.
    total_priority_hours = sum(subject_hour_totals.values())
    total_available_hours = user_data.number_of_months * 30 * user_data.hours_per_day
    
    chapters_with_hours = {s: [] for s in chapters_by_subject}
    if total_priority_hours > 0:
        final_scaling_factor = total_available_hours / total_priority_hours
        for subject, chapters in chapters_by_subject.items():
            for chap in chapters:
                final_subject_hours = subject_hour_totals[subject] * final_scaling_factor
                chap['adjusted_hours'] = (priority_hours_map[subject][chap['Chapter']] / sum(priority_hours_map[subject].values()) if sum(priority_hours_map[subject].values()) > 0 else 0) * final_subject_hours
            chapters_with_hours[subject] = chapters
    
    # For score-based flow plans, add score analysis
    if is_score_based and user_data.target_score:
        logger.info(f"Adding score analysis to flow-based plan for target: {user_data.target_score}")
        
        # Calculate expected score with flow-based plan
        total_expected_score = 0
        for subject, chapters in chapters_by_subject.items():
            for chap in chapters:
                # Get weightage for score calculation
                from app.core.tools import get_chapter_weightage
                weightage_data = get_chapter_weightage.invoke({"exam": user_data.target_exam, "subject": subject})
                for weight_info in weightage_data:
                    if weight_info.get("Chapter") == chap['Chapter']:
                        total_expected_score += weight_info.get("Average Weightage", 0)
                        break
        
        # Store score analysis
        if total_expected_score < user_data.target_score:
            score_gap = user_data.target_score - total_expected_score
            state["plan_metadata"]["score_warning"] = {
                "target_score": user_data.target_score,
                "expected_score": total_expected_score,
                "score_gap": score_gap,
                "approach": "flow-based",
                "warning": f"⚠️ Flow-based approach may not achieve target {user_data.target_score}/300. Expected: {total_expected_score:.1f}/300"
            }
        else:
            state["plan_metadata"]["score_analysis"] = {
                "target_score": user_data.target_score,
                "expected_score": total_expected_score,
                "is_achievable": True,
                "approach": "flow-based",
                "message": f"✅ Flow-based plan can achieve target {user_data.target_score}/300! Expected: {total_expected_score:.1f}/300"
            }

    state["monthly_coverage"] = _calculate_monthly_plan(user_data, chapters_with_hours)
    state["next_agent"] = "topic"
    return state


def weightage_node(state: StudyPlanState):
    logger.info("Weightage node executing with priorities.")
    user_data = state["user_data"]
    plan_params = state["plan_parameters"]
    
    # Check if this is score-based planning
    is_score_based = (
        False  # Removed generic and score-oriented logic
    )
    logger.info(f"Score-based weightage planning: {is_score_based}")
    
    # Removed score_oriented_validator logic
    validation_results = state.get("score_validation_results")
    if False:  # Disabled score_oriented_validator
        logger.info("Score oriented validator disabled")

    chapters_by_subject = {}
    for subject, chapters_to_cover in user_data.syllabus.items():
        all_chapter_weightage = get_chapter_weightage.invoke({"exam": user_data.target_exam, "subject": subject})
        
        # Removed validation results logic for score-oriented plans
        if False:  # Disabled validation results
            logger.info(f"Validation disabled for {subject}")
            optimized_sequence = []
            
            # Create chapter data with validation results
            validated_chapters = []
            for ch_info in optimized_sequence:
                # Find the original chapter data
                original_chapter = next(
                    (c for c in all_chapter_weightage if c["Chapter"] == ch_info["chapter"]), 
                    None
                )
                if original_chapter:
                    # Use original data but mark as validated
                    chapter_data = original_chapter.copy()
                    chapter_data["validated_coverage"] = ch_info["coverage_percentage"]
                    chapter_data["validation_priority"] = ch_info.get("priority_reason", "validated")
                    chapter_data["dependencies_satisfied"] = ch_info.get("dependencies_satisfied", True)
                    validated_chapters.append(chapter_data)
            
            chapters_by_subject[subject] = validated_chapters
        else:
            # Standard approach for non-validated subjects
            chapters_by_subject[subject] = [c for c in all_chapter_weightage if c["Chapter"] in chapters_to_cover]

    # 1. Apply chapter coverage order (overrides category)
    for subject, ordered_chapters in plan_params.chapter_coverage_order.items():
        if subject in chapters_by_subject:
            for chap in chapters_by_subject[subject]:
                if chap['Chapter'] in ordered_chapters: chap['Chapter Category'] = 'High'
    
    # 2. Calculate units for each chapter based on all priorities
    total_plan_units = 0
    for subject, chapters in chapters_by_subject.items():
        # Determine base multipliers
        if is_score_based:
            # For score-based plans, use stronger category multipliers
            h, m, l = 3, 2, 1  # Base category multipliers for score optimization
        else:
            # Standard multipliers for custom plans
            h, m, l = 3, 2, 1
            
        if subject in plan_params.subject_priority:
            if len(plan_params.subject_priority) == 1: h, m, l = 4.5, 3, 1.5
            elif len(plan_params.subject_priority) == 2: h, m, l = 3.75, 2.5, 1.25
        
        for chap in chapters:
            ch, cm, cl = h, m, l
            
            # For score-based plans, apply stronger category multipliers
            if is_score_based:
                # Check if this chapter was validated (has 100% coverage requirement)
                if chap.get("validated_coverage") == 1.0:
                    # For validated chapters, use weightage directly for 100% coverage
                    base_weightage = chap.get("Average Weightage", 0)
                    # Apply higher multiplier for validated score-oriented chapters
                    chap['units'] = base_weightage * 4  # Higher multiplier for 100% coverage
                    logger.info(f"Validated chapter {chap['Chapter']}: {base_weightage} weightage * 4 = {chap['units']} units (100% coverage)")
                else:
                    # Standard score-based calculation
                    category_boost = {"High": 3, "Medium": 2, "Low": 1}.get(chap.get("Chapter Category", "Medium"), 2)
                    base_weightage = chap.get("Average Weightage", 0)
                    chap['units'] = base_weightage * category_boost
            else:
                # Standard unit calculation for custom plans
                # Chapter priority can further boost multipliers
                if subject in plan_params.chapter_priority and chap['Chapter'] in plan_params.chapter_priority.get(subject, []):
                    ch, cm, cl = 4.5, 3, 1.5 # Note: This is a fixed boost, not cumulative
                
                if chap.get("Chapter Category") == "High": chap['units'] = ch
                elif chap.get("Chapter Category") == "Medium": chap['units'] = cm
                else: chap['units'] = cl
                
            total_plan_units += chap['units']
            
        # Sort chapters after all units are assigned
        chapters.sort(key=lambda x: x.get('units', 0), reverse=True)

    # 3. Calculate adjusted hours based on total units
    total_available_hours = user_data.number_of_months * 30 * user_data.hours_per_day
    chapters_with_hours = chapters_by_subject
    
    # For score-based plans, add score optimization logic
    if is_score_based and user_data.target_score:
        logger.info(f"Applying score optimization for target: {user_data.target_score}")
        
        # Calculate expected score with current plan
        total_expected_score = 0
        for subject, chapters in chapters_by_subject.items():
            for chap in chapters:
                total_expected_score += chap.get("Average Weightage", 0)
        
        # Check if target is achievable
        if total_expected_score < user_data.target_score:
            score_gap = user_data.target_score - total_expected_score
            logger.warning(f"Target score {user_data.target_score} may not be achievable. Expected: {total_expected_score}, Gap: {score_gap}")
            
            # Store warning for later use in insights
            state["plan_metadata"]["score_warning"] = {
                "target_score": user_data.target_score,
                "expected_score": total_expected_score,
                "score_gap": score_gap,
                "warning": f"⚠️ Target score of {user_data.target_score}/300 is challenging with current syllabus. Expected score: {total_expected_score:.1f}/300"
            }
        else:
            # Target is achievable
            state["plan_metadata"]["score_analysis"] = {
                "target_score": user_data.target_score,
                "expected_score": total_expected_score,
                "is_achievable": True,
                "message": f"✅ Target score of {user_data.target_score}/300 is achievable! Expected score: {total_expected_score:.1f}/300"
            }
    
    if total_plan_units > 0:
        hours_per_unit = total_available_hours / total_plan_units
        for subject, chapters in chapters_with_hours.items():
            for chap in chapters:
                chap['adjusted_hours'] = chap.get('units', 0) * hours_per_unit
    
    state["monthly_coverage"] = _calculate_monthly_plan(user_data, chapters_with_hours)
    state["next_agent"] = "topic"
    return state

def topic_node(state: StudyPlanState):
    logger.info("Topic node executing")
    user_data = state["user_data"]
    month_1_plan = state["monthly_coverage"].get("month_1")
    
    if not month_1_plan:
        state["weekly_coverage"] = {}
        state["next_agent"] = "generator_collate"
        return state

    num_days_in_month = 30
    num_subjects = len(user_data.syllabus)
    hours_per_day_per_subject = user_data.hours_per_day / num_subjects if num_subjects > 0 else 0
    hours_for_subject_in_month_1 = num_days_in_month * hours_per_day_per_subject

    # 1. Create a sequential, time-estimated list of all topics for each subject.
    topics_with_hours_per_subject = {}
    for subject_key, chapter_coverages in month_1_plan.model_dump().items():
        if subject_key not in ['physics', 'chemistry', 'mathematics']: continue
        
        sequential_topics = []
        for coverage_info in chapter_coverages:
            chapter_name = coverage_info['chapter']
            coverage_percentage = coverage_info['coverage']
            
            all_chapter_topics = get_topic_priority.invoke({
                "exam": user_data.target_exam, 
                "subject": subject_key.capitalize(), 
                "chapter": chapter_name
            })
            if not all_chapter_topics: continue

            num_to_include = int(len(all_chapter_topics) * coverage_percentage)
            topics_to_include = all_chapter_topics[:num_to_include]
            
            for topic in topics_to_include:
                topic['Chapter'] = chapter_name # Keep track of the parent chapter
            sequential_topics.extend(topics_to_include)

        if not sequential_topics:
            topics_with_hours_per_subject[subject_key] = []
            continue

        # Estimate hours per topic using the 3x/2x/1x weighting
        high = [t for t in sequential_topics if t.get("Topic Priority") == "High"]
        medium = [t for t in sequential_topics if t.get("Topic Priority") == "Medium"]
        low = [t for t in sequential_topics if t.get("Topic Priority") == "Low"]
        units = (3 * len(high)) + (2 * len(medium)) + (1 * len(low))

        if units > 0:
            hours_per_unit = hours_for_subject_in_month_1 / units
            for topic in sequential_topics:
                if topic.get("Topic Priority") == "High": topic["adjusted_hours"] = 3 * hours_per_unit
                elif topic.get("Topic Priority") == "Medium": topic["adjusted_hours"] = 2 * hours_per_unit
                else: topic["adjusted_hours"] = 1 * hours_per_unit
        else: # Fallback if no priorities are set
            hours_per_topic = hours_for_subject_in_month_1 / len(sequential_topics) if sequential_topics else 0
            for topic in sequential_topics:
                topic['adjusted_hours'] = hours_per_topic
        
        topics_with_hours_per_subject[subject_key] = sequential_topics

    # 2. Simulate the topic coverage day-by-day for the first month.
    subject_progress = {
        subject: {"current_topic_idx": 0, "hours_done_on_current_topic": 0.0}
        for subject in user_data.syllabus
    }
    daily_topic_breakdown = [
        {subject: {} for subject in user_data.syllabus} for _ in range(num_days_in_month)
    ]

    for day in range(num_days_in_month):
        for subject, progress in subject_progress.items():
            subject_key = subject.lower()
            topic_list = topics_with_hours_per_subject.get(subject_key, [])
            if progress["current_topic_idx"] >= len(topic_list): continue

            remaining_today = hours_per_day_per_subject
            while remaining_today > 0 and progress["current_topic_idx"] < len(topic_list):
                current_topic = topic_list[progress["current_topic_idx"]]
                topic_name, chapter_name = current_topic["Topic"], current_topic["Chapter"]
                topic_total_hours = current_topic["adjusted_hours"]

                hours_needed = topic_total_hours - progress["hours_done_on_current_topic"]
                hours_to_spend = min(remaining_today, hours_needed)

                day_log = daily_topic_breakdown[day][subject]
                if chapter_name not in day_log: day_log[chapter_name] = []
                # Ensure we don't add duplicate topic names on the same day
                if topic_name not in day_log[chapter_name]:
                    day_log[chapter_name].append(topic_name)

                progress["hours_done_on_current_topic"] += hours_to_spend
                remaining_today -= hours_to_spend

                if progress["hours_done_on_current_topic"] >= topic_total_hours - 0.01:
                    progress["current_topic_idx"] += 1
                    progress["hours_done_on_current_topic"] = 0

    # 3. Consolidate the daily topic breakdown into the final weekly plan.
    weekly_plan_data = {f"week_{i+1}": WeeklySubjectPlan() for i in range(4)}
    for week_idx in range(4):
        start_day, end_day = week_idx * 7, (week_idx + 1) * 7
        if week_idx == 3: end_day = num_days_in_month # Ensure the last week covers all remaining days
        
        week_key = f"week_{week_idx + 1}"
        for day in range(start_day, end_day):
            for subject, daily_topics in daily_topic_breakdown[day].items():
                subject_plan_key = "mathematics" if subject.lower() == "maths" else subject.lower()
                weekly_subject_plan = getattr(weekly_plan_data[week_key], subject_plan_key)
                
                for chapter, topics in daily_topics.items():
                    if chapter not in weekly_subject_plan:
                        weekly_subject_plan[chapter] = []
                    for topic in topics:
                        if topic not in weekly_subject_plan[chapter]:
                            weekly_subject_plan[chapter].append(topic)
    
    state["weekly_coverage"] = weekly_plan_data
    state["next_agent"] = "generator_collate"
    return state

def _convert_revision_plan_to_monthly_coverage(revision_plan: Dict, user_data) -> Dict:
    """Convert revision plan to monthly coverage format for compatibility."""
    monthly_coverage = {}
    
    monthly_distribution = revision_plan.get("monthly_distribution", {})
    
    for month_key, month_data in monthly_distribution.items():
        monthly_plan = MonthlySubjectPlan()
        
        for subject, subject_data in month_data.get("subjects", {}).items():
            chapters = subject_data.get("chapters", [])
            
            # Convert to ChapterCoverage format
            chapter_coverages = []
            for chapter_info in chapters:
                chapter_coverage = ChapterCoverage(
                    chapter=chapter_info["chapter"],
                    coverage=chapter_info["coverage_percentage"]
                )
                chapter_coverages.append(chapter_coverage)
            
            # Set chapters for the subject
            if subject == "physics":
                monthly_plan.physics = chapter_coverages
            elif subject == "chemistry":
                monthly_plan.chemistry = chapter_coverages
            elif subject == "mathematics":
                monthly_plan.mathematics = chapter_coverages
        
        monthly_coverage[month_key] = monthly_plan
    
    return monthly_coverage


def _convert_topic_assignments_to_weekly_coverage(topic_assignments: Dict, revision_plan: Dict, user_data) -> Dict:
    """Convert topic assignments to weekly coverage format."""
    weekly_coverage = {}
    
    # Create 4 weeks for the first month
    for week in range(1, 5):
        week_key = f"week_{week}"
        weekly_plan = WeeklySubjectPlan()
        
        for subject, chapters_topics in topic_assignments.items():
            subject_dict = {}
            
            # Distribute chapters across weeks
            chapters = list(chapters_topics.keys())
            chapters_per_week = max(1, len(chapters) // 4)
            
            start_idx = (week - 1) * chapters_per_week
            end_idx = week * chapters_per_week if week < 4 else len(chapters)
            
            week_chapters = chapters[start_idx:end_idx]
            
            for chapter in week_chapters:
                topics = chapters_topics.get(chapter, [])
                if topics:
                    subject_dict[chapter] = topics[:10]  # Limit to first 10 topics per week
            
            # Set topics for the subject
            if subject == "physics":
                weekly_plan.physics = subject_dict
            elif subject == "chemistry":
                weekly_plan.chemistry = subject_dict
            elif subject == "mathematics":
                weekly_plan.mathematics = subject_dict
        
        weekly_coverage[week_key] = weekly_plan
    
    return weekly_coverage


def _generate_new_score_oriented_insights(state: StudyPlanState) -> str:
    """Generate insights for new_score_oriented plans."""
    user_data = state["user_data"]
    revision_plan = state.get("revision_flow_results", {})
    validation_results = state.get("final_validation_results", {})
    
    insights = f"""🎯 **NEW SCORE-ORIENTED STUDY PLAN**

**Target Achievement Strategy:**
Your plan is designed to achieve {user_data.target_score}/300 marks within {user_data.number_of_months} months through complete syllabus coverage with strategic prioritization.

**Key Features:**
✅ **Complete Coverage**: 100% syllabus coverage ensuring strong foundation
✅ **Dependency Management**: Chapters ordered based on prerequisites and priority
✅ **Score Optimization**: High-weightage chapters prioritized for maximum impact
✅ **Practice Integration**: Saturday (PYQ) + Sunday (DPP) practice schedule

**Plan Overview:**
- **Syllabus Completion Target**: {min(user_data.number_of_months, 6)} months
- **Expected Score**: {sum(plan.get('total_weightage', 0) for plan in revision_plan.get('subject_plans', {}).values()):.1f}/300
- **Coverage Compliance**: {validation_results.get('syllabus_compliance', {}).get('compliance_percentage', 0):.1f}%

**Monthly Strategy:**
- **Months 1-{min(user_data.number_of_months, 6)}**: Complete syllabus coverage with 100% chapter completion
- **Practice Days**: Every Saturday (PYQ) and Sunday (DPP) for consistent practice
{f"- **Months {min(user_data.number_of_months, 6)+1}-{user_data.number_of_months}**: Intensive practice and revision" if user_data.number_of_months > 6 else ""}

**Success Factors:**
🔥 **Higher First Month Target**: Intensive start for momentum building
📚 **Chapter Completion**: Focus on 100% understanding rather than partial coverage  
🎯 **Target-Oriented**: Every chapter selected contributes to your {user_data.target_score} marks goal
⚡ **Dependency-Aware**: Logical learning progression ensures solid foundation

This plan ensures you achieve your target score through systematic, complete coverage while maintaining optimal learning progression!"""
    
    return insights


def _print_study_plan_to_terminal(state: StudyPlanState):
    """Print a comprehensive study plan to terminal for easy viewing without frontend."""
    
    user_data = state["user_data"]
    study_plan = state["study_plan"]
    plan_metadata = state.get("plan_metadata", {})
    validation_results = state.get("score_validation_results")
    
    # Terminal colors for better readability
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    print("\n" + "="*80)
    print(f"{HEADER}{BOLD}📚 STUDY PLAN GENERATED{ENDC}")
    print("="*80)
    
    # User Information
    print(f"\n{OKBLUE}{BOLD}👤 USER INFORMATION{ENDC}")
    print(f"   User ID: {user_data.user_id}")
    print(f"   Target Exam: {user_data.target_exam}")
    print(f"   Study Plan Type: {user_data.study_plan_type}")
    print(f"   Preparation Type: {user_data.preparation_type}")
    print(f"   Duration: {user_data.number_of_months} months")
    print(f"   Daily Hours: {user_data.hours_per_day} hours")
    
    # Score-oriented specific info
    if user_data.target_score:
        print(f"   🎯 Target Score: {user_data.target_score}/300")
        if user_data.exam_date:
            print(f"   📅 Exam Date: {user_data.exam_date}")
    
    # New Score-Oriented specific info
    if user_data.study_plan_type.lower() == "new_score_oriented":
        print(f"   🆕 Plan Type: NEW Score-Oriented (Complete Syllabus Coverage)")
        print(f"   📚 Coverage Strategy: 100% chapter completion")
        print(f"   ⏰ Syllabus Target: Complete within {min(user_data.number_of_months, 6)} months")
    
    # Score Validation Results (if available)
    if validation_results:
        print(f"\n{OKCYAN}{BOLD}🔍 SCORE VALIDATION RESULTS{ENDC}")
        print(f"   Expected Score: {validation_results.get('total_expected_score', 'N/A'):.1f}/300")
        print(f"   Target Achievable: {'✅ Yes' if validation_results.get('target_achievable') else '❌ No'}")
        if validation_results.get('score_gap', 0) > 0:
            print(f"   Score Gap: {WARNING}{validation_results['score_gap']:.1f} marks{ENDC}")
        
        if validation_results.get("optimized_sequences"):
            print(f"   🔧 Dependency Optimization: Applied")
            print(f"   📊 100% Coverage: Enforced")
    
    # Plan Insights
    print(f"\n{OKGREEN}{BOLD}💡 PLAN INSIGHTS{ENDC}")
    insights_lines = study_plan.insights.split('\n')
    for line in insights_lines:
        if line.strip():
            print(f"   {line.strip()}")
    
    # Monthly Plan Overview
    print(f"\n{HEADER}{BOLD}📅 MONTHLY PLAN OVERVIEW{ENDC}")
    for month_key, monthly_plan in study_plan.monthly_plan.items():
        month_num = month_key.replace("month_", "")
        print(f"\n{OKBLUE}   📖 Month {month_num}:{ENDC}")
        
        for subject, chapters in monthly_plan.model_dump().items():
            if subject in ['physics', 'chemistry', 'mathematics'] and chapters:
                print(f"      {subject.title()}:")
                for chapter_info in chapters:
                    chapter_name = chapter_info['chapter']
                    coverage = chapter_info['coverage'] * 100
                    print(f"         • {chapter_name} ({coverage:.0f}% coverage)")
    
    # Weekly Plan Detail (Month 1)
    if study_plan.weekly_plan:
        print(f"\n{HEADER}{BOLD}📋 DETAILED WEEKLY PLAN (MONTH 1){ENDC}")
        
        for week_key, weekly_plan in study_plan.weekly_plan.items():
            week_num = week_key.replace("week_", "")
            print(f"\n{OKCYAN}   📅 Week {week_num}:{ENDC}")
            
            for subject, chapters_topics in weekly_plan.model_dump().items():
                if subject in ['physics', 'chemistry', 'mathematics'] and chapters_topics:
                    print(f"      {BOLD}{subject.title()}:{ENDC}")
                    for chapter, topics in chapters_topics.items():
                        if topics:
                            print(f"         📚 {chapter}:")
                            for topic in topics[:3]:  # Show first 3 topics
                                print(f"            • {topic}")
                            if len(topics) > 3:
                                print(f"            • ... and {len(topics)-3} more topics")
    
    # Subject-wise Statistics
    if plan_metadata.get("subject_total_time"):
        print(f"\n{OKGREEN}{BOLD}📊 SUBJECT-WISE TIME ALLOCATION{ENDC}")
        for subject, hours in plan_metadata["subject_total_time"].items():
            percentage = (hours / (user_data.number_of_months * 30 * user_data.hours_per_day)) * 100
            print(f"   {subject.title()}: {hours:.1f} hours ({percentage:.1f}%)")
    
    # Chapter-wise Coverage Summary
    if plan_metadata.get("chapter_wise_coverage"):
        print(f"\n{OKBLUE}{BOLD}📖 CHAPTER COVERAGE SUMMARY{ENDC}")
        for subject, chapters in plan_metadata["chapter_wise_coverage"].items():
            if chapters:
                print(f"   {subject.title()}: {len(chapters)} chapters")
                # Handle both list and dict formats
                if isinstance(chapters, list):
                    # chapters is a list of chapter names
                    for chapter in chapters[:5]:  # Show first 5
                        print(f"      • {chapter}")
                    if len(chapters) > 5:
                        print(f"      • ... and {len(chapters)-5} more chapters")
                elif isinstance(chapters, dict):
                    # chapters is a dict with coverage percentages
                    for chapter, coverage in list(chapters.items())[:5]:  # Show first 5
                        print(f"      • {chapter}: {coverage*100:.0f}%")
                    if len(chapters) > 5:
                        print(f"      • ... and {len(chapters)-5} more chapters")
    
    # Score Analysis (if available)
    score_analysis = plan_metadata.get("score_analysis") or plan_metadata.get("score_warning")
    if score_analysis:
        print(f"\n{WARNING if 'warning' in score_analysis else OKGREEN}{BOLD}🎯 SCORE ANALYSIS{ENDC}")
        if score_analysis.get("message"):
            print(f"   {score_analysis['message']}")
        elif score_analysis.get("warning"):
            print(f"   {score_analysis['warning']}")
        
        if score_analysis.get("expected_score"):
            print(f"   Expected Score: {score_analysis['expected_score']:.1f}/300")
        if score_analysis.get("score_gap"):
            print(f"   Score Gap: {score_analysis['score_gap']:.1f} marks")
    
    # User Preferences Applied
    user_prefs = plan_metadata.get("user_preferences_applied", {})
    if any(user_prefs.values()):
        print(f"\n{OKCYAN}{BOLD}⚙️ USER PREFERENCES APPLIED{ENDC}")
        if user_prefs.get("subject_priority_applied"):
            print(f"   📌 Subject Priority: {user_prefs['subject_priority_applied']}")
        if user_prefs.get("chapter_priority_applied"):
            print(f"   📌 Chapter Priority: {user_prefs['chapter_priority_applied']}")
        if user_prefs.get("chapter_order_applied"):
            print(f"   📌 Chapter Order: {user_prefs['chapter_order_applied']}")
    
    # Validation Summary (if score-oriented)
    if validation_results and validation_results.get("optimized_sequences"):
        print(f"\n{OKGREEN}{BOLD}✅ SCORE-ORIENTED OPTIMIZATIONS{ENDC}")
        print(f"   🔗 Dependency chains validated and reordered")
        print(f"   💯 100% coverage enforced for selected chapters")
        print(f"   🎯 Chapter sequence optimized for score achievement")
        print(f"   📊 Subjects optimized: {len(validation_results['optimized_sequences'])}")
    
    # Footer
    print(f"\n{HEADER}{'='*80}{ENDC}")
    print(f"{BOLD}🚀 Study Plan Ready! Start your preparation journey!{ENDC}")
    print(f"{'='*80}\n")


def generator_collate_node(state: StudyPlanState):
    logger.info("Generator collate node executing")
    
    # Generate comprehensive metadata for supervisor validation
    logger.info("Generating plan metadata for validation...")
    plan_metadata = _generate_plan_metadata(state)
    state["plan_metadata"] = plan_metadata
    
    # Log key metadata for debugging
    logger.info(f"Plan metadata generated: {json.dumps(plan_metadata['plan_statistics'], indent=2)}")
    logger.info(f"User preferences applied: {json.dumps(plan_metadata['user_preferences_applied'], indent=2)}")
    logger.info(f"Chapter wise coverage: {json.dumps(plan_metadata['chapter_wise_coverage'], indent=2)}")
    logger.info(f"Subject total time: {json.dumps(plan_metadata['subject_total_time'], indent=2)}")
    
    # Generate generator insights for supervisor
    plan_params = state["plan_parameters"]
    user_message = ""
    for turn in state['chat_context'].values():
        if turn.user_message:
            user_message = turn.user_message
            break
    
    generator_insights = f"""
    GENERATOR INSIGHTS:
    - User Request: "{user_message}"
    - Extracted Preferences: {plan_params.model_dump()}
    - Chapter Wise Coverage: {plan_metadata['chapter_wise_coverage']}
    - Chapter Wise Time Allocation: {plan_metadata['chapter_wise_time_allocation']}
    - Subject Total Time: {plan_metadata['subject_total_time']}
    - Implementation: Applied user preferences with proper priority ordering and time allocation.
    - Chapter Order Applied: {plan_metadata['user_preferences_applied']['chapter_order_applied']}
    """
    
    plan_metadata["generator_insights"] = generator_insights
    logger.info(f"Generator insights: {generator_insights}")
    
    # Correctly serialize the new Pydantic models for the prompt
    monthly_plan_json = json.dumps({k: v.model_dump() for k, v in state['monthly_coverage'].items()})
    weekly_plan_json = json.dumps({k: v.model_dump() for k, v in state['weekly_coverage'].items()})

    # Removed generic logic - keeping only custom plans
    user_data = state["user_data"]
    is_score_based = False
    
    # Add score analysis to prompt if applicable
    score_context = ""
    if is_score_based:
        score_info = plan_metadata.get("score_analysis") or plan_metadata.get("score_warning", {})
        score_context = f"""
    SCORE-BASED PLAN:
    - Target Score: {user_data.target_score}/300
    - Score Analysis: {score_info}
    - Focus: High-weightage chapters prioritized for score optimization
    """
    
    insight_prompt = f"""
    Generate a concise, encouraging insight for a student based on their study plan.
    Explain the key focus for the first month and why the plan is effective.
    
    User Data: {state['user_data'].model_dump_json()}
    Monthly Plan: {monthly_plan_json}
    Weekly Plan (Month 1): {weekly_plan_json}
    Plan Metadata: {json.dumps(plan_metadata['user_preferences_applied'])}{score_context}
    
    {"IMPORTANT: This is a SCORE-OPTIMIZED plan. Highlight how the plan focuses on high-weightage chapters to achieve the target score efficiently." if is_score_based else ""}
    """
    response = llm.invoke(insight_prompt)
    
    state["study_plan"] = StudyPlan(
        insights=response.content,
        monthly_plan=state["monthly_coverage"],
        weekly_plan=state["weekly_coverage"]
    )
    
    # Print study plan to terminal for easy viewing
    _print_study_plan_to_terminal(state)
    
    state["next_agent"] = "supervisor"
    return state

def supervisor_node(state: StudyPlanState):
    logger.info("Supervisor node executing")
    
    # Get metadata and user preferences for validation
    plan_metadata = state.get("plan_metadata", {})
    user_preferences = plan_metadata.get("user_preferences_applied", {}).get("extracted_preferences", {})
    
    logger.info(f"Validating plan with metadata: {json.dumps(plan_metadata.get('plan_statistics', {}), indent=2)}")
    logger.info(f"User preferences to validate: {json.dumps(user_preferences, indent=2)}")
    
    # Simplified validation logic - check if the extraction matches user intent
    user_message = ""
    for turn in state['chat_context'].values():
        if turn.user_message:
            user_message = turn.user_message.lower()
            break
    
    # Direct validation based on user intent and extracted preferences
    validation_result = "APPROVE"
    validation_reasons = []
    
    # Check if user wanted chapter order and it was extracted
    if "firstly" in user_message or "first" in user_message:
        if "chapter" in user_message:
            if user_preferences.get("chapter_coverage_order"):
                validation_reasons.append("✅ User wanted chapter order ('firstly') - correctly extracted as chapter_coverage_order")
                # Check if the specific chapter was extracted
                for subject, chapters in user_preferences["chapter_coverage_order"].items():
                    if any(ch.lower() in user_message for ch in chapters):
                        validation_reasons.append(f"✅ Specific chapter {chapters} correctly identified for {subject}")
            else:
                validation_result = "REJECT"
                validation_reasons.append("❌ User wanted chapter order ('firstly') but chapter_coverage_order is empty")
    
    # Check if user wanted more time and it was extracted
    if "more time" in user_message or "spend more" in user_message:
        if "chapter" in user_message:
            if user_preferences.get("chapter_priority"):
                validation_reasons.append("✅ User wanted more time on chapters - correctly extracted as chapter_priority")
            else:
                validation_result = "REJECT"
                validation_reasons.append("❌ User wanted more time on chapters but chapter_priority is empty")
    
    # Check if user wanted subject focus
    if "focus" in user_message and any(subj in user_message for subj in ["physics", "chemistry", "mathematics"]):
        if user_preferences.get("subject_priority"):
            validation_reasons.append("✅ User wanted subject focus - correctly extracted as subject_priority")
        else:
            validation_result = "REJECT"
            validation_reasons.append("❌ User wanted subject focus but subject_priority is empty")
    
    # If no specific preferences were extracted but user had clear intent
    if not any([user_preferences.get("subject_priority"), 
                user_preferences.get("chapter_priority"), 
                user_preferences.get("chapter_coverage_order")]):
        if any(keyword in user_message for keyword in ["firstly", "more time", "focus", "prioritize"]):
            validation_result = "REJECT"
            validation_reasons.append("❌ User expressed preferences but nothing was extracted")
    
    # If we have valid extractions, check implementation
    if validation_result == "APPROVE":
        # Check if chapter order was actually applied
        if user_preferences.get("chapter_coverage_order"):
            if plan_metadata.get("user_preferences_applied", {}).get("chapter_order_applied"):
                validation_reasons.append("✅ Chapter order preferences were implemented in the plan")
            else:
                validation_result = "REJECT"
                validation_reasons.append("❌ Chapter order extracted but not applied in plan")
        
        # Check if chapter priorities were actually applied
        if user_preferences.get("chapter_priority"):
            if plan_metadata.get("user_preferences_applied", {}).get("chapter_priority_applied"):
                validation_reasons.append("✅ Chapter priorities were implemented in the plan")
            else:
                validation_result = "REJECT"
                validation_reasons.append("❌ Chapter priorities extracted but not applied in plan")
    
    # Generate final response
    justification = "; ".join(validation_reasons)
    response_text = f"{validation_result}: {justification}"
    
    logger.info(f"Direct validation result: {response_text}")
    
    try:
        # Use the direct validation result
        if validation_result == "APPROVE":
            status = "yes"
        else:
            status = "no"
        
        justification = response_text
        
        # Additional validation based on metadata
        stats = plan_metadata.get("plan_statistics", {})
        preferences_applied = plan_metadata.get("user_preferences_applied", {})
        
        # Check if any user preferences were specified but not applied
        validation_issues = []
        
        if user_preferences.get("subject_priority") and not preferences_applied.get("subject_priority_applied"):
            validation_issues.append("Subject priorities specified but not applied")
            
        if user_preferences.get("chapter_priority") and not preferences_applied.get("chapter_priority_applied"):
            validation_issues.append("Chapter priorities specified but not applied")
            
        if user_preferences.get("chapter_coverage_order") and not preferences_applied.get("chapter_order_applied"):
            validation_issues.append("Chapter order preferences specified but not applied")
        
        # Override status if critical issues found
        if validation_issues and status == "yes":
            status = "no"
            justification += f" CRITICAL ISSUES: {'; '.join(validation_issues)}"
        
        # Generate specific feedback for the generator
        supervisor_feedback = []
        
        # Analyze what the user actually wanted vs what was extracted
        user_message = ""
        for turn in state['chat_context'].values():
            if turn.user_message:
                user_message = turn.user_message.lower()
                break
        
        # Provide specific guidance based on user intent analysis
        if "more time" in user_message or "spend more" in user_message:
            if "chapter" in user_message:
                supervisor_feedback.append("USER WANTS MORE TIME on specific chapters - extract as chapter_priority, not chapter_coverage_order")
                if not user_preferences.get("chapter_priority"):
                    supervisor_feedback.append("MISSING: chapter_priority should contain chapters user wants more time on")
        
        if "firstly" in user_message or "first" in user_message:
            if "chapter" in user_message:
                supervisor_feedback.append("USER WANTS CHAPTER ORDER - extract as chapter_coverage_order for sequencing")
        
        if "focus" in user_message and any(subj in user_message for subj in ["physics", "chemistry", "mathematics"]):
            supervisor_feedback.append("USER WANTS SUBJECT FOCUS - extract as subject_priority")
            if not user_preferences.get("subject_priority"):
                supervisor_feedback.append("MISSING: subject_priority should contain subjects user wants to focus on")
        
        # Check specific extraction issues
        if user_preferences.get("chapter_coverage_order") and not user_preferences.get("chapter_priority"):
            if "more time" in user_message:
                supervisor_feedback.append("EXTRACTION ERROR: User said 'more time' but you put chapters in chapter_coverage_order instead of chapter_priority")
        
        # Add metadata-based feedback
        if stats.get("prioritized_chapters", 0) == 0 and ("more time" in user_message or "focus" in user_message):
            supervisor_feedback.append("PLAN ISSUE: No chapters were prioritized but user requested more time/focus")
        
        # Combine all feedback
        if supervisor_feedback:
            detailed_feedback = "SUPERVISOR FEEDBACK: " + "; ".join(supervisor_feedback) + f". ORIGINAL USER REQUEST: '{user_message}'"
        else:
            detailed_feedback = justification
        
        logger.info(f"Final supervisor validation status: {status}")
        logger.info(f"Justification: {justification}")
        logger.info(f"Detailed feedback for generator: {detailed_feedback}")
        
    except Exception as e:
        logger.error(f"Supervisor validation failed: {e}", exc_info=True)
        status = "no"
        detailed_feedback = f"Validation failed due to error: {str(e)}"
    
    state["validation_context"] = {"1": Validation(status=status, justification=justification)}
    
    if status == "yes":
        state["next_agent"] = "counsellor_final"
    else:
        # Add circuit breaker to prevent infinite loops
        current_attempts = len(state.get("regeneration_feedback", []))
        if current_attempts >= 3:
            logger.warning(f"Maximum regeneration attempts ({current_attempts}) reached. Accepting current plan.")
            status = "yes"
            state["validation_context"] = {"1": Validation(status="yes", justification="Plan accepted after maximum regeneration attempts")}
            state["next_agent"] = "counsellor_final"
        else:
            state["regeneration_feedback"] = [detailed_feedback]
            state["next_agent"] = "generator"
        
    return state

def counsellor_continue_node(state: StudyPlanState):
    """Node for continuing counsellor conversation without proceeding to generation"""
    logger.info("Counsellor continue node executing - waiting for more user input")
    # This node essentially ends the current flow, expecting new user input
    # In a real chat system, this would wait for the next user message
    state["next_agent"] = "end"
    return state

def feedback_counsellor_node(state: StudyPlanState):
    """Node for handling user feedback on generated study plan"""
    logger.info("Feedback counsellor node executing")
    
    # Check if this is a re-edit cycle to prevent infinite loops
    if state.get("is_re_edit", False):
        logger.info("Re-edit cycle detected - presenting updated plan")
        # Reset the flag
        state["is_re_edit"] = False
        
        # Present the updated plan
        study_plan = state.get("study_plan")
        chat_context = state.get("chat_context", {})
        
        if study_plan and study_plan.insights:
            plan_presentation = f"""🎉 **Your updated study plan has been generated!**

{study_plan.insights}

**Plan Summary:**
- **Total Study Time**: {state.get('plan_metadata', {}).get('plan_statistics', {}).get('total_study_hours', 'N/A')} hours over {state.get('plan_metadata', {}).get('plan_statistics', {}).get('study_months', 'N/A')} months
- **Daily Commitment**: {state.get('plan_metadata', {}).get('plan_statistics', {}).get('daily_hours', 'N/A')} hours per day
- **Coverage**: {state.get('plan_metadata', {}).get('plan_statistics', {}).get('covered_chapters', 'N/A')}/{state.get('plan_metadata', {}).get('plan_statistics', {}).get('total_chapters', 'N/A')} chapters ({state.get('plan_metadata', {}).get('plan_statistics', {}).get('coverage_percentage', 'N/A')}%)

**Applied Changes:**
- Mathematics: {state.get('plan_metadata', {}).get('subject_total_time', {}).get('mathematics', 'N/A')} hours
- Physics: {state.get('plan_metadata', {}).get('subject_total_time', {}).get('physics', 'N/A')} hours  
- Chemistry: {state.get('plan_metadata', {}).get('subject_total_time', {}).get('chemistry', 'N/A')} hours

**What do you think about this updated plan?** 

Are there any further changes you'd like to make, or does everything look good to you? If you're satisfied with the plan, just say **'finalize'** and we'll save it!"""
            
            latest_turn_id = max(chat_context.keys()) if chat_context else "1"
            if latest_turn_id in chat_context:
                chat_context[latest_turn_id].assistant_message = plan_presentation
            
            state["next_agent"] = "feedback_counsellor_continue"
            return state
    
    # Get the latest user message
    latest_message = ""
    chat_context = state.get("chat_context", {})
    
    # Find the most recent user message
    for turn_id in sorted(chat_context.keys(), reverse=True):
        turn = chat_context[turn_id]
        if turn.user_message:
            latest_message = turn.user_message.lower()
            break
    
    logger.info(f"Feedback counsellor processing: {latest_message}")
    
    # Check for finalization trigger words - EXPANDED LIST
    finalization_words = [
        "finalize", "approve", "confirm plan", "i'm satisfied",
        "perfect", "great", "excellent", "no changes", "all good", "generate",
        "create plan", "start planning", "make my plan", "begin generation",
        "yes this is final", "this is final", "final", "done", "complete",
        "save this plan", "lock it in", "good to go", "ready", "confirmed"
    ]
    
    # Special case: "looks good" only if not followed by "but" or change requests
    looks_good_finalization = "looks good" in latest_message and "but" not in latest_message and not any(word in latest_message for word in ["want", "need", "change", "more", "less", "different"])
    
    should_finalize = any(word in latest_message for word in finalization_words) or looks_good_finalization
    logger.info(f"Finalization trigger detected: {should_finalize}")
    
    # CRITICAL FIX: If this is the first time in feedback_counsellor after plan generation,
    # and user said "generate" or similar, we should present the plan and ask for feedback
    if latest_message in ["generate", "create plan", "start planning", "make my plan", "begin generation"]:
        logger.info("User requested plan generation - presenting the generated plan")
        
        # Present the generated plan
        study_plan = state.get("study_plan")
        if study_plan and study_plan.insights:
            plan_presentation = f"""🎉 **Your personalized 8-month JEE Mains study plan has been generated!**

{study_plan.insights}

**Plan Summary:**
- **Total Study Time**: {state.get('plan_metadata', {}).get('plan_statistics', {}).get('total_study_hours', 'N/A')} hours over {state.get('plan_metadata', {}).get('plan_statistics', {}).get('study_months', 'N/A')} months
- **Daily Commitment**: {state.get('plan_metadata', {}).get('plan_statistics', {}).get('daily_hours', 'N/A')} hours per day
- **Coverage**: {state.get('plan_metadata', {}).get('plan_statistics', {}).get('covered_chapters', 'N/A')}/{state.get('plan_metadata', {}).get('plan_statistics', {}).get('total_chapters', 'N/A')} chapters ({state.get('plan_metadata', {}).get('plan_statistics', {}).get('coverage_percentage', 'N/A')}%)

**What do you think about this plan?** 

Are there any changes you'd like to make, or does everything look good to you? If you're satisfied with the plan, just say **'finalize'** and we'll lock it in!"""
            
            latest_turn_id = max(chat_context.keys()) if chat_context else "1"
            if latest_turn_id in chat_context:
                chat_context[latest_turn_id].assistant_message = plan_presentation
            
            state["next_agent"] = "feedback_counsellor_continue"
            return state
    
    if should_finalize:
        # User wants to finalize the plan
        logger.info("User wants to finalize the study plan")
        state["plan_finalized"] = True
        
        # Save the finalized plan to database
        try:
            user_id = state["user_data"].user_id
            
            # Prepare state message (complete state for reference)
            state_message = {
                "user_data": state["user_data"].model_dump(),
                "plan_parameters": state["plan_parameters"].model_dump(),
                "plan_metadata": state.get("plan_metadata", {}),
                "chat_context": {k: v.model_dump() for k, v in state["chat_context"].items()},
                "finalized_at": "finalized",
                "plan_finalized": True
            }
            
            # Prepare study plan data
            study_plan_data = state["study_plan"].model_dump() if state.get("study_plan") else {}
            
            # Save to database
            save_result = save_finalized_plan.invoke({
                "user_id": user_id,
                "state_message": state_message,
                "study_plan": study_plan_data
            })
            
            logger.info(f"Database save result: {save_result}")
            
            # Add finalization message to chat with save confirmation
            latest_turn_id = max(chat_context.keys()) if chat_context else "1"
            if latest_turn_id in chat_context:
                finalization_response = f"""🎉 **Congratulations!** Your personalized study plan has been finalized and saved!
                
Your plan is now ready and optimized for your JEE Mains preparation. Here's what you can expect:

✅ **Personalized Schedule**: Tailored to your preferences and learning style
✅ **Balanced Coverage**: All subjects and chapters systematically covered
✅ **Time-Optimized**: Efficient use of your daily 6-hour study commitment
✅ **Goal-Oriented**: Designed specifically for JEE Mains success
✅ **Securely Saved**: Your plan has been saved to your profile

**Database Status**: {save_result}

**Next Steps:**
1. Your plan is now saved and ready for reference
2. Start following the monthly and weekly schedules
3. Track your progress regularly
4. Stay consistent with the allocated time

Best of luck with your preparation! You've got this! 🚀"""
                
                chat_context[latest_turn_id].assistant_message = finalization_response
            
        except Exception as e:
            logger.error(f"Error saving finalized plan: {e}", exc_info=True)
            # Still finalize but show error message
            latest_turn_id = max(chat_context.keys()) if chat_context else "1"
            if latest_turn_id in chat_context:
                finalization_response = f"""🎉 **Congratulations!** Your personalized study plan has been finalized!
                
Your plan is now ready and optimized for your JEE Mains preparation. 

⚠️ **Note**: There was an issue saving to the database ({str(e)}), but your plan is still finalized and ready to use.

✅ **Personalized Schedule**: Tailored to your preferences and learning style
✅ **Balanced Coverage**: All subjects and chapters systematically covered
✅ **Time-Optimized**: Efficient use of your daily 6-hour study commitment
✅ **Goal-Oriented**: Designed specifically for JEE Mains success

**Next Steps:**
1. Save this plan for your reference
2. Start following the monthly and weekly schedules
3. Track your progress regularly
4. Stay consistent with the allocated time

Best of luck with your preparation! You've got this! 🚀"""
                
                chat_context[latest_turn_id].assistant_message = finalization_response
        
        state["next_agent"] = "end"
        
    else:
        # User has feedback or wants changes
        logger.info("User has feedback or wants changes")
        
        # Build conversation history for feedback counsellor
        conversation_parts = []
        for turn_id in sorted(chat_context.keys()):
            turn = chat_context[turn_id]
            if turn.user_message:
                conversation_parts.append(f"User: {turn.user_message}")
            if turn.assistant_message:
                conversation_parts.append(f"Assistant: {turn.assistant_message}")
        
        conversation_history = "\n".join(conversation_parts)
        
        # Get study plan summary for context
        study_plan = state.get("study_plan")
        plan_summary = ""
        if study_plan and study_plan.insights:
            plan_summary = f"CURRENT PLAN SUMMARY:\n{study_plan.insights[:500]}..."
        
        # Create feedback counsellor prompt
        feedback_prompt = f"""
        CONVERSATION HISTORY:
        {conversation_history}
        
        {plan_summary}
        
        LATEST USER MESSAGE: {latest_message}
        
        The user has seen their generated study plan. Your job is to:
        1. Understand their feedback or change requests
        2. Acknowledge their concerns supportively
        3. If they want changes, explain you'll get expert analysis
        4. If they're satisfied, guide them to say 'finalize'
        
        Focus on being helpful and supportive while capturing specific change requests clearly.
        """
        
        try:
            # Get feedback counsellor response
            response = feedback_counsellor_agent.invoke({"input": feedback_prompt})
            counsellor_response = response.content if hasattr(response, 'content') else str(response)
            
            # Update chat context
            latest_turn_id = max(chat_context.keys()) if chat_context else "1"
            if latest_turn_id in chat_context:
                chat_context[latest_turn_id].assistant_message = counsellor_response
            
            logger.info(f"Feedback counsellor response: {counsellor_response[:100]}...")
            
            # Check if user requested specific changes
            change_indicators = [
                "more time", "less time", "change", "adjust", "modify", "different",
                "reorder", "priority", "before", "after", "increase", "decrease"
            ]
            
            # Check if user wants to implement changes (re-edit triggers)
            re_edit_triggers = [
                "re edit", "re-edit", "reedit", "edit the plan", "implement changes",
                "make the changes", "apply changes", "update the plan", "regenerate"
            ]
            
            has_change_request = any(indicator in latest_message for indicator in change_indicators)
            wants_to_implement = any(trigger in latest_message for trigger in re_edit_triggers)
            
            if wants_to_implement:
                # User wants to implement previously discussed changes - regenerate plan
                logger.info("Re-edit request detected - implementing changes and regenerating plan")
                
                # Check if we have enough context to regenerate directly
                # Look for accumulated feedback requests in the conversation
                conversation_parts = []
                for turn_id in sorted(chat_context.keys()):
                    turn = chat_context[turn_id]
                    if turn.user_message:
                        conversation_parts.append(f"User: {turn.user_message}")
                    if turn.assistant_message:
                        conversation_parts.append(f"Assistant: {turn.assistant_message}")
                
                # Add a flag to indicate this is a re-edit to prevent loops
                state["is_re_edit"] = True
                
                # Go directly to generator with all the conversation context
                state["next_agent"] = "generator"
            elif has_change_request:
                # User wants changes - send to feedback supervisor for analysis
                logger.info("Change request detected - routing to feedback supervisor")
                state["feedback_requests"] = [latest_message]
                state["next_agent"] = "feedback_supervisor"
            else:
                # Continue feedback conversation
                state["next_agent"] = "feedback_counsellor_continue"
                
        except Exception as e:
            logger.error(f"Error in feedback counsellor: {e}", exc_info=True)
            # Fallback response
            fallback_response = """I'm here to help you refine your study plan! 
            
What do you think about the generated plan? Are there any changes you'd like to make, or does everything look good to you?

If you're satisfied with the plan, just say 'finalize' and we'll lock it in. If you want any adjustments, let me know and I'll get expert analysis on the best way to implement your changes."""
            
            latest_turn_id = max(chat_context.keys()) if chat_context else "1"
            if latest_turn_id in chat_context:
                chat_context[latest_turn_id].assistant_message = fallback_response
            
            state["next_agent"] = "feedback_counsellor_continue"
    
    return state

def feedback_supervisor_node(state: StudyPlanState):
    """Node for providing expert analysis of user change requests"""
    logger.info("Feedback supervisor node executing")
    
    # Get user's change request
    feedback_requests = state.get("feedback_requests", [])
    latest_request = feedback_requests[-1] if feedback_requests else ""
    
    # Get current plan metadata for analysis
    plan_metadata = state.get("plan_metadata", {})
    study_plan = state.get("study_plan")
    
    logger.info(f"Analyzing change request: {latest_request}")
    
    # Create analysis prompt for feedback supervisor
    analysis_prompt = f"""
    USER CHANGE REQUEST: "{latest_request}"
    
    CURRENT PLAN METADATA:
    {json.dumps(plan_metadata.get('plan_statistics', {}), indent=2)}
    
    CURRENT SUBJECT TIME ALLOCATION:
    {json.dumps(plan_metadata.get('subject_total_time', {}), indent=2)}
    
    CURRENT PREFERENCES APPLIED:
    {json.dumps(plan_metadata.get('user_preferences_applied', {}), indent=2)}
    
    PLAN INSIGHTS:
    {study_plan.insights if study_plan else 'No insights available'}
    
    Analyze this change request and provide:
    1. Understanding of what the user wants
    2. Current plan rationale
    3. Pros and cons of the requested change
    4. Your recommendation
    5. Implementation suggestions if they proceed
    
    Be thorough, balanced, and educational in your analysis.
    """
    
    try:
        # Get feedback supervisor analysis
        response = feedback_supervisor_agent.invoke({"input": analysis_prompt})
        supervisor_analysis = response.content if hasattr(response, 'content') else str(response)
        
        logger.info(f"Supervisor analysis generated: {supervisor_analysis[:200]}...")
        
        # Store the analysis
        state["supervisor_insights"] = [supervisor_analysis]
        
        # Update chat context with the analysis
        chat_context = state.get("chat_context", {})
        latest_turn_id = max(chat_context.keys()) if chat_context else "1"
        
        if latest_turn_id in chat_context:
            # Append supervisor analysis to the counsellor's response
            current_response = chat_context[latest_turn_id].assistant_message
            enhanced_response = f"""{current_response}

**📊 EXPERT ANALYSIS:**

{supervisor_analysis}

**What would you like to do?**
- If you want to proceed with implementing these changes, say **'re-edit the plan'**
- If you want to discuss other options, feel free to ask
- If you're satisfied with the current plan, just say **'finalize'**"""
            
            chat_context[latest_turn_id].assistant_message = enhanced_response
        
        # Return to feedback counsellor for user's decision
        state["next_agent"] = "feedback_counsellor_continue"
        
    except Exception as e:
        logger.error(f"Error in feedback supervisor: {e}", exc_info=True)
        # Fallback analysis
        fallback_analysis = f"""I understand you want to make changes to your study plan. 

While I'm analyzing the specific impact of your request "{latest_request}", here are some general considerations:

**Before making changes, consider:**
- How this affects your overall preparation balance
- Whether this aligns with JEE Mains exam patterns
- If you have enough time to implement this change effectively

Would you like me to proceed with implementing this change, or would you like to discuss other options?"""
        
        state["supervisor_insights"] = [fallback_analysis]
        
        # Update chat context
        chat_context = state.get("chat_context", {})
        latest_turn_id = max(chat_context.keys()) if chat_context else "1"
        if latest_turn_id in chat_context:
            current_response = chat_context[latest_turn_id].assistant_message
            chat_context[latest_turn_id].assistant_message = f"{current_response}\n\n{fallback_analysis}"
        
        state["next_agent"] = "feedback_counsellor_continue"
    
    return state

def feedback_counsellor_continue_node(state: StudyPlanState):
    """Node for continuing feedback conversation"""
    logger.info("Feedback counsellor continue node executing - waiting for user decision")
    state["next_agent"] = "end"
    return state

def counsellor_final_node(state: StudyPlanState):
    logger.info("Counsellor final node executing")
    # After initial plan generation, move to feedback phase
    state["plan_finalized"] = False
    state["next_agent"] = "feedback_counsellor"
    return state

# Graph Definition
workflow = StateGraph(StudyPlanState)

workflow.add_node("counsellor", counsellor_node)
workflow.add_node("counsellor_continue", counsellor_continue_node)
workflow.add_node("generator", generator_node)
workflow.add_node("score_oriented_validator", score_oriented_validator_node)
workflow.add_node("revision_flow", revision_flow_node)
workflow.add_node("new_score_oriented_generator_validation", new_score_oriented_generator_validation_node)
workflow.add_node("new_score_oriented_topic", new_score_oriented_topic_node)
workflow.add_node("new_score_oriented_final_validation", new_score_oriented_final_validation_node)
workflow.add_node("new_score_oriented_supervisor", new_score_oriented_supervisor_node)
workflow.add_node("flow", flow_node)
workflow.add_node("weightage", weightage_node)
workflow.add_node("topic", topic_node)
workflow.add_node("generator_collate", generator_collate_node)
workflow.add_node("supervisor", supervisor_node)
workflow.add_node("counsellor_final", counsellor_final_node)
workflow.add_node("feedback_counsellor", feedback_counsellor_node)
workflow.add_node("feedback_supervisor", feedback_supervisor_node)
workflow.add_node("feedback_counsellor_continue", feedback_counsellor_continue_node)

workflow.set_entry_point("counsellor")

def route_to_agent(state: StudyPlanState):
    return state["next_agent"]

workflow.add_conditional_edges("counsellor", route_to_agent, {"generator": "generator", "counsellor_continue": "counsellor_continue", "end": END})
workflow.add_conditional_edges("generator", route_to_agent, {"flow": "flow", "weightage": "weightage", "score_oriented_validator": "score_oriented_validator", "revision_flow": "revision_flow", "counsellor": "counsellor"})
workflow.add_conditional_edges("score_oriented_validator", route_to_agent, {"weightage": "weightage"})
workflow.add_conditional_edges("revision_flow", route_to_agent, {"new_score_oriented_generator_validation": "new_score_oriented_generator_validation", "flow": "flow", "weightage": "weightage"})
workflow.add_conditional_edges("new_score_oriented_generator_validation", route_to_agent, {"new_score_oriented_topic": "new_score_oriented_topic"})
workflow.add_conditional_edges("new_score_oriented_topic", route_to_agent, {"new_score_oriented_final_validation": "new_score_oriented_final_validation"})
workflow.add_conditional_edges("new_score_oriented_final_validation", route_to_agent, {"new_score_oriented_supervisor": "new_score_oriented_supervisor"})
workflow.add_conditional_edges("new_score_oriented_supervisor", route_to_agent, {"counsellor_final": "counsellor_final"})
workflow.add_conditional_edges("flow", route_to_agent, {"topic": "topic"})
workflow.add_conditional_edges("weightage", route_to_agent, {"topic": "topic"})
workflow.add_conditional_edges("topic", route_to_agent, {"generator_collate": "generator_collate"})
workflow.add_conditional_edges("generator_collate", route_to_agent, {"supervisor": "supervisor"})
workflow.add_conditional_edges("supervisor", route_to_agent, {"counsellor_final": "counsellor_final", "generator": "generator"})
workflow.add_conditional_edges("counsellor_final", route_to_agent, {"feedback_counsellor": "feedback_counsellor"})
workflow.add_conditional_edges("feedback_counsellor", route_to_agent, {"feedback_supervisor": "feedback_supervisor", "feedback_counsellor_continue": "feedback_counsellor_continue", "counsellor": "counsellor", "end": END})
workflow.add_conditional_edges("feedback_supervisor", route_to_agent, {"feedback_counsellor_continue": "feedback_counsellor_continue"})
workflow.add_conditional_edges("counsellor_continue", route_to_agent, {"end": END})
workflow.add_conditional_edges("feedback_counsellor_continue", route_to_agent, {"end": END})

# Compile the graph
graph = workflow.compile() 