from langchain_core.tools import tool
from typing import Dict, List, Optional
from datetime import datetime, timedelta
from app.core.tools import supabase
from app.core.utils import get_logger

logger = get_logger(__name__)

@tool
def validate_new_score_oriented_exam_date(exam_date: str) -> Dict:
    """
    Validate exam date for new_score_oriented plans (minimum 6 months required).
    
    Args:
        exam_date: Exam date in YYYY-MM-DD format
        
    Returns:
        Dict with validation result and calculated months
    """
    try:
        exam_dt = datetime.strptime(exam_date, "%Y-%m-%d")
        today = datetime.now()
        
        # Calculate difference in months
        months_diff = (exam_dt.year - today.year) * 12 + (exam_dt.month - today.month)
        
        # Adjust for day of month
        if exam_dt.day < today.day:
            months_diff -= 1
        
        is_valid = months_diff >= 6
        
        result = {
            "is_valid": is_valid,
            "calculated_months": months_diff,
            "exam_date": exam_date,
            "minimum_required": 6,
            "message": f"Exam date is {months_diff} months away. " + 
                      ("Valid for new_score_oriented plan." if is_valid else 
                       "Minimum 6 months required for new_score_oriented plan.")
        }
        
        logger.info(f"Exam date validation: {result}")
        return result
        
    except ValueError as e:
        logger.error(f"Invalid date format: {exam_date}")
        return {
            "is_valid": False,
            "calculated_months": 0,
            "exam_date": exam_date,
            "message": "Invalid date format. Please use YYYY-MM-DD format."
        }
    except Exception as e:
        logger.error(f"Error validating exam date: {e}")
        return {
            "is_valid": False,
            "calculated_months": 0,
            "exam_date": exam_date,
            "message": f"Error validating date: {str(e)}"
        }

@tool
def get_chapter_weightage_for_revision(exam: str, subject: str = None) -> List[Dict]:
    """
    Get chapter weightage data for revision flow planning.
    
    Args:
        exam: Target exam name
        subject: Optional subject filter
        
    Returns:
        List of chapter weightage data
    """
    if not supabase:
        logger.error("Database connection not available. Cannot fetch chapter weightage data.")
        return []
    
    try:
        logger.info(f"Fetching chapter weightage for exam: {exam}, subject: {subject}")
        query = supabase.table("Chapter_Weightage").select("*").eq("Exam", exam)
        
        if subject:
            query = query.eq("Subject", subject.title())
            
        response = query.execute()
        return response.data
        
    except Exception as e:
        logger.error(f"Error fetching chapter weightage: {e}")
        return []

@tool
def get_chapter_flow_with_dependencies(exam: str, subject: str = None) -> List[Dict]:
    """
    Get chapter flow data with dependencies for revision planning.
    
    Args:
        exam: Target exam name
        subject: Optional subject filter
        
    Returns:
        List of chapter flow data with dependencies
    """
    if not supabase:
        logger.error("Database connection not available. Cannot fetch chapter flow data.")
        return []
    
    try:
        logger.info(f"Fetching chapter flow for exam: {exam}, subject: {subject}")
        query = supabase.table("Chapter_Flow").select("*").eq("Exam", exam)
        
        if subject:
            query = query.eq("Subject", subject.title())
            
        response = query.execute()
        return response.data
        
    except Exception as e:
        logger.error(f"Error fetching chapter flow: {e}")
        return []

@tool
def get_topic_priority_for_chapter(exam: str, subject: str, chapter: str) -> List[Dict]:
    """
    Get topic priority data for a specific chapter.
    
    Args:
        exam: Target exam name
        subject: Subject name
        chapter: Chapter name
        
    Returns:
        List of topic priority data
    """
    if not supabase:
        logger.error("Database connection not available. Cannot fetch topic priority data.")
        return []
    
    try:
        logger.info(f"Fetching topic priority for exam: {exam}, subject: {subject}, chapter: {chapter}")
        response = supabase.table("Topic_Priority").select("*").eq("Exam", exam).eq("Subject", subject.title()).eq("Chapter", chapter).execute()
        return response.data
        
    except Exception as e:
        logger.error(f"Error fetching topic priority: {e}")
        return []

@tool
def get_complete_syllabus_for_revision(exam: str) -> List[Dict]:
    """
    Get complete syllabus for revision flow validation.
    
    Args:
        exam: Target exam name
        
    Returns:
        List of complete syllabus data
    """
    if not supabase:
        logger.error("Database connection not available. Cannot fetch complete syllabus data.")
        return []
    
    try:
        logger.info(f"Fetching complete syllabus for exam: {exam}")
        response = supabase.table("Syllabus").select("*").eq("Exam", exam).execute()
        return response.data
        
    except Exception as e:
        logger.error(f"Error fetching complete syllabus: {e}")
        return []

@tool
def save_new_score_oriented_progress(user_id: str, progress_data: Dict) -> str:
    """
    Save new_score_oriented plan progress to database.
    
    Args:
        user_id: User identifier
        progress_data: Progress data to save
        
    Returns:
        Success/failure message
    """
    if not supabase:
        logger.warning("Supabase not available. Cannot save progress.")
        return "Database not available - progress not saved"
    
    try:
        logger.info(f"Saving new_score_oriented progress for user: {user_id}")
        
        # Prepare progress data
        save_data = {
            "user_id": user_id,
            "plan_type": "new_score_oriented",
            "progress_data": progress_data,
            "last_updated": datetime.now().isoformat()
        }
        
        # Use upsert to handle both insert and update
        response = supabase.table("New_Score_Oriented_Progress").upsert(save_data).execute()
        
        if response.data:
            logger.info(f"Successfully saved progress for user: {user_id}")
            return f"Progress successfully saved for user {user_id}"
        else:
            logger.error(f"Failed to save progress for user {user_id}")
            return f"Failed to save progress for user {user_id}"
            
    except Exception as e:
        logger.error(f"Error saving progress for user {user_id}: {e}")
        return f"Error saving progress: {str(e)}"

@tool
def resolve_chapter_dependencies_advanced(exam: str, subject: str) -> Dict:
    """
    Resolve chapter dependencies using Chapter_Flow table and create proper sequence.
    
    Args:
        exam: Target exam name
        subject: Subject name
        
    Returns:
        Dict with resolved dependency order and dependency chains
    """
    try:
        # Get chapter flow data with dependencies
        flow_data = get_chapter_flow_with_dependencies.invoke({
            "exam": exam,
            "subject": subject
        })
        
        # Get weightage data for priority
        weightage_data = get_chapter_weightage_for_revision.invoke({
            "exam": exam,
            "subject": subject
        })
        
        # Create weightage lookup
        weightage_lookup = {}
        for item in weightage_data:
            chapter = item.get("Chapter", "")
            weightage = item.get("Average Weightage", 0)
            weightage_lookup[chapter] = weightage
        
        # Build dependency graph
        dependency_graph = {}
        all_chapters = set()
        
        for item in flow_data:
            chapter = item.get("Chapter", "")
            dependencies = item.get("Dependencies", "")
            
            all_chapters.add(chapter)
            dependency_graph[chapter] = {
                "dependencies": [],
                "weightage": weightage_lookup.get(chapter, 0),
                "required_hours": item.get("Required Hours", 0)
            }
            
            # Parse dependencies (could be comma-separated)
            if dependencies and dependencies.strip():
                deps = [dep.strip() for dep in dependencies.split(",") if dep.strip()]
                dependency_graph[chapter]["dependencies"] = deps
                all_chapters.update(deps)
        
        # Topological sort with priority consideration
        resolved_order = []
        visited = set()
        temp_visited = set()
        
        def dfs_visit(chapter):
            if chapter in temp_visited:
                # Circular dependency detected - log warning and continue
                logger.warning(f"Circular dependency detected involving {chapter}")
                return
            if chapter in visited:
                return
            
            temp_visited.add(chapter)
            
            # Visit all dependencies first
            chapter_info = dependency_graph.get(chapter, {})
            dependencies = chapter_info.get("dependencies", [])
            
            for dep in dependencies:
                if dep in dependency_graph:
                    dfs_visit(dep)
            
            temp_visited.remove(chapter)
            visited.add(chapter)
            resolved_order.append(chapter)
        
        # Sort chapters by weightage first, then resolve dependencies
        chapters_by_priority = sorted(
            all_chapters,
            key=lambda ch: dependency_graph.get(ch, {}).get("weightage", 0),
            reverse=True
        )
        
        # Resolve dependencies while maintaining priority
        for chapter in chapters_by_priority:
            if chapter not in visited:
                dfs_visit(chapter)
        
        # Create dependency chains for analysis
        dependency_chains = {}
        for chapter, info in dependency_graph.items():
            if info["dependencies"]:
                dependency_chains[chapter] = info["dependencies"]
        
        result = {
            "resolved_order": resolved_order,
            "dependency_chains": dependency_chains,
            "dependency_graph": dependency_graph,
            "total_chapters": len(all_chapters),
            "subject": subject,
            "exam": exam
        }
        
        logger.info(f"Resolved dependencies for {subject}: {len(resolved_order)} chapters in proper order")
        return result
        
    except Exception as e:
        logger.error(f"Error resolving dependencies for {subject}: {e}")
        return {
            "resolved_order": [],
            "dependency_chains": {},
            "dependency_graph": {},
            "total_chapters": 0,
            "error": str(e)
        }

@tool
def resolve_chapter_dependencies_with_weightage(exam: str, subject: str) -> Dict:
    """
    Advanced dependency resolution using the new dependency resolver system.
    Considers both chapter dependencies and weightage priorities.
    
    Args:
        exam: Target exam name
        subject: Subject name
        
    Returns:
        Dict with properly resolved chapter order considering dependencies
    """
    try:
        from app.dependency_resolver import resolve_subject_dependencies
        
        # Get flow and weightage data
        flow_data = get_chapter_flow_with_dependencies.invoke({
            "exam": exam,
            "subject": subject
        })
        
        weightage_data = get_chapter_weightage_for_revision.invoke({
            "exam": exam,
            "subject": subject
        })
        
        # Use advanced dependency resolver
        result = resolve_subject_dependencies(exam, subject, flow_data, weightage_data)
        
        logger.info(f"Advanced dependency resolution completed for {subject}: {result.get('total_chapters', 0)} chapters")
        return result
        
    except Exception as e:
        logger.error(f"Error in advanced dependency resolution for {subject}: {e}")
        return {
            "resolved_order": [],
            "dependency_chains": {},
            "validation": {"is_valid": False, "violations": [], "total_chapters": 0},
            "total_chapters": 0,
            "subject": subject,
            "exam": exam,
            "error": str(e)
        }

@tool
def enhanced_dependency_resolution_tool(exam: str, subject: str) -> Dict:
    """
    Enhanced dependency resolution tool that strictly ensures dependent chapters 
    are scheduled before their dependents, regardless of priority scores.
    
    Uses Chapter_Flow and Chapter_Weightage tables for accurate dependency resolution.
    
    Example: If Chapter 2 depends on Chapter 3, then Chapter 3 will be scheduled
    first, even if Chapter 2 has higher priority.
    
    Args:
        exam: Target exam name
        subject: Subject name
        
    Returns:
        Dict with strictly dependency-ordered chapters and comprehensive analysis
    """
    try:
        # Note: enhanced_dependency_resolver was removed during cleanup
        # This functionality should be implemented directly in this module
        
        # Get flow and weightage data from database tables
        flow_data = get_chapter_flow_with_dependencies.invoke({
            "exam": exam,
            "subject": subject
        })
        
        weightage_data = get_chapter_weightage_for_revision.invoke({
            "exam": exam,
            "subject": subject
        })
        
        logger.info(f"Starting enhanced dependency resolution for {subject}")
        logger.info(f"Flow data: {len(flow_data)} chapters with dependencies")
        logger.info(f"Weightage data: {len(weightage_data)} chapters with priorities")
        
        # Apply enhanced dependency resolution
        result = _enhanced_dependency_resolution(exam, subject, flow_data, weightage_data)
        
        # Log the resolution results
        if result.get("status") == "success":
            resolved_order = result.get("resolved_order", [])
            dependency_report = result.get("dependency_report", {})
            
            logger.info(f"Enhanced dependency resolution for {subject}:")
            logger.info(f"  Total chapters: {len(resolved_order)}")
            logger.info(f"  Chapters with dependencies: {dependency_report.get('chapters_with_dependencies', 0)}")
            logger.info(f"  All dependencies satisfied: {dependency_report.get('dependency_satisfaction', {}).get('all_satisfied', False)}")
            
            # Log the final order with dependency information
            logger.info("Final chapter order (dependencies first):")
            for i, ch in enumerate(resolved_order):
                chapter_info = result.get("chapter_analysis", {}).get(ch, {})
                if chapter_info.get("dependencies"):
                    deps_str = ", ".join(chapter_info["dependencies"])
                    logger.info(f"  {i+1:2d}. {ch} (depends on: {deps_str}) - Priority: {chapter_info.get('priority_score', 0):.1f}")
                else:
                    logger.info(f"  {i+1:2d}. {ch} (no dependencies) - Priority: {chapter_info.get('priority_score', 0):.1f}")
            
            # Log critical path
            critical_path = dependency_report.get("critical_path", [])
            if critical_path:
                logger.info(f"Critical path: {' → '.join(critical_path)}")
            
            # Log optimization suggestions
            suggestions = dependency_report.get("optimization_suggestions", [])
            if suggestions:
                logger.info("Optimization suggestions:")
                for suggestion in suggestions:
                    logger.info(f"  • {suggestion}")
            
            # Log any violations (should be none with enhanced resolver)
            violations = dependency_report.get("dependency_satisfaction", {}).get("violations", [])
            if violations:
                logger.warning(f"Dependency violations found: {len(violations)}")
                for violation in violations:
                    logger.warning(f"  - {violation['issue']}")
            else:
                logger.info("✅ All dependencies perfectly satisfied!")
        
        return result
        
    except Exception as e:
        logger.error(f"Error in enhanced dependency resolution tool for {subject}: {e}")
        return {
            "status": "error",
            "resolved_order": [],
            "dependency_chains": {},
            "total_chapters": 0,
            "subject": subject,
            "exam": exam,
            "error": str(e)
        }

@tool
def perfect_dependency_adjustment_tool(exam: str, subject: str) -> Dict:
    """
    Perfect dependency adjustment tool that ensures dependent chapters are scheduled
    before their dependents, regardless of priority scores.
    
    Example: If Chapter 2 depends on Chapter 3, then Chapter 3 will be scheduled
    first, even if Chapter 2 has higher priority.
    
    Args:
        exam: Target exam name
        subject: Subject name
        
    Returns:
        Dict with perfectly adjusted chapter order considering dependencies first
    """
    try:
        from app.perfect_dependency_adjuster import perfect_dependency_adjustment
        
        # Get flow and weightage data
        flow_data = get_chapter_flow_with_dependencies.invoke({
            "exam": exam,
            "subject": subject
        })
        
        weightage_data = get_chapter_weightage_for_revision.invoke({
            "exam": exam,
            "subject": subject
        })
        
        # Apply perfect dependency adjustment
        result = perfect_dependency_adjustment(exam, subject, flow_data, weightage_data)
        
        # Log the adjustment results
        if result.get("status") == "success":
            resolved_order = result.get("resolved_order", [])
            logger.info(f"Perfect dependency adjustment for {subject}:")
            logger.info(f"  Total chapters: {len(resolved_order)}")
            
            # Log dependency satisfaction
            for i, ch in enumerate(resolved_order):
                if ch.get("dependencies"):
                    deps_str = ", ".join(ch["dependencies"])
                    logger.info(f"  {i+1}. {ch['chapter']} (depends on: {deps_str}) - Priority: {ch.get('priority_score', 0):.1f}")
                else:
                    logger.info(f"  {i+1}. {ch['chapter']} (no dependencies) - Priority: {ch.get('priority_score', 0):.1f}")
            
            # Log optimization suggestions
            suggestions = result.get("dependency_analysis", {}).get("optimization_suggestions", [])
            if suggestions:
                logger.info("Optimization suggestions:")
                for suggestion in suggestions:
                    logger.info(f"  - {suggestion}")
        
        return result
        
    except Exception as e:
        logger.error(f"Error in perfect dependency adjustment tool for {subject}: {e}")
        return {
            "status": "error",
            "resolved_order": [],
            "dependency_chains": {},
            "total_chapters": 0,
            "subject": subject,
            "exam": exam,
            "error": str(e)
        }

@tool
def validate_syllabus_coverage(exam: str, planned_chapters: Dict[str, List[str]]) -> Dict:
    """
    Validate that all syllabus chapters are covered in the plan.
    
    Args:
        exam: Target exam name
        planned_chapters: Dict of subject -> [chapter names]
        
    Returns:
        Validation result with coverage analysis
    """
    try:
        # Get complete syllabus
        complete_syllabus = get_complete_syllabus_for_revision.invoke({"exam": exam})
        
        # Group syllabus by subject
        syllabus_by_subject = {}
        for item in complete_syllabus:
            subject = item["Subject"]
            chapter = item["Chapter"]
            
            if subject not in syllabus_by_subject:
                syllabus_by_subject[subject] = set()
            syllabus_by_subject[subject].add(chapter)
        
        # Check coverage
        validation_result = {
            "complete_coverage": True,
            "coverage_percentage": 0.0,
            "missing_chapters": {},
            "covered_chapters": {},
            "total_chapters": 0,
            "covered_count": 0
        }
        
        total_chapters = sum(len(chapters) for chapters in syllabus_by_subject.values())
        covered_count = 0
        
        for subject, syllabus_chapters in syllabus_by_subject.items():
            planned_for_subject = set(planned_chapters.get(subject, []))
            missing = syllabus_chapters - planned_for_subject
            
            validation_result["covered_chapters"][subject] = list(planned_for_subject & syllabus_chapters)
            covered_count += len(planned_for_subject & syllabus_chapters)
            
            if missing:
                validation_result["missing_chapters"][subject] = list(missing)
                validation_result["complete_coverage"] = False
        
        validation_result["total_chapters"] = total_chapters
        validation_result["covered_count"] = covered_count
        validation_result["coverage_percentage"] = (covered_count / total_chapters * 100) if total_chapters > 0 else 0
        
        logger.info(f"Syllabus coverage validation: {validation_result['coverage_percentage']:.1f}% coverage")
        return validation_result
        
    except Exception as e:
        logger.error(f"Error validating syllabus coverage: {e}")
        return {
            "complete_coverage": False,
            "coverage_percentage": 0.0,
            "error": str(e)
        }

def _enhanced_dependency_resolution(exam: str, subject: str, flow_data: List[Dict], weightage_data: List[Dict]) -> Dict:
    """
    Enhanced dependency resolution algorithm that considers both dependencies and weightage
    """
    try:
        # Create chapter mapping
        chapter_map = {}
        for chapter_info in flow_data:
            chapter_name = chapter_info.get("chapter", "")
            dependencies = chapter_info.get("dependencies", "")
            chapter_map[chapter_name] = {
                "dependencies": [dep.strip() for dep in dependencies.split(",") if dep.strip()] if dependencies else [],
                "weightage": 0.0,
                "priority_score": 0.0
            }
        
        # Add weightage information
        for weight_info in weightage_data:
            chapter_name = weight_info.get("chapter", "")
            if chapter_name in chapter_map:
                chapter_map[chapter_name]["weightage"] = float(weight_info.get("average_weightage", 0))
                chapter_map[chapter_name]["priority_score"] = float(weight_info.get("average_weightage", 0))
        
        # Topological sort with priority consideration
        resolved_order = []
        remaining_chapters = set(chapter_map.keys())
        dependency_report = {
            "chapters_with_dependencies": sum(1 for ch in chapter_map.values() if ch["dependencies"]),
            "dependency_satisfaction": {"all_satisfied": True, "unsatisfied": []},
            "resolution_method": "topological_sort_with_priority"
        }
        
        # Process chapters in dependency order
        while remaining_chapters:
            # Find chapters with no unresolved dependencies
            ready_chapters = []
            for chapter in remaining_chapters:
                deps = chapter_map[chapter]["dependencies"]
                if all(dep in resolved_order or dep not in chapter_map for dep in deps):
                    ready_chapters.append(chapter)
            
            if not ready_chapters:
                # Handle circular dependencies by picking highest priority
                ready_chapters = [max(remaining_chapters, key=lambda ch: chapter_map[ch]["priority_score"])]
                dependency_report["dependency_satisfaction"]["all_satisfied"] = False
                dependency_report["dependency_satisfaction"]["unsatisfied"].extend(ready_chapters)
            
            # Sort ready chapters by priority (highest weightage first)
            ready_chapters.sort(key=lambda ch: chapter_map[ch]["priority_score"], reverse=True)
            
            # Add the highest priority chapter
            next_chapter = ready_chapters[0]
            resolved_order.append(next_chapter)
            remaining_chapters.remove(next_chapter)
        
        return {
            "status": "success",
            "resolved_order": resolved_order,
            "dependency_report": dependency_report,
            "chapter_analysis": chapter_map
        }
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "resolved_order": list(chapter_map.keys()) if 'chapter_map' in locals() else [],
            "dependency_report": {"error": str(e)}
        }