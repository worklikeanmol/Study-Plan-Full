```✅ NEW SCORE-ORIENTED PLAN DISPLAY COMPLETE
================================================================================

INFO:     127.0.0.1:65470 - "POST /chat HTTP/1.1" 200 OK
INFO:     127.0.0.1:65478 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:65479 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:65479 - "POST /score/validate-exam-date HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:65478 - "POST /score/validate-exam-date HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:65478 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:65479 - "GET /docs HTTP/1.1" 200 OK
2025-08-12 15:15:29,414 - app.main - INFO - Received chat message from user: user_5oar134id
2025-08-12 15:15:29,416 - app.regen_tools - INFO - Checking if user exists: user_5oar134id
2025-08-12 15:15:29,571 - app.regen_tools - INFO - User user_5oar134id found in database
2025-08-12 15:15:29,571 - app.main - INFO - User existence check for user_5oar134id: exists=True, has_study_plan=False, treating_as_existing=False
2025-08-12 15:15:29,572 - app.main - INFO - New user detected: user_5oar134id - routing to normal flow
2025-08-12 15:15:29,712 - app.main - INFO - Retrieved stored form data for user: user_5oar134id
2025-08-12 15:15:29,712 - app.main - INFO - Using stored form data for user: user_5oar134id
2025-08-12 15:15:29,713 - app.new_score_oriented_tools - INFO - Exam date validation: {'is_valid': True, 'calculated_months': 8, 'exam_date': '2026-04-12', 'minimum_required': 6, 'message': 'Exam date is 8 months away. Valid for new_score_oriented plan.'}
2025-08-12 15:15:29,714 - app.main - INFO - Handling feedback for existing new_score_oriented plan: user_5oar134id
2025-08-12 15:15:29,714 - app.main - INFO - Processing new_score_oriented feedback: change target score to 210
2025-08-12 15:15:29,714 - app.main - INFO - Routing to feedback_counsellor for user message: change target score to 210
2025-08-12 15:15:29,715 - app.new_score_oriented_graph - INFO - Counsellor Generator Agent executing for new_score_oriented plan
2025-08-12 15:15:29,716 - app.new_score_oriented_tools - INFO - Exam date validation: {'is_valid': True, 'calculated_months': 8, 'exam_date': '2026-04-12', 'minimum_required': 6, 'message': 'Exam date is 8 months away. Valid for new_score_oriented plan.'}
2025-08-12 15:15:29,716 - app.new_score_oriented_graph - INFO - New Score-Oriented Requirement Extractor executing
2025-08-12 15:15:33,700 - app.new_score_oriented_graph - INFO - Requirement extraction result: success
2025-08-12 15:15:33,700 - app.new_score_oriented_graph - INFO - Extracted requirements: subject_priority=['physics', 'chemistry', 'mathematics'] chapter_coverage={} time_allocation={}
2025-08-12 15:15:33,700 - app.new_score_oriented_graph - INFO - RevisionFlow Agent executing
2025-08-12 15:15:33,701 - app.new_score_oriented_agents - INFO - RevisionFlow Agent executing: Generating complete syllabus coverage plan
2025-08-12 15:15:33,701 - app.new_score_oriented_agents - INFO - Processing new_score_oriented plan for target: 190/300
2025-08-12 15:15:33,701 - app.new_score_oriented_agents - INFO - Processing complete syllabus for Physics
2025-08-12 15:15:33,701 - app.new_score_oriented_agents - INFO - Generating perfect dependency sequence for Physics
2025-08-12 15:15:33,701 - app.new_score_oriented_tools - INFO - Fetching chapter flow for exam: JEE Mains, subject: Physics
2025-08-12 15:15:33,781 - app.new_score_oriented_tools - INFO - Fetching chapter weightage for exam: JEE Mains, subject: Physics
2025-08-12 15:15:33,858 - app.new_score_oriented_tools - INFO - Starting enhanced dependency resolution for Physics
2025-08-12 15:15:33,859 - app.new_score_oriented_tools - INFO - Flow data: 12 chapters with dependencies
2025-08-12 15:15:33,859 - app.new_score_oriented_tools - INFO - Weightage data: 12 chapters with priorities
2025-08-12 15:15:33,859 - app.enhanced_dependency_resolver - INFO - Building comprehensive dependency graph from Chapter_Flow and Chapter_Weightage tables
2025-08-12 15:15:33,859 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_1]' for chapter 'Chapter_3' not found in chapter list
2025-08-12 15:15:33,860 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_2]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 15:15:33,860 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_3]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 15:15:33,860 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_4]' for chapter 'Chapter_7' not found in chapter list
2025-08-12 15:15:33,860 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_6]' for chapter 'Chapter_10' not found in chapter list
2025-08-12 15:15:33,861 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_5]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 15:15:33,861 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_7]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 15:15:33,861 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_1]' for chapter 'Chapter_2' not found in chapter list
2025-08-12 15:15:33,861 - app.enhanced_dependency_resolver - INFO - Dependency graph built: 12 chapters, 8 dependencies
2025-08-12 15:15:33,861 - app.enhanced_dependency_resolver - INFO - Starting strict dependency resolution for Physics
2025-08-12 15:15:33,861 - app.enhanced_dependency_resolver - WARNING - Some chapters could not be resolved due to dependency cycles: {'Chapter_5', 'Chapter_3', 'Chapter_10', 'Chapter_2', 'Chapter_12', 'Chapter_7'}
2025-08-12 15:15:33,862 - app.enhanced_dependency_resolver - INFO - Strict dependency resolution completed for Physics: 12 chapters
2025-08-12 15:15:33,862 - app.enhanced_dependency_resolver - INFO - Enhanced dependency resolution completed for Physics: 12 chapters with strict dependency ordering
2025-08-12 15:15:33,862 - app.new_score_oriented_tools - INFO - Enhanced dependency resolution for Physics:
2025-08-12 15:15:33,862 - app.new_score_oriented_tools - INFO -   Total chapters: 12
2025-08-12 15:15:33,863 - app.new_score_oriented_tools - INFO -   Chapters with dependencies: 6
2025-08-12 15:15:33,863 - app.new_score_oriented_tools - INFO -   All dependencies satisfied: True
2025-08-12 15:15:33,863 - app.new_score_oriented_tools - INFO - Final chapter order (dependencies first):
2025-08-12 15:15:33,863 - app.new_score_oriented_tools - INFO -    1. Chapter_9 (no dependencies) - Priority: 44.3
2025-08-12 15:15:33,863 - app.new_score_oriented_tools - INFO -    2. Chapter_8 (no dependencies) - Priority: 38.2
2025-08-12 15:15:33,863 - app.new_score_oriented_tools - INFO -    3. Chapter_11 (no dependencies) - Priority: 15.6
2025-08-12 15:15:33,863 - app.new_score_oriented_tools - INFO -    4. Chapter_4 (no dependencies) - Priority: 3.4
2025-08-12 15:15:33,863 - app.new_score_oriented_tools - INFO -    5. Chapter_6 (no dependencies) - Priority: 2.3
2025-08-12 15:15:33,864 - app.new_score_oriented_tools - INFO -    6. Chapter_1 (no dependencies) - Priority: 0.9
2025-08-12 15:15:33,864 - app.new_score_oriented_tools - INFO -    7. Chapter_5 (depends on: [Chapter_2], [Chapter_3]) - Priority: 41.9
2025-08-12 15:15:33,864 - app.new_score_oriented_tools - INFO -    8. Chapter_3 (depends on: [Chapter_1]) - Priority: 0.9
2025-08-12 15:15:33,864 - app.new_score_oriented_tools - INFO -    9. Chapter_10 (depends on: [Chapter_6]) - Priority: 22.6
2025-08-12 15:15:33,864 - app.new_score_oriented_tools - INFO -   10. Chapter_2 (depends on: [Chapter_1]) - Priority: 44.0
2025-08-12 15:15:33,864 - app.new_score_oriented_tools - INFO -   11. Chapter_12 (depends on: [Chapter_5], [Chapter_7]) - Priority: 22.6
2025-08-12 15:15:33,864 - app.new_score_oriented_tools - INFO -   12. Chapter_7 (depends on: [Chapter_4]) - Priority: 11.7
2025-08-12 15:15:33,864 - app.new_score_oriented_tools - INFO - Critical path: [Chapter_2] → Chapter_5
2025-08-12 15:15:33,864 - app.new_score_oriented_tools - INFO - Optimization suggestions:
2025-08-12 15:15:33,864 - app.new_score_oriented_tools - INFO -   • Consider parallel study tracks for efficiency: 3 groups of independent chapters identified
2025-08-12 15:15:33,865 - app.new_score_oriented_tools - INFO - ✅ All dependencies perfectly satisfied!
2025-08-12 15:15:33,865 - app.new_score_oriented_agents - INFO - Applying user preferences to dependency-resolved order for Physics
2025-08-12 15:15:33,865 - app.new_score_oriented_agents - INFO - User preferences applied to 12 chapters while maintaining dependencies
2025-08-12 15:15:33,865 - app.new_score_oriented_agents - INFO - Perfect dependency sequence generated for Physics: 12 chapters
2025-08-12 15:15:33,865 - app.new_score_oriented_agents - INFO - Dependency-first ordering applied successfully
2025-08-12 15:15:33,865 - app.new_score_oriented_agents - INFO - Ensuring 100% coverage for all chapters
2025-08-12 15:15:33,865 - app.new_score_oriented_agents - INFO - Processing complete syllabus for Chemistry
2025-08-12 15:15:33,865 - app.new_score_oriented_agents - INFO - Generating perfect dependency sequence for Chemistry
2025-08-12 15:15:33,866 - app.new_score_oriented_tools - INFO - Fetching chapter flow for exam: JEE Mains, subject: Chemistry
2025-08-12 15:15:33,933 - app.new_score_oriented_tools - INFO - Fetching chapter weightage for exam: JEE Mains, subject: Chemistry
2025-08-12 15:15:33,996 - app.new_score_oriented_tools - INFO - Starting enhanced dependency resolution for Chemistry
2025-08-12 15:15:33,997 - app.new_score_oriented_tools - INFO - Flow data: 12 chapters with dependencies
2025-08-12 15:15:33,997 - app.new_score_oriented_tools - INFO - Weightage data: 12 chapters with priorities
2025-08-12 15:15:33,998 - app.enhanced_dependency_resolver - INFO - Building comprehensive dependency graph from Chapter_Flow and Chapter_Weightage tables
2025-08-12 15:15:33,998 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_1]' for chapter 'Chapter_3' not found in chapter list
2025-08-12 15:15:33,999 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_2]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 15:15:33,999 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_3]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 15:15:33,999 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_4]' for chapter 'Chapter_7' not found in chapter list
2025-08-12 15:15:34,000 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_6]' for chapter 'Chapter_10' not found in chapter list
2025-08-12 15:15:34,000 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_5]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 15:15:34,000 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_7]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 15:15:34,001 - app.enhanced_dependency_resolver - INFO - Dependency graph built: 12 chapters, 7 dependencies
2025-08-12 15:15:34,001 - app.enhanced_dependency_resolver - INFO - Starting strict dependency resolution for Chemistry
2025-08-12 15:15:34,001 - app.enhanced_dependency_resolver - WARNING - Some chapters could not be resolved due to dependency cycles: {'Chapter_5', 'Chapter_3', 'Chapter_10', 'Chapter_12', 'Chapter_7'}
2025-08-12 15:15:34,002 - app.enhanced_dependency_resolver - INFO - Strict dependency resolution completed for Chemistry: 12 chapters
2025-08-12 15:15:34,002 - app.enhanced_dependency_resolver - INFO - Enhanced dependency resolution completed for Chemistry: 12 chapters with strict dependency ordering
2025-08-12 15:15:34,002 - app.new_score_oriented_tools - INFO - Enhanced dependency resolution for Chemistry:
2025-08-12 15:15:34,003 - app.new_score_oriented_tools - INFO -   Total chapters: 12
2025-08-12 15:15:34,003 - app.new_score_oriented_tools - INFO -   Chapters with dependencies: 5
2025-08-12 15:15:34,003 - app.new_score_oriented_tools - INFO -   All dependencies satisfied: True
2025-08-12 15:15:34,003 - app.new_score_oriented_tools - INFO - Final chapter order (dependencies first):
2025-08-12 15:15:34,003 - app.new_score_oriented_tools - INFO -    1. Chapter_8 (no dependencies) - Priority: 42.4
2025-08-12 15:15:34,003 - app.new_score_oriented_tools - INFO -    2. Chapter_1 (no dependencies) - Priority: 37.0
2025-08-12 15:15:34,003 - app.new_score_oriented_tools - INFO -    3. Chapter_4 (no dependencies) - Priority: 20.0
2025-08-12 15:15:34,003 - app.new_score_oriented_tools - INFO -    4. Chapter_9 (no dependencies) - Priority: 15.8
2025-08-12 15:15:34,003 - app.new_score_oriented_tools - INFO -    5. Chapter_11 (no dependencies) - Priority: 6.0
2025-08-12 15:15:34,004 - app.new_score_oriented_tools - INFO -    6. Chapter_6 (no dependencies) - Priority: 2.3
2025-08-12 15:15:34,004 - app.new_score_oriented_tools - INFO -    7. Chapter_2 (no dependencies) - Priority: 0.6
2025-08-12 15:15:34,004 - app.new_score_oriented_tools - INFO -    8. Chapter_5 (depends on: [Chapter_2], [Chapter_3]) - Priority: 18.0
2025-08-12 15:15:34,004 - app.new_score_oriented_tools - INFO -    9. Chapter_3 (depends on: [Chapter_1]) - Priority: 33.9
2025-08-12 15:15:34,005 - app.new_score_oriented_tools - INFO -   10. Chapter_10 (depends on: [Chapter_6]) - Priority: 45.1
2025-08-12 15:15:34,005 - app.new_score_oriented_tools - INFO -   11. Chapter_12 (depends on: [Chapter_5], [Chapter_7]) - Priority: 3.1
2025-08-12 15:15:34,005 - app.new_score_oriented_tools - INFO -   12. Chapter_7 (depends on: [Chapter_4]) - Priority: 16.6
2025-08-12 15:15:34,005 - app.new_score_oriented_tools - INFO - Critical path: [Chapter_2] → Chapter_5
2025-08-12 15:15:34,005 - app.new_score_oriented_tools - INFO - Optimization suggestions:
2025-08-12 15:15:34,005 - app.new_score_oriented_tools - INFO -   • Consider parallel study tracks for efficiency: 3 groups of independent chapters identified
2025-08-12 15:15:34,005 - app.new_score_oriented_tools - INFO - ✅ All dependencies perfectly satisfied!
2025-08-12 15:15:34,005 - app.new_score_oriented_agents - INFO - Applying user preferences to dependency-resolved order for Chemistry
2025-08-12 15:15:34,005 - app.new_score_oriented_agents - INFO - User preferences applied to 12 chapters while maintaining dependencies
2025-08-12 15:15:34,005 - app.new_score_oriented_agents - INFO - Perfect dependency sequence generated for Chemistry: 12 chapters
2025-08-12 15:15:34,006 - app.new_score_oriented_agents - INFO - Dependency-first ordering applied successfully
2025-08-12 15:15:34,006 - app.new_score_oriented_agents - INFO - Ensuring 100% coverage for all chapters
2025-08-12 15:15:34,006 - app.new_score_oriented_agents - INFO - Processing complete syllabus for Mathematics
2025-08-12 15:15:34,006 - app.new_score_oriented_agents - INFO - Generating perfect dependency sequence for Mathematics
2025-08-12 15:15:34,008 - app.new_score_oriented_tools - INFO - Fetching chapter flow for exam: JEE Mains, subject: Mathematics
2025-08-12 15:15:34,081 - app.new_score_oriented_tools - INFO - Fetching chapter weightage for exam: JEE Mains, subject: Mathematics
2025-08-12 15:15:34,163 - app.new_score_oriented_tools - INFO - Starting enhanced dependency resolution for Mathematics
2025-08-12 15:15:34,163 - app.new_score_oriented_tools - INFO - Flow data: 12 chapters with dependencies
2025-08-12 15:15:34,164 - app.new_score_oriented_tools - INFO - Weightage data: 12 chapters with priorities
2025-08-12 15:15:34,164 - app.enhanced_dependency_resolver - INFO - Building comprehensive dependency graph from Chapter_Flow and Chapter_Weightage tables
2025-08-12 15:15:34,164 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_1]' for chapter 'Chapter_3' not found in chapter list
2025-08-12 15:15:34,165 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_2]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 15:15:34,165 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_3]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 15:15:34,166 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_4]' for chapter 'Chapter_7' not found in chapter list
2025-08-12 15:15:34,166 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_6]' for chapter 'Chapter_10' not found in chapter list
2025-08-12 15:15:34,166 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_5]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 15:15:34,167 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_7]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 15:15:34,167 - app.enhanced_dependency_resolver - INFO - Dependency graph built: 12 chapters, 7 dependencies
2025-08-12 15:15:34,167 - app.enhanced_dependency_resolver - INFO - Starting strict dependency resolution for Mathematics
2025-08-12 15:15:34,167 - app.enhanced_dependency_resolver - WARNING - Some chapters could not be resolved due to dependency cycles: {'Chapter_5', 'Chapter_3', 'Chapter_10', 'Chapter_12', 'Chapter_7'}
2025-08-12 15:15:34,168 - app.enhanced_dependency_resolver - INFO - Strict dependency resolution completed for Mathematics: 12 chapters
2025-08-12 15:15:34,168 - app.enhanced_dependency_resolver - INFO - Enhanced dependency resolution completed for Mathematics: 12 chapters with strict dependency ordering
2025-08-12 15:15:34,168 - app.new_score_oriented_tools - INFO - Enhanced dependency resolution for Mathematics:
2025-08-12 15:15:34,168 - app.new_score_oriented_tools - INFO -   Total chapters: 12
2025-08-12 15:15:34,169 - app.new_score_oriented_tools - INFO -   Chapters with dependencies: 5
2025-08-12 15:15:34,169 - app.new_score_oriented_tools - INFO -   All dependencies satisfied: True
2025-08-12 15:15:34,169 - app.new_score_oriented_tools - INFO - Final chapter order (dependencies first):
2025-08-12 15:15:34,169 - app.new_score_oriented_tools - INFO -    1. Chapter_2 (no dependencies) - Priority: 42.9
2025-08-12 15:15:34,169 - app.new_score_oriented_tools - INFO -    2. Chapter_1 (no dependencies) - Priority: 37.5
2025-08-12 15:15:34,169 - app.new_score_oriented_tools - INFO -    3. Chapter_8 (no dependencies) - Priority: 34.2
2025-08-12 15:15:34,169 - app.new_score_oriented_tools - INFO -    4. Chapter_6 (no dependencies) - Priority: 32.3
2025-08-12 15:15:34,170 - app.new_score_oriented_tools - INFO -    5. Chapter_11 (no dependencies) - Priority: 21.0
2025-08-12 15:15:34,170 - app.new_score_oriented_tools - INFO -    6. Chapter_4 (no dependencies) - Priority: 16.5
2025-08-12 15:15:34,170 - app.new_score_oriented_tools - INFO -    7. Chapter_9 (no dependencies) - Priority: 15.8
2025-08-12 15:15:34,170 - app.new_score_oriented_tools - INFO -    8. Chapter_5 (depends on: [Chapter_2], [Chapter_3]) - Priority: 5.8
2025-08-12 15:15:34,170 - app.new_score_oriented_tools - INFO -    9. Chapter_3 (depends on: [Chapter_1]) - Priority: 12.6
2025-08-12 15:15:34,170 - app.new_score_oriented_tools - INFO -   10. Chapter_10 (depends on: [Chapter_6]) - Priority: 5.0
2025-08-12 15:15:34,170 - app.new_score_oriented_tools - INFO -   11. Chapter_12 (depends on: [Chapter_5], [Chapter_7]) - Priority: 2.1
2025-08-12 15:15:34,170 - app.new_score_oriented_tools - INFO -   12. Chapter_7 (depends on: [Chapter_4]) - Priority: 3.9
2025-08-12 15:15:34,170 - app.new_score_oriented_tools - INFO - Critical path: [Chapter_2] → Chapter_5
2025-08-12 15:15:34,171 - app.new_score_oriented_tools - INFO - Optimization suggestions:
2025-08-12 15:15:34,171 - app.new_score_oriented_tools - INFO -   • Consider parallel study tracks for efficiency: 3 groups of independent chapters identified
2025-08-12 15:15:34,171 - app.new_score_oriented_tools - INFO - ✅ All dependencies perfectly satisfied!
2025-08-12 15:15:34,171 - app.new_score_oriented_agents - INFO - Applying user preferences to dependency-resolved order for Mathematics
2025-08-12 15:15:34,171 - app.new_score_oriented_agents - INFO - User preferences applied to 12 chapters while maintaining dependencies
2025-08-12 15:15:34,171 - app.new_score_oriented_agents - INFO - Perfect dependency sequence generated for Mathematics: 12 chapters
2025-08-12 15:15:34,172 - app.new_score_oriented_agents - INFO - Dependency-first ordering applied successfully
2025-08-12 15:15:34,172 - app.new_score_oriented_agents - INFO - Ensuring 100% coverage for all chapters
2025-08-12 15:15:34,172 - app.new_score_oriented_agents - INFO - Distributing syllabus across 6 months (total: 8)
2025-08-12 15:15:34,172 - app.new_score_oriented_agents - INFO - Starting enhanced features generation...
2025-08-12 15:15:34,172 - app.new_score_oriented_agents - INFO - Generating enhanced features for new_score_oriented plan
2025-08-12 15:15:34,172 - app.new_score_oriented_agents - INFO - Monthly chapters data prepared: ['month_1', 'month_2', 'month_3', 'month_4', 'month_5', 'month_6']
2025-08-12 15:15:34,172 - app.new_score_oriented_agents - INFO - Sample month data structure: {'physics': ['Chapter_9', 'Chapter_8'], 'chemistry': ['Chapter_8', 'Chapter_1'], 'mathematics': ['Chapter_2', 'Chapter_1']}
2025-08-12 15:15:34,173 - app.enhanced_new_score_oriented_tools - INFO - Calculating monthly target scores for user target: 190/300
2025-08-12 15:15:34,575 - app.enhanced_new_score_oriented_tools - INFO - month_1: Achievable=80.75, Target=51.14
2025-08-12 15:15:34,998 - app.enhanced_new_score_oriented_tools - INFO - month_2: Achievable=51.24, Target=32.45
2025-08-12 15:15:35,425 - app.enhanced_new_score_oriented_tools - INFO - month_3: Achievable=30.37, Target=19.23
2025-08-12 15:15:35,828 - app.enhanced_new_score_oriented_tools - INFO - month_4: Achievable=38.16, Target=24.17
2025-08-12 15:15:36,222 - app.enhanced_new_score_oriented_tools - INFO - month_5: Achievable=63.59, Target=40.27
2025-08-12 15:15:36,647 - app.enhanced_new_score_oriented_tools - INFO - month_6: Achievable=34.57, Target=21.89
2025-08-12 15:15:36,647 - app.enhanced_new_score_oriented_tools - INFO - Monthly target calculation completed: 6 months processed
2025-08-12 15:15:36,648 - app.enhanced_new_score_oriented_tools - INFO - Generating extended months plan: 8 total, 6 for syllabus
2025-08-12 15:15:36,648 - app.enhanced_new_score_oriented_tools - INFO - Extended months plan generated: 2 months of intensive practice
2025-08-12 15:15:36,649 - app.enhanced_new_score_oriented_tools - INFO - Generating weekly topic breakdown for 6 months
2025-08-12 15:15:39,034 - app.enhanced_new_score_oriented_tools - INFO - Weekly topic breakdown generated for 6 months
2025-08-12 15:15:39,035 - app.enhanced_new_score_oriented_tools - INFO - Creating comprehensive weekend schedule for 8 months
2025-08-12 15:15:39,035 - app.enhanced_new_score_oriented_tools - INFO - Comprehensive weekend schedule created for 8 months
2025-08-12 15:15:39,035 - app.new_score_oriented_agents - INFO - Enhanced features generated successfully
2025-08-12 15:15:39,035 - app.new_score_oriented_agents - INFO - Enhanced features generated: ['monthly_target_scores', 'extended_months_plan', 'weekly_topic_breakdown', 'weekend_schedule', 'strategy_summary']
2025-08-12 15:15:39,036 - app.new_score_oriented_agents - INFO - RevisionFlow plan generated with 6 months for syllabus completion
2025-08-12 15:15:39,036 - app.new_score_oriented_graph - INFO - Generator Validator Agent executing
2025-08-12 15:15:39,036 - app.new_score_oriented_agents - INFO - Validating chapter coverage for new_score_oriented plan
2025-08-12 15:15:39,037 - app.new_score_oriented_graph - INFO - Topic Agent executing
2025-08-12 15:15:39,037 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_9
2025-08-12 15:15:39,106 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_8
2025-08-12 15:15:39,167 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_11
2025-08-12 15:15:39,235 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_4
2025-08-12 15:15:39,304 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_6
2025-08-12 15:15:39,390 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_1
2025-08-12 15:15:39,462 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_5
2025-08-12 15:15:39,616 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_3
2025-08-12 15:15:39,681 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_10
2025-08-12 15:15:39,747 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_2
2025-08-12 15:15:39,817 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_12
2025-08-12 15:15:39,875 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_7
2025-08-12 15:15:39,935 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_8
2025-08-12 15:15:39,999 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_1
2025-08-12 15:15:40,063 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_4
2025-08-12 15:15:40,122 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_9
2025-08-12 15:15:40,182 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_11
2025-08-12 15:15:40,275 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_6
2025-08-12 15:15:40,340 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_2
2025-08-12 15:15:40,396 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_5
2025-08-12 15:15:40,457 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_3
2025-08-12 15:15:40,517 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_10
2025-08-12 15:15:40,582 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_12
2025-08-12 15:15:40,670 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_7
2025-08-12 15:15:40,752 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_2
2025-08-12 15:15:40,810 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_1
2025-08-12 15:15:40,867 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_8
2025-08-12 15:15:40,931 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_6
2025-08-12 15:15:40,998 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_11
2025-08-12 15:15:41,056 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_4
2025-08-12 15:15:41,127 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_9
2025-08-12 15:15:41,192 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_5
2025-08-12 15:15:41,257 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_3
2025-08-12 15:15:41,329 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_10
2025-08-12 15:15:41,398 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_12
2025-08-12 15:15:41,459 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_7
2025-08-12 15:15:41,518 - app.new_score_oriented_graph - INFO - Topic Validator Agent executing
2025-08-12 15:15:41,518 - app.new_score_oriented_agents - INFO - Validating topic coverage for new_score_oriented plan
2025-08-12 15:15:41,519 - app.new_score_oriented_agents - INFO - Performing final syllabus compliance validation
2025-08-12 15:15:41,520 - app.new_score_oriented_graph - INFO - Supervisor Agent executing
2025-08-12 15:15:41,520 - app.new_score_oriented_agents - INFO - Supervising new_score_oriented plan for target achievement
2025-08-12 15:15:41,521 - app.new_score_oriented_graph - INFO - Finalizing new_score_oriented study plan with enhanced calendar features

================================================================================
🎯 NEW SCORE-ORIENTED STUDY PLAN - DETAILED BREAKDOWN
================================================================================
2025-08-12 to 2026-04-09 | Target: 190/300

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
63.3% of target
80.8
Total Achievable Score
51.1
Your Target Score
Efficiency Required
63.3%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_9', 'Chapter_8'], 'subject_weightage': 27.51, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_8', 'Chapter_1'], 'subject_weightage': 26.46, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_2', 'Chapter_1'], 'subject_weightage': 26.78, 'chapter_count': 2}

Month 2
63.3% of target
51.2
Total Achievable Score
32.5
Your Target Score
Efficiency Required
63.3%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_11', 'Chapter_4'], 'subject_weightage': 11.15, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_4', 'Chapter_9'], 'subject_weightage': 17.91, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_8', 'Chapter_6'], 'subject_weightage': 22.18, 'chapter_count': 2}

Month 3
63.3% of target
30.4
Total Achievable Score
19.2
Your Target Score
Efficiency Required
63.3%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_6', 'Chapter_1'], 'subject_weightage': 3.26, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_11', 'Chapter_6'], 'subject_weightage': 8.36, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_11', 'Chapter_4'], 'subject_weightage': 18.75, 'chapter_count': 2}

Month 4
63.3% of target
38.2
Total Achievable Score
24.2
Your Target Score
Efficiency Required
63.3%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_5', 'Chapter_3'], 'subject_weightage': 14.92, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_2', 'Chapter_5'], 'subject_weightage': 9.55, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_9', 'Chapter_5'], 'subject_weightage': 13.69, 'chapter_count': 2}

Month 5
63.3% of target
63.6
Total Achievable Score
40.3
Your Target Score
Efficiency Required
63.3%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_10', 'Chapter_2'], 'subject_weightage': 26.0, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_3', 'Chapter_10'], 'subject_weightage': 26.32, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_3', 'Chapter_10'], 'subject_weightage': 11.27, 'chapter_count': 2}

Month 6
63.3% of target
34.6
Total Achievable Score
21.9
Your Target Score
Efficiency Required
63.3%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_12', 'Chapter_7'], 'subject_weightage': 17.15, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_12', 'Chapter_7'], 'subject_weightage': 11.38, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_12', 'Chapter_7'], 'subject_weightage': 6.04, 'chapter_count': 2}

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
Chapter_5
  Topic_2
  Topic_7
  Topic_1
  Topic_3
  Topic_4
  Topic_5
  Topic_6
7 topics

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
Chapter_5
  Topic_1
  Topic_2
  Topic_5
  Topic_6
  Topic_3
  Topic_4
  Topic_7
7 topics

--- Month 5 Weekly Breakdown ---

mathematics
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

chemistry
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

--- Month 6 Weekly Breakdown ---

mathematics
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

physics
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

================================================================================
📋 JSON OUTPUT:
================================================================================
{
  "plan_info": {
    "start_date": "2025-08-12",
    "end_date": "2026-04-09",
    "target_score": "190/300",
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
      "target_ratio": "63.3% of target",
      "total_achievable_score": 80.75,
      "user_target_score": 51.14,
      "efficiency_required": "63.3%",
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
      "target_ratio": "63.3% of target",
      "total_achievable_score": 51.24,
      "user_target_score": 32.45,
      "efficiency_required": "63.3%",
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
      "target_ratio": "63.3% of target",
      "total_achievable_score": 30.37,
      "user_target_score": 19.23,
      "efficiency_required": "63.3%",
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
      "target_ratio": "63.3% of target",
      "total_achievable_score": 38.16,
      "user_target_score": 24.17,
      "efficiency_required": "63.3%",
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
            "Chapter_2",
            "Chapter_5"
          ],
          "subject_weightage": 9.55,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_9",
            "Chapter_5"
          ],
          "subject_weightage": 13.69,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 5": {
      "target_ratio": "63.3% of target",
      "total_achievable_score": 63.59,
      "user_target_score": 40.27,
      "efficiency_required": "63.3%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_10",
            "Chapter_2"
          ],
          "subject_weightage": 26.0,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_3",
            "Chapter_10"
          ],
          "subject_weightage": 26.32,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_3",
            "Chapter_10"
          ],
          "subject_weightage": 11.27,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 6": {
      "target_ratio": "63.3% of target",
      "total_achievable_score": 34.57,
      "user_target_score": 21.89,
      "efficiency_required": "63.3%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_12",
            "Chapter_7"
          ],
          "subject_weightage": 17.15,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_12",
            "Chapter_7"
          ],
          "subject_weightage": 11.38,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_12",
            "Chapter_7"
          ],
          "subject_weightage": 6.04,
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
        "Chapter_5"
      ],
      "physics": [
        "Chapter_5",
        "Chapter_3"
      ],
      "chemistry": [
        "Chapter_2",
        "Chapter_5"
      ]
    },
    "month_5": {
      "mathematics": [
        "Chapter_3",
        "Chapter_10"
      ],
      "physics": [
        "Chapter_10",
        "Chapter_2"
      ],
      "chemistry": [
        "Chapter_3",
        "Chapter_10"
      ]
    },
    "month_6": {
      "mathematics": [
        "Chapter_12",
        "Chapter_7"
      ],
      "physics": [
        "Chapter_12",
        "Chapter_7"
      ],
      "chemistry": [
        "Chapter_12",
        "Chapter_7"
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
              "Chapter_5": [
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6"
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
              "Chapter_5": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
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
              "Chapter_5": [
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6"
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
              "Chapter_5": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
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
              "Chapter_5": [
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6"
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
              "Chapter_5": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
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
              "Chapter_5": [
                "Topic_2",
                "Topic_7",
                "Topic_1",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6"
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
              "Chapter_5": [
                "Topic_1",
                "Topic_2",
                "Topic_5",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_7"
              ]
            },
            "total_topic_count": 18
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
              "Chapter_3": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_7"
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
              ]
            },
            "total_topic_count": 27
          },
          "chemistry": {
            "chapters": {
              "Chapter_3": [
                "Topic_7",
                "Topic_8",
                "Topic_3",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_6"
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
            "total_topic_count": 24
          }
        }
      },
      "week 2": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_3": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_7"
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
              ]
            },
            "total_topic_count": 27
          },
          "chemistry": {
            "chapters": {
              "Chapter_3": [
                "Topic_7",
                "Topic_8",
                "Topic_3",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_6"
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
            "total_topic_count": 24
          }
        }
      },
      "week 3": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_3": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_7"
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
              ]
            },
            "total_topic_count": 27
          },
          "chemistry": {
            "chapters": {
              "Chapter_3": [
                "Topic_7",
                "Topic_8",
                "Topic_3",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_6"
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
            "total_topic_count": 24
          }
        }
      },
      "week 4": {
        "total_pyq": 2,
        "total_dpp": 15,
        "subject_breakdown": {
          "mathematics": {
            "chapters": {
              "Chapter_3": [
                "Topic_8",
                "Topic_1",
                "Topic_2",
                "Topic_6",
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_7"
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
              ]
            },
            "total_topic_count": 27
          },
          "chemistry": {
            "chapters": {
              "Chapter_3": [
                "Topic_7",
                "Topic_8",
                "Topic_3",
                "Topic_1",
                "Topic_2",
                "Topic_4",
                "Topic_5",
                "Topic_6"
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
            "total_topic_count": 24
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
              ],
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
              ]
            },
            "total_topic_count": 23
          },
          "physics": {
            "chapters": {
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
            "total_topic_count": 23
          },
          "chemistry": {
            "chapters": {
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
              ],
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
              ],
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
              ]
            },
            "total_topic_count": 23
          },
          "physics": {
            "chapters": {
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
            "total_topic_count": 23
          },
          "chemistry": {
            "chapters": {
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
              ],
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
              ],
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
              ]
            },
            "total_topic_count": 23
          },
          "physics": {
            "chapters": {
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
            "total_topic_count": 23
          },
          "chemistry": {
            "chapters": {
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
              ],
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
              ],
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
              ]
            },
            "total_topic_count": 23
          },
          "physics": {
            "chapters": {
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
            "total_topic_count": 23
          },
          "chemistry": {
            "chapters": {
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
              ],
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
              ]
            },
            "total_topic_count": 23
          }
        }
      }
    }
  }
}

================================================================================
✅ NEW SCORE-ORIENTED PLAN DISPLAY COMPLETE
================================================================================

2025-08-12 15:15:41,579 - app.new_score_oriented_graph - INFO - New Score-Oriented Feedback Counsellor executing
2025-08-12 15:15:41,579 - app.new_score_oriented_graph - INFO - Processing user message: change target score to 210
2025-08-12 15:15:41,580 - app.new_score_oriented_graph - INFO - User change request detected, routing to feedback supervisor
2025-08-12 15:15:41,580 - app.new_score_oriented_graph - INFO - Extracted changes: {'target_score_change': 210, 'duration_change': None, 'subject_priority_change': None, 'chapter_coverage_change': None, 'other_changes': []}
2025-08-12 15:15:41,583 - app.new_score_oriented_graph - INFO - New Score-Oriented Feedback Supervisor executing
2025-08-12 15:15:41,584 - app.new_score_oriented_graph - INFO - Extracted user feedback from chat: change target score to 210
2025-08-12 15:15:41,585 - app.new_score_oriented_graph - INFO - Analyzing feedback request: change target score to 210
2025-08-12 15:16:06,801 - app.new_score_oriented_graph - INFO - Supervisor analysis completed: 12023 characters
2025-08-12 15:16:06,801 - app.new_score_oriented_graph - INFO - Analysis complete, routing back to feedback counsellor for user decision
2025-08-12 15:16:06,802 - app.new_score_oriented_graph - INFO - New Score-Oriented Feedback Counsellor Continue executing
2025-08-12 15:16:06,802 - app.new_score_oriented_graph - INFO - Feedback processed, finalizing plan
INFO:     127.0.0.1:65484 - "POST /chat HTTP/1.1" 200 OK
```