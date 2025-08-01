from pydantic import BaseModel, Field
from typing import List, Dict, Optional

# A new model to hold the extracted user preferences for personalization
class PlanParameters(BaseModel):
    subject_priority: List[str] = Field(default_factory=list, description="A list of subjects the user wants to prioritize.")
    chapter_priority: Dict[str, List[str]] = Field(default_factory=dict, description="A dictionary of specific chapters to prioritize, grouped by subject.")
    chapter_coverage_order: Dict[str, List[str]] = Field(default_factory=dict, description="A dictionary specifying a custom chapter order for any subject.")

# A new model to represent the coverage of a single chapter in a month
class ChapterCoverage(BaseModel):
    chapter: str
    # The fraction of the chapter to be covered (e.g., 0.8 for 80%)
    coverage: float = Field(..., ge=0.0, le=1.0)

# The monthly plan for a single subject, now using ChapterCoverage
class MonthlySubjectPlan(BaseModel):
    physics: List[ChapterCoverage] = Field(default_factory=list)
    chemistry: List[ChapterCoverage] = Field(default_factory=list)
    mathematics: List[ChapterCoverage] = Field(default_factory=list)

# The weekly plan for a single subject remains a mapping of chapter to topics
class WeeklySubjectPlan(BaseModel):
    physics: Dict[str, List[str]] = Field(default_factory=dict)
    chemistry: Dict[str, List[str]] = Field(default_factory=dict)
    mathematics: Dict[str, List[str]] = Field(default_factory=dict)

# User data model with target score support
class UserData(BaseModel):
    user_id: str
    target_exam: str
    study_plan_type: str
    preparation_type: str
    syllabus: Dict[str, List[str]]
    number_of_months: int
    hours_per_day: int
    target_score: Optional[int] = None  # For generic study plans (e.g., 252 out of 300)

# Chat message model remains the same
class ChatMessage(BaseModel):
    user_message: str
    assistant_message: str

# Validation model remains the same
class Validation(BaseModel):
    status: str = Field(description="Must be 'yes' or 'no'")
    justification: str = Field(description="A brief explanation for the status.")

# The final study plan, updated to use the new monthly plan structure
class StudyPlan(BaseModel):
    insights: str = ""
    monthly_plan: Dict[str, MonthlySubjectPlan] = Field(default_factory=dict)
    weekly_plan: Dict[str, WeeklySubjectPlan] = Field(default_factory=dict) 