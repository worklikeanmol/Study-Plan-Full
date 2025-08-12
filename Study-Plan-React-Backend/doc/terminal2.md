```
INFO:     127.0.0.1:65213 - "OPTIONS /chat HTTP/1.1" 200 OK
2025-08-12 15:01:55,424 - app.main - INFO - Received chat message from user: user_igha5v6vx
2025-08-12 15:01:55,429 - app.regen_tools - INFO - Checking if user exists: user_igha5v6vx
2025-08-12 15:01:55,818 - app.regen_tools - INFO - User user_igha5v6vx found in database
2025-08-12 15:01:55,819 - app.main - INFO - User existence check for user_igha5v6vx: exists=True, has_study_plan=False, treating_as_existing=False
2025-08-12 15:01:55,820 - app.main - INFO - New user detected: user_igha5v6vx - routing to normal flow
2025-08-12 15:01:56,024 - app.main - INFO - Retrieved stored form data for user: user_igha5v6vx
2025-08-12 15:01:56,024 - app.main - INFO - Using stored form data for user: user_igha5v6vx
2025-08-12 15:01:56,025 - app.new_score_oriented_tools - INFO - Exam date validation: {'is_valid': True, 'calculated_months': 8, 'exam_date': '2026-04-12', 'minimum_required': 6, 'message': 'Exam date is 8 months away. Valid for new_score_oriented plan.'}
2025-08-12 15:01:56,026 - app.new_score_oriented_graph - INFO - Counsellor Generator Agent executing for new_score_oriented plan
2025-08-12 15:01:56,027 - app.new_score_oriented_tools - INFO - Exam date validation: {'is_valid': True, 'calculated_months': 8, 'exam_date': '2026-04-12', 'minimum_required': 6, 'message': 'Exam date is 8 months away. Valid for new_score_oriented plan.'}
2025-08-12 15:01:56,028 - app.new_score_oriented_graph - INFO - New Score-Oriented Requirement Extractor executing
2025-08-12 15:02:00,611 - app.new_score_oriented_graph - INFO - Requirement extraction result: success
2025-08-12 15:02:00,611 - app.new_score_oriented_graph - INFO - Extracted requirements: subject_priority=['physics', 'chemistry', 'mathematics'] chapter_coverage={} time_allocation={}
2025-08-12 15:02:00,612 - app.new_score_oriented_graph - INFO - RevisionFlow Agent executing
2025-08-12 15:02:00,613 - app.new_score_oriented_agents - INFO - RevisionFlow Agent executing: Generating complete syllabus coverage plan
2025-08-12 15:02:00,613 - app.new_score_oriented_agents - INFO - Processing new_score_oriented plan for target: 230/300
2025-08-12 15:02:00,614 - app.tools - INFO - Fetching syllabus for exam: JEE Mains
2025-08-12 15:02:00,784 - app.new_score_oriented_agents - INFO - Processing complete syllabus for Physics
2025-08-12 15:02:00,785 - app.tools - INFO - Fetching chapter flow for exam: JEE Mains, subject: Physics
2025-08-12 15:02:00,903 - app.tools - INFO - Fetching chapter weightage for exam: JEE Mains, subject: Physics
2025-08-12 15:02:00,986 - app.new_score_oriented_agents - INFO - Generating perfect dependency sequence for Physics
2025-08-12 15:02:00,988 - app.new_score_oriented_tools - INFO - Fetching chapter flow for exam: JEE Mains, subject: Physics
2025-08-12 15:02:01,135 - app.new_score_oriented_tools - INFO - Fetching chapter weightage for exam: JEE Mains, subject: Physics
2025-08-12 15:02:01,250 - app.new_score_oriented_tools - INFO - Starting enhanced dependency resolution for Physics
2025-08-12 15:02:01,250 - app.new_score_oriented_tools - INFO - Flow data: 12 chapters with dependencies
2025-08-12 15:02:01,250 - app.new_score_oriented_tools - INFO - Weightage data: 12 chapters with priorities
2025-08-12 15:02:01,250 - app.enhanced_dependency_resolver - INFO - Building comprehensive dependency graph from Chapter_Flow and Chapter_Weightage tables
2025-08-12 15:02:01,251 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_1]' for chapter 'Chapter_3' not found in chapter list
2025-08-12 15:02:01,251 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_2]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 15:02:01,251 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_3]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 15:02:01,251 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_4]' for chapter 'Chapter_7' not found in chapter list
2025-08-12 15:02:01,251 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_6]' for chapter 'Chapter_10' not found in chapter list
2025-08-12 15:02:01,251 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_5]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 15:02:01,251 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_7]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 15:02:01,251 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_1]' for chapter 'Chapter_2' not found in chapter list
2025-08-12 15:02:01,252 - app.enhanced_dependency_resolver - INFO - Dependency graph built: 12 chapters, 8 dependencies
2025-08-12 15:02:01,252 - app.enhanced_dependency_resolver - INFO - Starting strict dependency resolution for Physics
2025-08-12 15:02:01,252 - app.enhanced_dependency_resolver - WARNING - Some chapters could not be resolved due to dependency cycles: {'Chapter_10', 'Chapter_7', 'Chapter_2', 'Chapter_12', 'Chapter_5', 'Chapter_3'}
2025-08-12 15:02:01,252 - app.enhanced_dependency_resolver - INFO - Strict dependency resolution completed for Physics: 12 chapters
2025-08-12 15:02:01,252 - app.enhanced_dependency_resolver - INFO - Enhanced dependency resolution completed for Physics: 12 chapters with strict dependency ordering
2025-08-12 15:02:01,252 - app.new_score_oriented_tools - INFO - Enhanced dependency resolution for Physics:
2025-08-12 15:02:01,252 - app.new_score_oriented_tools - INFO -   Total chapters: 12
2025-08-12 15:02:01,252 - app.new_score_oriented_tools - INFO -   Chapters with dependencies: 6
2025-08-12 15:02:01,253 - app.new_score_oriented_tools - INFO -   All dependencies satisfied: True
2025-08-12 15:02:01,253 - app.new_score_oriented_tools - INFO - Final chapter order (dependencies first):
2025-08-12 15:02:01,253 - app.new_score_oriented_tools - INFO -    1. Chapter_9 (no dependencies) - Priority: 44.3
2025-08-12 15:02:01,253 - app.new_score_oriented_tools - INFO -    2. Chapter_8 (no dependencies) - Priority: 38.2
2025-08-12 15:02:01,253 - app.new_score_oriented_tools - INFO -    3. Chapter_11 (no dependencies) - Priority: 15.6
2025-08-12 15:02:01,253 - app.new_score_oriented_tools - INFO -    4. Chapter_4 (no dependencies) - Priority: 3.4
2025-08-12 15:02:01,253 - app.new_score_oriented_tools - INFO -    5. Chapter_6 (no dependencies) - Priority: 2.3
2025-08-12 15:02:01,253 - app.new_score_oriented_tools - INFO -    6. Chapter_1 (no dependencies) - Priority: 0.9
2025-08-12 15:02:01,253 - app.new_score_oriented_tools - INFO -    7. Chapter_10 (depends on: [Chapter_6]) - Priority: 22.6
2025-08-12 15:02:01,254 - app.new_score_oriented_tools - INFO -    8. Chapter_7 (depends on: [Chapter_4]) - Priority: 11.7
2025-08-12 15:02:01,254 - app.new_score_oriented_tools - INFO -    9. Chapter_2 (depends on: [Chapter_1]) - Priority: 44.0
2025-08-12 15:02:01,254 - app.new_score_oriented_tools - INFO -   10. Chapter_12 (depends on: [Chapter_5], [Chapter_7]) - Priority: 22.6
2025-08-12 15:02:01,254 - app.new_score_oriented_tools - INFO -   11. Chapter_5 (depends on: [Chapter_2], [Chapter_3]) - Priority: 41.9
2025-08-12 15:02:01,254 - app.new_score_oriented_tools - INFO -   12. Chapter_3 (depends on: [Chapter_1]) - Priority: 0.9
2025-08-12 15:02:01,254 - app.new_score_oriented_tools - INFO - Critical path: [Chapter_6] → Chapter_10
2025-08-12 15:02:01,254 - app.new_score_oriented_tools - INFO - Optimization suggestions:
2025-08-12 15:02:01,254 - app.new_score_oriented_tools - INFO -   • Consider parallel study tracks for efficiency: 3 groups of independent chapters identified
2025-08-12 15:02:01,254 - app.new_score_oriented_tools - INFO - ✅ All dependencies perfectly satisfied!
2025-08-12 15:02:01,255 - app.new_score_oriented_agents - INFO - Applying user preferences to dependency-resolved order for Physics
2025-08-12 15:02:01,255 - app.new_score_oriented_agents - INFO - User preferences applied to 12 chapters while maintaining dependencies
2025-08-12 15:02:01,255 - app.new_score_oriented_agents - INFO - Perfect dependency sequence generated for Physics: 12 chapters
2025-08-12 15:02:01,255 - app.new_score_oriented_agents - INFO - Dependency-first ordering applied successfully
2025-08-12 15:02:01,255 - app.new_score_oriented_agents - INFO - Ensuring 100% coverage for all chapters
2025-08-12 15:02:01,255 - app.new_score_oriented_agents - INFO - Processing complete syllabus for Chemistry
2025-08-12 15:02:01,256 - app.tools - INFO - Fetching chapter flow for exam: JEE Mains, subject: Chemistry
2025-08-12 15:02:01,418 - app.tools - INFO - Fetching chapter weightage for exam: JEE Mains, subject: Chemistry
2025-08-12 15:02:01,505 - app.new_score_oriented_agents - INFO - Generating perfect dependency sequence for Chemistry
2025-08-12 15:02:01,506 - app.new_score_oriented_tools - INFO - Fetching chapter flow for exam: JEE Mains, subject: Chemistry
2025-08-12 15:02:01,585 - app.new_score_oriented_tools - INFO - Fetching chapter weightage for exam: JEE Mains, subject: Chemistry
2025-08-12 15:02:01,645 - app.new_score_oriented_tools - INFO - Starting enhanced dependency resolution for Chemistry
2025-08-12 15:02:01,646 - app.new_score_oriented_tools - INFO - Flow data: 12 chapters with dependencies
2025-08-12 15:02:01,646 - app.new_score_oriented_tools - INFO - Weightage data: 12 chapters with priorities
2025-08-12 15:02:01,646 - app.enhanced_dependency_resolver - INFO - Building comprehensive dependency graph from Chapter_Flow and Chapter_Weightage tables
2025-08-12 15:02:01,646 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_1]' for chapter 'Chapter_3' not found in chapter list
2025-08-12 15:02:01,647 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_2]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 15:02:01,647 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_3]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 15:02:01,647 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_4]' for chapter 'Chapter_7' not found in chapter list
2025-08-12 15:02:01,647 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_6]' for chapter 'Chapter_10' not found in chapter list
2025-08-12 15:02:01,647 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_5]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 15:02:01,647 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_7]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 15:02:01,647 - app.enhanced_dependency_resolver - INFO - Dependency graph built: 12 chapters, 7 dependencies
2025-08-12 15:02:01,648 - app.enhanced_dependency_resolver - INFO - Starting strict dependency resolution for Chemistry
2025-08-12 15:02:01,648 - app.enhanced_dependency_resolver - WARNING - Some chapters could not be resolved due to dependency cycles: {'Chapter_10', 'Chapter_7', 'Chapter_12', 'Chapter_5', 'Chapter_3'}
2025-08-12 15:02:01,648 - app.enhanced_dependency_resolver - INFO - Strict dependency resolution completed for Chemistry: 12 chapters
2025-08-12 15:02:01,648 - app.enhanced_dependency_resolver - INFO - Enhanced dependency resolution completed for Chemistry: 12 chapters with strict dependency ordering
2025-08-12 15:02:01,648 - app.new_score_oriented_tools - INFO - Enhanced dependency resolution for Chemistry:
2025-08-12 15:02:01,648 - app.new_score_oriented_tools - INFO -   Total chapters: 12
2025-08-12 15:02:01,648 - app.new_score_oriented_tools - INFO -   Chapters with dependencies: 5
2025-08-12 15:02:01,648 - app.new_score_oriented_tools - INFO -   All dependencies satisfied: True
2025-08-12 15:02:01,649 - app.new_score_oriented_tools - INFO - Final chapter order (dependencies first):
2025-08-12 15:02:01,649 - app.new_score_oriented_tools - INFO -    1. Chapter_8 (no dependencies) - Priority: 42.4
2025-08-12 15:02:01,649 - app.new_score_oriented_tools - INFO -    2. Chapter_1 (no dependencies) - Priority: 37.0
2025-08-12 15:02:01,649 - app.new_score_oriented_tools - INFO -    3. Chapter_4 (no dependencies) - Priority: 20.0
2025-08-12 15:02:01,649 - app.new_score_oriented_tools - INFO -    4. Chapter_9 (no dependencies) - Priority: 15.8
2025-08-12 15:02:01,649 - app.new_score_oriented_tools - INFO -    5. Chapter_11 (no dependencies) - Priority: 6.0
2025-08-12 15:02:01,649 - app.new_score_oriented_tools - INFO -    6. Chapter_6 (no dependencies) - Priority: 2.3
2025-08-12 15:02:01,649 - app.new_score_oriented_tools - INFO -    7. Chapter_2 (no dependencies) - Priority: 0.6
2025-08-12 15:02:01,649 - app.new_score_oriented_tools - INFO -    8. Chapter_10 (depends on: [Chapter_6]) - Priority: 45.1
2025-08-12 15:02:01,649 - app.new_score_oriented_tools - INFO -    9. Chapter_7 (depends on: [Chapter_4]) - Priority: 16.6
2025-08-12 15:02:01,649 - app.new_score_oriented_tools - INFO -   10. Chapter_12 (depends on: [Chapter_5], [Chapter_7]) - Priority: 3.1
2025-08-12 15:02:01,650 - app.new_score_oriented_tools - INFO -   11. Chapter_5 (depends on: [Chapter_2], [Chapter_3]) - Priority: 18.0
2025-08-12 15:02:01,650 - app.new_score_oriented_tools - INFO -   12. Chapter_3 (depends on: [Chapter_1]) - Priority: 33.9
2025-08-12 15:02:01,650 - app.new_score_oriented_tools - INFO - Critical path: [Chapter_6] → Chapter_10
2025-08-12 15:02:01,650 - app.new_score_oriented_tools - INFO - Optimization suggestions:
2025-08-12 15:02:01,650 - app.new_score_oriented_tools - INFO -   • Consider parallel study tracks for efficiency: 3 groups of independent chapters identified
2025-08-12 15:02:01,650 - app.new_score_oriented_tools - INFO - ✅ All dependencies perfectly satisfied!
2025-08-12 15:02:01,650 - app.new_score_oriented_agents - INFO - Applying user preferences to dependency-resolved order for Chemistry
2025-08-12 15:02:01,650 - app.new_score_oriented_agents - INFO - User preferences applied to 12 chapters while maintaining dependencies
2025-08-12 15:02:01,650 - app.new_score_oriented_agents - INFO - Perfect dependency sequence generated for Chemistry: 12 chapters
2025-08-12 15:02:01,650 - app.new_score_oriented_agents - INFO - Dependency-first ordering applied successfully
2025-08-12 15:02:01,651 - app.new_score_oriented_agents - INFO - Ensuring 100% coverage for all chapters
2025-08-12 15:02:01,651 - app.new_score_oriented_agents - INFO - Processing complete syllabus for Mathematics
2025-08-12 15:02:01,651 - app.tools - INFO - Fetching chapter flow for exam: JEE Mains, subject: Mathematics
2025-08-12 15:02:01,730 - app.tools - INFO - Fetching chapter weightage for exam: JEE Mains, subject: Mathematics
2025-08-12 15:02:01,812 - app.new_score_oriented_agents - INFO - Generating perfect dependency sequence for Mathematics
2025-08-12 15:02:01,813 - app.new_score_oriented_tools - INFO - Fetching chapter flow for exam: JEE Mains, subject: Mathematics
2025-08-12 15:02:01,879 - app.new_score_oriented_tools - INFO - Fetching chapter weightage for exam: JEE Mains, subject: Mathematics
2025-08-12 15:02:01,975 - app.new_score_oriented_tools - INFO - Starting enhanced dependency resolution for Mathematics
2025-08-12 15:02:01,976 - app.new_score_oriented_tools - INFO - Flow data: 12 chapters with dependencies
2025-08-12 15:02:01,977 - app.new_score_oriented_tools - INFO - Weightage data: 12 chapters with priorities
2025-08-12 15:02:01,977 - app.enhanced_dependency_resolver - INFO - Building comprehensive dependency graph from Chapter_Flow and Chapter_Weightage tables
2025-08-12 15:02:01,978 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_1]' for chapter 'Chapter_3' not found in chapter list
2025-08-12 15:02:01,978 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_2]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 15:02:01,979 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_3]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 15:02:01,979 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_4]' for chapter 'Chapter_7' not found in chapter list
2025-08-12 15:02:01,979 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_6]' for chapter 'Chapter_10' not found in chapter list
2025-08-12 15:02:01,980 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_5]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 15:02:01,980 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_7]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 15:02:01,981 - app.enhanced_dependency_resolver - INFO - Dependency graph built: 12 chapters, 7 dependencies
2025-08-12 15:02:01,981 - app.enhanced_dependency_resolver - INFO - Starting strict dependency resolution for Mathematics
2025-08-12 15:02:01,981 - app.enhanced_dependency_resolver - WARNING - Some chapters could not be resolved due to dependency cycles: {'Chapter_10', 'Chapter_7', 'Chapter_12', 'Chapter_5', 'Chapter_3'}
2025-08-12 15:02:01,982 - app.enhanced_dependency_resolver - INFO - Strict dependency resolution completed for Mathematics: 12 chapters
2025-08-12 15:02:01,983 - app.enhanced_dependency_resolver - INFO - Enhanced dependency resolution completed for Mathematics: 12 chapters with strict dependency ordering
2025-08-12 15:02:01,983 - app.new_score_oriented_tools - INFO - Enhanced dependency resolution for Mathematics:
2025-08-12 15:02:01,983 - app.new_score_oriented_tools - INFO -   Total chapters: 12
2025-08-12 15:02:01,984 - app.new_score_oriented_tools - INFO -   Chapters with dependencies: 5
2025-08-12 15:02:01,984 - app.new_score_oriented_tools - INFO -   All dependencies satisfied: True
2025-08-12 15:02:01,984 - app.new_score_oriented_tools - INFO - Final chapter order (dependencies first):
2025-08-12 15:02:01,985 - app.new_score_oriented_tools - INFO -    1. Chapter_2 (no dependencies) - Priority: 42.9
2025-08-12 15:02:01,985 - app.new_score_oriented_tools - INFO -    2. Chapter_1 (no dependencies) - Priority: 37.5
2025-08-12 15:02:01,985 - app.new_score_oriented_tools - INFO -    3. Chapter_8 (no dependencies) - Priority: 34.2
2025-08-12 15:02:01,986 - app.new_score_oriented_tools - INFO -    4. Chapter_6 (no dependencies) - Priority: 32.3
2025-08-12 15:02:01,986 - app.new_score_oriented_tools - INFO -    5. Chapter_11 (no dependencies) - Priority: 21.0
2025-08-12 15:02:01,986 - app.new_score_oriented_tools - INFO -    6. Chapter_4 (no dependencies) - Priority: 16.5
2025-08-12 15:02:01,986 - app.new_score_oriented_tools - INFO -    7. Chapter_9 (no dependencies) - Priority: 15.8
2025-08-12 15:02:01,987 - app.new_score_oriented_tools - INFO -    8. Chapter_10 (depends on: [Chapter_6]) - Priority: 5.0
2025-08-12 15:02:01,987 - app.new_score_oriented_tools - INFO -    9. Chapter_7 (depends on: [Chapter_4]) - Priority: 3.9
2025-08-12 15:02:01,987 - app.new_score_oriented_tools - INFO -   10. Chapter_12 (depends on: [Chapter_5], [Chapter_7]) - Priority: 2.1
2025-08-12 15:02:01,987 - app.new_score_oriented_tools - INFO -   11. Chapter_5 (depends on: [Chapter_2], [Chapter_3]) - Priority: 5.8
2025-08-12 15:02:01,987 - app.new_score_oriented_tools - INFO -   12. Chapter_3 (depends on: [Chapter_1]) - Priority: 12.6
2025-08-12 15:02:01,988 - app.new_score_oriented_tools - INFO - Critical path: [Chapter_6] → Chapter_10
2025-08-12 15:02:01,988 - app.new_score_oriented_tools - INFO - Optimization suggestions:
2025-08-12 15:02:01,988 - app.new_score_oriented_tools - INFO -   • Consider parallel study tracks for efficiency: 3 groups of independent chapters identified
2025-08-12 15:02:01,988 - app.new_score_oriented_tools - INFO - ✅ All dependencies perfectly satisfied!
2025-08-12 15:02:01,989 - app.new_score_oriented_agents - INFO - Applying user preferences to dependency-resolved order for Mathematics
2025-08-12 15:02:01,989 - app.new_score_oriented_agents - INFO - User preferences applied to 12 chapters while maintaining dependencies
2025-08-12 15:02:01,989 - app.new_score_oriented_agents - INFO - Perfect dependency sequence generated for Mathematics: 12 chapters
2025-08-12 15:02:01,989 - app.new_score_oriented_agents - INFO - Dependency-first ordering applied successfully
2025-08-12 15:02:01,989 - app.new_score_oriented_agents - INFO - Ensuring 100% coverage for all chapters
2025-08-12 15:02:01,990 - app.new_score_oriented_agents - INFO - Distributing syllabus across 6 months (total: 8)
2025-08-12 15:02:01,990 - app.new_score_oriented_agents - INFO - Starting enhanced features generation...
2025-08-12 15:02:01,990 - app.new_score_oriented_agents - INFO - Generating enhanced features for new_score_oriented plan
2025-08-12 15:02:01,990 - app.new_score_oriented_agents - INFO - Monthly chapters data prepared: ['month_1', 'month_2', 'month_3', 'month_4', 'month_5', 'month_6']
2025-08-12 15:02:01,990 - app.new_score_oriented_agents - INFO - Sample month data structure: {'physics': ['Chapter_9', 'Chapter_8'], 'chemistry': ['Chapter_8', 'Chapter_1'], 'mathematics': ['Chapter_2', 'Chapter_1']}
2025-08-12 15:02:01,991 - app.enhanced_new_score_oriented_tools - INFO - Calculating monthly target scores for user target: 230/300
2025-08-12 15:02:02,374 - app.enhanced_new_score_oriented_tools - INFO - month_1: Achievable=80.75, Target=61.91
2025-08-12 15:02:02,715 - app.enhanced_new_score_oriented_tools - INFO - month_2: Achievable=51.24, Target=39.28
2025-08-12 15:02:03,085 - app.enhanced_new_score_oriented_tools - INFO - month_3: Achievable=30.37, Target=23.28
2025-08-12 15:02:03,445 - app.enhanced_new_score_oriented_tools - INFO - month_4: Achievable=45.64, Target=34.99
2025-08-12 15:02:03,830 - app.enhanced_new_score_oriented_tools - INFO - month_5: Achievable=43.38, Target=33.26
2025-08-12 15:02:04,180 - app.enhanced_new_score_oriented_tools - INFO - month_6: Achievable=47.30, Target=36.26
2025-08-12 15:02:04,181 - app.enhanced_new_score_oriented_tools - INFO - Monthly target calculation completed: 6 months processed
2025-08-12 15:02:04,182 - app.enhanced_new_score_oriented_tools - INFO - Generating extended months plan: 8 total, 6 for syllabus
2025-08-12 15:02:04,182 - app.enhanced_new_score_oriented_tools - INFO - Extended months plan generated: 2 months of intensive practice
2025-08-12 15:02:04,183 - app.enhanced_new_score_oriented_tools - INFO - Generating weekly topic breakdown for 6 months
2025-08-12 15:02:06,288 - app.enhanced_new_score_oriented_tools - INFO - Weekly topic breakdown generated for 6 months
2025-08-12 15:02:06,290 - app.enhanced_new_score_oriented_tools - INFO - Creating comprehensive weekend schedule for 8 months
2025-08-12 15:02:06,290 - app.enhanced_new_score_oriented_tools - INFO - Comprehensive weekend schedule created for 8 months
2025-08-12 15:02:06,290 - app.new_score_oriented_agents - INFO - Enhanced features generated successfully
2025-08-12 15:02:06,290 - app.new_score_oriented_agents - INFO - Enhanced features generated: ['monthly_target_scores', 'extended_months_plan', 'weekly_topic_breakdown', 'weekend_schedule', 'strategy_summary']
2025-08-12 15:02:06,291 - app.new_score_oriented_agents - INFO - RevisionFlow plan generated with 6 months for syllabus completion
2025-08-12 15:02:06,291 - app.new_score_oriented_graph - INFO - Generator Validator Agent executing
2025-08-12 15:02:06,291 - app.new_score_oriented_agents - INFO - Validating chapter coverage for new_score_oriented plan
2025-08-12 15:02:06,292 - app.new_score_oriented_graph - INFO - Topic Agent executing
2025-08-12 15:02:06,292 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_9
2025-08-12 15:02:06,354 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_8
2025-08-12 15:02:06,410 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_11
2025-08-12 15:02:06,455 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_4
2025-08-12 15:02:06,514 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_6
2025-08-12 15:02:06,583 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_1
2025-08-12 15:02:06,647 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_10
2025-08-12 15:02:06,726 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_7
2025-08-12 15:02:06,783 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_2
2025-08-12 15:02:06,835 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_12
2025-08-12 15:02:06,883 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_5
2025-08-12 15:02:06,947 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_3
2025-08-12 15:02:07,001 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_8
2025-08-12 15:02:07,056 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_1
2025-08-12 15:02:07,117 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_4
2025-08-12 15:02:07,180 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_9
2025-08-12 15:02:07,255 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_11
2025-08-12 15:02:07,323 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_6
2025-08-12 15:02:07,385 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_2
2025-08-12 15:02:07,439 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_10
2025-08-12 15:02:07,496 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_7
2025-08-12 15:02:07,554 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_12
2025-08-12 15:02:07,626 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_5
2025-08-12 15:02:07,688 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_3
2025-08-12 15:02:07,757 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_2
2025-08-12 15:02:07,820 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_1
2025-08-12 15:02:07,888 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_8
2025-08-12 15:02:07,943 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_6
2025-08-12 15:02:07,995 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_11
2025-08-12 15:02:08,049 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_4
2025-08-12 15:02:08,108 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_9
2025-08-12 15:02:08,168 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_10
2025-08-12 15:02:08,225 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_7
2025-08-12 15:02:08,279 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_12
2025-08-12 15:02:08,346 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_5
2025-08-12 15:02:08,400 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_3
2025-08-12 15:02:08,450 - app.new_score_oriented_graph - INFO - Topic Validator Agent executing
2025-08-12 15:02:08,450 - app.new_score_oriented_agents - INFO - Validating topic coverage for new_score_oriented plan
2025-08-12 15:02:08,451 - app.tools - INFO - Fetching syllabus for exam: JEE Mains
2025-08-12 15:02:08,519 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_9
2025-08-12 15:02:08,590 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_8
2025-08-12 15:02:08,640 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_11
2025-08-12 15:02:08,690 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_4
2025-08-12 15:02:08,745 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_6
2025-08-12 15:02:08,812 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_1
2025-08-12 15:02:08,872 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_10
2025-08-12 15:02:08,928 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_7
2025-08-12 15:02:08,996 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_2
2025-08-12 15:02:09,049 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_12
2025-08-12 15:02:09,146 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_5
2025-08-12 15:02:09,222 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_3
2025-08-12 15:02:09,289 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_8
2025-08-12 15:02:09,348 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_1
2025-08-12 15:02:09,405 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_4
2025-08-12 15:02:09,469 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_9
2025-08-12 15:02:09,519 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_11
2025-08-12 15:02:09,573 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_6
2025-08-12 15:02:09,624 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_2
2025-08-12 15:02:09,673 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_10
2025-08-12 15:02:09,738 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_7
2025-08-12 15:02:09,790 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_12
2025-08-12 15:02:09,842 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_5
2025-08-12 15:02:09,899 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_3
2025-08-12 15:02:09,959 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_2
2025-08-12 15:02:10,023 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_1
2025-08-12 15:02:10,086 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_8
2025-08-12 15:02:10,140 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_6
2025-08-12 15:02:10,192 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_11
2025-08-12 15:02:10,250 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_4
2025-08-12 15:02:10,300 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_9
2025-08-12 15:02:10,359 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_10
2025-08-12 15:02:10,415 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_7
2025-08-12 15:02:10,475 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_12
2025-08-12 15:02:10,551 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_5
2025-08-12 15:02:10,607 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_3
2025-08-12 15:02:10,674 - app.new_score_oriented_agents - INFO - Performing final syllabus compliance validation
2025-08-12 15:02:10,675 - app.new_score_oriented_graph - INFO - Supervisor Agent executing
2025-08-12 15:02:10,675 - app.new_score_oriented_agents - INFO - Supervising new_score_oriented plan for target achievement
2025-08-12 15:02:10,676 - app.new_score_oriented_graph - INFO - Finalizing new_score_oriented study plan with enhanced calendar features

================================================================================
🎯 NEW SCORE-ORIENTED STUDY PLAN - DETAILED BREAKDOWN
================================================================================
2025-08-12 to 2026-04-09 | Target: 230/300

8
Months
132
Study Days
64
PYQ Days
64
Weekend Sessions
396
DPP Sessions

📊 MONTHLY TARGET BREAKDOWN:
--------------------------------------------------

Month 1
76.7% of target
80.8
Total Achievable Score
61.9
Your Target Score
Efficiency Required
76.7%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_9', 'Chapter_8'], 'subject_weightage': 27.51, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_8', 'Chapter_1'], 'subject_weightage': 26.46, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_2', 'Chapter_1'], 'subject_weightage': 26.78, 'chapter_count': 2}

Month 2
76.7% of target
51.2
Total Achievable Score
39.3
Your Target Score
Efficiency Required
76.7%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_11', 'Chapter_4'], 'subject_weightage': 11.15, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_4', 'Chapter_9'], 'subject_weightage': 17.91, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_8', 'Chapter_6'], 'subject_weightage': 22.18, 'chapter_count': 2}

Month 3
76.7% of target
30.4
Total Achievable Score
23.3
Your Target Score
Efficiency Required
76.7%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_6', 'Chapter_1'], 'subject_weightage': 3.26, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_11', 'Chapter_6'], 'subject_weightage': 8.36, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_11', 'Chapter_4'], 'subject_weightage': 18.75, 'chapter_count': 2}

Month 4
76.7% of target
45.6
Total Achievable Score
35.0
Your Target Score
Efficiency Required
76.7%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_10', 'Chapter_7'], 'subject_weightage': 17.19, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_2', 'Chapter_10'], 'subject_weightage': 15.59, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_9', 'Chapter_10'], 'subject_weightage': 12.86, 'chapter_count': 2}

Month 5
76.7% of target
43.4
Total Achievable Score
33.3
Your Target Score
Efficiency Required
76.7%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_2', 'Chapter_12'], 'subject_weightage': 25.96, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_7', 'Chapter_12'], 'subject_weightage': 11.38, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_7', 'Chapter_12'], 'subject_weightage': 6.04, 'chapter_count': 2}

Month 6
76.7% of target
47.3
Total Achievable Score
36.3
Your Target Score
Efficiency Required
76.7%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_5', 'Chapter_3'], 'subject_weightage': 14.92, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_5', 'Chapter_3'], 'subject_weightage': 20.28, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_5', 'Chapter_3'], 'subject_weightage': 12.1, 'chapter_count': 2}

Weekly Breakdown
--------------------------------------------------

--- Month 1 Weekly Breakdown ---

mathematics
Chapter_2
  Topic_2
  Topic_4
  Topic_6
  Topic_7
  Topic_8
  Topic_10
  Topic_11
  Topic_1
  Topic_3
  Topic_5
  Topic_9
11 topics
Chapter_1
  Topic_6
  Topic_2
  Topic_4
  Topic_1
  Topic_3
  Topic_5
  Topic_7
7 topics

physics
Chapter_9
  Topic_1
  Topic_3
  Topic_4
  Topic_2
  Topic_5
  Topic_6
  Topic_7
  Topic_8
8 topics
Chapter_8
  Topic_1
  Topic_10
  Topic_11
  Topic_12
  Topic_13
  Topic_2
  Topic_3
  Topic_4
  Topic_5
  Topic_6
  Topic_7
  Topic_8
  Topic_9
13 topics

chemistry
Chapter_8
  Topic_1
  Topic_5
  Topic_7
  Topic_8
  Topic_9
  Topic_10
  Topic_6
  Topic_11
  Topic_12
  Topic_2
  Topic_3
  Topic_4
  Topic_13
13 topics
Chapter_1
  Topic_3
  Topic_5
  Topic_6
  Topic_1
  Topic_2
  Topic_4
  Topic_7
7 topics

--- Month 2 Weekly Breakdown ---

mathematics
Chapter_8
  Topic_2
  Topic_4
  Topic_5
  Topic_7
  Topic_8
  Topic_11
  Topic_12
  Topic_13
  Topic_9
  Topic_1
  Topic_3
  Topic_6
  Topic_10
13 topics
Chapter_6
  Topic_2
  Topic_3
  Topic_4
  Topic_1
4 topics

physics
Chapter_11
  Topic_2
  Topic_5
  Topic_7
  Topic_1
  Topic_6
  Topic_3
  Topic_4
7 topics
Chapter_4
  Topic_1
  Topic_4
  Topic_2
  Topic_5
  Topic_6
  Topic_3
6 topics

chemistry
Chapter_4
  Topic_2
  Topic_3
  Topic_5
  Topic_4
  Topic_6
  Topic_1
6 topics
Chapter_9
  Topic_8
  Topic_1
  Topic_2
  Topic_3
  Topic_4
  Topic_5
  Topic_6
  Topic_7
8 topics

--- Month 3 Weekly Breakdown ---

mathematics
Chapter_11
  Topic_7
  Topic_1
  Topic_6
  Topic_2
  Topic_3
  Topic_4
  Topic_5
7 topics
Chapter_4
  Topic_3
  Topic_5
  Topic_6
  Topic_1
  Topic_2
  Topic_4
6 topics

physics
Chapter_6
  Topic_1
  Topic_2
  Topic_3
  Topic_4
4 topics
Chapter_1
  Topic_2
  Topic_3
  Topic_5
  Topic_6
  Topic_1
  Topic_7
  Topic_4
7 topics

chemistry
Chapter_11
  Topic_6
  Topic_2
  Topic_7
  Topic_1
  Topic_3
  Topic_4
  Topic_5
7 topics
Chapter_6
  Topic_1
  Topic_4
  Topic_2
  Topic_3
4 topics

--- Month 4 Weekly Breakdown ---

mathematics
Chapter_9
  Topic_2
  Topic_4
  Topic_1
  Topic_3
  Topic_7
  Topic_5
  Topic_6
  Topic_8
8 topics
Chapter_10
  Topic_7
  Topic_9
  Topic_11
  Topic_12
  Topic_16
  Topic_2
  Topic_8
  Topic_10
  Topic_14
  Topic_15
  Topic_1
  Topic_3
  Topic_4
  Topic_5
  Topic_6
  Topic_13
16 topics

physics
Chapter_10
  Topic_3
  Topic_4
  Topic_5
  Topic_6
  Topic_7
  Topic_9
  Topic_12
  Topic_16
  Topic_2
  Topic_8
  Topic_10
  Topic_11
  Topic_15
  Topic_1
  Topic_13
  Topic_14
16 topics
Chapter_7
  Topic_1
  Topic_3
  Topic_5
  Topic_8
  Topic_10
  Topic_2
  Topic_6
  Topic_9
  Topic_4
  Topic_7
  Topic_11
11 topics

chemistry
Chapter_2
  Topic_1
  Topic_2
  Topic_5
  Topic_7
  Topic_9
  Topic_11
  Topic_3
  Topic_6
  Topic_10
  Topic_4
  Topic_8
11 topics
Chapter_10
  Topic_2
  Topic_4
  Topic_5
  Topic_10
  Topic_13
  Topic_15
  Topic_7
  Topic_9
  Topic_11
  Topic_12
  Topic_14
  Topic_16
  Topic_1
  Topic_3
  Topic_6
  Topic_8
16 topics

--- Month 5 Weekly Breakdown ---

mathematics
Chapter_7
  Topic_2
  Topic_4
  Topic_6
  Topic_10
  Topic_3
  Topic_7
  Topic_8
  Topic_9
  Topic_11
  Topic_1
  Topic_5
11 topics
Chapter_12
  Topic_1
  Topic_3
  Topic_11
  Topic_2
  Topic_6
  Topic_7
  Topic_8
  Topic_12
  Topic_4
  Topic_5
  Topic_9
  Topic_10
12 topics

physics
Chapter_2
  Topic_3
  Topic_9
  Topic_1
  Topic_2
  Topic_4
  Topic_5
  Topic_7
  Topic_8
  Topic_6
  Topic_10
  Topic_11
11 topics
Chapter_12
  Topic_1
  Topic_2
  Topic_4
  Topic_7
  Topic_12
  Topic_3
  Topic_5
  Topic_6
  Topic_10
  Topic_11
  Topic_8
  Topic_9
12 topics

chemistry
Chapter_7
  Topic_3
  Topic_5
  Topic_2
  Topic_4
  Topic_8
  Topic_1
  Topic_6
  Topic_7
  Topic_9
  Topic_10
  Topic_11
11 topics
Chapter_12
  Topic_1
  Topic_5
  Topic_7
  Topic_4
  Topic_6
  Topic_8
  Topic_9
  Topic_10
  Topic_11
  Topic_12
  Topic_2
  Topic_3
12 topics

--- Month 6 Weekly Breakdown ---

mathematics
Chapter_5
  Topic_2
  Topic_7
  Topic_1
  Topic_3
  Topic_4
  Topic_5
  Topic_6
7 topics
Chapter_3
  Topic_8
  Topic_1
  Topic_2
  Topic_6
  Topic_3
  Topic_4
  Topic_5
  Topic_7
8 topics

physics
Chapter_5
  Topic_4
  Topic_6
  Topic_7
  Topic_3
  Topic_5
  Topic_1
  Topic_2
7 topics
Chapter_3
  Topic_3
  Topic_4
  Topic_5
  Topic_6
  Topic_1
  Topic_2
  Topic_7
  Topic_8
8 topics

chemistry
Chapter_5
  Topic_1
  Topic_2
  Topic_5
  Topic_6
  Topic_3
  Topic_4
  Topic_7
7 topics
Chapter_3
  Topic_7
  Topic_8
  Topic_3
  Topic_1
  Topic_2
  Topic_4
  Topic_5
  Topic_6
8 topics

================================================================================
📋 JSON OUTPUT:
================================================================================
{
  "plan_info": {
    "start_date": "2025-08-12",
    "end_date": "2026-04-09",
    "target_score": "230/300",
    "total_months": 8,
    "syllabus_completion_months": 6,
    "study_days": 132,
    "pyq_days": 64,
    "weekend_sessions": 64,
    "dpp_sessions": 396,
    "Full_month_revision": 2
  },
  "monthly_breakdown": {
    "Month 1": {
      "target_ratio": "76.7% of target",
      "total_achievable_score": 80.75,
      "user_target_score": 61.91,
      "efficiency_required": "76.7%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_9",
            "Chapter_8"
          ],
          "subject_weightage": 27.51,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_8",
            "Chapter_1"
          ],
          "subject_weightage": 26.46,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_2",
            "Chapter_1"
          ],
          "subject_weightage": 26.78,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 2": {
      "target_ratio": "76.7% of target",
      "total_achievable_score": 51.24,
      "user_target_score": 39.28,
      "efficiency_required": "76.7%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_11",
            "Chapter_4"
          ],
          "subject_weightage": 11.15,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_4",
            "Chapter_9"
          ],
          "subject_weightage": 17.91,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_8",
            "Chapter_6"
          ],
          "subject_weightage": 22.18,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 3": {
      "target_ratio": "76.7% of target",
      "total_achievable_score": 30.37,
      "user_target_score": 23.28,
      "efficiency_required": "76.7%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_6",
            "Chapter_1"
          ],
          "subject_weightage": 3.26,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_11",
            "Chapter_6"
          ],
          "subject_weightage": 8.36,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_11",
            "Chapter_4"
          ],
          "subject_weightage": 18.75,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 4": {
      "target_ratio": "76.7% of target",
      "total_achievable_score": 45.64,
      "user_target_score": 34.99,
      "efficiency_required": "76.7%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_10",
            "Chapter_7"
          ],
          "subject_weightage": 17.19,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_2",
            "Chapter_10"
          ],
          "subject_weightage": 15.59,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_9",
            "Chapter_10"
          ],
          "subject_weightage": 12.86,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 5": {
      "target_ratio": "76.7% of target",
      "total_achievable_score": 43.38,
      "user_target_score": 33.26,
      "efficiency_required": "76.7%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_2",
            "Chapter_12"
          ],
          "subject_weightage": 25.96,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_7",
            "Chapter_12"
          ],
          "subject_weightage": 11.38,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_7",
            "Chapter_12"
          ],
          "subject_weightage": 6.04,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 6": {
      "target_ratio": "76.7% of target",
      "total_achievable_score": 47.3,
      "user_target_score": 36.26,
      "efficiency_required": "76.7%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_5",
            "Chapter_3"
          ],
          "subject_weightage": 14.92,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_5",
            "Chapter_3"
          ],
          "subject_weightage": 20.28,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_5",
            "Chapter_3"
          ],
          "subject_weightage": 12.1,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 7": {
      "Total_PYQs_in_this_Month": 50
    },
    "Month 8": {
      "Total_PYQs_in_this_Month": 60
    }
  },
  "chapter_breakdown": {
    "month_1": {
      "mathematics": [
        "Chapter_2",
        "Chapter_1"
      ],
      "physics": [
        "Chapter_9",
        "Chapter_8"
      ],
      "chemistry": [
        "Chapter_8",
        "Chapter_1"
      ]
    },
    "month_2": {
      "mathematics": [
        "Chapter_8",
        "Chapter_6"
      ],
      "physics": [
        "Chapter_11",
        "Chapter_4"
      ],
      "chemistry": [
        "Chapter_4",
        "Chapter_9"
      ]
    },
    "month_3": {
      "mathematics": [
        "Chapter_11",
        "Chapter_4"
      ],
      "physics": [
        "Chapter_6",
        "Chapter_1"
      ],
      "chemistry": [
        "Chapter_11",
        "Chapter_6"
      ]
    },
    "month_4": {
      "mathematics": [
        "Chapter_9",
        "Chapter_10"
      ],
      "physics": [
        "Chapter_10",
        "Chapter_7"
      ],
      "chemistry": [
        "Chapter_2",
        "Chapter_10"
      ]
    },
    "month_5": {
      "mathematics": [
        "Chapter_7",
        "Chapter_12"
      ],
      "physics": [
        "Chapter_2",
        "Chapter_12"
      ],
      "chemistry": [
        "Chapter_7",
        "Chapter_12"
      ]
    },
    "month_6": {
      "mathematics": [
        "Chapter_5",
        "Chapter_3"
      ],
      "physics": [
        "Chapter_5",
        "Chapter_3"
      ],
      "chemistry": [
        "Chapter_5",
        "Chapter_3"
      ]
    }
  },
  "weekly_breakdown": {
    "month_1": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_2": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_9"
              ],
              "Chapter_1": [
                "Topic_6",
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          },
          "physics": {
            "chapters": {
              "Chapter_9": [
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_8": [
                "Topic_1",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 21
          },
          "chemistry": {
            "chapters": {
              "Chapter_8": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_6",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_13"
              ],
              "Chapter_1": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_2": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_9"
              ],
              "Chapter_1": [
                "Topic_6",
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          },
          "physics": {
            "chapters": {
              "Chapter_9": [
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_8": [
                "Topic_1",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 21
          },
          "chemistry": {
            "chapters": {
              "Chapter_8": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_6",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_13"
              ],
              "Chapter_1": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_2": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_9"
              ],
              "Chapter_1": [
                "Topic_6",
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          },
          "physics": {
            "chapters": {
              "Chapter_9": [
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_8": [
                "Topic_1",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 21
          },
          "chemistry": {
            "chapters": {
              "Chapter_8": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_6",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_13"
              ],
              "Chapter_1": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_2": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_9"
              ],
              "Chapter_1": [
                "Topic_6",
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          },
          "physics": {
            "chapters": {
              "Chapter_9": [
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_8": [
                "Topic_1",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 21
          },
          "chemistry": {
            "chapters": {
              "Chapter_8": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_6",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_13"
              ],
              "Chapter_1": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          }
        }
      }
    },
    "month_2": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_8": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_9",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_10"
              ],
              "Chapter_6": [
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_1"
              ]
            },
            "total_topic_count": 17
          },
          "physics": {
            "chapters": {
              "Chapter_11": [
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_4": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3"
              ]
            },
            "total_topic_count": 13
          },
          "chemistry": {
            "chapters": {
              "Chapter_4": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_4",
                "Topic_6",
                "Topic_1"
              ],
              "Chapter_9": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7"
              ]
            },
            "total_topic_count": 14
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_8": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_9",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_10"
              ],
              "Chapter_6": [
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_1"
              ]
            },
            "total_topic_count": 17
          },
          "physics": {
            "chapters": {
              "Chapter_11": [
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_4": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3"
              ]
            },
            "total_topic_count": 13
          },
          "chemistry": {
            "chapters": {
              "Chapter_4": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_4",
                "Topic_6",
                "Topic_1"
              ],
              "Chapter_9": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7"
              ]
            },
            "total_topic_count": 14
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_8": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_9",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_10"
              ],
              "Chapter_6": [
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_1"
              ]
            },
            "total_topic_count": 17
          },
          "physics": {
            "chapters": {
              "Chapter_11": [
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_4": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3"
              ]
            },
            "total_topic_count": 13
          },
          "chemistry": {
            "chapters": {
              "Chapter_4": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_4",
                "Topic_6",
                "Topic_1"
              ],
              "Chapter_9": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7"
              ]
            },
            "total_topic_count": 14
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_8": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_9",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_10"
              ],
              "Chapter_6": [
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_1"
              ]
            },
            "total_topic_count": 17
          },
          "physics": {
            "chapters": {
              "Chapter_11": [
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_4": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3"
              ]
            },
            "total_topic_count": 13
          },
          "chemistry": {
            "chapters": {
              "Chapter_4": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_4",
                "Topic_6",
                "Topic_1"
              ],
              "Chapter_9": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7"
              ]
            },
            "total_topic_count": 14
          }
        }
      }
    },
    "month_3": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_11": [
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_4": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4"
              ]
            },
            "total_topic_count": 13
          },
          "physics": {
            "chapters": {
              "Chapter_6": [
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_1": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_7",
                "Topic_4"
              ]
            },
            "total_topic_count": 11
          },
          "chemistry": {
            "chapters": {
              "Chapter_11": [
                "Topic_6",
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_6": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 11
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_11": [
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_4": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4"
              ]
            },
            "total_topic_count": 13
          },
          "physics": {
            "chapters": {
              "Chapter_6": [
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_1": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_7",
                "Topic_4"
              ]
            },
            "total_topic_count": 11
          },
          "chemistry": {
            "chapters": {
              "Chapter_11": [
                "Topic_6",
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_6": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 11
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_11": [
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_4": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4"
              ]
            },
            "total_topic_count": 13
          },
          "physics": {
            "chapters": {
              "Chapter_6": [
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_1": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_7",
                "Topic_4"
              ]
            },
            "total_topic_count": 11
          },
          "chemistry": {
            "chapters": {
              "Chapter_11": [
                "Topic_6",
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_6": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 11
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_11": [
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_4": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4"
              ]
            },
            "total_topic_count": 13
          },
          "physics": {
            "chapters": {
              "Chapter_6": [
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_1": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_7",
                "Topic_4"
              ]
            },
            "total_topic_count": 11
          },
          "chemistry": {
            "chapters": {
              "Chapter_11": [
                "Topic_6",
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_6": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 11
          }
        }
      }
    },
    "month_4": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_9": [
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_7",
                "Topic_5",
                "Topic_6",
                "Topic_8"
              ],
              "Chapter_10": [
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_14",
                "Topic_15",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_13"
              ]
            },
            "total_topic_count": 24
          },
          "physics": {
            "chapters": {
              "Chapter_10": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_15",
                "Topic_1",
                "Topic_13",
                "Topic_14"
              ],
              "Chapter_7": [
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_8",
                "Topic_10",
                "Topic_2",
                "Topic_6",
                "Topic_9",
                "Topic_4",
                "Topic_7",
                "Topic_11"
              ]
            },
            "total_topic_count": 27
          },
          "chemistry": {
            "chapters": {
              "Chapter_2": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_3",
                "Topic_6",
                "Topic_10",
                "Topic_4",
                "Topic_8"
              ],
              "Chapter_10": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_10",
                "Topic_13",
                "Topic_15",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_14",
                "Topic_16",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_8"
              ]
            },
            "total_topic_count": 27
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_9": [
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_7",
                "Topic_5",
                "Topic_6",
                "Topic_8"
              ],
              "Chapter_10": [
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_14",
                "Topic_15",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_13"
              ]
            },
            "total_topic_count": 24
          },
          "physics": {
            "chapters": {
              "Chapter_10": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_15",
                "Topic_1",
                "Topic_13",
                "Topic_14"
              ],
              "Chapter_7": [
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_8",
                "Topic_10",
                "Topic_2",
                "Topic_6",
                "Topic_9",
                "Topic_4",
                "Topic_7",
                "Topic_11"
              ]
            },
            "total_topic_count": 27
          },
          "chemistry": {
            "chapters": {
              "Chapter_2": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_3",
                "Topic_6",
                "Topic_10",
                "Topic_4",
                "Topic_8"
              ],
              "Chapter_10": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_10",
                "Topic_13",
                "Topic_15",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_14",
                "Topic_16",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_8"
              ]
            },
            "total_topic_count": 27
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_9": [
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_7",
                "Topic_5",
                "Topic_6",
                "Topic_8"
              ],
              "Chapter_10": [
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_14",
                "Topic_15",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_13"
              ]
            },
            "total_topic_count": 24
          },
          "physics": {
            "chapters": {
              "Chapter_10": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_15",
                "Topic_1",
                "Topic_13",
                "Topic_14"
              ],
              "Chapter_7": [
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_8",
                "Topic_10",
                "Topic_2",
                "Topic_6",
                "Topic_9",
                "Topic_4",
                "Topic_7",
                "Topic_11"
              ]
            },
            "total_topic_count": 27
          },
          "chemistry": {
            "chapters": {
              "Chapter_2": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_3",
                "Topic_6",
                "Topic_10",
                "Topic_4",
                "Topic_8"
              ],
              "Chapter_10": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_10",
                "Topic_13",
                "Topic_15",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_14",
                "Topic_16",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_8"
              ]
            },
            "total_topic_count": 27
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_9": [
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_7",
                "Topic_5",
                "Topic_6",
                "Topic_8"
              ],
              "Chapter_10": [
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_14",
                "Topic_15",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_13"
              ]
            },
            "total_topic_count": 24
          },
          "physics": {
            "chapters": {
              "Chapter_10": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_15",
                "Topic_1",
                "Topic_13",
                "Topic_14"
              ],
              "Chapter_7": [
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_8",
                "Topic_10",
                "Topic_2",
                "Topic_6",
                "Topic_9",
                "Topic_4",
                "Topic_7",
                "Topic_11"
              ]
            },
            "total_topic_count": 27
          },
          "chemistry": {
            "chapters": {
              "Chapter_2": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_3",
                "Topic_6",
                "Topic_10",
                "Topic_4",
                "Topic_8"
              ],
              "Chapter_10": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_10",
                "Topic_13",
                "Topic_15",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_14",
                "Topic_16",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_8"
              ]
            },
            "total_topic_count": 27
          }
        }
      }
    },
    "month_5": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_7": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_10",
                "Topic_3",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_11",
                "Topic_1",
                "Topic_5"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_3",
                "Topic_11",
                "Topic_2",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_12",
                "Topic_4",
                "Topic_5",
                "Topic_9",
                "Topic_10"
              ]
            },
            "total_topic_count": 23
          },
          "physics": {
            "chapters": {
              "Chapter_2": [
                "Topic_3",
                "Topic_9",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_6",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7",
                "Topic_12",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_10",
                "Topic_11",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 23
          },
          "chemistry": {
            "chapters": {
              "Chapter_7": [
                "Topic_3",
                "Topic_5",
                "Topic_2",
                "Topic_4",
                "Topic_8",
                "Topic_1",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_4",
                "Topic_6",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 23
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_7": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_10",
                "Topic_3",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_11",
                "Topic_1",
                "Topic_5"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_3",
                "Topic_11",
                "Topic_2",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_12",
                "Topic_4",
                "Topic_5",
                "Topic_9",
                "Topic_10"
              ]
            },
            "total_topic_count": 23
          },
          "physics": {
            "chapters": {
              "Chapter_2": [
                "Topic_3",
                "Topic_9",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_6",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7",
                "Topic_12",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_10",
                "Topic_11",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 23
          },
          "chemistry": {
            "chapters": {
              "Chapter_7": [
                "Topic_3",
                "Topic_5",
                "Topic_2",
                "Topic_4",
                "Topic_8",
                "Topic_1",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_4",
                "Topic_6",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 23
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_7": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_10",
                "Topic_3",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_11",
                "Topic_1",
                "Topic_5"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_3",
                "Topic_11",
                "Topic_2",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_12",
                "Topic_4",
                "Topic_5",
                "Topic_9",
                "Topic_10"
              ]
            },
            "total_topic_count": 23
          },
          "physics": {
            "chapters": {
              "Chapter_2": [
                "Topic_3",
                "Topic_9",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_6",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7",
                "Topic_12",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_10",
                "Topic_11",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 23
          },
          "chemistry": {
            "chapters": {
              "Chapter_7": [
                "Topic_3",
                "Topic_5",
                "Topic_2",
                "Topic_4",
                "Topic_8",
                "Topic_1",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_4",
                "Topic_6",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 23
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_7": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_10",
                "Topic_3",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_11",
                "Topic_1",
                "Topic_5"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_3",
                "Topic_11",
                "Topic_2",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_12",
                "Topic_4",
                "Topic_5",
                "Topic_9",
                "Topic_10"
              ]
            },
            "total_topic_count": 23
          },
          "physics": {
            "chapters": {
              "Chapter_2": [
                "Topic_3",
                "Topic_9",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_6",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7",
                "Topic_12",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_10",
                "Topic_11",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 23
          },
          "chemistry": {
            "chapters": {
              "Chapter_7": [
                "Topic_3",
                "Topic_5",
                "Topic_2",
                "Topic_4",
                "Topic_8",
                "Topic_1",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_4",
                "Topic_6",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 23
          }
        }
      }
    },
    "month_6": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_5": [
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ],
              "Chapter_3": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 15
          },
          "physics": {
            "chapters": {
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ],
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
              ]
            },
            "total_topic_count": 15
          },
          "chemistry": {
            "chapters": {
              "Chapter_5": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_7"
              ],
              "Chapter_3": [
                "Topic_7",
                "Topic_8",
                "Topic_3",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 15
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_5": [
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ],
              "Chapter_3": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 15
          },
          "physics": {
            "chapters": {
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ],
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
              ]
            },
            "total_topic_count": 15
          },
          "chemistry": {
            "chapters": {
              "Chapter_5": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_7"
              ],
              "Chapter_3": [
                "Topic_7",
                "Topic_8",
                "Topic_3",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 15
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_5": [
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ],
              "Chapter_3": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 15
          },
          "physics": {
            "chapters": {
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ],
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
              ]
            },
            "total_topic_count": 15
          },
          "chemistry": {
            "chapters": {
              "Chapter_5": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_7"
              ],
              "Chapter_3": [
                "Topic_7",
                "Topic_8",
                "Topic_3",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 15
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_5": [
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ],
              "Chapter_3": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 15
          },
          "physics": {
            "chapters": {
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ],
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
              ]
            },
            "total_topic_count": 15
          },
          "chemistry": {
            "chapters": {
              "Chapter_5": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_7"
              ],
              "Chapter_3": [
                "Topic_7",
                "Topic_8",
                "Topic_3",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 15
          }
        }
      }
    }
  }
}

================================================================================
✅ NEW SCORE-ORIENTED PLAN DISPLAY COMPLETE
================================================================================

2025-08-12 15:02:10,732 - app.new_score_oriented_graph - INFO - New Score-Oriented Feedback Counsellor executing
2025-08-12 15:02:10,732 - app.new_score_oriented_graph - INFO - Processing user message: generate
2025-08-12 15:02:10,732 - app.new_score_oriented_graph - INFO - New Score-Oriented Feedback Counsellor Continue executing
2025-08-12 15:02:10,732 - app.new_score_oriented_graph - INFO - Feedback processed, finalizing plan
=== NEW SCORE ORIENTED PLAN DEBUG ===
Plan keys: ['user_id', 'target_score', 'exam_date', 'total_months', 'syllabus_completion_months', 'practice_months', 'monthly_plans', 'revision_flow_results', 'overall_strategy', 'dependency_analysis', 'coverage_validation', 'target_achievement_probability', 'enhanced_features', 'calendar_plan', 'monthly_targets_data', 'extended_months_plan', 'weekend_schedule', 'weekly_topic_breakdown', 'user_target_score', 'start_date', 'end_date', 'overall_summary']
Plan type: <class 'dict'>
Plan content preview: {'user_id': 'user_igha5v6vx', 'target_score': 230, 'exam_date': '2026-04-12', 'total_months': 8, 'syllabus_completion_months': 6, 'practice_months': 2, 'monthly_plans': [], 'revision_flow_results': {'physics': {'chapters': [{'chapter': 'Chapter_9', 'weightage': 14.77, 'category': 'High', 'coverage_percentage': 1.0, 'priority_reason': 'dependency_optimized', 'dependencies_satisfied': True, 'completion_order': 1, 'dependency_level': 0, 'dependencies': [], 'coverage_reason': 'complete_syllabus_cove...
=====================================
=== STUDY PLAN RESPONSE DEBUG ===
Response keys: ['insights', 'monthly_plan', 'weekly_plan', 'new_score_oriented_data']
Monthly plan keys: ['Month 1', 'Month 2', 'Month 3', 'Month 4', 'Month 5', 'Month 6']
====================================

================================================================================
🎯 NEW SCORE-ORIENTED STUDY PLAN - DETAILED BREAKDOWN
================================================================================
2025-08-12 to 2026-04-09 | Target: 230/300

8
Months
132
Study Days
64
PYQ Days
64
Weekend Sessions
396
DPP Sessions

📊 MONTHLY TARGET BREAKDOWN:
--------------------------------------------------

Month 1
76.7% of target
80.8
Total Achievable Score
61.9
Your Target Score
Efficiency Required
76.7%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_9', 'Chapter_8'], 'subject_weightage': 27.51, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_8', 'Chapter_1'], 'subject_weightage': 26.46, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_2', 'Chapter_1'], 'subject_weightage': 26.78, 'chapter_count': 2}

Month 2
76.7% of target
51.2
Total Achievable Score
39.3
Your Target Score
Efficiency Required
76.7%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_11', 'Chapter_4'], 'subject_weightage': 11.15, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_4', 'Chapter_9'], 'subject_weightage': 17.91, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_8', 'Chapter_6'], 'subject_weightage': 22.18, 'chapter_count': 2}

Month 3
76.7% of target
30.4
Total Achievable Score
23.3
Your Target Score
Efficiency Required
76.7%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_6', 'Chapter_1'], 'subject_weightage': 3.26, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_11', 'Chapter_6'], 'subject_weightage': 8.36, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_11', 'Chapter_4'], 'subject_weightage': 18.75, 'chapter_count': 2}

Month 4
76.7% of target
45.6
Total Achievable Score
35.0
Your Target Score
Efficiency Required
76.7%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_10', 'Chapter_7'], 'subject_weightage': 17.19, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_2', 'Chapter_10'], 'subject_weightage': 15.59, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_9', 'Chapter_10'], 'subject_weightage': 12.86, 'chapter_count': 2}

Month 5
76.7% of target
43.4
Total Achievable Score
33.3
Your Target Score
Efficiency Required
76.7%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_2', 'Chapter_12'], 'subject_weightage': 25.96, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_7', 'Chapter_12'], 'subject_weightage': 11.38, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_7', 'Chapter_12'], 'subject_weightage': 6.04, 'chapter_count': 2}

Month 6
76.7% of target
47.3
Total Achievable Score
36.3
Your Target Score
Efficiency Required
76.7%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_5', 'Chapter_3'], 'subject_weightage': 14.92, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_5', 'Chapter_3'], 'subject_weightage': 20.28, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_5', 'Chapter_3'], 'subject_weightage': 12.1, 'chapter_count': 2}

Weekly Breakdown
--------------------------------------------------

--- Month 1 Weekly Breakdown ---

mathematics
Chapter_2
  Topic_2
  Topic_4
  Topic_6
  Topic_7
  Topic_8
  Topic_10
  Topic_11
  Topic_1
  Topic_3
  Topic_5
  Topic_9
11 topics
Chapter_1
  Topic_6
  Topic_2
  Topic_4
  Topic_1
  Topic_3
  Topic_5
  Topic_7
7 topics

physics
Chapter_9
  Topic_1
  Topic_3
  Topic_4
  Topic_2
  Topic_5
  Topic_6
  Topic_7
  Topic_8
8 topics
Chapter_8
  Topic_1
  Topic_10
  Topic_11
  Topic_12
  Topic_13
  Topic_2
  Topic_3
  Topic_4
  Topic_5
  Topic_6
  Topic_7
  Topic_8
  Topic_9
13 topics

chemistry
Chapter_8
  Topic_1
  Topic_5
  Topic_7
  Topic_8
  Topic_9
  Topic_10
  Topic_6
  Topic_11
  Topic_12
  Topic_2
  Topic_3
  Topic_4
  Topic_13
13 topics
Chapter_1
  Topic_3
  Topic_5
  Topic_6
  Topic_1
  Topic_2
  Topic_4
  Topic_7
7 topics

--- Month 2 Weekly Breakdown ---

mathematics
Chapter_8
  Topic_2
  Topic_4
  Topic_5
  Topic_7
  Topic_8
  Topic_11
  Topic_12
  Topic_13
  Topic_9
  Topic_1
  Topic_3
  Topic_6
  Topic_10
13 topics
Chapter_6
  Topic_2
  Topic_3
  Topic_4
  Topic_1
4 topics

physics
Chapter_11
  Topic_2
  Topic_5
  Topic_7
  Topic_1
  Topic_6
  Topic_3
  Topic_4
7 topics
Chapter_4
  Topic_1
  Topic_4
  Topic_2
  Topic_5
  Topic_6
  Topic_3
6 topics

chemistry
Chapter_4
  Topic_2
  Topic_3
  Topic_5
  Topic_4
  Topic_6
  Topic_1
6 topics
Chapter_9
  Topic_8
  Topic_1
  Topic_2
  Topic_3
  Topic_4
  Topic_5
  Topic_6
  Topic_7
8 topics

--- Month 3 Weekly Breakdown ---

mathematics
Chapter_11
  Topic_7
  Topic_1
  Topic_6
  Topic_2
  Topic_3
  Topic_4
  Topic_5
7 topics
Chapter_4
  Topic_3
  Topic_5
  Topic_6
  Topic_1
  Topic_2
  Topic_4
6 topics

physics
Chapter_6
  Topic_1
  Topic_2
  Topic_3
  Topic_4
4 topics
Chapter_1
  Topic_2
  Topic_3
  Topic_5
  Topic_6
  Topic_1
  Topic_7
  Topic_4
7 topics

chemistry
Chapter_11
  Topic_6
  Topic_2
  Topic_7
  Topic_1
  Topic_3
  Topic_4
  Topic_5
7 topics
Chapter_6
  Topic_1
  Topic_4
  Topic_2
  Topic_3
4 topics

--- Month 4 Weekly Breakdown ---

mathematics
Chapter_9
  Topic_2
  Topic_4
  Topic_1
  Topic_3
  Topic_7
  Topic_5
  Topic_6
  Topic_8
8 topics
Chapter_10
  Topic_7
  Topic_9
  Topic_11
  Topic_12
  Topic_16
  Topic_2
  Topic_8
  Topic_10
  Topic_14
  Topic_15
  Topic_1
  Topic_3
  Topic_4
  Topic_5
  Topic_6
  Topic_13
16 topics

physics
Chapter_10
  Topic_3
  Topic_4
  Topic_5
  Topic_6
  Topic_7
  Topic_9
  Topic_12
  Topic_16
  Topic_2
  Topic_8
  Topic_10
  Topic_11
  Topic_15
  Topic_1
  Topic_13
  Topic_14
16 topics
Chapter_7
  Topic_1
  Topic_3
  Topic_5
  Topic_8
  Topic_10
  Topic_2
  Topic_6
  Topic_9
  Topic_4
  Topic_7
  Topic_11
11 topics

chemistry
Chapter_2
  Topic_1
  Topic_2
  Topic_5
  Topic_7
  Topic_9
  Topic_11
  Topic_3
  Topic_6
  Topic_10
  Topic_4
  Topic_8
11 topics
Chapter_10
  Topic_2
  Topic_4
  Topic_5
  Topic_10
  Topic_13
  Topic_15
  Topic_7
  Topic_9
  Topic_11
  Topic_12
  Topic_14
  Topic_16
  Topic_1
  Topic_3
  Topic_6
  Topic_8
16 topics

--- Month 5 Weekly Breakdown ---

mathematics
Chapter_7
  Topic_2
  Topic_4
  Topic_6
  Topic_10
  Topic_3
  Topic_7
  Topic_8
  Topic_9
  Topic_11
  Topic_1
  Topic_5
11 topics
Chapter_12
  Topic_1
  Topic_3
  Topic_11
  Topic_2
  Topic_6
  Topic_7
  Topic_8
  Topic_12
  Topic_4
  Topic_5
  Topic_9
  Topic_10
12 topics

physics
Chapter_2
  Topic_3
  Topic_9
  Topic_1
  Topic_2
  Topic_4
  Topic_5
  Topic_7
  Topic_8
  Topic_6
  Topic_10
  Topic_11
11 topics
Chapter_12
  Topic_1
  Topic_2
  Topic_4
  Topic_7
  Topic_12
  Topic_3
  Topic_5
  Topic_6
  Topic_10
  Topic_11
  Topic_8
  Topic_9
12 topics

chemistry
Chapter_7
  Topic_3
  Topic_5
  Topic_2
  Topic_4
  Topic_8
  Topic_1
  Topic_6
  Topic_7
  Topic_9
  Topic_10
  Topic_11
11 topics
Chapter_12
  Topic_1
  Topic_5
  Topic_7
  Topic_4
  Topic_6
  Topic_8
  Topic_9
  Topic_10
  Topic_11
  Topic_12
  Topic_2
  Topic_3
12 topics

--- Month 6 Weekly Breakdown ---

mathematics
Chapter_5
  Topic_2
  Topic_7
  Topic_1
  Topic_3
  Topic_4
  Topic_5
  Topic_6
7 topics
Chapter_3
  Topic_8
  Topic_1
  Topic_2
  Topic_6
  Topic_3
  Topic_4
  Topic_5
  Topic_7
8 topics

physics
Chapter_5
  Topic_4
  Topic_6
  Topic_7
  Topic_3
  Topic_5
  Topic_1
  Topic_2
7 topics
Chapter_3
  Topic_3
  Topic_4
  Topic_5
  Topic_6
  Topic_1
  Topic_2
  Topic_7
  Topic_8
8 topics

chemistry
Chapter_5
  Topic_1
  Topic_2
  Topic_5
  Topic_6
  Topic_3
  Topic_4
  Topic_7
7 topics
Chapter_3
  Topic_7
  Topic_8
  Topic_3
  Topic_1
  Topic_2
  Topic_4
  Topic_5
  Topic_6
8 topics

================================================================================
📋 JSON OUTPUT:
================================================================================
{
  "plan_info": {
    "start_date": "2025-08-12",
    "end_date": "2026-04-09",
    "target_score": "230/300",
    "total_months": 8,
    "syllabus_completion_months": 6,
    "study_days": 132,
    "pyq_days": 64,
    "weekend_sessions": 64,
    "dpp_sessions": 396,
    "Full_month_revision": 2
  },
  "monthly_breakdown": {
    "Month 1": {
      "target_ratio": "76.7% of target",
      "total_achievable_score": 80.75,
      "user_target_score": 61.91,
      "efficiency_required": "76.7%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_9",
            "Chapter_8"
          ],
          "subject_weightage": 27.51,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_8",
            "Chapter_1"
          ],
          "subject_weightage": 26.46,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_2",
            "Chapter_1"
          ],
          "subject_weightage": 26.78,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 2": {
      "target_ratio": "76.7% of target",
      "total_achievable_score": 51.24,
      "user_target_score": 39.28,
      "efficiency_required": "76.7%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_11",
            "Chapter_4"
          ],
          "subject_weightage": 11.15,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_4",
            "Chapter_9"
          ],
          "subject_weightage": 17.91,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_8",
            "Chapter_6"
          ],
          "subject_weightage": 22.18,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 3": {
      "target_ratio": "76.7% of target",
      "total_achievable_score": 30.37,
      "user_target_score": 23.28,
      "efficiency_required": "76.7%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_6",
            "Chapter_1"
          ],
          "subject_weightage": 3.26,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_11",
            "Chapter_6"
          ],
          "subject_weightage": 8.36,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_11",
            "Chapter_4"
          ],
          "subject_weightage": 18.75,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 4": {
      "target_ratio": "76.7% of target",
      "total_achievable_score": 45.64,
      "user_target_score": 34.99,
      "efficiency_required": "76.7%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_10",
            "Chapter_7"
          ],
          "subject_weightage": 17.19,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_2",
            "Chapter_10"
          ],
          "subject_weightage": 15.59,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_9",
            "Chapter_10"
          ],
          "subject_weightage": 12.86,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 5": {
      "target_ratio": "76.7% of target",
      "total_achievable_score": 43.38,
      "user_target_score": 33.26,
      "efficiency_required": "76.7%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_2",
            "Chapter_12"
          ],
          "subject_weightage": 25.96,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_7",
            "Chapter_12"
          ],
          "subject_weightage": 11.38,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_7",
            "Chapter_12"
          ],
          "subject_weightage": 6.04,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 6": {
      "target_ratio": "76.7% of target",
      "total_achievable_score": 47.3,
      "user_target_score": 36.26,
      "efficiency_required": "76.7%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_5",
            "Chapter_3"
          ],
          "subject_weightage": 14.92,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_5",
            "Chapter_3"
          ],
          "subject_weightage": 20.28,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_5",
            "Chapter_3"
          ],
          "subject_weightage": 12.1,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 7": {
      "Total_PYQs_in_this_Month": 50
    },
    "Month 8": {
      "Total_PYQs_in_this_Month": 60
    }
  },
  "chapter_breakdown": {
    "month_1": {
      "mathematics": [
        "Chapter_2",
        "Chapter_1"
      ],
      "physics": [
        "Chapter_9",
        "Chapter_8"
      ],
      "chemistry": [
        "Chapter_8",
        "Chapter_1"
      ]
    },
    "month_2": {
      "mathematics": [
        "Chapter_8",
        "Chapter_6"
      ],
      "physics": [
        "Chapter_11",
        "Chapter_4"
      ],
      "chemistry": [
        "Chapter_4",
        "Chapter_9"
      ]
    },
    "month_3": {
      "mathematics": [
        "Chapter_11",
        "Chapter_4"
      ],
      "physics": [
        "Chapter_6",
        "Chapter_1"
      ],
      "chemistry": [
        "Chapter_11",
        "Chapter_6"
      ]
    },
    "month_4": {
      "mathematics": [
        "Chapter_9",
        "Chapter_10"
      ],
      "physics": [
        "Chapter_10",
        "Chapter_7"
      ],
      "chemistry": [
        "Chapter_2",
        "Chapter_10"
      ]
    },
    "month_5": {
      "mathematics": [
        "Chapter_7",
        "Chapter_12"
      ],
      "physics": [
        "Chapter_2",
        "Chapter_12"
      ],
      "chemistry": [
        "Chapter_7",
        "Chapter_12"
      ]
    },
    "month_6": {
      "mathematics": [
        "Chapter_5",
        "Chapter_3"
      ],
      "physics": [
        "Chapter_5",
        "Chapter_3"
      ],
      "chemistry": [
        "Chapter_5",
        "Chapter_3"
      ]
    }
  },
  "weekly_breakdown": {
    "month_1": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_2": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_9"
              ],
              "Chapter_1": [
                "Topic_6",
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          },
          "physics": {
            "chapters": {
              "Chapter_9": [
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_8": [
                "Topic_1",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 21
          },
          "chemistry": {
            "chapters": {
              "Chapter_8": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_6",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_13"
              ],
              "Chapter_1": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_2": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_9"
              ],
              "Chapter_1": [
                "Topic_6",
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          },
          "physics": {
            "chapters": {
              "Chapter_9": [
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_8": [
                "Topic_1",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 21
          },
          "chemistry": {
            "chapters": {
              "Chapter_8": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_6",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_13"
              ],
              "Chapter_1": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_2": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_9"
              ],
              "Chapter_1": [
                "Topic_6",
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          },
          "physics": {
            "chapters": {
              "Chapter_9": [
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_8": [
                "Topic_1",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 21
          },
          "chemistry": {
            "chapters": {
              "Chapter_8": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_6",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_13"
              ],
              "Chapter_1": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_2": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_9"
              ],
              "Chapter_1": [
                "Topic_6",
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          },
          "physics": {
            "chapters": {
              "Chapter_9": [
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_8": [
                "Topic_1",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 21
          },
          "chemistry": {
            "chapters": {
              "Chapter_8": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_6",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_13"
              ],
              "Chapter_1": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          }
        }
      }
    },
    "month_2": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_8": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_9",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_10"
              ],
              "Chapter_6": [
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_1"
              ]
            },
            "total_topic_count": 17
          },
          "physics": {
            "chapters": {
              "Chapter_11": [
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_4": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3"
              ]
            },
            "total_topic_count": 13
          },
          "chemistry": {
            "chapters": {
              "Chapter_4": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_4",
                "Topic_6",
                "Topic_1"
              ],
              "Chapter_9": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7"
              ]
            },
            "total_topic_count": 14
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_8": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_9",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_10"
              ],
              "Chapter_6": [
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_1"
              ]
            },
            "total_topic_count": 17
          },
          "physics": {
            "chapters": {
              "Chapter_11": [
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_4": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3"
              ]
            },
            "total_topic_count": 13
          },
          "chemistry": {
            "chapters": {
              "Chapter_4": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_4",
                "Topic_6",
                "Topic_1"
              ],
              "Chapter_9": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7"
              ]
            },
            "total_topic_count": 14
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_8": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_9",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_10"
              ],
              "Chapter_6": [
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_1"
              ]
            },
            "total_topic_count": 17
          },
          "physics": {
            "chapters": {
              "Chapter_11": [
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_4": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3"
              ]
            },
            "total_topic_count": 13
          },
          "chemistry": {
            "chapters": {
              "Chapter_4": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_4",
                "Topic_6",
                "Topic_1"
              ],
              "Chapter_9": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7"
              ]
            },
            "total_topic_count": 14
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_8": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_9",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_10"
              ],
              "Chapter_6": [
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_1"
              ]
            },
            "total_topic_count": 17
          },
          "physics": {
            "chapters": {
              "Chapter_11": [
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_4": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3"
              ]
            },
            "total_topic_count": 13
          },
          "chemistry": {
            "chapters": {
              "Chapter_4": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_4",
                "Topic_6",
                "Topic_1"
              ],
              "Chapter_9": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7"
              ]
            },
            "total_topic_count": 14
          }
        }
      }
    },
    "month_3": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_11": [
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_4": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4"
              ]
            },
            "total_topic_count": 13
          },
          "physics": {
            "chapters": {
              "Chapter_6": [
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_1": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_7",
                "Topic_4"
              ]
            },
            "total_topic_count": 11
          },
          "chemistry": {
            "chapters": {
              "Chapter_11": [
                "Topic_6",
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_6": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 11
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_11": [
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_4": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4"
              ]
            },
            "total_topic_count": 13
          },
          "physics": {
            "chapters": {
              "Chapter_6": [
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_1": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_7",
                "Topic_4"
              ]
            },
            "total_topic_count": 11
          },
          "chemistry": {
            "chapters": {
              "Chapter_11": [
                "Topic_6",
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_6": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 11
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_11": [
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_4": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4"
              ]
            },
            "total_topic_count": 13
          },
          "physics": {
            "chapters": {
              "Chapter_6": [
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_1": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_7",
                "Topic_4"
              ]
            },
            "total_topic_count": 11
          },
          "chemistry": {
            "chapters": {
              "Chapter_11": [
                "Topic_6",
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_6": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 11
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_11": [
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_4": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4"
              ]
            },
            "total_topic_count": 13
          },
          "physics": {
            "chapters": {
              "Chapter_6": [
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_1": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_7",
                "Topic_4"
              ]
            },
            "total_topic_count": 11
          },
          "chemistry": {
            "chapters": {
              "Chapter_11": [
                "Topic_6",
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_6": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 11
          }
        }
      }
    },
    "month_4": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_9": [
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_7",
                "Topic_5",
                "Topic_6",
                "Topic_8"
              ],
              "Chapter_10": [
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_14",
                "Topic_15",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_13"
              ]
            },
            "total_topic_count": 24
          },
          "physics": {
            "chapters": {
              "Chapter_10": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_15",
                "Topic_1",
                "Topic_13",
                "Topic_14"
              ],
              "Chapter_7": [
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_8",
                "Topic_10",
                "Topic_2",
                "Topic_6",
                "Topic_9",
                "Topic_4",
                "Topic_7",
                "Topic_11"
              ]
            },
            "total_topic_count": 27
          },
          "chemistry": {
            "chapters": {
              "Chapter_2": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_3",
                "Topic_6",
                "Topic_10",
                "Topic_4",
                "Topic_8"
              ],
              "Chapter_10": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_10",
                "Topic_13",
                "Topic_15",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_14",
                "Topic_16",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_8"
              ]
            },
            "total_topic_count": 27
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_9": [
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_7",
                "Topic_5",
                "Topic_6",
                "Topic_8"
              ],
              "Chapter_10": [
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_14",
                "Topic_15",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_13"
              ]
            },
            "total_topic_count": 24
          },
          "physics": {
            "chapters": {
              "Chapter_10": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_15",
                "Topic_1",
                "Topic_13",
                "Topic_14"
              ],
              "Chapter_7": [
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_8",
                "Topic_10",
                "Topic_2",
                "Topic_6",
                "Topic_9",
                "Topic_4",
                "Topic_7",
                "Topic_11"
              ]
            },
            "total_topic_count": 27
          },
          "chemistry": {
            "chapters": {
              "Chapter_2": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_3",
                "Topic_6",
                "Topic_10",
                "Topic_4",
                "Topic_8"
              ],
              "Chapter_10": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_10",
                "Topic_13",
                "Topic_15",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_14",
                "Topic_16",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_8"
              ]
            },
            "total_topic_count": 27
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_9": [
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_7",
                "Topic_5",
                "Topic_6",
                "Topic_8"
              ],
              "Chapter_10": [
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_14",
                "Topic_15",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_13"
              ]
            },
            "total_topic_count": 24
          },
          "physics": {
            "chapters": {
              "Chapter_10": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_15",
                "Topic_1",
                "Topic_13",
                "Topic_14"
              ],
              "Chapter_7": [
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_8",
                "Topic_10",
                "Topic_2",
                "Topic_6",
                "Topic_9",
                "Topic_4",
                "Topic_7",
                "Topic_11"
              ]
            },
            "total_topic_count": 27
          },
          "chemistry": {
            "chapters": {
              "Chapter_2": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_3",
                "Topic_6",
                "Topic_10",
                "Topic_4",
                "Topic_8"
              ],
              "Chapter_10": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_10",
                "Topic_13",
                "Topic_15",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_14",
                "Topic_16",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_8"
              ]
            },
            "total_topic_count": 27
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_9": [
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_7",
                "Topic_5",
                "Topic_6",
                "Topic_8"
              ],
              "Chapter_10": [
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_14",
                "Topic_15",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_13"
              ]
            },
            "total_topic_count": 24
          },
          "physics": {
            "chapters": {
              "Chapter_10": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_15",
                "Topic_1",
                "Topic_13",
                "Topic_14"
              ],
              "Chapter_7": [
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_8",
                "Topic_10",
                "Topic_2",
                "Topic_6",
                "Topic_9",
                "Topic_4",
                "Topic_7",
                "Topic_11"
              ]
            },
            "total_topic_count": 27
          },
          "chemistry": {
            "chapters": {
              "Chapter_2": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_3",
                "Topic_6",
                "Topic_10",
                "Topic_4",
                "Topic_8"
              ],
              "Chapter_10": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_10",
                "Topic_13",
                "Topic_15",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_14",
                "Topic_16",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_8"
              ]
            },
            "total_topic_count": 27
          }
        }
      }
    },
    "month_5": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_7": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_10",
                "Topic_3",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_11",
                "Topic_1",
                "Topic_5"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_3",
                "Topic_11",
                "Topic_2",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_12",
                "Topic_4",
                "Topic_5",
                "Topic_9",
                "Topic_10"
              ]
            },
            "total_topic_count": 23
          },
          "physics": {
            "chapters": {
              "Chapter_2": [
                "Topic_3",
                "Topic_9",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_6",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7",
                "Topic_12",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_10",
                "Topic_11",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 23
          },
          "chemistry": {
            "chapters": {
              "Chapter_7": [
                "Topic_3",
                "Topic_5",
                "Topic_2",
                "Topic_4",
                "Topic_8",
                "Topic_1",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_4",
                "Topic_6",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 23
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_7": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_10",
                "Topic_3",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_11",
                "Topic_1",
                "Topic_5"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_3",
                "Topic_11",
                "Topic_2",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_12",
                "Topic_4",
                "Topic_5",
                "Topic_9",
                "Topic_10"
              ]
            },
            "total_topic_count": 23
          },
          "physics": {
            "chapters": {
              "Chapter_2": [
                "Topic_3",
                "Topic_9",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_6",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7",
                "Topic_12",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_10",
                "Topic_11",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 23
          },
          "chemistry": {
            "chapters": {
              "Chapter_7": [
                "Topic_3",
                "Topic_5",
                "Topic_2",
                "Topic_4",
                "Topic_8",
                "Topic_1",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_4",
                "Topic_6",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 23
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_7": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_10",
                "Topic_3",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_11",
                "Topic_1",
                "Topic_5"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_3",
                "Topic_11",
                "Topic_2",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_12",
                "Topic_4",
                "Topic_5",
                "Topic_9",
                "Topic_10"
              ]
            },
            "total_topic_count": 23
          },
          "physics": {
            "chapters": {
              "Chapter_2": [
                "Topic_3",
                "Topic_9",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_6",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7",
                "Topic_12",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_10",
                "Topic_11",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 23
          },
          "chemistry": {
            "chapters": {
              "Chapter_7": [
                "Topic_3",
                "Topic_5",
                "Topic_2",
                "Topic_4",
                "Topic_8",
                "Topic_1",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_4",
                "Topic_6",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 23
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_7": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_10",
                "Topic_3",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_11",
                "Topic_1",
                "Topic_5"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_3",
                "Topic_11",
                "Topic_2",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_12",
                "Topic_4",
                "Topic_5",
                "Topic_9",
                "Topic_10"
              ]
            },
            "total_topic_count": 23
          },
          "physics": {
            "chapters": {
              "Chapter_2": [
                "Topic_3",
                "Topic_9",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_6",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7",
                "Topic_12",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_10",
                "Topic_11",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 23
          },
          "chemistry": {
            "chapters": {
              "Chapter_7": [
                "Topic_3",
                "Topic_5",
                "Topic_2",
                "Topic_4",
                "Topic_8",
                "Topic_1",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_4",
                "Topic_6",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 23
          }
        }
      }
    },
    "month_6": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_5": [
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ],
              "Chapter_3": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 15
          },
          "physics": {
            "chapters": {
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ],
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
              ]
            },
            "total_topic_count": 15
          },
          "chemistry": {
            "chapters": {
              "Chapter_5": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_7"
              ],
              "Chapter_3": [
                "Topic_7",
                "Topic_8",
                "Topic_3",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 15
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_5": [
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ],
              "Chapter_3": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 15
          },
          "physics": {
            "chapters": {
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ],
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
              ]
            },
            "total_topic_count": 15
          },
          "chemistry": {
            "chapters": {
              "Chapter_5": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_7"
              ],
              "Chapter_3": [
                "Topic_7",
                "Topic_8",
                "Topic_3",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 15
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_5": [
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ],
              "Chapter_3": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 15
          },
          "physics": {
            "chapters": {
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ],
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
              ]
            },
            "total_topic_count": 15
          },
          "chemistry": {
            "chapters": {
              "Chapter_5": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_7"
              ],
              "Chapter_3": [
                "Topic_7",
                "Topic_8",
                "Topic_3",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 15
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_5": [
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ],
              "Chapter_3": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 15
          },
          "physics": {
            "chapters": {
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ],
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
              ]
            },
            "total_topic_count": 15
          },
          "chemistry": {
            "chapters": {
              "Chapter_5": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_7"
              ],
              "Chapter_3": [
                "Topic_7",
                "Topic_8",
                "Topic_3",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 15
          }
        }
      }
    }
  }
}

================================================================================
✅ NEW SCORE-ORIENTED PLAN DISPLAY COMPLETE
================================================================================

INFO:     127.0.0.1:65213 - "POST /chat HTTP/1.1" 200 OK
2025-08-12 15:02:46,977 - app.main - INFO - Received chat message from user: user_igha5v6vx
2025-08-12 15:02:46,977 - app.regen_tools - INFO - Checking if user exists: user_igha5v6vx
2025-08-12 15:02:47,152 - app.regen_tools - INFO - User user_igha5v6vx found in database
2025-08-12 15:02:47,153 - app.main - INFO - User existence check for user_igha5v6vx: exists=True, has_study_plan=False, treating_as_existing=False
2025-08-12 15:02:47,153 - app.main - INFO - New user detected: user_igha5v6vx - routing to normal flow
2025-08-12 15:02:47,237 - app.main - INFO - Retrieved stored form data for user: user_igha5v6vx
2025-08-12 15:02:47,237 - app.main - INFO - Using stored form data for user: user_igha5v6vx
2025-08-12 15:02:47,238 - app.new_score_oriented_tools - INFO - Exam date validation: {'is_valid': True, 'calculated_months': 8, 'exam_date': '2026-04-12', 'minimum_required': 6, 'message': 'Exam date is 8 months away. Valid for new_score_oriented plan.'}
2025-08-12 15:02:47,238 - app.main - INFO - Handling feedback for existing new_score_oriented plan: user_igha5v6vx
2025-08-12 15:02:47,238 - app.main - INFO - Processing new_score_oriented feedback: change my target score to  255
2025-08-12 15:02:47,238 - app.main - INFO - Routing to feedback_counsellor for user message: change my target score to  255
2025-08-12 15:02:47,240 - app.new_score_oriented_graph - INFO - Counsellor Generator Agent executing for new_score_oriented plan
2025-08-12 15:02:47,241 - app.new_score_oriented_tools - INFO - Exam date validation: {'is_valid': True, 'calculated_months': 8, 'exam_date': '2026-04-12', 'minimum_required': 6, 'message': 'Exam date is 8 months away. Valid for new_score_oriented plan.'}
2025-08-12 15:02:47,242 - app.new_score_oriented_graph - INFO - New Score-Oriented Requirement Extractor executing
2025-08-12 15:02:51,126 - app.new_score_oriented_graph - INFO - Requirement extraction result: success
2025-08-12 15:02:51,127 - app.new_score_oriented_graph - INFO - Extracted requirements: subject_priority=['physics', 'chemistry', 'mathematics'] chapter_coverage={} time_allocation={}
2025-08-12 15:02:51,127 - app.new_score_oriented_graph - INFO - RevisionFlow Agent executing
2025-08-12 15:02:51,128 - app.new_score_oriented_agents - INFO - RevisionFlow Agent executing: Generating complete syllabus coverage plan
2025-08-12 15:02:51,128 - app.new_score_oriented_agents - INFO - Processing new_score_oriented plan for target: 230/300
2025-08-12 15:02:51,128 - app.new_score_oriented_agents - INFO - Processing complete syllabus for Physics
2025-08-12 15:02:51,128 - app.new_score_oriented_agents - INFO - Generating perfect dependency sequence for Physics
2025-08-12 15:02:51,129 - app.new_score_oriented_tools - INFO - Fetching chapter flow for exam: JEE Mains, subject: Physics
2025-08-12 15:02:51,206 - app.new_score_oriented_tools - INFO - Fetching chapter weightage for exam: JEE Mains, subject: Physics
2025-08-12 15:02:51,264 - app.new_score_oriented_tools - INFO - Starting enhanced dependency resolution for Physics
2025-08-12 15:02:51,264 - app.new_score_oriented_tools - INFO - Flow data: 12 chapters with dependencies
2025-08-12 15:02:51,264 - app.new_score_oriented_tools - INFO - Weightage data: 12 chapters with priorities
2025-08-12 15:02:51,265 - app.enhanced_dependency_resolver - INFO - Building comprehensive dependency graph from Chapter_Flow and Chapter_Weightage tables
2025-08-12 15:02:51,265 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_1]' for chapter 'Chapter_3' not found in chapter list
2025-08-12 15:02:51,265 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_2]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 15:02:51,265 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_3]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 15:02:51,266 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_4]' for chapter 'Chapter_7' not found in chapter list
2025-08-12 15:02:51,266 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_6]' for chapter 'Chapter_10' not found in chapter list
2025-08-12 15:02:51,266 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_5]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 15:02:51,266 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_7]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 15:02:51,266 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_1]' for chapter 'Chapter_2' not found in chapter list
2025-08-12 15:02:51,267 - app.enhanced_dependency_resolver - INFO - Dependency graph built: 12 chapters, 8 dependencies
2025-08-12 15:02:51,267 - app.enhanced_dependency_resolver - INFO - Starting strict dependency resolution for Physics
2025-08-12 15:02:51,267 - app.enhanced_dependency_resolver - WARNING - Some chapters could not be resolved due to dependency cycles: {'Chapter_10', 'Chapter_7', 'Chapter_2', 'Chapter_12', 'Chapter_5', 'Chapter_3'}
2025-08-12 15:02:51,267 - app.enhanced_dependency_resolver - INFO - Strict dependency resolution completed for Physics: 12 chapters
2025-08-12 15:02:51,267 - app.enhanced_dependency_resolver - INFO - Enhanced dependency resolution completed for Physics: 12 chapters with strict dependency ordering
2025-08-12 15:02:51,267 - app.new_score_oriented_tools - INFO - Enhanced dependency resolution for Physics:
2025-08-12 15:02:51,268 - app.new_score_oriented_tools - INFO -   Total chapters: 12
2025-08-12 15:02:51,268 - app.new_score_oriented_tools - INFO -   Chapters with dependencies: 6
2025-08-12 15:02:51,268 - app.new_score_oriented_tools - INFO -   All dependencies satisfied: True
2025-08-12 15:02:51,268 - app.new_score_oriented_tools - INFO - Final chapter order (dependencies first):
2025-08-12 15:02:51,268 - app.new_score_oriented_tools - INFO -    1. Chapter_9 (no dependencies) - Priority: 44.3
2025-08-12 15:02:51,268 - app.new_score_oriented_tools - INFO -    2. Chapter_8 (no dependencies) - Priority: 38.2
2025-08-12 15:02:51,268 - app.new_score_oriented_tools - INFO -    3. Chapter_11 (no dependencies) - Priority: 15.6
2025-08-12 15:02:51,268 - app.new_score_oriented_tools - INFO -    4. Chapter_4 (no dependencies) - Priority: 3.4
2025-08-12 15:02:51,269 - app.new_score_oriented_tools - INFO -    5. Chapter_6 (no dependencies) - Priority: 2.3
2025-08-12 15:02:51,269 - app.new_score_oriented_tools - INFO -    6. Chapter_1 (no dependencies) - Priority: 0.9
2025-08-12 15:02:51,269 - app.new_score_oriented_tools - INFO -    7. Chapter_10 (depends on: [Chapter_6]) - Priority: 22.6
2025-08-12 15:02:51,269 - app.new_score_oriented_tools - INFO -    8. Chapter_7 (depends on: [Chapter_4]) - Priority: 11.7
2025-08-12 15:02:51,269 - app.new_score_oriented_tools - INFO -    9. Chapter_2 (depends on: [Chapter_1]) - Priority: 44.0
2025-08-12 15:02:51,269 - app.new_score_oriented_tools - INFO -   10. Chapter_12 (depends on: [Chapter_5], [Chapter_7]) - Priority: 22.6
2025-08-12 15:02:51,270 - app.new_score_oriented_tools - INFO -   11. Chapter_5 (depends on: [Chapter_2], [Chapter_3]) - Priority: 41.9
2025-08-12 15:02:51,270 - app.new_score_oriented_tools - INFO -   12. Chapter_3 (depends on: [Chapter_1]) - Priority: 0.9
2025-08-12 15:02:51,270 - app.new_score_oriented_tools - INFO - Critical path: [Chapter_6] → Chapter_10
2025-08-12 15:02:51,270 - app.new_score_oriented_tools - INFO - Optimization suggestions:
2025-08-12 15:02:51,270 - app.new_score_oriented_tools - INFO -   • Consider parallel study tracks for efficiency: 3 groups of independent chapters identified
2025-08-12 15:02:51,270 - app.new_score_oriented_tools - INFO - ✅ All dependencies perfectly satisfied!
2025-08-12 15:02:51,271 - app.new_score_oriented_agents - INFO - Applying user preferences to dependency-resolved order for Physics
2025-08-12 15:02:51,271 - app.new_score_oriented_agents - INFO - User preferences applied to 12 chapters while maintaining dependencies
2025-08-12 15:02:51,271 - app.new_score_oriented_agents - INFO - Perfect dependency sequence generated for Physics: 12 chapters
2025-08-12 15:02:51,271 - app.new_score_oriented_agents - INFO - Dependency-first ordering applied successfully
2025-08-12 15:02:51,271 - app.new_score_oriented_agents - INFO - Ensuring 100% coverage for all chapters
2025-08-12 15:02:51,271 - app.new_score_oriented_agents - INFO - Processing complete syllabus for Chemistry
2025-08-12 15:02:51,272 - app.new_score_oriented_agents - INFO - Generating perfect dependency sequence for Chemistry
2025-08-12 15:02:51,273 - app.new_score_oriented_tools - INFO - Fetching chapter flow for exam: JEE Mains, subject: Chemistry
2025-08-12 15:02:51,368 - app.new_score_oriented_tools - INFO - Fetching chapter weightage for exam: JEE Mains, subject: Chemistry
2025-08-12 15:02:51,441 - app.new_score_oriented_tools - INFO - Starting enhanced dependency resolution for Chemistry
2025-08-12 15:02:51,441 - app.new_score_oriented_tools - INFO - Flow data: 12 chapters with dependencies
2025-08-12 15:02:51,442 - app.new_score_oriented_tools - INFO - Weightage data: 12 chapters with priorities
2025-08-12 15:02:51,442 - app.enhanced_dependency_resolver - INFO - Building comprehensive dependency graph from Chapter_Flow and Chapter_Weightage tables
2025-08-12 15:02:51,442 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_1]' for chapter 'Chapter_3' not found in chapter list
2025-08-12 15:02:51,443 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_2]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 15:02:51,443 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_3]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 15:02:51,443 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_4]' for chapter 'Chapter_7' not found in chapter list
2025-08-12 15:02:51,443 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_6]' for chapter 'Chapter_10' not found in chapter list
2025-08-12 15:02:51,443 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_5]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 15:02:51,444 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_7]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 15:02:51,444 - app.enhanced_dependency_resolver - INFO - Dependency graph built: 12 chapters, 7 dependencies
2025-08-12 15:02:51,444 - app.enhanced_dependency_resolver - INFO - Starting strict dependency resolution for Chemistry
2025-08-12 15:02:51,444 - app.enhanced_dependency_resolver - WARNING - Some chapters could not be resolved due to dependency cycles: {'Chapter_10', 'Chapter_7', 'Chapter_12', 'Chapter_5', 'Chapter_3'}
2025-08-12 15:02:51,445 - app.enhanced_dependency_resolver - INFO - Strict dependency resolution completed for Chemistry: 12 chapters
2025-08-12 15:02:51,445 - app.enhanced_dependency_resolver - INFO - Enhanced dependency resolution completed for Chemistry: 12 chapters with strict dependency ordering
2025-08-12 15:02:51,445 - app.new_score_oriented_tools - INFO - Enhanced dependency resolution for Chemistry:
2025-08-12 15:02:51,445 - app.new_score_oriented_tools - INFO -   Total chapters: 12
2025-08-12 15:02:51,445 - app.new_score_oriented_tools - INFO -   Chapters with dependencies: 5
2025-08-12 15:02:51,445 - app.new_score_oriented_tools - INFO -   All dependencies satisfied: True
2025-08-12 15:02:51,445 - app.new_score_oriented_tools - INFO - Final chapter order (dependencies first):
2025-08-12 15:02:51,446 - app.new_score_oriented_tools - INFO -    1. Chapter_8 (no dependencies) - Priority: 42.4
2025-08-12 15:02:51,446 - app.new_score_oriented_tools - INFO -    2. Chapter_1 (no dependencies) - Priority: 37.0
2025-08-12 15:02:51,446 - app.new_score_oriented_tools - INFO -    3. Chapter_4 (no dependencies) - Priority: 20.0
2025-08-12 15:02:51,446 - app.new_score_oriented_tools - INFO -    4. Chapter_9 (no dependencies) - Priority: 15.8
2025-08-12 15:02:51,446 - app.new_score_oriented_tools - INFO -    5. Chapter_11 (no dependencies) - Priority: 6.0
2025-08-12 15:02:51,446 - app.new_score_oriented_tools - INFO -    6. Chapter_6 (no dependencies) - Priority: 2.3
2025-08-12 15:02:51,446 - app.new_score_oriented_tools - INFO -    7. Chapter_2 (no dependencies) - Priority: 0.6
2025-08-12 15:02:51,446 - app.new_score_oriented_tools - INFO -    8. Chapter_10 (depends on: [Chapter_6]) - Priority: 45.1
2025-08-12 15:02:51,446 - app.new_score_oriented_tools - INFO -    9. Chapter_7 (depends on: [Chapter_4]) - Priority: 16.6
2025-08-12 15:02:51,446 - app.new_score_oriented_tools - INFO -   10. Chapter_12 (depends on: [Chapter_5], [Chapter_7]) - Priority: 3.1
2025-08-12 15:02:51,446 - app.new_score_oriented_tools - INFO -   11. Chapter_5 (depends on: [Chapter_2], [Chapter_3]) - Priority: 18.0
2025-08-12 15:02:51,447 - app.new_score_oriented_tools - INFO -   12. Chapter_3 (depends on: [Chapter_1]) - Priority: 33.9
2025-08-12 15:02:51,447 - app.new_score_oriented_tools - INFO - Critical path: [Chapter_6] → Chapter_10
2025-08-12 15:02:51,447 - app.new_score_oriented_tools - INFO - Optimization suggestions:
2025-08-12 15:02:51,447 - app.new_score_oriented_tools - INFO -   • Consider parallel study tracks for efficiency: 3 groups of independent chapters identified
2025-08-12 15:02:51,447 - app.new_score_oriented_tools - INFO - ✅ All dependencies perfectly satisfied!
2025-08-12 15:02:51,447 - app.new_score_oriented_agents - INFO - Applying user preferences to dependency-resolved order for Chemistry
2025-08-12 15:02:51,447 - app.new_score_oriented_agents - INFO - User preferences applied to 12 chapters while maintaining dependencies
2025-08-12 15:02:51,447 - app.new_score_oriented_agents - INFO - Perfect dependency sequence generated for Chemistry: 12 chapters
2025-08-12 15:02:51,448 - app.new_score_oriented_agents - INFO - Dependency-first ordering applied successfully
2025-08-12 15:02:51,448 - app.new_score_oriented_agents - INFO - Ensuring 100% coverage for all chapters
2025-08-12 15:02:51,448 - app.new_score_oriented_agents - INFO - Processing complete syllabus for Mathematics
2025-08-12 15:02:51,448 - app.new_score_oriented_agents - INFO - Generating perfect dependency sequence for Mathematics
2025-08-12 15:02:51,449 - app.new_score_oriented_tools - INFO - Fetching chapter flow for exam: JEE Mains, subject: Mathematics
2025-08-12 15:02:51,510 - app.new_score_oriented_tools - INFO - Fetching chapter weightage for exam: JEE Mains, subject: Mathematics
2025-08-12 15:02:51,582 - app.new_score_oriented_tools - INFO - Starting enhanced dependency resolution for Mathematics
2025-08-12 15:02:51,582 - app.new_score_oriented_tools - INFO - Flow data: 12 chapters with dependencies
2025-08-12 15:02:51,583 - app.new_score_oriented_tools - INFO - Weightage data: 12 chapters with priorities
2025-08-12 15:02:51,584 - app.enhanced_dependency_resolver - INFO - Building comprehensive dependency graph from Chapter_Flow and Chapter_Weightage tables
2025-08-12 15:02:51,584 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_1]' for chapter 'Chapter_3' not found in chapter list
2025-08-12 15:02:51,585 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_2]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 15:02:51,587 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_3]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 15:02:51,587 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_4]' for chapter 'Chapter_7' not found in chapter list
2025-08-12 15:02:51,588 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_6]' for chapter 'Chapter_10' not found in chapter list
2025-08-12 15:02:51,588 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_5]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 15:02:51,588 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_7]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 15:02:51,588 - app.enhanced_dependency_resolver - INFO - Dependency graph built: 12 chapters, 7 dependencies
2025-08-12 15:02:51,588 - app.enhanced_dependency_resolver - INFO - Starting strict dependency resolution for Mathematics
2025-08-12 15:02:51,588 - app.enhanced_dependency_resolver - WARNING - Some chapters could not be resolved due to dependency cycles: {'Chapter_10', 'Chapter_7', 'Chapter_12', 'Chapter_5', 'Chapter_3'}
2025-08-12 15:02:51,589 - app.enhanced_dependency_resolver - INFO - Strict dependency resolution completed for Mathematics: 12 chapters
2025-08-12 15:02:51,589 - app.enhanced_dependency_resolver - INFO - Enhanced dependency resolution completed for Mathematics: 12 chapters with strict dependency ordering
2025-08-12 15:02:51,590 - app.new_score_oriented_tools - INFO - Enhanced dependency resolution for Mathematics:
2025-08-12 15:02:51,590 - app.new_score_oriented_tools - INFO -   Total chapters: 12
2025-08-12 15:02:51,590 - app.new_score_oriented_tools - INFO -   Chapters with dependencies: 5
2025-08-12 15:02:51,591 - app.new_score_oriented_tools - INFO -   All dependencies satisfied: True
2025-08-12 15:02:51,591 - app.new_score_oriented_tools - INFO - Final chapter order (dependencies first):
2025-08-12 15:02:51,591 - app.new_score_oriented_tools - INFO -    1. Chapter_2 (no dependencies) - Priority: 42.9
2025-08-12 15:02:51,591 - app.new_score_oriented_tools - INFO -    2. Chapter_1 (no dependencies) - Priority: 37.5
2025-08-12 15:02:51,592 - app.new_score_oriented_tools - INFO -    3. Chapter_8 (no dependencies) - Priority: 34.2
2025-08-12 15:02:51,592 - app.new_score_oriented_tools - INFO -    4. Chapter_6 (no dependencies) - Priority: 32.3
2025-08-12 15:02:51,592 - app.new_score_oriented_tools - INFO -    5. Chapter_11 (no dependencies) - Priority: 21.0
2025-08-12 15:02:51,592 - app.new_score_oriented_tools - INFO -    6. Chapter_4 (no dependencies) - Priority: 16.5
2025-08-12 15:02:51,593 - app.new_score_oriented_tools - INFO -    7. Chapter_9 (no dependencies) - Priority: 15.8
2025-08-12 15:02:51,593 - app.new_score_oriented_tools - INFO -    8. Chapter_10 (depends on: [Chapter_6]) - Priority: 5.0
2025-08-12 15:02:51,593 - app.new_score_oriented_tools - INFO -    9. Chapter_7 (depends on: [Chapter_4]) - Priority: 3.9
2025-08-12 15:02:51,593 - app.new_score_oriented_tools - INFO -   10. Chapter_12 (depends on: [Chapter_5], [Chapter_7]) - Priority: 2.1
2025-08-12 15:02:51,593 - app.new_score_oriented_tools - INFO -   11. Chapter_5 (depends on: [Chapter_2], [Chapter_3]) - Priority: 5.8
2025-08-12 15:02:51,594 - app.new_score_oriented_tools - INFO -   12. Chapter_3 (depends on: [Chapter_1]) - Priority: 12.6
2025-08-12 15:02:51,594 - app.new_score_oriented_tools - INFO - Critical path: [Chapter_6] → Chapter_10
2025-08-12 15:02:51,594 - app.new_score_oriented_tools - INFO - Optimization suggestions:
2025-08-12 15:02:51,594 - app.new_score_oriented_tools - INFO -   • Consider parallel study tracks for efficiency: 3 groups of independent chapters identified
2025-08-12 15:02:51,594 - app.new_score_oriented_tools - INFO - ✅ All dependencies perfectly satisfied!
2025-08-12 15:02:51,594 - app.new_score_oriented_agents - INFO - Applying user preferences to dependency-resolved order for Mathematics
2025-08-12 15:02:51,594 - app.new_score_oriented_agents - INFO - User preferences applied to 12 chapters while maintaining dependencies
2025-08-12 15:02:51,594 - app.new_score_oriented_agents - INFO - Perfect dependency sequence generated for Mathematics: 12 chapters
2025-08-12 15:02:51,595 - app.new_score_oriented_agents - INFO - Dependency-first ordering applied successfully
2025-08-12 15:02:51,595 - app.new_score_oriented_agents - INFO - Ensuring 100% coverage for all chapters
2025-08-12 15:02:51,595 - app.new_score_oriented_agents - INFO - Distributing syllabus across 6 months (total: 8)
2025-08-12 15:02:51,595 - app.new_score_oriented_agents - INFO - Starting enhanced features generation...
2025-08-12 15:02:51,595 - app.new_score_oriented_agents - INFO - Generating enhanced features for new_score_oriented plan
2025-08-12 15:02:51,595 - app.new_score_oriented_agents - INFO - Monthly chapters data prepared: ['month_1', 'month_2', 'month_3', 'month_4', 'month_5', 'month_6']
2025-08-12 15:02:51,596 - app.new_score_oriented_agents - INFO - Sample month data structure: {'physics': ['Chapter_9', 'Chapter_8'], 'chemistry': ['Chapter_8', 'Chapter_1'], 'mathematics': ['Chapter_2', 'Chapter_1']}
2025-08-12 15:02:51,596 - app.enhanced_new_score_oriented_tools - INFO - Calculating monthly target scores for user target: 230/300
2025-08-12 15:02:51,959 - app.enhanced_new_score_oriented_tools - INFO - month_1: Achievable=80.75, Target=61.91
2025-08-12 15:02:52,336 - app.enhanced_new_score_oriented_tools - INFO - month_2: Achievable=51.24, Target=39.28
2025-08-12 15:02:52,717 - app.enhanced_new_score_oriented_tools - INFO - month_3: Achievable=30.37, Target=23.28
2025-08-12 15:02:53,074 - app.enhanced_new_score_oriented_tools - INFO - month_4: Achievable=45.64, Target=34.99
2025-08-12 15:02:53,418 - app.enhanced_new_score_oriented_tools - INFO - month_5: Achievable=43.38, Target=33.26
2025-08-12 15:02:53,805 - app.enhanced_new_score_oriented_tools - INFO - month_6: Achievable=47.30, Target=36.26
2025-08-12 15:02:53,806 - app.enhanced_new_score_oriented_tools - INFO - Monthly target calculation completed: 6 months processed
2025-08-12 15:02:53,807 - app.enhanced_new_score_oriented_tools - INFO - Generating extended months plan: 8 total, 6 for syllabus
2025-08-12 15:02:53,807 - app.enhanced_new_score_oriented_tools - INFO - Extended months plan generated: 2 months of intensive practice
2025-08-12 15:02:53,808 - app.enhanced_new_score_oriented_tools - INFO - Generating weekly topic breakdown for 6 months
2025-08-12 15:02:56,220 - app.enhanced_new_score_oriented_tools - INFO - Weekly topic breakdown generated for 6 months
2025-08-12 15:02:56,221 - app.enhanced_new_score_oriented_tools - INFO - Creating comprehensive weekend schedule for 8 months
2025-08-12 15:02:56,221 - app.enhanced_new_score_oriented_tools - INFO - Comprehensive weekend schedule created for 8 months
2025-08-12 15:02:56,222 - app.new_score_oriented_agents - INFO - Enhanced features generated successfully
2025-08-12 15:02:56,222 - app.new_score_oriented_agents - INFO - Enhanced features generated: ['monthly_target_scores', 'extended_months_plan', 'weekly_topic_breakdown', 'weekend_schedule', 'strategy_summary']
2025-08-12 15:02:56,222 - app.new_score_oriented_agents - INFO - RevisionFlow plan generated with 6 months for syllabus completion
2025-08-12 15:02:56,223 - app.new_score_oriented_graph - INFO - Generator Validator Agent executing
2025-08-12 15:02:56,223 - app.new_score_oriented_agents - INFO - Validating chapter coverage for new_score_oriented plan
2025-08-12 15:02:56,224 - app.new_score_oriented_graph - INFO - Topic Agent executing
2025-08-12 15:02:56,224 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_9
2025-08-12 15:02:56,279 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_8
2025-08-12 15:02:56,338 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_11
2025-08-12 15:02:56,405 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_4
2025-08-12 15:02:56,453 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_6
2025-08-12 15:02:56,507 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_1
2025-08-12 15:02:56,567 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_10
2025-08-12 15:02:56,624 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_7
2025-08-12 15:02:56,687 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_2
2025-08-12 15:02:56,751 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_12
2025-08-12 15:02:56,816 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_5
2025-08-12 15:02:56,883 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_3
2025-08-12 15:02:56,944 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_8
2025-08-12 15:02:56,999 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_1
2025-08-12 15:02:57,056 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_4
2025-08-12 15:02:57,111 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_9
2025-08-12 15:02:57,165 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_11
2025-08-12 15:02:57,244 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_6
2025-08-12 15:02:57,306 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_2
2025-08-12 15:02:57,373 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_10
2025-08-12 15:02:57,426 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_7
2025-08-12 15:02:57,498 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_12
2025-08-12 15:02:57,567 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_5
2025-08-12 15:02:57,623 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_3
2025-08-12 15:02:57,682 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_2
2025-08-12 15:02:57,753 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_1
2025-08-12 15:02:57,816 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_8
2025-08-12 15:02:57,881 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_6
2025-08-12 15:02:57,938 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_11
2025-08-12 15:02:58,001 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_4
2025-08-12 15:02:58,061 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_9
2025-08-12 15:02:58,120 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_10
2025-08-12 15:02:58,177 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_7
2025-08-12 15:02:58,231 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_12
2025-08-12 15:02:58,285 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_5
2025-08-12 15:02:58,344 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_3
2025-08-12 15:02:58,422 - app.new_score_oriented_graph - INFO - Topic Validator Agent executing
2025-08-12 15:02:58,423 - app.new_score_oriented_agents - INFO - Validating topic coverage for new_score_oriented plan
2025-08-12 15:02:58,424 - app.new_score_oriented_agents - INFO - Performing final syllabus compliance validation
2025-08-12 15:02:58,425 - app.new_score_oriented_graph - INFO - Supervisor Agent executing
2025-08-12 15:02:58,425 - app.new_score_oriented_agents - INFO - Supervising new_score_oriented plan for target achievement
2025-08-12 15:02:58,426 - app.new_score_oriented_graph - INFO - Finalizing new_score_oriented study plan with enhanced calendar features

================================================================================
🎯 NEW SCORE-ORIENTED STUDY PLAN - DETAILED BREAKDOWN
================================================================================
2025-08-12 to 2026-04-09 | Target: 230/300

8
Months
132
Study Days
64
PYQ Days
64
Weekend Sessions
396
DPP Sessions

📊 MONTHLY TARGET BREAKDOWN:
--------------------------------------------------

Month 1
76.7% of target
80.8
Total Achievable Score
61.9
Your Target Score
Efficiency Required
76.7%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_9', 'Chapter_8'], 'subject_weightage': 27.51, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_8', 'Chapter_1'], 'subject_weightage': 26.46, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_2', 'Chapter_1'], 'subject_weightage': 26.78, 'chapter_count': 2}

Month 2
76.7% of target
51.2
Total Achievable Score
39.3
Your Target Score
Efficiency Required
76.7%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_11', 'Chapter_4'], 'subject_weightage': 11.15, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_4', 'Chapter_9'], 'subject_weightage': 17.91, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_8', 'Chapter_6'], 'subject_weightage': 22.18, 'chapter_count': 2}

Month 3
76.7% of target
30.4
Total Achievable Score
23.3
Your Target Score
Efficiency Required
76.7%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_6', 'Chapter_1'], 'subject_weightage': 3.26, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_11', 'Chapter_6'], 'subject_weightage': 8.36, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_11', 'Chapter_4'], 'subject_weightage': 18.75, 'chapter_count': 2}

Month 4
76.7% of target
45.6
Total Achievable Score
35.0
Your Target Score
Efficiency Required
76.7%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_10', 'Chapter_7'], 'subject_weightage': 17.19, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_2', 'Chapter_10'], 'subject_weightage': 15.59, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_9', 'Chapter_10'], 'subject_weightage': 12.86, 'chapter_count': 2}

Month 5
76.7% of target
43.4
Total Achievable Score
33.3
Your Target Score
Efficiency Required
76.7%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_2', 'Chapter_12'], 'subject_weightage': 25.96, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_7', 'Chapter_12'], 'subject_weightage': 11.38, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_7', 'Chapter_12'], 'subject_weightage': 6.04, 'chapter_count': 2}

Month 6
76.7% of target
47.3
Total Achievable Score
36.3
Your Target Score
Efficiency Required
76.7%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_5', 'Chapter_3'], 'subject_weightage': 14.92, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_5', 'Chapter_3'], 'subject_weightage': 20.28, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_5', 'Chapter_3'], 'subject_weightage': 12.1, 'chapter_count': 2}

Weekly Breakdown
--------------------------------------------------

--- Month 1 Weekly Breakdown ---

mathematics
Chapter_2
  Topic_2
  Topic_4
  Topic_6
  Topic_7
  Topic_8
  Topic_10
  Topic_11
  Topic_1
  Topic_3
  Topic_5
  Topic_9
11 topics
Chapter_1
  Topic_6
  Topic_2
  Topic_4
  Topic_1
  Topic_3
  Topic_5
  Topic_7
7 topics

physics
Chapter_9
  Topic_1
  Topic_3
  Topic_4
  Topic_2
  Topic_5
  Topic_6
  Topic_7
  Topic_8
8 topics
Chapter_8
  Topic_1
  Topic_10
  Topic_11
  Topic_12
  Topic_13
  Topic_2
  Topic_3
  Topic_4
  Topic_5
  Topic_6
  Topic_7
  Topic_8
  Topic_9
13 topics

chemistry
Chapter_8
  Topic_1
  Topic_5
  Topic_7
  Topic_8
  Topic_9
  Topic_10
  Topic_6
  Topic_11
  Topic_12
  Topic_2
  Topic_3
  Topic_4
  Topic_13
13 topics
Chapter_1
  Topic_3
  Topic_5
  Topic_6
  Topic_1
  Topic_2
  Topic_4
  Topic_7
7 topics

--- Month 2 Weekly Breakdown ---

mathematics
Chapter_8
  Topic_2
  Topic_4
  Topic_5
  Topic_7
  Topic_8
  Topic_11
  Topic_12
  Topic_13
  Topic_9
  Topic_1
  Topic_3
  Topic_6
  Topic_10
13 topics
Chapter_6
  Topic_2
  Topic_3
  Topic_4
  Topic_1
4 topics

physics
Chapter_11
  Topic_2
  Topic_5
  Topic_7
  Topic_1
  Topic_6
  Topic_3
  Topic_4
7 topics
Chapter_4
  Topic_1
  Topic_4
  Topic_2
  Topic_5
  Topic_6
  Topic_3
6 topics

chemistry
Chapter_4
  Topic_2
  Topic_3
  Topic_5
  Topic_4
  Topic_6
  Topic_1
6 topics
Chapter_9
  Topic_8
  Topic_1
  Topic_2
  Topic_3
  Topic_4
  Topic_5
  Topic_6
  Topic_7
8 topics

--- Month 3 Weekly Breakdown ---

mathematics
Chapter_11
  Topic_7
  Topic_1
  Topic_6
  Topic_2
  Topic_3
  Topic_4
  Topic_5
7 topics
Chapter_4
  Topic_3
  Topic_5
  Topic_6
  Topic_1
  Topic_2
  Topic_4
6 topics

physics
Chapter_6
  Topic_1
  Topic_2
  Topic_3
  Topic_4
4 topics
Chapter_1
  Topic_2
  Topic_3
  Topic_5
  Topic_6
  Topic_1
  Topic_7
  Topic_4
7 topics

chemistry
Chapter_11
  Topic_6
  Topic_2
  Topic_7
  Topic_1
  Topic_3
  Topic_4
  Topic_5
7 topics
Chapter_6
  Topic_1
  Topic_4
  Topic_2
  Topic_3
4 topics

--- Month 4 Weekly Breakdown ---

mathematics
Chapter_9
  Topic_2
  Topic_4
  Topic_1
  Topic_3
  Topic_7
  Topic_5
  Topic_6
  Topic_8
8 topics
Chapter_10
  Topic_7
  Topic_9
  Topic_11
  Topic_12
  Topic_16
  Topic_2
  Topic_8
  Topic_10
  Topic_14
  Topic_15
  Topic_1
  Topic_3
  Topic_4
  Topic_5
  Topic_6
  Topic_13
16 topics

physics
Chapter_10
  Topic_3
  Topic_4
  Topic_5
  Topic_6
  Topic_7
  Topic_9
  Topic_12
  Topic_16
  Topic_2
  Topic_8
  Topic_10
  Topic_11
  Topic_15
  Topic_1
  Topic_13
  Topic_14
16 topics
Chapter_7
  Topic_1
  Topic_3
  Topic_5
  Topic_8
  Topic_10
  Topic_2
  Topic_6
  Topic_9
  Topic_4
  Topic_7
  Topic_11
11 topics

chemistry
Chapter_2
  Topic_1
  Topic_2
  Topic_5
  Topic_7
  Topic_9
  Topic_11
  Topic_3
  Topic_6
  Topic_10
  Topic_4
  Topic_8
11 topics
Chapter_10
  Topic_2
  Topic_4
  Topic_5
  Topic_10
  Topic_13
  Topic_15
  Topic_7
  Topic_9
  Topic_11
  Topic_12
  Topic_14
  Topic_16
  Topic_1
  Topic_3
  Topic_6
  Topic_8
16 topics

--- Month 5 Weekly Breakdown ---

mathematics
Chapter_7
  Topic_2
  Topic_4
  Topic_6
  Topic_10
  Topic_3
  Topic_7
  Topic_8
  Topic_9
  Topic_11
  Topic_1
  Topic_5
11 topics
Chapter_12
  Topic_1
  Topic_3
  Topic_11
  Topic_2
  Topic_6
  Topic_7
  Topic_8
  Topic_12
  Topic_4
  Topic_5
  Topic_9
  Topic_10
12 topics

physics
Chapter_2
  Topic_3
  Topic_9
  Topic_1
  Topic_2
  Topic_4
  Topic_5
  Topic_7
  Topic_8
  Topic_6
  Topic_10
  Topic_11
11 topics
Chapter_12
  Topic_1
  Topic_2
  Topic_4
  Topic_7
  Topic_12
  Topic_3
  Topic_5
  Topic_6
  Topic_10
  Topic_11
  Topic_8
  Topic_9
12 topics

chemistry
Chapter_7
  Topic_3
  Topic_5
  Topic_2
  Topic_4
  Topic_8
  Topic_1
  Topic_6
  Topic_7
  Topic_9
  Topic_10
  Topic_11
11 topics
Chapter_12
  Topic_1
  Topic_5
  Topic_7
  Topic_4
  Topic_6
  Topic_8
  Topic_9
  Topic_10
  Topic_11
  Topic_12
  Topic_2
  Topic_3
12 topics

--- Month 6 Weekly Breakdown ---

mathematics
Chapter_5
  Topic_2
  Topic_7
  Topic_1
  Topic_3
  Topic_4
  Topic_5
  Topic_6
7 topics
Chapter_3
  Topic_8
  Topic_1
  Topic_2
  Topic_6
  Topic_3
  Topic_4
  Topic_5
  Topic_7
8 topics

physics
Chapter_5
  Topic_4
  Topic_6
  Topic_7
  Topic_3
  Topic_5
  Topic_1
  Topic_2
7 topics
Chapter_3
  Topic_3
  Topic_4
  Topic_5
  Topic_6
  Topic_1
  Topic_2
  Topic_7
  Topic_8
8 topics

chemistry
Chapter_5
  Topic_1
  Topic_2
  Topic_5
  Topic_6
  Topic_3
  Topic_4
  Topic_7
7 topics
Chapter_3
  Topic_7
  Topic_8
  Topic_3
  Topic_1
  Topic_2
  Topic_4
  Topic_5
  Topic_6
8 topics

================================================================================
📋 JSON OUTPUT:
================================================================================
{
  "plan_info": {
    "start_date": "2025-08-12",
    "end_date": "2026-04-09",
    "target_score": "230/300",
    "total_months": 8,
    "syllabus_completion_months": 6,
    "study_days": 132,
    "pyq_days": 64,
    "weekend_sessions": 64,
    "dpp_sessions": 396,
    "Full_month_revision": 2
  },
  "monthly_breakdown": {
    "Month 1": {
      "target_ratio": "76.7% of target",
      "total_achievable_score": 80.75,
      "user_target_score": 61.91,
      "efficiency_required": "76.7%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_9",
            "Chapter_8"
          ],
          "subject_weightage": 27.51,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_8",
            "Chapter_1"
          ],
          "subject_weightage": 26.46,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_2",
            "Chapter_1"
          ],
          "subject_weightage": 26.78,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 2": {
      "target_ratio": "76.7% of target",
      "total_achievable_score": 51.24,
      "user_target_score": 39.28,
      "efficiency_required": "76.7%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_11",
            "Chapter_4"
          ],
          "subject_weightage": 11.15,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_4",
            "Chapter_9"
          ],
          "subject_weightage": 17.91,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_8",
            "Chapter_6"
          ],
          "subject_weightage": 22.18,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 3": {
      "target_ratio": "76.7% of target",
      "total_achievable_score": 30.37,
      "user_target_score": 23.28,
      "efficiency_required": "76.7%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_6",
            "Chapter_1"
          ],
          "subject_weightage": 3.26,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_11",
            "Chapter_6"
          ],
          "subject_weightage": 8.36,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_11",
            "Chapter_4"
          ],
          "subject_weightage": 18.75,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 4": {
      "target_ratio": "76.7% of target",
      "total_achievable_score": 45.64,
      "user_target_score": 34.99,
      "efficiency_required": "76.7%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_10",
            "Chapter_7"
          ],
          "subject_weightage": 17.19,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_2",
            "Chapter_10"
          ],
          "subject_weightage": 15.59,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_9",
            "Chapter_10"
          ],
          "subject_weightage": 12.86,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 5": {
      "target_ratio": "76.7% of target",
      "total_achievable_score": 43.38,
      "user_target_score": 33.26,
      "efficiency_required": "76.7%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_2",
            "Chapter_12"
          ],
          "subject_weightage": 25.96,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_7",
            "Chapter_12"
          ],
          "subject_weightage": 11.38,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_7",
            "Chapter_12"
          ],
          "subject_weightage": 6.04,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 6": {
      "target_ratio": "76.7% of target",
      "total_achievable_score": 47.3,
      "user_target_score": 36.26,
      "efficiency_required": "76.7%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_5",
            "Chapter_3"
          ],
          "subject_weightage": 14.92,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_5",
            "Chapter_3"
          ],
          "subject_weightage": 20.28,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_5",
            "Chapter_3"
          ],
          "subject_weightage": 12.1,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 7": {
      "Total_PYQs_in_this_Month": 50
    },
    "Month 8": {
      "Total_PYQs_in_this_Month": 60
    }
  },
  "chapter_breakdown": {
    "month_1": {
      "mathematics": [
        "Chapter_2",
        "Chapter_1"
      ],
      "physics": [
        "Chapter_9",
        "Chapter_8"
      ],
      "chemistry": [
        "Chapter_8",
        "Chapter_1"
      ]
    },
    "month_2": {
      "mathematics": [
        "Chapter_8",
        "Chapter_6"
      ],
      "physics": [
        "Chapter_11",
        "Chapter_4"
      ],
      "chemistry": [
        "Chapter_4",
        "Chapter_9"
      ]
    },
    "month_3": {
      "mathematics": [
        "Chapter_11",
        "Chapter_4"
      ],
      "physics": [
        "Chapter_6",
        "Chapter_1"
      ],
      "chemistry": [
        "Chapter_11",
        "Chapter_6"
      ]
    },
    "month_4": {
      "mathematics": [
        "Chapter_9",
        "Chapter_10"
      ],
      "physics": [
        "Chapter_10",
        "Chapter_7"
      ],
      "chemistry": [
        "Chapter_2",
        "Chapter_10"
      ]
    },
    "month_5": {
      "mathematics": [
        "Chapter_7",
        "Chapter_12"
      ],
      "physics": [
        "Chapter_2",
        "Chapter_12"
      ],
      "chemistry": [
        "Chapter_7",
        "Chapter_12"
      ]
    },
    "month_6": {
      "mathematics": [
        "Chapter_5",
        "Chapter_3"
      ],
      "physics": [
        "Chapter_5",
        "Chapter_3"
      ],
      "chemistry": [
        "Chapter_5",
        "Chapter_3"
      ]
    }
  },
  "weekly_breakdown": {
    "month_1": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_2": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_9"
              ],
              "Chapter_1": [
                "Topic_6",
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          },
          "physics": {
            "chapters": {
              "Chapter_9": [
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_8": [
                "Topic_1",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 21
          },
          "chemistry": {
            "chapters": {
              "Chapter_8": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_6",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_13"
              ],
              "Chapter_1": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_2": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_9"
              ],
              "Chapter_1": [
                "Topic_6",
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          },
          "physics": {
            "chapters": {
              "Chapter_9": [
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_8": [
                "Topic_1",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 21
          },
          "chemistry": {
            "chapters": {
              "Chapter_8": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_6",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_13"
              ],
              "Chapter_1": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_2": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_9"
              ],
              "Chapter_1": [
                "Topic_6",
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          },
          "physics": {
            "chapters": {
              "Chapter_9": [
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_8": [
                "Topic_1",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 21
          },
          "chemistry": {
            "chapters": {
              "Chapter_8": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_6",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_13"
              ],
              "Chapter_1": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_2": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_9"
              ],
              "Chapter_1": [
                "Topic_6",
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
          },
          "physics": {
            "chapters": {
              "Chapter_9": [
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8"
              ],
              "Chapter_8": [
                "Topic_1",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 21
          },
          "chemistry": {
            "chapters": {
              "Chapter_8": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_6",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_13"
              ],
              "Chapter_1": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 20
          }
        }
      }
    },
    "month_2": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_8": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_9",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_10"
              ],
              "Chapter_6": [
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_1"
              ]
            },
            "total_topic_count": 17
          },
          "physics": {
            "chapters": {
              "Chapter_11": [
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_4": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3"
              ]
            },
            "total_topic_count": 13
          },
          "chemistry": {
            "chapters": {
              "Chapter_4": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_4",
                "Topic_6",
                "Topic_1"
              ],
              "Chapter_9": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7"
              ]
            },
            "total_topic_count": 14
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_8": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_9",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_10"
              ],
              "Chapter_6": [
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_1"
              ]
            },
            "total_topic_count": 17
          },
          "physics": {
            "chapters": {
              "Chapter_11": [
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_4": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3"
              ]
            },
            "total_topic_count": 13
          },
          "chemistry": {
            "chapters": {
              "Chapter_4": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_4",
                "Topic_6",
                "Topic_1"
              ],
              "Chapter_9": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7"
              ]
            },
            "total_topic_count": 14
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_8": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_9",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_10"
              ],
              "Chapter_6": [
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_1"
              ]
            },
            "total_topic_count": 17
          },
          "physics": {
            "chapters": {
              "Chapter_11": [
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_4": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3"
              ]
            },
            "total_topic_count": 13
          },
          "chemistry": {
            "chapters": {
              "Chapter_4": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_4",
                "Topic_6",
                "Topic_1"
              ],
              "Chapter_9": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7"
              ]
            },
            "total_topic_count": 14
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_8": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_11",
                "Topic_12",
                "Topic_13",
                "Topic_9",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_10"
              ],
              "Chapter_6": [
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_1"
              ]
            },
            "total_topic_count": 17
          },
          "physics": {
            "chapters": {
              "Chapter_11": [
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_4": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3"
              ]
            },
            "total_topic_count": 13
          },
          "chemistry": {
            "chapters": {
              "Chapter_4": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_4",
                "Topic_6",
                "Topic_1"
              ],
              "Chapter_9": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7"
              ]
            },
            "total_topic_count": 14
          }
        }
      }
    },
    "month_3": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_11": [
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_4": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4"
              ]
            },
            "total_topic_count": 13
          },
          "physics": {
            "chapters": {
              "Chapter_6": [
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_1": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_7",
                "Topic_4"
              ]
            },
            "total_topic_count": 11
          },
          "chemistry": {
            "chapters": {
              "Chapter_11": [
                "Topic_6",
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_6": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 11
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_11": [
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_4": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4"
              ]
            },
            "total_topic_count": 13
          },
          "physics": {
            "chapters": {
              "Chapter_6": [
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_1": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_7",
                "Topic_4"
              ]
            },
            "total_topic_count": 11
          },
          "chemistry": {
            "chapters": {
              "Chapter_11": [
                "Topic_6",
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_6": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 11
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_11": [
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_4": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4"
              ]
            },
            "total_topic_count": 13
          },
          "physics": {
            "chapters": {
              "Chapter_6": [
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_1": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_7",
                "Topic_4"
              ]
            },
            "total_topic_count": 11
          },
          "chemistry": {
            "chapters": {
              "Chapter_11": [
                "Topic_6",
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_6": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 11
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_11": [
                "Topic_7",
                "Topic_1",
                "Topic_6",
                "Topic_2",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_4": [
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_4"
              ]
            },
            "total_topic_count": 13
          },
          "physics": {
            "chapters": {
              "Chapter_6": [
                "Topic_1",
                "Topic_2",
                "Topic_3",
                "Topic_4"
              ],
              "Chapter_1": [
                "Topic_2",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_7",
                "Topic_4"
              ]
            },
            "total_topic_count": 11
          },
          "chemistry": {
            "chapters": {
              "Chapter_11": [
                "Topic_6",
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5"
              ],
              "Chapter_6": [
                "Topic_1",
                "Topic_4",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 11
          }
        }
      }
    },
    "month_4": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_9": [
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_7",
                "Topic_5",
                "Topic_6",
                "Topic_8"
              ],
              "Chapter_10": [
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_14",
                "Topic_15",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_13"
              ]
            },
            "total_topic_count": 24
          },
          "physics": {
            "chapters": {
              "Chapter_10": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_15",
                "Topic_1",
                "Topic_13",
                "Topic_14"
              ],
              "Chapter_7": [
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_8",
                "Topic_10",
                "Topic_2",
                "Topic_6",
                "Topic_9",
                "Topic_4",
                "Topic_7",
                "Topic_11"
              ]
            },
            "total_topic_count": 27
          },
          "chemistry": {
            "chapters": {
              "Chapter_2": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_3",
                "Topic_6",
                "Topic_10",
                "Topic_4",
                "Topic_8"
              ],
              "Chapter_10": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_10",
                "Topic_13",
                "Topic_15",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_14",
                "Topic_16",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_8"
              ]
            },
            "total_topic_count": 27
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_9": [
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_7",
                "Topic_5",
                "Topic_6",
                "Topic_8"
              ],
              "Chapter_10": [
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_14",
                "Topic_15",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_13"
              ]
            },
            "total_topic_count": 24
          },
          "physics": {
            "chapters": {
              "Chapter_10": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_15",
                "Topic_1",
                "Topic_13",
                "Topic_14"
              ],
              "Chapter_7": [
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_8",
                "Topic_10",
                "Topic_2",
                "Topic_6",
                "Topic_9",
                "Topic_4",
                "Topic_7",
                "Topic_11"
              ]
            },
            "total_topic_count": 27
          },
          "chemistry": {
            "chapters": {
              "Chapter_2": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_3",
                "Topic_6",
                "Topic_10",
                "Topic_4",
                "Topic_8"
              ],
              "Chapter_10": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_10",
                "Topic_13",
                "Topic_15",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_14",
                "Topic_16",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_8"
              ]
            },
            "total_topic_count": 27
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_9": [
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_7",
                "Topic_5",
                "Topic_6",
                "Topic_8"
              ],
              "Chapter_10": [
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_14",
                "Topic_15",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_13"
              ]
            },
            "total_topic_count": 24
          },
          "physics": {
            "chapters": {
              "Chapter_10": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_15",
                "Topic_1",
                "Topic_13",
                "Topic_14"
              ],
              "Chapter_7": [
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_8",
                "Topic_10",
                "Topic_2",
                "Topic_6",
                "Topic_9",
                "Topic_4",
                "Topic_7",
                "Topic_11"
              ]
            },
            "total_topic_count": 27
          },
          "chemistry": {
            "chapters": {
              "Chapter_2": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_3",
                "Topic_6",
                "Topic_10",
                "Topic_4",
                "Topic_8"
              ],
              "Chapter_10": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_10",
                "Topic_13",
                "Topic_15",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_14",
                "Topic_16",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_8"
              ]
            },
            "total_topic_count": 27
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_9": [
                "Topic_2",
                "Topic_4",
                "Topic_1",
                "Topic_3",
                "Topic_7",
                "Topic_5",
                "Topic_6",
                "Topic_8"
              ],
              "Chapter_10": [
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_14",
                "Topic_15",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_13"
              ]
            },
            "total_topic_count": 24
          },
          "physics": {
            "chapters": {
              "Chapter_10": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_12",
                "Topic_16",
                "Topic_2",
                "Topic_8",
                "Topic_10",
                "Topic_11",
                "Topic_15",
                "Topic_1",
                "Topic_13",
                "Topic_14"
              ],
              "Chapter_7": [
                "Topic_1",
                "Topic_3",
                "Topic_5",
                "Topic_8",
                "Topic_10",
                "Topic_2",
                "Topic_6",
                "Topic_9",
                "Topic_4",
                "Topic_7",
                "Topic_11"
              ]
            },
            "total_topic_count": 27
          },
          "chemistry": {
            "chapters": {
              "Chapter_2": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_3",
                "Topic_6",
                "Topic_10",
                "Topic_4",
                "Topic_8"
              ],
              "Chapter_10": [
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_10",
                "Topic_13",
                "Topic_15",
                "Topic_7",
                "Topic_9",
                "Topic_11",
                "Topic_12",
                "Topic_14",
                "Topic_16",
                "Topic_1",
                "Topic_3",
                "Topic_6",
                "Topic_8"
              ]
            },
            "total_topic_count": 27
          }
        }
      }
    },
    "month_5": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_7": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_10",
                "Topic_3",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_11",
                "Topic_1",
                "Topic_5"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_3",
                "Topic_11",
                "Topic_2",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_12",
                "Topic_4",
                "Topic_5",
                "Topic_9",
                "Topic_10"
              ]
            },
            "total_topic_count": 23
          },
          "physics": {
            "chapters": {
              "Chapter_2": [
                "Topic_3",
                "Topic_9",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_6",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7",
                "Topic_12",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_10",
                "Topic_11",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 23
          },
          "chemistry": {
            "chapters": {
              "Chapter_7": [
                "Topic_3",
                "Topic_5",
                "Topic_2",
                "Topic_4",
                "Topic_8",
                "Topic_1",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_4",
                "Topic_6",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 23
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_7": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_10",
                "Topic_3",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_11",
                "Topic_1",
                "Topic_5"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_3",
                "Topic_11",
                "Topic_2",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_12",
                "Topic_4",
                "Topic_5",
                "Topic_9",
                "Topic_10"
              ]
            },
            "total_topic_count": 23
          },
          "physics": {
            "chapters": {
              "Chapter_2": [
                "Topic_3",
                "Topic_9",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_6",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7",
                "Topic_12",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_10",
                "Topic_11",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 23
          },
          "chemistry": {
            "chapters": {
              "Chapter_7": [
                "Topic_3",
                "Topic_5",
                "Topic_2",
                "Topic_4",
                "Topic_8",
                "Topic_1",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_4",
                "Topic_6",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 23
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_7": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_10",
                "Topic_3",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_11",
                "Topic_1",
                "Topic_5"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_3",
                "Topic_11",
                "Topic_2",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_12",
                "Topic_4",
                "Topic_5",
                "Topic_9",
                "Topic_10"
              ]
            },
            "total_topic_count": 23
          },
          "physics": {
            "chapters": {
              "Chapter_2": [
                "Topic_3",
                "Topic_9",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_6",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7",
                "Topic_12",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_10",
                "Topic_11",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 23
          },
          "chemistry": {
            "chapters": {
              "Chapter_7": [
                "Topic_3",
                "Topic_5",
                "Topic_2",
                "Topic_4",
                "Topic_8",
                "Topic_1",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_4",
                "Topic_6",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 23
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_7": [
                "Topic_2",
                "Topic_4",
                "Topic_6",
                "Topic_10",
                "Topic_3",
                "Topic_7",
                "Topic_8",
                "Topic_9",
                "Topic_11",
                "Topic_1",
                "Topic_5"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_3",
                "Topic_11",
                "Topic_2",
                "Topic_6",
                "Topic_7",
                "Topic_8",
                "Topic_12",
                "Topic_4",
                "Topic_5",
                "Topic_9",
                "Topic_10"
              ]
            },
            "total_topic_count": 23
          },
          "physics": {
            "chapters": {
              "Chapter_2": [
                "Topic_3",
                "Topic_9",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_7",
                "Topic_8",
                "Topic_6",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_7",
                "Topic_12",
                "Topic_3",
                "Topic_5",
                "Topic_6",
                "Topic_10",
                "Topic_11",
                "Topic_8",
                "Topic_9"
              ]
            },
            "total_topic_count": 23
          },
          "chemistry": {
            "chapters": {
              "Chapter_7": [
                "Topic_3",
                "Topic_5",
                "Topic_2",
                "Topic_4",
                "Topic_8",
                "Topic_1",
                "Topic_6",
                "Topic_7",
                "Topic_9",
                "Topic_10",
                "Topic_11"
              ],
              "Chapter_12": [
                "Topic_1",
                "Topic_5",
                "Topic_7",
                "Topic_4",
                "Topic_6",
                "Topic_8",
                "Topic_9",
                "Topic_10",
                "Topic_11",
                "Topic_12",
                "Topic_2",
                "Topic_3"
              ]
            },
            "total_topic_count": 23
          }
        }
      }
    },
    "month_6": {
      "week 1": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_5": [
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ],
              "Chapter_3": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 15
          },
          "physics": {
            "chapters": {
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ],
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
              ]
            },
            "total_topic_count": 15
          },
          "chemistry": {
            "chapters": {
              "Chapter_5": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_7"
              ],
              "Chapter_3": [
                "Topic_7",
                "Topic_8",
                "Topic_3",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 15
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_5": [
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ],
              "Chapter_3": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 15
          },
          "physics": {
            "chapters": {
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ],
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
              ]
            },
            "total_topic_count": 15
          },
          "chemistry": {
            "chapters": {
              "Chapter_5": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_7"
              ],
              "Chapter_3": [
                "Topic_7",
                "Topic_8",
                "Topic_3",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 15
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_5": [
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ],
              "Chapter_3": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 15
          },
          "physics": {
            "chapters": {
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ],
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
              ]
            },
            "total_topic_count": 15
          },
          "chemistry": {
            "chapters": {
              "Chapter_5": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_7"
              ],
              "Chapter_3": [
                "Topic_7",
                "Topic_8",
                "Topic_3",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 15
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_5": [
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ],
              "Chapter_3": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_7"
              ]
            },
            "total_topic_count": 15
          },
          "physics": {
            "chapters": {
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ],
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
              ]
            },
            "total_topic_count": 15
          },
          "chemistry": {
            "chapters": {
              "Chapter_5": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_7"
              ],
              "Chapter_3": [
                "Topic_7",
                "Topic_8",
                "Topic_3",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_6"
              ]
            },
            "total_topic_count": 15
          }
        }
      }
    }
  }
}

================================================================================
✅ NEW SCORE-ORIENTED PLAN DISPLAY COMPLETE
================================================================================

2025-08-12 15:02:58,475 - app.new_score_oriented_graph - INFO - New Score-Oriented Feedback Counsellor executing
2025-08-12 15:02:58,476 - app.new_score_oriented_graph - INFO - Processing user message: change my target score to  255
2025-08-12 15:02:58,476 - app.new_score_oriented_graph - INFO - User change request detected, routing to feedback supervisor
2025-08-12 15:02:58,477 - app.new_score_oriented_graph - INFO - New Score-Oriented Feedback Supervisor executing
2025-08-12 15:02:58,477 - app.new_score_oriented_graph - INFO - Analyzing feedback request:
2025-08-12 15:03:08,627 - app.new_score_oriented_graph - INFO - Supervisor analysis completed: 4970 characters
2025-08-12 15:03:08,627 - app.new_score_oriented_graph - INFO - Analysis complete, routing back to feedback counsellor for user decision
2025-08-12 15:03:08,628 - app.new_score_oriented_graph - INFO - New Score-Oriented Feedback Counsellor Continue executing
2025-08-12 15:03:08,628 - app.new_score_oriented_graph - INFO - Feedback processed, finalizing plan
INFO:     127.0.0.1:65218 - "POST /chat HTTP/1.1" 200 OK

```