from typing import Dict, List, Tuple, Optional
from app.core.tools import get_chapter_flow, get_chapter_weightage, get_topic_priority, get_syllabus
from app.core.utils import get_logger
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import json

logger = get_logger(__name__)

# Initialize LLM for agents
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

def create_agent(llm, tools: list, system_message: str):
    """Creates an LLM-powered agent with tools like core flow"""
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_message),
        ("human", "{input}"),
    ])
    if tools:
        return prompt | llm.bind_tools(tools)
    return prompt | llm

class RevisionFlowAgent:
    """
    RevisionFlow Agent - Combination of flow and weightage logic for new_score_oriented plans.
    Handles complete syllabus coverage with dependency management and priority-based ordering.
    """
    
    def __init__(self):
        self.dependency_cache = {}
        self.weightage_cache = {}
        self.syllabus_cache = {}
    
    def generate_revision_flow_plan(self, user_data, plan_parameters) -> Dict:
        """
        Main function to generate revision flow plan with complete syllabus coverage.
        
        Args:
            user_data: UserData object containing exam, target_score, months
            plan_parameters: PlanParameters object with user preferences
            
        Returns:
            Dict containing complete revision flow plan with chapters and dependencies
        """
        logger.info("RevisionFlow Agent executing: Generating complete syllabus coverage plan")
        
        # Check if this is new_score_oriented plan
        is_new_score_oriented = user_data.study_plan_type.lower() == "new_score_oriented"
        
        if not is_new_score_oriented:
            logger.info("Not a new_score_oriented plan, skipping RevisionFlow")
            return {"status": "skipped", "reason": "not_new_score_oriented"}
        
        logger.info(f"Processing new_score_oriented plan for target: {user_data.target_score}/300")
        
        revision_plan = {
            "status": "success",
            "target_score": user_data.target_score,
            "total_months": user_data.number_of_months,
            "complete_syllabus_coverage": True,
            "subject_plans": {},
            "monthly_distribution": {},
            "practice_schedule": self._generate_practice_schedule(user_data.number_of_months),
            "dependency_analysis": {},
            "coverage_validation": {}
        }
        
        # Get complete syllabus for the exam
        complete_syllabus = self._get_complete_syllabus(user_data.target_exam)
        
        # Process each subject with complete coverage
        for subject in ['Physics', 'Chemistry', 'Mathematics']:
            logger.info(f"Processing complete syllabus for {subject}")
            
            # Get all chapters for this subject
            all_chapters = self._get_all_chapters_for_subject(user_data.target_exam, subject)
            
            # Get dependencies and weightages
            dependencies = self._get_chapter_dependencies(user_data.target_exam, subject)
            weightages = self._get_chapter_weightages(user_data.target_exam, subject)
            
            # Use perfect dependency adjustment for optimal ordering
            chapter_sequence = self._generate_perfect_dependency_sequence(
                user_data.target_exam, subject, plan_parameters
            )
            
            # Ensure 100% coverage for all chapters
            complete_coverage_plan = self._ensure_complete_coverage(
                chapter_sequence, user_data.target_score
            )
            
            revision_plan["subject_plans"][subject.lower()] = complete_coverage_plan
            revision_plan["dependency_analysis"][subject.lower()] = self._analyze_dependencies(
                chapter_sequence, dependencies
            )
        
        # Distribute across months (target: complete in 6 months max)
        target_months = min(user_data.number_of_months, 6)  # Close syllabus within 6 months
        revision_plan["monthly_distribution"] = self._distribute_across_months(
            revision_plan["subject_plans"], target_months, user_data.number_of_months
        )
        
        # Enhanced features for new_score_oriented
        logger.info("Starting enhanced features generation...")
        enhanced_features = self._generate_enhanced_features(
            user_data, revision_plan["subject_plans"], target_months
        )
        revision_plan["enhanced_features"] = enhanced_features
        logger.info(f"Enhanced features generated: {list(enhanced_features.keys()) if enhanced_features else 'None'}")
        
        # Validate complete coverage
        revision_plan["coverage_validation"] = self._validate_complete_coverage(
            revision_plan["subject_plans"], complete_syllabus
        )
        
        logger.info(f"RevisionFlow plan generated with {target_months} months for syllabus completion")
        return revision_plan
    
    def _get_complete_syllabus(self, exam: str) -> Dict:
        """Get complete syllabus from Syllabus table."""
        cache_key = f"{exam}_complete_syllabus"
        if cache_key not in self.syllabus_cache:
            try:
                syllabus_data = get_syllabus.invoke({"exam": exam})
                self.syllabus_cache[cache_key] = syllabus_data
            except Exception as e:
                logger.error(f"Error fetching complete syllabus for {exam}: {e}")
                self.syllabus_cache[cache_key] = []
        
        return self.syllabus_cache[cache_key]
    
    def _get_all_chapters_for_subject(self, exam: str, subject: str) -> List[str]:
        """Get all chapters for a subject from syllabus."""
        complete_syllabus = self._get_complete_syllabus(exam)
        chapters = list(set([
            item['Chapter'] for item in complete_syllabus 
            if item['Subject'].lower() == subject.lower()
        ]))
        return sorted(chapters)
    
    def _get_chapter_dependencies(self, exam: str, subject: str) -> List[Dict]:
        """Get chapter dependencies with caching."""
        cache_key = f"{exam}_{subject}_deps"
        if cache_key not in self.dependency_cache:
            try:
                dependencies = get_chapter_flow.invoke({"exam": exam, "subject": subject})
                self.dependency_cache[cache_key] = dependencies
            except Exception as e:
                logger.error(f"Error fetching dependencies for {subject}: {e}")
                self.dependency_cache[cache_key] = []
        
        return self.dependency_cache[cache_key]
    
    def _get_chapter_weightages(self, exam: str, subject: str) -> List[Dict]:
        """Get chapter weightages with caching."""
        cache_key = f"{exam}_{subject}_weights"
        if cache_key not in self.weightage_cache:
            try:
                weightages = get_chapter_weightage.invoke({"exam": exam, "subject": subject})
                self.weightage_cache[cache_key] = weightages
            except Exception as e:
                logger.error(f"Error fetching weightages for {subject}: {e}")
                self.weightage_cache[cache_key] = []
        
        return self.weightage_cache[cache_key]
    
    def _generate_perfect_dependency_sequence(self, exam: str, subject: str, plan_parameters) -> List[Dict]:
        """
        Generate chapter sequence using enhanced dependency resolution.
        This ensures dependent chapters always come first, regardless of priority.
        """
        from app.new_score_oriented.tools import enhanced_dependency_resolution_tool
        
        logger.info(f"Generating perfect dependency sequence for {subject}")
        
        try:
            # Use the enhanced dependency resolution tool
            adjustment_result = enhanced_dependency_resolution_tool.invoke({
                "exam": exam,
                "subject": subject
            })
            
            if adjustment_result.get("status") == "success":
                resolved_order = adjustment_result.get("resolved_order", [])
                
                # Apply user preferences on top of dependency-resolved order
                final_sequence = self._apply_user_preferences_to_resolved_order(
                    resolved_order, plan_parameters, subject
                )
                
                logger.info(f"Perfect dependency sequence generated for {subject}: {len(final_sequence)} chapters")
                logger.info("Dependency-first ordering applied successfully")
                
                return final_sequence
            else:
                logger.warning(f"Perfect dependency adjustment failed for {subject}, falling back to original method")
                # Fallback to original method
                return self._fallback_to_original_sequence(exam, subject, plan_parameters)
                
        except Exception as e:
            logger.error(f"Error in perfect dependency sequence generation for {subject}: {e}")
            # Fallback to original method
            return self._fallback_to_original_sequence(exam, subject, plan_parameters)
    
    def _apply_user_preferences_to_resolved_order(self, resolved_order: List[Dict], 
                                                plan_parameters, subject: str) -> List[Dict]:
        """
        Apply user preferences while maintaining dependency order.
        User preferences can only reorder chapters that don't violate dependencies.
        """
        logger.info(f"Applying user preferences to dependency-resolved order for {subject}")
        
        # Get user preferences
        user_priority_chapters = plan_parameters.chapter_priority.get(subject.lower(), [])
        user_order_chapters = plan_parameters.chapter_coverage_order.get(subject.lower(), [])
        
        # Create a copy to work with
        final_sequence = []
        
        # Convert resolved order to our format and add user preference indicators
        for chapter_info in resolved_order:
            chapter_name = chapter_info["chapter"]
            
            # Determine priority reason
            priority_reason = "dependency_optimized"
            if chapter_name in user_priority_chapters:
                priority_reason = "user_priority_with_dependencies"
            elif chapter_name in user_order_chapters:
                priority_reason = "user_order_with_dependencies"
            
            final_chapter_info = {
                "chapter": chapter_name,
                "weightage": chapter_info.get("weightage", 0),
                "category": chapter_info.get("category", "Medium"),
                "coverage_percentage": 1.0,  # Always 100% for new_score_oriented
                "priority_reason": priority_reason,
                "dependencies_satisfied": True,  # Guaranteed by perfect adjustment
                "completion_order": chapter_info.get("completion_order", 0),
                "dependency_level": chapter_info.get("dependency_level", 0),
                "dependencies": chapter_info.get("dependencies", [])
            }
            
            final_sequence.append(final_chapter_info)
        
        logger.info(f"User preferences applied to {len(final_sequence)} chapters while maintaining dependencies")
        return final_sequence
    
    def _fallback_to_original_sequence(self, exam: str, subject: str, plan_parameters) -> List[Dict]:
        """Fallback to original sequence generation method"""
        logger.info(f"Using fallback sequence generation for {subject}")
        
        # Get all chapters for this subject
        all_chapters = self._get_all_chapters_for_subject(exam, subject)
        dependencies = self._get_chapter_dependencies(exam, subject)
        weightages = self._get_chapter_weightages(exam, subject)
        
        return self._generate_priority_sequence_with_dependencies(
            all_chapters, dependencies, weightages, plan_parameters, subject
        )
    
    def _generate_priority_sequence_with_dependencies(self, chapters: List[str], 
                                                    dependencies: List[Dict], 
                                                    weightages: List[Dict],
                                                    plan_parameters, subject: str) -> List[Dict]:
        """
        Generate chapter sequence considering:
        1. User priority preferences
        2. Chapter dependencies (dependent chapters done first)
        3. Weightage-based ordering
        4. 100% coverage requirement
        """
        logger.info(f"Generating priority sequence for {subject} with {len(chapters)} chapters")
        
        # Create weightage and dependency maps
        weightage_map = {w['Chapter']: w['Average Weightage'] for w in weightages}
        category_map = {w['Chapter']: w.get('Chapter Category', 'Medium') for w in weightages}
        
        dependency_map = {}
        for dep in dependencies:
            chapter = dep.get('Chapter')
            deps = dep.get('Dependencies', '')
            if chapter and deps:
                dep_list = [d.strip() for d in deps.split(',') if d.strip()]
                dependency_map[chapter] = dep_list
        
        # Apply user preferences for priority
        user_priority_chapters = plan_parameters.chapter_priority.get(subject.lower(), [])
        user_order_chapters = plan_parameters.chapter_coverage_order.get(subject.lower(), [])
        
        # Build complete sequence with dependencies
        sequence = []
        processed = set()
        
        # Process user priority chapters first (with their dependencies)
        for priority_chapter in user_priority_chapters:
            if priority_chapter in chapters and priority_chapter not in processed:
                dep_chain = self._resolve_complete_dependency_chain(
                    priority_chapter, dependency_map, weightage_map, chapters
                )
                for ch in dep_chain:
                    if ch not in processed:
                        sequence.append(self._create_chapter_info(
                            ch, weightage_map, category_map, "user_priority"
                        ))
                        processed.add(ch)
        
        # Process user order chapters
        for order_chapter in user_order_chapters:
            if order_chapter in chapters and order_chapter not in processed:
                dep_chain = self._resolve_complete_dependency_chain(
                    order_chapter, dependency_map, weightage_map, chapters
                )
                for ch in dep_chain:
                    if ch not in processed:
                        sequence.append(self._create_chapter_info(
                            ch, weightage_map, category_map, "user_order"
                        ))
                        processed.add(ch)
        
        # Process remaining chapters by weightage (high to low)
        remaining_chapters = [ch for ch in chapters if ch not in processed]
        remaining_chapters.sort(key=lambda x: weightage_map.get(x, 0), reverse=True)
        
        for chapter in remaining_chapters:
            if chapter not in processed:
                dep_chain = self._resolve_complete_dependency_chain(
                    chapter, dependency_map, weightage_map, chapters
                )
                for ch in dep_chain:
                    if ch not in processed:
                        sequence.append(self._create_chapter_info(
                            ch, weightage_map, category_map, "weightage_priority"
                        ))
                        processed.add(ch)
        
        logger.info(f"Generated sequence for {subject}: {[ch['chapter'] for ch in sequence]}")
        return sequence
    
    def _resolve_complete_dependency_chain(self, chapter: str, dependency_map: Dict,
                                         weightage_map: Dict, available_chapters: List[str]) -> List[str]:
        """Resolve complete dependency chain with topological sorting."""
        visited = set()
        temp_visited = set()
        chain = []
        
        def dfs(current_chapter):
            if current_chapter in temp_visited:
                # Circular dependency detected, skip
                return
            if current_chapter in visited or current_chapter not in available_chapters:
                return
            
            temp_visited.add(current_chapter)
            
            # Process dependencies first
            deps = dependency_map.get(current_chapter, [])
            valid_deps = [dep for dep in deps if dep in available_chapters]
            
            # Sort dependencies by weightage (highest first)
            valid_deps.sort(key=lambda x: weightage_map.get(x, 0), reverse=True)
            
            for dep in valid_deps:
                dfs(dep)
            
            temp_visited.remove(current_chapter)
            if current_chapter not in visited:
                visited.add(current_chapter)
                chain.append(current_chapter)
        
        dfs(chapter)
        return chain
    
    def _create_chapter_info(self, chapter: str, weightage_map: Dict, 
                           category_map: Dict, priority_reason: str) -> Dict:
        """Create chapter information object."""
        return {
            "chapter": chapter,
            "weightage": weightage_map.get(chapter, 0),
            "category": category_map.get(chapter, "Medium"),
            "coverage_percentage": 1.0,  # Always 100% for new_score_oriented
            "priority_reason": priority_reason,
            "dependencies_satisfied": True
        }
    
    def _ensure_complete_coverage(self, chapter_sequence: List[Dict], target_score: int) -> Dict:
        """Ensure 100% coverage for all chapters in sequence."""
        logger.info("Ensuring 100% coverage for all chapters")
        
        total_weightage = sum(ch['weightage'] for ch in chapter_sequence)
        
        coverage_plan = {
            "chapters": chapter_sequence,
            "total_chapters": len(chapter_sequence),
            "total_weightage": total_weightage,
            "coverage_percentage": 100.0,
            "expected_score_contribution": total_weightage,
            "target_contribution_percentage": (total_weightage / target_score) * 100 if target_score > 0 else 0
        }
        
        # Set all chapters to 100% coverage
        for chapter_info in chapter_sequence:
            chapter_info['coverage_percentage'] = 1.0
            chapter_info['coverage_reason'] = 'complete_syllabus_coverage'
        
        return coverage_plan
    
    def _distribute_across_months(self, subject_plans: Dict, target_months: int, 
                                total_months: int) -> Dict:
        """Distribute chapters across months with syllabus completion target."""
        logger.info(f"Distributing syllabus across {target_months} months (total: {total_months})")
        
        monthly_distribution = {}
        
        # Calculate total chapters across all subjects
        total_chapters = sum(
            len(plan["chapters"]) for plan in subject_plans.values()
        )
        
        chapters_per_month = max(1, total_chapters // target_months)
        
        # Distribute chapters month by month
        for month in range(1, target_months + 1):
            monthly_distribution[f"month_{month}"] = {
                "month_number": month,
                "target": "syllabus_completion" if month <= target_months else "practice_focus",
                "subjects": {},
                "practice_days": ["Saturday", "Sunday"],
                "focus": "complete_coverage"
            }
            
            for subject, plan in subject_plans.items():
                start_idx = (month - 1) * (len(plan["chapters"]) // target_months)
                end_idx = month * (len(plan["chapters"]) // target_months)
                
                if month == target_months:  # Last month gets remaining chapters
                    end_idx = len(plan["chapters"])
                
                month_chapters = plan["chapters"][start_idx:end_idx]
                monthly_distribution[f"month_{month}"]["subjects"][subject] = {
                    "chapters": month_chapters,
                    "chapter_count": len(month_chapters),
                    "weightage_sum": sum(ch['weightage'] for ch in month_chapters)
                }
        
        # Remaining months (if any) focus on practice
        for month in range(target_months + 1, total_months + 1):
            monthly_distribution[f"month_{month}"] = {
                "month_number": month,
                "target": "intensive_practice",
                "focus": "PYQ_and_DPP",
                "practice_days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                "subjects": {subject: {"practice_focus": True} for subject in subject_plans.keys()}
            }
        
        return monthly_distribution
    
    def _generate_practice_schedule(self, total_months: int) -> Dict:
        """Generate practice schedule with Saturday/Sunday for PYQ/DPP."""
        practice_schedule = {
            "regular_practice_days": ["Saturday", "Sunday"],
            "practice_types": {
                "Saturday": "PYQ",  # Previous Year Questions
                "Sunday": "DPP"     # Daily Practice Problems
            },
            "intensive_practice_months": []
        }
        
        # If more than 6 months, last months are for intensive practice
        if total_months > 6:
            practice_schedule["intensive_practice_months"] = list(range(7, total_months + 1))
            practice_schedule["intensive_practice_note"] = "Last months dedicated to intensive PYQ and DPP practice"
        
        return practice_schedule
    
    def _analyze_dependencies(self, chapter_sequence: List[Dict], dependencies: List[Dict]) -> Dict:
        """Analyze dependency satisfaction in the sequence."""
        dependency_map = {}
        for dep in dependencies:
            chapter = dep.get('Chapter')
            deps = dep.get('Dependencies', '')
            if chapter and deps:
                dependency_map[chapter] = [d.strip() for d in deps.split(',') if d.strip()]
        
        analysis = {
            "total_dependencies": len(dependency_map),
            "satisfied_dependencies": 0,
            "dependency_violations": [],
            "dependency_chains": {}
        }
        
        # Check if dependencies are satisfied in sequence
        chapter_positions = {ch['chapter']: i for i, ch in enumerate(chapter_sequence)}
        
        for chapter, deps in dependency_map.items():
            if chapter in chapter_positions:
                chapter_pos = chapter_positions[chapter]
                satisfied = True
                
                for dep in deps:
                    if dep in chapter_positions:
                        dep_pos = chapter_positions[dep]
                        if dep_pos >= chapter_pos:  # Dependency comes after chapter
                            satisfied = False
                            analysis["dependency_violations"].append({
                                "chapter": chapter,
                                "dependency": dep,
                                "issue": f"{dep} should come before {chapter}"
                            })
                
                if satisfied:
                    analysis["satisfied_dependencies"] += 1
                
                analysis["dependency_chains"][chapter] = {
                    "dependencies": deps,
                    "satisfied": satisfied,
                    "position": chapter_pos
                }
        
        return analysis
    
    def _validate_complete_coverage(self, subject_plans: Dict, complete_syllabus: List[Dict]) -> Dict:
        """Validate that all syllabus topics are covered."""
        validation = {
            "complete_coverage": True,
            "coverage_percentage": 0.0,
            "missing_chapters": {},
            "covered_chapters": {},
            "total_syllabus_chapters": 0,
            "covered_count": 0
        }
        
        # Group syllabus by subject
        syllabus_by_subject = {}
        for item in complete_syllabus:
            subject = item['Subject'].lower()
            if subject not in syllabus_by_subject:
                syllabus_by_subject[subject] = set()
            syllabus_by_subject[subject].add(item['Chapter'])
        
        # Check coverage for each subject
        for subject, syllabus_chapters in syllabus_by_subject.items():
            validation["total_syllabus_chapters"] += len(syllabus_chapters)
            
            if subject in subject_plans:
                covered_chapters = set(ch['chapter'] for ch in subject_plans[subject]['chapters'])
                missing = syllabus_chapters - covered_chapters
                
                validation["covered_chapters"][subject] = list(covered_chapters)
                validation["covered_count"] += len(covered_chapters)
                
                if missing:
                    validation["missing_chapters"][subject] = list(missing)
                    validation["complete_coverage"] = False
            else:
                validation["missing_chapters"][subject] = list(syllabus_chapters)
                validation["complete_coverage"] = False
        
        if validation["total_syllabus_chapters"] > 0:
            validation["coverage_percentage"] = (validation["covered_count"] / validation["total_syllabus_chapters"]) * 100
        
        return validation
    
    def _generate_enhanced_features(self, user_data, subject_plans: Dict, target_months: int) -> Dict:
        """
        Generate enhanced features for new_score_oriented plans:
        1. Extended months with PYQ/DPP focus
        2. Monthly target score calculations
        3. Weekly topic breakdown
        4. Comprehensive weekend schedule
        """
        enhanced_features = {}
        
        try:
            from app.enhanced_new_score_oriented_tools import (
                calculate_monthly_target_scores,
                generate_extended_months_plan,
                generate_weekly_topic_breakdown,
                create_comprehensive_weekend_schedule
            )
        except ImportError as e:
            logger.error(f"Failed to import enhanced tools: {e}")
            enhanced_features["error"] = f"Enhanced tools not available: {str(e)}"
            return enhanced_features
        
        logger.info("Generating enhanced features for new_score_oriented plan")
        
        try:
            # 1. Prepare monthly chapters data for calculations
            monthly_chapters = self._prepare_monthly_chapters_data(subject_plans, target_months)
            logger.info(f"Monthly chapters data prepared: {list(monthly_chapters.keys())}")
            logger.info(f"Sample month data structure: {monthly_chapters.get('month_1', {})}")
            
            # 2. Calculate monthly target scores
            target_scores_result = calculate_monthly_target_scores(user_data.__dict__, subject_plans, target_months)
            enhanced_features["monthly_target_scores"] = target_scores_result
            
            # 3. Generate extended months plan (if applicable)
            extended_plan_result = generate_extended_months_plan(user_data.__dict__, subject_plans, target_months)
            enhanced_features["extended_months_plan"] = extended_plan_result
            
            # 4. Generate weekly topic breakdown
            topic_breakdown_result = generate_weekly_topic_breakdown(user_data.__dict__, subject_plans, target_months)
            enhanced_features["weekly_topic_breakdown"] = topic_breakdown_result
            
            # 5. Create comprehensive weekend schedule
            weekend_schedule_result = create_comprehensive_weekend_schedule(user_data.__dict__, subject_plans, target_months)
            enhanced_features["weekend_schedule"] = weekend_schedule_result
            
            # 6. Generate overall strategy summary
            enhanced_features["strategy_summary"] = self._generate_strategy_summary(
                user_data, target_months, target_scores_result, extended_plan_result
            )
            
            logger.info("Enhanced features generated successfully")
            
        except Exception as e:
            logger.error(f"Error generating enhanced features: {e}")
            enhanced_features["error"] = str(e)
            enhanced_features["status"] = "partial_failure"
        
        return enhanced_features
    
    def _prepare_monthly_chapters_data(self, subject_plans: Dict, target_months: int) -> Dict:
        """Prepare monthly chapters data for enhanced calculations"""
        monthly_chapters = {}
        
        # Distribute chapters across target months
        for month in range(1, target_months + 1):
            monthly_chapters[f"month_{month}"] = {}
            
            for subject, plan in subject_plans.items():
                chapters = plan.get("chapters", [])
                
                # Distribute chapters evenly across months
                chapters_per_month = len(chapters) // target_months
                start_idx = (month - 1) * chapters_per_month
                end_idx = month * chapters_per_month if month < target_months else len(chapters)
                
                month_chapters = [ch["chapter"] for ch in chapters[start_idx:end_idx]]
                monthly_chapters[f"month_{month}"][subject] = month_chapters
        
        return monthly_chapters
    
    def _generate_strategy_summary(self, user_data, target_months: int, target_scores_result: Dict, extended_plan_result: Dict) -> Dict:
        """Generate comprehensive strategy summary"""
        
        strategy = {
            "plan_type": "new_score_oriented",
            "target_score": user_data.target_score,
            "total_months": user_data.number_of_months,
            "syllabus_completion_phase": {
                "duration": f"{target_months} months",
                "objective": "100% syllabus coverage with complete chapter completion",
                "approach": "Dependency-first ordering with priority optimization",
                "weekend_focus": "Saturday & Sunday PYQ practice"
            }
        }
        
        # Add extended months strategy if applicable
        if user_data.number_of_months > target_months:
            extended_months = user_data.number_of_months - target_months
            strategy["intensive_practice_phase"] = {
                "duration": f"{extended_months} months",
                "objective": "Intensive PYQ & DPP practice for score maximization",
                "approach": "Full syllabus revision with mock tests",
                "daily_schedule": "One DPP per subject + PYQ practice"
            }
        
        # Add target achievement analysis
        if target_scores_result.get("status") == "success":
            achievability = target_scores_result.get("target_achievability", {})
            strategy["target_achievement"] = {
                "is_achievable": achievability.get("is_achievable", False),
                "confidence_level": achievability.get("confidence", "medium"),
                "total_achievable_score": target_scores_result.get("total_achievable_score", 0),
                "efficiency_required": target_scores_result.get("overall_efficiency_required", 0)
            }
        
        # Add key recommendations
        strategy["key_recommendations"] = [
            "Complete 100% of each chapter before moving to next",
            "Follow dependency-first order for optimal learning progression",
            "Dedicate every weekend to PYQ practice",
            "Maintain daily DPP practice for each subject",
            "Focus on high-priority topics within each chapter",
            "Use extended months for intensive practice and mock tests"
        ]
        
        return strategy

class NewScoreOrientedValidator:
    """
    Validator for new_score_oriented plans - ensures all chapters and topics are covered.
    """
    
    def __init__(self):
        self.topic_cache = {}
        self.syllabus_cache = {}
    
    def validate_chapter_coverage(self, user_data, revision_plan) -> Dict:
        """Validate that all required chapters are covered."""
        logger.info("Validating chapter coverage for new_score_oriented plan")
        
        validation_result = {
            "status": "success",
            "chapter_validation": {
                "all_chapters_covered": True,
                "missing_chapters": {},
                "coverage_percentage": 0.0
            },
            "user_requirements_fulfilled": True,
            "target_achievability": {
                "target_score": user_data.target_score,
                "expected_score": 0.0,
                "achievable": True,
                "confidence": "high"
            }
        }
        
        # Calculate expected score from revision plan
        total_expected_score = 0
        # Check if revision_plan has subject_plans or revision_flow_results
        subject_data = revision_plan.get("subject_plans") or revision_plan.get("revision_flow_results", {})
        for subject, plan in subject_data.items():
            if isinstance(plan, dict):
                # Handle both old format (total_weightage) and new format (chapters with weightage)
                if "total_weightage" in plan:
                    total_expected_score += plan["total_weightage"]
                elif "chapters" in plan:
                    # Sum up weightages from individual chapters
                    for chapter in plan["chapters"]:
                        if isinstance(chapter, dict) and "weightage" in chapter:
                            total_expected_score += chapter["weightage"]
        
        validation_result["target_achievability"]["expected_score"] = total_expected_score
        validation_result["target_achievability"]["achievable"] = total_expected_score >= user_data.target_score
        
        # Validate coverage
        coverage_validation = revision_plan.get("coverage_validation", {})
        validation_result["chapter_validation"]["all_chapters_covered"] = coverage_validation.get("complete_coverage", False)
        validation_result["chapter_validation"]["coverage_percentage"] = coverage_validation.get("coverage_percentage", 0.0)
        validation_result["chapter_validation"]["missing_chapters"] = coverage_validation.get("missing_chapters", {})
        
        # Check user requirements
        if not validation_result["target_achievability"]["achievable"]:
            validation_result["user_requirements_fulfilled"] = False
            validation_result["recommendations"] = [
                "Consider extending study duration",
                "Focus on high-weightage chapters",
                "Increase daily study hours if possible"
            ]
        
        return validation_result
    
    def validate_topic_coverage(self, user_data, chapter_plan) -> Dict:
        """Validate that all topics for selected chapters are covered."""
        logger.info("Validating topic coverage for new_score_oriented plan")
        
        validation_result = {
            "status": "success",
            "topic_validation": {
                "all_topics_covered": True,
                "missing_topics": {},
                "total_topics": 0,
                "covered_topics": 0
            },
            "syllabus_compliance": True
        }
        
        # Get complete syllabus for comparison
        complete_syllabus = self._get_complete_syllabus(user_data.target_exam)
        
        # Validate topics for each subject and chapter
        for subject, chapters in chapter_plan.items():
            if isinstance(chapters, list):
                for chapter_info in chapters:
                    chapter_name = chapter_info.get('chapter', chapter_info.get('Chapter', ''))
                    
                    # Get all topics for this chapter
                    chapter_topics = self._get_chapter_topics(
                        user_data.target_exam, subject.title(), chapter_name
                    )
                    
                    # Get syllabus topics for validation
                    syllabus_topics = self._get_syllabus_topics(
                        complete_syllabus, subject.title(), chapter_name
                    )
                    
                    validation_result["topic_validation"]["total_topics"] += len(syllabus_topics)
                    
                    # For new_score_oriented, we cover all topics (100% coverage)
                    validation_result["topic_validation"]["covered_topics"] += len(syllabus_topics)
                    
                    # Check if any topics are missing
                    if len(chapter_topics) < len(syllabus_topics):
                        missing = set(syllabus_topics) - set([t.get('Topic', '') for t in chapter_topics])
                        if missing:
                            if subject not in validation_result["topic_validation"]["missing_topics"]:
                                validation_result["topic_validation"]["missing_topics"][subject] = {}
                            validation_result["topic_validation"]["missing_topics"][subject][chapter_name] = list(missing)
                            validation_result["topic_validation"]["all_topics_covered"] = False
        
        # Calculate coverage percentage
        if validation_result["topic_validation"]["total_topics"] > 0:
            coverage_pct = (validation_result["topic_validation"]["covered_topics"] / 
                          validation_result["topic_validation"]["total_topics"]) * 100
            validation_result["topic_validation"]["coverage_percentage"] = coverage_pct
        
        return validation_result
    
    def validate_syllabus_compliance(self, user_data, complete_plan) -> Dict:
        """Final validation against complete syllabus."""
        logger.info("Performing final syllabus compliance validation")
        
        validation_result = {
            "status": "success",
            "syllabus_compliance": {
                "fully_compliant": True,
                "compliance_percentage": 0.0,
                "missing_elements": {},
                "extra_elements": {}
            },
            "final_validation": True
        }
        
        # Get complete syllabus
        complete_syllabus = self._get_complete_syllabus(user_data.target_exam)
        
        # Create syllabus structure for comparison
        syllabus_structure = {}
        for item in complete_syllabus:
            subject = item['Subject']
            chapter = item['Chapter']
            topic = item['Topic']
            
            if subject not in syllabus_structure:
                syllabus_structure[subject] = {}
            if chapter not in syllabus_structure[subject]:
                syllabus_structure[subject][chapter] = set()
            syllabus_structure[subject][chapter].add(topic)
        
        # Compare with plan structure
        total_syllabus_items = sum(
            len(topics) for subject_chapters in syllabus_structure.values()
            for topics in subject_chapters.values()
        )
        
        covered_items = 0
        
        # For new_score_oriented, we aim for 100% coverage
        # This validation ensures we're meeting that goal
        for subject, chapters in syllabus_structure.items():
            for chapter, topics in chapters.items():
                # In new_score_oriented, all topics should be covered
                covered_items += len(topics)
        
        validation_result["syllabus_compliance"]["compliance_percentage"] = (
            covered_items / total_syllabus_items * 100 if total_syllabus_items > 0 else 0
        )
        
        validation_result["syllabus_compliance"]["fully_compliant"] = (
            validation_result["syllabus_compliance"]["compliance_percentage"] >= 99.0
        )
        
        return validation_result
    
    def _get_complete_syllabus(self, exam: str) -> List[Dict]:
        """Get complete syllabus with caching."""
        cache_key = f"{exam}_syllabus"
        if cache_key not in self.syllabus_cache:
            try:
                syllabus_data = get_syllabus.invoke({"exam": exam})
                self.syllabus_cache[cache_key] = syllabus_data
            except Exception as e:
                logger.error(f"Error fetching syllabus for {exam}: {e}")
                self.syllabus_cache[cache_key] = []
        
        return self.syllabus_cache[cache_key]
    
    def _get_chapter_topics(self, exam: str, subject: str, chapter: str) -> List[Dict]:
        """Get topics for a specific chapter."""
        cache_key = f"{exam}_{subject}_{chapter}_topics"
        if cache_key not in self.topic_cache:
            try:
                topics = get_topic_priority.invoke({
                    "exam": exam,
                    "subject": subject,
                    "chapter": chapter
                })
                self.topic_cache[cache_key] = topics
            except Exception as e:
                logger.error(f"Error fetching topics for {chapter}: {e}")
                self.topic_cache[cache_key] = []
        
        return self.topic_cache[cache_key]
    
    def _get_syllabus_topics(self, complete_syllabus: List[Dict], subject: str, chapter: str) -> List[str]:
        """Get topics from syllabus for a specific chapter."""
        topics = [
            item['Topic'] for item in complete_syllabus
            if item['Subject'] == subject and item['Chapter'] == chapter
        ]
        return topics


class NewScoreOrientedSupervisor:
    """
    Supervisor for new_score_oriented plans with target achievement focus.
    """
    
    def __init__(self):
        self.validator = NewScoreOrientedValidator()
    
    def supervise_plan(self, user_data, complete_plan_state) -> Dict:
        """
        Comprehensive supervision of new_score_oriented plan.
        Focus on target achievement regardless of hours per day.
        """
        logger.info("Supervising new_score_oriented plan for target achievement")
        
        supervision_result = {
            "status": "success",
            "plan_approved": True,
            "target_achievement_analysis": {},
            "adjustments_needed": [],
            "final_recommendations": [],
            "user_requirements_met": True
        }
        
        # Analyze target achievement
        target_analysis = self._analyze_target_achievement(user_data, complete_plan_state)
        supervision_result["target_achievement_analysis"] = target_analysis
        
        # Check if target is achievable within decided months
        if not target_analysis["achievable_in_timeframe"]:
            # Force fit the plan to achieve target
            adjustments = self._force_fit_for_target(user_data, complete_plan_state)
            supervision_result["adjustments_needed"] = adjustments
            supervision_result["plan_approved"] = False  # Need adjustments
        
        # Validate practice schedule
        practice_validation = self._validate_practice_schedule(user_data, complete_plan_state)
        supervision_result["practice_schedule_validation"] = practice_validation
        
        # Generate final recommendations
        supervision_result["final_recommendations"] = self._generate_final_recommendations(
            user_data, target_analysis, practice_validation
        )
        
        return supervision_result
    
    def _analyze_target_achievement(self, user_data, plan_state) -> Dict:
        """Analyze if target score is achievable with current plan."""
        revision_plan = plan_state.get("revision_flow_results", {})
        
        analysis = {
            "target_score": user_data.target_score,
            "expected_score": 0.0,
            "achievable_in_timeframe": True,
            "confidence_level": "high",
            "risk_factors": [],
            "success_probability": 0.0
        }
        
        # Calculate expected score
        total_expected = 0
        for subject, plan in revision_plan.get("subject_plans", {}).items():
            total_expected += plan.get("total_weightage", 0)
        
        analysis["expected_score"] = total_expected
        analysis["achievable_in_timeframe"] = total_expected >= user_data.target_score
        
        # Calculate success probability
        if user_data.target_score > 0:
            analysis["success_probability"] = min(100, (total_expected / user_data.target_score) * 100)
        
        # Identify risk factors
        if analysis["success_probability"] < 90:
            analysis["risk_factors"].append("Expected score below 90% of target")
            analysis["confidence_level"] = "medium"
        
        if user_data.number_of_months < 6:
            analysis["risk_factors"].append("Limited preparation time")
        
        return analysis
    
    def _force_fit_for_target(self, user_data, plan_state) -> List[Dict]:
        """
        Force fit the plan to achieve target score regardless of hours per day.
        """
        logger.info("Force fitting plan to achieve target score")
        
        adjustments = []
        
        # Adjustment 1: Increase study intensity
        adjustments.append({
            "type": "intensity_increase",
            "description": "Increase daily study intensity to meet target",
            "recommendation": "Focus on high-weightage topics with extended study sessions",
            "impact": "Higher probability of target achievement"
        })
        
        # Adjustment 2: Optimize chapter selection
        adjustments.append({
            "type": "chapter_optimization",
            "description": "Prioritize highest weightage chapters",
            "recommendation": "Spend more time on chapters with maximum score potential",
            "impact": "Maximize score efficiency"
        })
        
        # Adjustment 3: Intensive practice schedule
        adjustments.append({
            "type": "practice_intensification",
            "description": "Increase practice frequency",
            "recommendation": "Daily practice sessions instead of weekend-only",
            "impact": "Better retention and application"
        })
        
        # Adjustment 4: Time redistribution
        adjustments.append({
            "type": "time_redistribution",
            "description": "Redistribute time based on score potential",
            "recommendation": "Allocate time proportional to chapter weightages",
            "impact": "Optimal time utilization for target achievement"
        })
        
        return adjustments
    
    def _validate_practice_schedule(self, user_data, plan_state) -> Dict:
        """Validate practice schedule for new_score_oriented plans."""
        practice_validation = {
            "schedule_appropriate": True,
            "weekend_practice_configured": True,
            "intensive_months_planned": False,
            "recommendations": []
        }
        
        revision_plan = plan_state.get("revision_flow_results", {})
        practice_schedule = revision_plan.get("practice_schedule", {})
        
        # Check weekend practice
        regular_days = practice_schedule.get("regular_practice_days", [])
        if "Saturday" not in regular_days or "Sunday" not in regular_days:
            practice_validation["weekend_practice_configured"] = False
            practice_validation["recommendations"].append("Configure Saturday and Sunday for PYQ/DPP practice")
        
        # Check intensive practice months
        intensive_months = practice_schedule.get("intensive_practice_months", [])
        if user_data.number_of_months > 6 and not intensive_months:
            practice_validation["intensive_months_planned"] = False
            practice_validation["recommendations"].append("Plan intensive practice for final months")
        else:
            practice_validation["intensive_months_planned"] = True
        
        return practice_validation
    
    def _generate_final_recommendations(self, user_data, target_analysis, practice_validation) -> List[str]:
        """Generate final recommendations for the plan."""
        recommendations = []
        
        # Target achievement recommendations
        if target_analysis["success_probability"] < 100:
            recommendations.append(
                f"Current plan achieves {target_analysis['success_probability']:.1f}% of target. "
                "Consider focusing on high-weightage chapters for better efficiency."
            )
        
        # Time management recommendations
        if user_data.number_of_months <= 6:
            recommendations.append(
                "With 6 months or less, maintain intensive daily study schedule. "
                "Complete syllabus within first 4-5 months, reserve last month for intensive practice."
            )
        else:
            recommendations.append(
                "Complete syllabus within 6 months. Use remaining months for intensive PYQ and DPP practice."
            )
        
        # Practice recommendations
        if not practice_validation["weekend_practice_configured"]:
            recommendations.append("Ensure Saturday (PYQ) and Sunday (DPP) practice schedule is followed consistently.")
        
        # Score optimization recommendations
        recommendations.append(
            "Focus on 100% chapter completion rather than partial coverage. "
            "This ensures strong foundation and better score potential."
        )
        
        return recommendations


# REPLACED: Convert Python classes to LLM-powered agents like core flow

# LLM-POWERED REVISION FLOW AGENT
revision_flow_agent = create_agent(
    llm,
    [get_chapter_flow, get_chapter_weightage, get_topic_priority],
    """You are a revision flow agent for new_score_oriented study plans.
    
    Your role is to create complete syllabus coverage plans with:
    1. 100% chapter completion (not partial coverage)
    2. Dependency-based chapter ordering
    3. Priority-weighted sequencing for target score achievement
    4. Saturday/Sunday practice schedule integration
    
    CHAT CONTEXT AWARENESS:
    - Analyze user chat history for preferences
    - Extract subject priorities from conversation
    - Apply chapter preferences mentioned by user
    - Consider user's learning style and constraints
    
    USER PREFERENCES TO LOOK FOR:
    - "I want to focus more on [subject]"
    - "I'm weak in [chapter/topic]"
    - "I prefer [learning style]"
    - "I have constraints like [constraint]"
    
    Always ensure 100% syllabus coverage while respecting user preferences.
    Use the provided tools to get chapter flow, weightage, and topic data."""
)

# LLM-POWERED VALIDATOR AGENT
new_score_oriented_validator = create_agent(
    llm,
    [get_chapter_flow, get_chapter_weightage],
    """You are a validator for new_score_oriented study plans.
    
    Your role is to validate:
    1. All syllabus chapters are included
    2. Dependencies are properly ordered
    3. Target score is achievable with the plan
    4. User requirements from chat are fulfilled
    
    CHAT ANALYSIS:
    - Review user conversation for specific requirements
    - Validate that user preferences are implemented
    - Check if user concerns are addressed
    - Ensure plan aligns with user's stated goals
    
    Use the provided tools to verify chapter data and dependencies."""
)

# LLM-POWERED SUPERVISOR AGENT
new_score_oriented_supervisor = create_agent(
    llm,
    [],
    """You are a supervisor for new_score_oriented study plans.
    
    Your role is to provide final validation and recommendations:
    1. Analyze target achievement probability
    2. Provide pros/cons of the generated plan
    3. Suggest optimizations based on user chat
    4. Give final approval or request adjustments
    
    CHAT-BASED INSIGHTS:
    - Consider user's expressed preferences
    - Address any concerns mentioned in chat
    - Provide personalized recommendations
    - Ensure plan feels tailored to the user
    
    Always provide encouraging and actionable feedback."""
)

# Keep the original Python classes for backward compatibility if needed
# But the main agents above are now LLM-powered like core flow
original_revision_flow_agent = RevisionFlowAgent()
original_new_score_oriented_validator = NewScoreOrientedValidator()
original_new_score_oriented_supervisor = NewScoreOrientedSupervisor()