from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import date

class ScoreOrientedUserData(BaseModel):
    """User data specifically for Score-Oriented plans"""
    user_id: str
    target_exam: str
    study_plan_type: str = "Score-Oriented"
    preparation_type: str = "revision"  # Always revision for score-oriented
    target_score: int = Field(..., ge=1, le=300)
    exam_date: str  # YYYY-MM-DD format
    number_of_months: int  # Auto-calculated from exam date
    # No hours_per_day or syllabus selection for score-oriented

class MonthlyScoreTarget(BaseModel):
    """Monthly score target and breakdown"""
    month_number: int
    target_score_for_month: float  # e.g., 33.35 marks to achieve this month
    cumulative_target: float  # Total score to achieve by end of this month
    chapters_to_cover: List[str]  # Chapters planned for this month
    estimated_score_from_chapters: float  # Expected score from these chapters

class WeeklyBreakdown(BaseModel):
    """Weekly breakdown within a month"""
    week_number: int  # 1-4 within the month
    study_days: List[str]  # ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    practice_days: List[str] = ["Saturday", "Sunday"]  # Default practice days
    chapters_this_week: Dict[str, List[str]]  # Subject -> [chapters]
    topics_this_week: Dict[str, Dict[str, List[str]]]  # Subject -> Chapter -> [topics]

class MonthlyPlan(BaseModel):
    """Complete monthly plan with score targets and weekly breakdown"""
    month_number: int
    month_name: str  # e.g., "January 2025"
    score_target: MonthlyScoreTarget
    weekly_breakdown: List[WeeklyBreakdown]
    practice_schedule: Dict[str, str]  # Day -> "PYQ" or "DPP"

class ScoreOrientedStudyPlan(BaseModel):
    """Complete Score-Oriented study plan"""
    user_id: str
    target_score: int
    exam_date: str
    total_months: int
    monthly_score_requirement: float  # Score needed per month
    score_ratio: float  # target_score / 300
    monthly_plans: List[MonthlyPlan]
    overall_strategy: str
    score_tracking: Dict[str, float]  # Month -> Expected cumulative score
    practice_configuration: Dict[str, List[str]]  # "practice_days" -> ["Saturday", "Sunday"]

class ChapterWithScore(BaseModel):
    """Chapter information with score data"""
    exam: str
    subject: str
    chapter: str
    average_weightage: float
    chapter_category: str
    dependencies: Optional[str] = None
    priority_score: float  # Calculated priority for score optimization

class ScoreCalculationResult(BaseModel):
    """Result of score calculation and chapter selection"""
    selected_chapters: Dict[str, List[ChapterWithScore]]  # Subject -> [chapters]
    total_expected_score: float
    monthly_distribution: List[MonthlyScoreTarget]
    is_target_achievable: bool
    optimization_notes: List[str]