from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from app.core.models import PlanParameters, StudyPlan, MonthlySubjectPlan, WeeklySubjectPlan, ChatMessage, Validation

# Regeneration-specific models
class UserPerformanceData(BaseModel):
    """Model for user performance data from User_Performance table"""
    user_id: str
    completed_topics: Dict[str, Dict[str, List[str]]] = Field(default_factory=dict)  # subject -> chapter -> topics
    not_completed_topics: Dict[str, Dict[str, List[str]]] = Field(default_factory=dict)  # subject -> chapter -> topics
    overall_progress_percentage: float = 0.0
    subject_wise_progress: Dict[str, float] = Field(default_factory=dict)
    performance_metrics: Dict[str, Any] = Field(default_factory=dict)
    last_updated: Optional[str] = None
    created_at: Optional[str] = None

class PreviousStudyPlan(BaseModel):
    """Model for previous study plan data"""
    insights: str = ""
    monthly_plan: Dict[str, Any] = Field(default_factory=dict)
    weekly_plan: Dict[str, Any] = Field(default_factory=dict)
    plan_metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: Optional[str] = None

class RegenerationPreferences(BaseModel):
    """Model for regeneration-specific preferences"""
    regeneration_type: str = Field(default="extend_plan", description="extend_plan, create_new, or hybrid")
    time_adjustments: Dict[str, Any] = Field(default_factory=dict)
    priority_changes: Dict[str, List[str]] = Field(default_factory=dict)
    include_pending_topics: bool = True
    focus_on_weak_areas: bool = True
    maintain_strong_areas: bool = True
    new_months: Optional[int] = None
    new_hours_per_day: Optional[int] = None

class TopicImportanceAnalysis(BaseModel):
    """Model for topic importance analysis"""
    topic: str
    importance_score: int = Field(ge=1, le=10)
    importance_level: str = Field(description="Critical, Important, or Moderate")
    exam_weightage: str = Field(description="High, Medium, or Low")
    dependency_impact: str
    recommendation: str

class RegenerationInsights(BaseModel):
    """Model for regeneration insights and analysis"""
    progress_analysis: str
    topic_importance_summary: Dict[str, Any] = Field(default_factory=dict)
    recommendations: List[str] = Field(default_factory=list)
    critical_topics: List[str] = Field(default_factory=list)
    suggested_approach: str = ""

# Extended state for regeneration workflow
class RegenerationState(BaseModel):
    """Extended state for regeneration workflow"""
    # Original user data
    user_id: str
    is_existing_user: bool = False
    
    # Previous plan and performance data
    previous_plan: Optional[PreviousStudyPlan] = None
    performance_data: Optional[UserPerformanceData] = None
    
    # Current regeneration context
    regeneration_preferences: RegenerationPreferences = Field(default_factory=RegenerationPreferences)
    regeneration_insights: Optional[RegenerationInsights] = None
    
    # Chat and conversation context
    chat_context: Dict[str, ChatMessage] = Field(default_factory=dict)
    
    # Plan generation context (reused from normal flow)
    plan_parameters: PlanParameters = Field(default_factory=PlanParameters)
    monthly_coverage: Dict[str, MonthlySubjectPlan] = Field(default_factory=dict)
    weekly_coverage: Dict[str, WeeklySubjectPlan] = Field(default_factory=dict)
    validation_context: Dict[str, Validation] = Field(default_factory=dict)
    study_plan: Optional[StudyPlan] = None
    plan_metadata: Dict[str, Any] = Field(default_factory=dict)
    
    # Regeneration-specific feedback and control
    regen_feedback: List[str] = Field(default_factory=list)
    regen_supervisor_insights: List[str] = Field(default_factory=list)
    plan_finalized: bool = False
    is_re_edit: bool = False
    next_agent: str = "regen_counsellor"

class RegenerationUserData(BaseModel):
    """Extended user data model for regeneration"""
    user_id: str
    target_exam: str
    study_plan_type: str
    preparation_type: str
    syllabus: Dict[str, List[str]]
    number_of_months: int
    hours_per_day: int
    target_score: Optional[int] = None  # For generic study plans
    
    # Regeneration-specific fields
    remaining_months: Optional[int] = None
    completed_chapters: Dict[str, List[str]] = Field(default_factory=dict)
    pending_chapters: Dict[str, List[str]] = Field(default_factory=dict)
    weak_subjects: List[str] = Field(default_factory=list)
    strong_subjects: List[str] = Field(default_factory=list)
    current_score: Optional[float] = None  # Score achieved so far
    updated_target_score: Optional[int] = None  # Updated target for regeneration