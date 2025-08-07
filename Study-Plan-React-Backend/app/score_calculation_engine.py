from typing import Dict, List, Tuple
from datetime import datetime, timedelta
import math
from app.score_oriented_models import (
    ScoreOrientedUserData, 
    MonthlyScoreTarget, 
    WeeklyBreakdown, 
    MonthlyPlan,
    ScoreOrientedStudyPlan,
    ChapterWithScore,
    ScoreCalculationResult
)
from app.tools import get_chapter_weightage, get_chapter_flow, get_syllabus
from app.utils import get_logger

logger = get_logger(__name__)

class ScoreCalculationEngine:
    """Engine for calculating score-oriented study plans"""
    
    def __init__(self):
        self.max_marks = 300
        self.practice_days = ["Saturday", "Sunday"]
        self.study_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    def calculate_score_oriented_plan(self, user_data: ScoreOrientedUserData) -> ScoreOrientedStudyPlan:
        """Main function to calculate complete score-oriented plan"""
        
        # Step 1: Calculate score ratio and monthly requirements
        score_ratio = user_data.target_score / self.max_marks
        monthly_score_requirement = user_data.target_score / user_data.number_of_months
        
        logger.info(f"Score ratio: {score_ratio:.3f}, Monthly requirement: {monthly_score_requirement:.2f}")
        
        # Step 2: Get all available chapters with scores
        all_chapters = self._get_all_chapters_with_scores(user_data.target_exam)
        
        # Step 3: Select optimal chapters for target score
        score_calculation = self._select_optimal_chapters(all_chapters, user_data.target_score, user_data.number_of_months)
        
        # Step 4: Distribute chapters across months
        monthly_plans = self._distribute_chapters_monthly(
            score_calculation, 
            user_data.number_of_months, 
            monthly_score_requirement,
            user_data.exam_date
        )
        
        # Step 5: Create weekly breakdowns for each month
        for monthly_plan in monthly_plans:
            monthly_plan.weekly_breakdown = self._create_weekly_breakdown(monthly_plan)
        
        # Step 6: Build final study plan
        study_plan = ScoreOrientedStudyPlan(
            user_id=user_data.user_id,
            target_score=user_data.target_score,
            exam_date=user_data.exam_date,
            total_months=user_data.number_of_months,
            monthly_score_requirement=monthly_score_requirement,
            score_ratio=score_ratio,
            monthly_plans=monthly_plans,
            overall_strategy=self._generate_strategy_summary(score_calculation),
            score_tracking=self._calculate_score_tracking(monthly_plans),
            practice_configuration={"practice_days": self.practice_days, "study_days": self.study_days}
        )
        
        return study_plan
    
    def _get_all_chapters_with_scores(self, exam: str) -> List[ChapterWithScore]:
        """Get all chapters with their weightage and dependency information"""
        all_chapters = []
        subjects = ["Physics", "Chemistry", "Mathematics"]
        
        for subject in subjects:
            try:
                # Get chapter weightages
                weightage_data = get_chapter_weightage.invoke({"exam": exam, "subject": subject})
                
                # Get chapter dependencies
                flow_data = get_chapter_flow.invoke({"exam": exam, "subject": subject})
                dependency_map = {item.get("Chapter"): item.get("Dependencies") for item in flow_data}
                
                for chapter_info in weightage_data:
                    chapter = ChapterWithScore(
                        exam=exam,
                        subject=subject,
                        chapter=chapter_info.get("Chapter", ""),
                        average_weightage=chapter_info.get("Average Weightage", 0),
                        chapter_category=chapter_info.get("Chapter Category", "Medium"),
                        dependencies=dependency_map.get(chapter_info.get("Chapter")),
                        priority_score=self._calculate_priority_score(chapter_info)
                    )
                    all_chapters.append(chapter)
                    
            except Exception as e:
                logger.error(f"Error getting chapters for {subject}: {e}")
                continue
        
        return all_chapters
    
    def _calculate_priority_score(self, chapter_info: dict) -> float:
        """Calculate priority score for chapter selection"""
        weightage = chapter_info.get("Average Weightage", 0)
        category = chapter_info.get("Chapter Category", "Medium")
        
        # Category multipliers for score optimization
        category_multiplier = {
            "High": 1.5,
            "Medium": 1.2,
            "Low": 1.0
        }.get(category, 1.0)
        
        return weightage * category_multiplier
    
    def _select_optimal_chapters(self, all_chapters: List[ChapterWithScore], target_score: int, months: int) -> ScoreCalculationResult:
        """Select optimal chapters to achieve target score"""
        
        # Sort chapters by priority score (highest first)
        sorted_chapters = sorted(all_chapters, key=lambda x: x.priority_score, reverse=True)
        
        selected_chapters = {"Physics": [], "Chemistry": [], "Mathematics": []}
        total_score = 0
        
        # Greedy selection with dependency consideration
        for chapter in sorted_chapters:
            if total_score >= target_score:
                break
                
            # Check dependencies
            if self._can_add_chapter(chapter, selected_chapters):
                selected_chapters[chapter.subject].append(chapter)
                total_score += chapter.average_weightage
                logger.info(f"Added {chapter.subject} {chapter.chapter}: +{chapter.average_weightage} (Total: {total_score})")
        
        # Create monthly distribution
        monthly_targets = self._create_monthly_targets(selected_chapters, target_score, months)
        
        return ScoreCalculationResult(
            selected_chapters=selected_chapters,
            total_expected_score=total_score,
            monthly_distribution=monthly_targets,
            is_target_achievable=total_score >= target_score,
            optimization_notes=self._generate_optimization_notes(total_score, target_score)
        )
    
    def _can_add_chapter(self, chapter: ChapterWithScore, selected_chapters: Dict[str, List[ChapterWithScore]]) -> bool:
        """Check if chapter can be added considering dependencies"""
        if not chapter.dependencies:
            return True
        
        # Check if dependencies are already selected
        subject_chapters = selected_chapters.get(chapter.subject, [])
        selected_chapter_names = [ch.chapter for ch in subject_chapters]
        
        dependencies = chapter.dependencies.split(",") if chapter.dependencies else []
        for dep in dependencies:
            dep = dep.strip()
            if dep and dep not in selected_chapter_names:
                return False
        
        return True
    
    def _create_monthly_targets(self, selected_chapters: Dict[str, List[ChapterWithScore]], target_score: int, months: int) -> List[MonthlyScoreTarget]:
        """Create monthly score targets"""
        monthly_targets = []
        monthly_requirement = target_score / months
        
        # Distribute chapters across months
        all_selected = []
        for subject_chapters in selected_chapters.values():
            all_selected.extend(subject_chapters)
        
        chapters_per_month = math.ceil(len(all_selected) / months)
        
        for month in range(months):
            start_idx = month * chapters_per_month
            end_idx = min((month + 1) * chapters_per_month, len(all_selected))
            month_chapters = all_selected[start_idx:end_idx]
            
            month_score = sum(ch.average_weightage for ch in month_chapters)
            cumulative_target = (month + 1) * monthly_requirement
            
            monthly_target = MonthlyScoreTarget(
                month_number=month + 1,
                target_score_for_month=monthly_requirement,
                cumulative_target=cumulative_target,
                chapters_to_cover=[f"{ch.subject} - {ch.chapter}" for ch in month_chapters],
                estimated_score_from_chapters=month_score
            )
            monthly_targets.append(monthly_target)
        
        return monthly_targets
    
    def _distribute_chapters_monthly(self, score_calc: ScoreCalculationResult, months: int, monthly_requirement: float, exam_date: str) -> List[MonthlyPlan]:
        """Distribute chapters across months with proper planning"""
        monthly_plans = []
        
        # Calculate start date
        exam_datetime = datetime.strptime(exam_date, "%Y-%m-%d")
        start_date = exam_datetime - timedelta(days=months * 30)
        
        for i, monthly_target in enumerate(score_calc.monthly_distribution):
            month_date = start_date + timedelta(days=i * 30)
            month_name = month_date.strftime("%B %Y")
            
            monthly_plan = MonthlyPlan(
                month_number=i + 1,
                month_name=month_name,
                score_target=monthly_target,
                weekly_breakdown=[],  # Will be filled later
                practice_schedule=self._create_practice_schedule()
            )
            monthly_plans.append(monthly_plan)
        
        return monthly_plans
    
    def _create_weekly_breakdown(self, monthly_plan: MonthlyPlan) -> List[WeeklyBreakdown]:
        """Create weekly breakdown for a month"""
        weekly_breakdowns = []
        
        # Get chapters for this month
        month_chapters = monthly_plan.score_target.chapters_to_cover
        chapters_per_week = math.ceil(len(month_chapters) / 4)  # 4 weeks per month
        
        for week in range(4):
            start_idx = week * chapters_per_week
            end_idx = min((week + 1) * chapters_per_week, len(month_chapters))
            week_chapters = month_chapters[start_idx:end_idx]
            
            # Organize by subject
            chapters_by_subject = {}
            topics_by_subject = {}
            
            for chapter_str in week_chapters:
                if " - " in chapter_str:
                    subject, chapter = chapter_str.split(" - ", 1)
                    if subject not in chapters_by_subject:
                        chapters_by_subject[subject] = []
                        topics_by_subject[subject] = {}
                    
                    chapters_by_subject[subject].append(chapter)
                    topics_by_subject[subject][chapter] = [f"Topic_1", f"Topic_2", f"Topic_3"]  # Placeholder
            
            weekly_breakdown = WeeklyBreakdown(
                week_number=week + 1,
                study_days=self.study_days,
                practice_days=self.practice_days,
                chapters_this_week=chapters_by_subject,
                topics_this_week=topics_by_subject
            )
            weekly_breakdowns.append(weekly_breakdown)
        
        return weekly_breakdowns
    
    def _create_practice_schedule(self) -> Dict[str, str]:
        """Create practice schedule for weekends"""
        return {
            "Saturday": "PYQ (Previous Year Questions)",
            "Sunday": "DPP (Daily Practice Problems)"
        }
    
    def _generate_strategy_summary(self, score_calc: ScoreCalculationResult) -> str:
        """Generate overall strategy summary"""
        total_chapters = sum(len(chapters) for chapters in score_calc.selected_chapters.values())
        
        strategy = f"""🎯 Score-Oriented Strategy Summary:
        
• Target Score: Optimized for maximum efficiency
• Total Chapters Selected: {total_chapters}
• Expected Score: {score_calc.total_expected_score:.1f}/300
• Strategy: Focus on high-weightage chapters with dependency management
• Practice Schedule: Weekends dedicated to PYQ and DPP
• Monthly Targets: Consistent score progression with minimum thresholds

📊 Subject Distribution:
"""
        
        for subject, chapters in score_calc.selected_chapters.items():
            if chapters:
                subject_score = sum(ch.average_weightage for ch in chapters)
                strategy += f"• {subject}: {len(chapters)} chapters ({subject_score:.1f} marks)\n"
        
        return strategy
    
    def _calculate_score_tracking(self, monthly_plans: List[MonthlyPlan]) -> Dict[str, float]:
        """Calculate cumulative score tracking"""
        tracking = {}
        cumulative = 0
        
        for plan in monthly_plans:
            cumulative += plan.score_target.target_score_for_month
            tracking[f"Month_{plan.month_number}"] = cumulative
        
        return tracking
    
    def _generate_optimization_notes(self, achieved_score: float, target_score: int) -> List[str]:
        """Generate optimization notes"""
        notes = []
        
        if achieved_score >= target_score:
            notes.append(f"✅ Target achievable! Expected score: {achieved_score:.1f}/{target_score}")
        else:
            gap = target_score - achieved_score
            notes.append(f"⚠️ Score gap: {gap:.1f} marks. Consider revising target or adding more chapters.")
        
        notes.append("📅 Practice days (Sat/Sun) reserved for PYQ and DPP")
        notes.append("🎯 Monthly targets ensure consistent progress")
        notes.append("📈 High-weightage chapters prioritized for efficiency")
        
        return notes

# Global instance
score_engine = ScoreCalculationEngine()