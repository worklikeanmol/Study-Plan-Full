from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any, Union
from datetime import date

class NewScoreOrientedUserData(BaseModel):
    """User data specifically for New Score-Oriented plans"""
    user_id: str
    target_exam: str
    study_plan_type: str = "new_score_oriented"
    preparation_type: str = "revision"  # Always revision for new_score_oriented
    syllabus_coverage: str = "complete"  # Always complete syllabus coverage
    target_score: int = Field(..., ge=1, le=300)
    exam_date: str  # YYYY-MM-DD format (minimum 6 months)
    number_of_months: int  # Auto-calculated from exam date

class ChapterWithDependencies(BaseModel):
    """Chapter information with dependency and priority data"""
    exam: str
    subject: str
    chapter: str
    average_weightage: float
    chapter_category: str
    dependencies: Optional[str] = None
    priority_score: float  # Calculated priority for revision flow
    completion_order: int  # Order in which chapter should be completed

class TopicWithPriority(BaseModel):
    """Topic information with priority data"""
    exam: str
    subject: str
    chapter: str
    topic: str
    topic_priority: str  # High, Medium, Low
    completion_required: bool = True  # Always True for new_score_oriented

class RevisionFlowPlan(BaseModel):
    """Complete revision flow plan with dependencies"""
    subject: str
    chapters: List[ChapterWithDependencies]
    total_chapters: int
    total_weightage: float
    dependency_chains: Dict[str, List[str]]  # Chapter -> [dependencies]
    completion_sequence: List[str]  # Ordered list of chapters

class MonthlyRevisionTarget(BaseModel):
    """Monthly revision target with complete coverage focus"""
    month_number: int
    target_type: str  # "syllabus_completion" or "intensive_practice"
    chapters_to_complete: List[ChapterWithDependencies]
    topics_breakdown: Dict[str, List[TopicWithPriority]]  # Chapter -> [topics]
    expected_score_contribution: float
    practice_focus: bool = False  # True for months > 6

class WeeklyRevisionBreakdown(BaseModel):
    """Weekly breakdown for revision flow"""
    week_number: int  # 1-4 within the month
    study_days: List[str] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    practice_days: List[str] = ["Saturday", "Sunday"]  # PYQ and DPP
    chapters_this_week: Dict[str, List[ChapterWithDependencies]]  # Subject -> [chapters]
    topics_this_week: Dict[str, Dict[str, List[TopicWithPriority]]]  # Subject -> Chapter -> [topics]
    completion_targets: Dict[str, float]  # Chapter -> completion percentage (always 100%)

class MonthlyRevisionPlan(BaseModel):
    """Complete monthly plan for new_score_oriented"""
    month_number: int
    month_name: str  # e.g., "January 2025"
    revision_target: MonthlyRevisionTarget
    weekly_breakdown: List[WeeklyRevisionBreakdown]
    practice_schedule: Dict[str, str]  # Day -> "PYQ" or "DPP"
    syllabus_completion_percentage: float  # Overall syllabus completion by this month

class EnhancedMonthlyTarget(BaseModel):
    """Enhanced monthly target with score calculations"""
    month_number: int
    month_name: str
    total_achievable_score: float
    user_target_score: float
    target_ratio: float
    efficiency_required: float
    subject_breakdown: Dict[str, Dict[str, Any]]

class WeeklyTopicBreakdown(BaseModel):
    """Weekly topic breakdown for a month"""
    week_number: int
    focus_area: str
    subjects_covered: List[str]
    topic_distribution: Dict[str, List[str]]  # Subject -> [topics]
    priority_focus: str  # High, Medium, Low

class ExtendedMonthPlan(BaseModel):
    """Extended month plan for PYQ/DPP focus"""
    month_number: int
    month_name: str
    tag: str  # "PYQ & DPP Focus"
    focus_type: str
    intensity_level: str
    practice_distribution: Dict[str, int]
    weekly_schedule: Dict[str, Dict[str, str]]
    daily_targets: Dict[str, int]
    subject_wise_practice: Dict[str, Dict[str, int]]

class WeekendSchedule(BaseModel):
    """Weekend schedule for PYQ practice"""
    month_number: int
    month_name: str
    schedule_type: str
    saturday: Dict[str, Any]
    sunday: Dict[str, Any]
    weekly_integration: Dict[str, str]

class EnhancedFeatures(BaseModel):
    """Enhanced features for new_score_oriented plans"""
    monthly_target_scores: Dict[str, Any]
    extended_months_plan: Dict[str, Any]
    weekly_topic_breakdown: Dict[str, Any]
    weekend_schedule: Dict[str, Any]
    strategy_summary: Dict[str, Any]

class NewScoreOrientedStudyPlan(BaseModel):
    """Complete New Score-Oriented study plan with enhanced features"""
    user_id: str
    target_score: int
    exam_date: str
    total_months: int
    syllabus_completion_months: int  # Target to complete syllabus (max 6)
    practice_months: int  # Remaining months for intensive practice
    monthly_plans: List[MonthlyRevisionPlan]
    revision_flow_results: Dict[str, RevisionFlowPlan]  # Subject -> RevisionFlowPlan
    overall_strategy: str
    dependency_analysis: Dict[str, Any]
    coverage_validation: Dict[str, Any]
    target_achievement_probability: float
    enhanced_features: Optional[EnhancedFeatures] = None  # New enhanced features

class ValidationResult(BaseModel):
    """Validation result for new_score_oriented plans"""
    status: str  # "success" or "failure"
    all_chapters_covered: bool
    all_topics_included: bool
    dependencies_satisfied: bool
    target_achievable: bool
    missing_elements: Dict[str, List[str]]  # Subject -> [missing items]
    recommendations: List[str]

class SupervisorFeedback(BaseModel):
    """Supervisor feedback for plan adjustments"""
    plan_approved: bool
    target_achievement_analysis: Dict[str, Any]
    required_adjustments: List[Dict[str, str]]
    final_recommendations: List[str]
    force_fit_applied: bool  # True if plan was adjusted to meet target