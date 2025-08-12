```
(ars) D:\StudyPlanRengen\Study-Plan-Full\Study-Plan-React-Backend>
(ars) D:\StudyPlanRengen\Study-Plan-Full\Study-Plan-React-Backend>uvicorn app.main:app --reload
INFO:     Will watch for changes in these directories: ['D:\\StudyPlanRengen\\Study-Plan-Full\\Study-Plan-React-Backend']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12352] using StatReload
2025-08-12 12:51:43,573 - app.tools - INFO - Supabase client initialized successfully.
2025-08-12 12:51:43,902 - app.regen_tools - INFO - Supabase client initialized successfully for regeneration tools.
INFO:     Started server process [20072]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:64330 - "POST /score/validate-exam-date HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:64330 - "OPTIONS /save-form HTTP/1.1" 200 OK
2025-08-12 12:51:54,722 - app.main - INFO - Saving form data for user: user_g0jpsqc1k
2025-08-12 12:51:55,345 - app.main - INFO - Created new user with form data: user_g0jpsqc1k
INFO:     127.0.0.1:64330 - "POST /save-form HTTP/1.1" 200 OK
INFO:     127.0.0.1:64330 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:64330 - "GET /docs HTTP/1.1" 200 OK
INFO:     127.0.0.1:64332 - "OPTIONS /chat HTTP/1.1" 200 OK
2025-08-12 12:52:01,230 - app.main - INFO - Received chat message from user: user_g0jpsqc1k
2025-08-12 12:52:01,235 - app.regen_tools - INFO - Checking if user exists: user_g0jpsqc1k
2025-08-12 12:52:01,598 - app.regen_tools - INFO - User user_g0jpsqc1k found in database
2025-08-12 12:52:01,598 - app.main - INFO - User existence check for user_g0jpsqc1k: exists=True, has_study_plan=False, treating_as_existing=False
2025-08-12 12:52:01,598 - app.main - INFO - New user detected: user_g0jpsqc1k - routing to normal flow
2025-08-12 12:52:01,741 - app.main - INFO - Retrieved stored form data for user: user_g0jpsqc1k
2025-08-12 12:52:01,741 - app.main - INFO - Using stored form data for user: user_g0jpsqc1k
2025-08-12 12:52:01,742 - app.new_score_oriented_tools - INFO - Exam date validation: {'is_valid': True, 'calculated_months': 7, 'exam_date': '2026-03-12', 'minimum_required': 6, 'message': 'Exam date is 7 months away. Valid for new_score_oriented plan.'}
2025-08-12 12:52:01,743 - app.new_score_oriented_graph - INFO - Counsellor Generator Agent executing for new_score_oriented plan
2025-08-12 12:52:01,744 - app.new_score_oriented_tools - INFO - Exam date validation: {'is_valid': True, 'calculated_months': 7, 'exam_date': '2026-03-12', 'minimum_required': 6, 'message': 'Exam date is 7 months away. Valid for new_score_oriented plan.'}
2025-08-12 12:52:01,744 - app.new_score_oriented_graph - INFO - RevisionFlow Agent executing
2025-08-12 12:52:01,745 - app.new_score_oriented_agents - INFO - RevisionFlow Agent executing: Generating complete syllabus coverage plan
2025-08-12 12:52:01,745 - app.new_score_oriented_agents - INFO - Processing new_score_oriented plan for target: 190/300
2025-08-12 12:52:01,745 - app.tools - INFO - Fetching syllabus for exam: JEE Mains
2025-08-12 12:52:01,910 - app.new_score_oriented_agents - INFO - Processing complete syllabus for Physics
2025-08-12 12:52:01,911 - app.tools - INFO - Fetching chapter flow for exam: JEE Mains, subject: Physics
2025-08-12 12:52:01,994 - app.tools - INFO - Fetching chapter weightage for exam: JEE Mains, subject: Physics
2025-08-12 12:52:02,096 - app.new_score_oriented_agents - INFO - Generating perfect dependency sequence for Physics
2025-08-12 12:52:02,099 - app.new_score_oriented_tools - INFO - Fetching chapter flow for exam: JEE Mains, subject: Physics
2025-08-12 12:52:02,238 - app.new_score_oriented_tools - INFO - Fetching chapter weightage for exam: JEE Mains, subject: Physics
2025-08-12 12:52:02,325 - app.new_score_oriented_tools - INFO - Starting enhanced dependency resolution for Physics
2025-08-12 12:52:02,326 - app.new_score_oriented_tools - INFO - Flow data: 12 chapters with dependencies
2025-08-12 12:52:02,326 - app.new_score_oriented_tools - INFO - Weightage data: 12 chapters with priorities
2025-08-12 12:52:02,326 - app.enhanced_dependency_resolver - INFO - Building comprehensive dependency graph from Chapter_Flow and Chapter_Weightage tables
2025-08-12 12:52:02,326 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_1]' for chapter 'Chapter_3' not found in chapter list
2025-08-12 12:52:02,327 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_2]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 12:52:02,327 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_3]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 12:52:02,327 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_4]' for chapter 'Chapter_7' not found in chapter list
2025-08-12 12:52:02,327 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_6]' for chapter 'Chapter_10' not found in chapter list
2025-08-12 12:52:02,327 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_5]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 12:52:02,327 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_7]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 12:52:02,328 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_1]' for chapter 'Chapter_2' not found in chapter list
2025-08-12 12:52:02,328 - app.enhanced_dependency_resolver - INFO - Dependency graph built: 12 chapters, 8 dependencies
2025-08-12 12:52:02,328 - app.enhanced_dependency_resolver - INFO - Starting strict dependency resolution for Physics
2025-08-12 12:52:02,328 - app.enhanced_dependency_resolver - WARNING - Some chapters could not be resolved due to dependency cycles: {'Chapter_10', 'Chapter_2', 'Chapter_3', 'Chapter_7', 'Chapter_12', 'Chapter_5'}
2025-08-12 12:52:02,328 - app.enhanced_dependency_resolver - INFO - Strict dependency resolution completed for Physics: 12 chapters
2025-08-12 12:52:02,328 - app.enhanced_dependency_resolver - INFO - Enhanced dependency resolution completed for Physics: 12 chapters with strict dependency ordering
2025-08-12 12:52:02,329 - app.new_score_oriented_tools - INFO - Enhanced dependency resolution for Physics:
2025-08-12 12:52:02,329 - app.new_score_oriented_tools - INFO -   Total chapters: 12
2025-08-12 12:52:02,329 - app.new_score_oriented_tools - INFO -   Chapters with dependencies: 6
2025-08-12 12:52:02,329 - app.new_score_oriented_tools - INFO -   All dependencies satisfied: True
2025-08-12 12:52:02,329 - app.new_score_oriented_tools - INFO - Final chapter order (dependencies first):
2025-08-12 12:52:02,329 - app.new_score_oriented_tools - INFO -    1. Chapter_9 (no dependencies) - Priority: 44.3
2025-08-12 12:52:02,329 - app.new_score_oriented_tools - INFO -    2. Chapter_8 (no dependencies) - Priority: 38.2
2025-08-12 12:52:02,330 - app.new_score_oriented_tools - INFO -    3. Chapter_11 (no dependencies) - Priority: 15.6
2025-08-12 12:52:02,330 - app.new_score_oriented_tools - INFO -    4. Chapter_4 (no dependencies) - Priority: 3.4
2025-08-12 12:52:02,330 - app.new_score_oriented_tools - INFO -    5. Chapter_6 (no dependencies) - Priority: 2.3
2025-08-12 12:52:02,330 - app.new_score_oriented_tools - INFO -    6. Chapter_1 (no dependencies) - Priority: 0.9
2025-08-12 12:52:02,330 - app.new_score_oriented_tools - INFO -    7. Chapter_10 (depends on: [Chapter_6]) - Priority: 22.6
2025-08-12 12:52:02,330 - app.new_score_oriented_tools - INFO -    8. Chapter_2 (depends on: [Chapter_1]) - Priority: 44.0
2025-08-12 12:52:02,330 - app.new_score_oriented_tools - INFO -    9. Chapter_3 (depends on: [Chapter_1]) - Priority: 0.9
2025-08-12 12:52:02,331 - app.new_score_oriented_tools - INFO -   10. Chapter_7 (depends on: [Chapter_4]) - Priority: 11.7
2025-08-12 12:52:02,331 - app.new_score_oriented_tools - INFO -   11. Chapter_12 (depends on: [Chapter_5], [Chapter_7]) - Priority: 22.6
2025-08-12 12:52:02,331 - app.new_score_oriented_tools - INFO -   12. Chapter_5 (depends on: [Chapter_2], [Chapter_3]) - Priority: 41.9
2025-08-12 12:52:02,331 - app.new_score_oriented_tools - INFO - Critical path: [Chapter_6] → Chapter_10
2025-08-12 12:52:02,331 - app.new_score_oriented_tools - INFO - Optimization suggestions:
2025-08-12 12:52:02,331 - app.new_score_oriented_tools - INFO -   • Consider parallel study tracks for efficiency: 3 groups of independent chapters identified
2025-08-12 12:52:02,331 - app.new_score_oriented_tools - INFO - ✅ All dependencies perfectly satisfied!
2025-08-12 12:52:02,332 - app.new_score_oriented_agents - INFO - Applying user preferences to dependency-resolved order for Physics
2025-08-12 12:52:02,332 - app.new_score_oriented_agents - INFO - User preferences applied to 12 chapters while maintaining dependencies
2025-08-12 12:52:02,332 - app.new_score_oriented_agents - INFO - Perfect dependency sequence generated for Physics: 12 chapters
2025-08-12 12:52:02,332 - app.new_score_oriented_agents - INFO - Dependency-first ordering applied successfully
2025-08-12 12:52:02,332 - app.new_score_oriented_agents - INFO - Ensuring 100% coverage for all chapters
2025-08-12 12:52:02,333 - app.new_score_oriented_agents - INFO - Processing complete syllabus for Chemistry
2025-08-12 12:52:02,334 - app.tools - INFO - Fetching chapter flow for exam: JEE Mains, subject: Chemistry
2025-08-12 12:52:02,411 - app.tools - INFO - Fetching chapter weightage for exam: JEE Mains, subject: Chemistry
2025-08-12 12:52:02,495 - app.new_score_oriented_agents - INFO - Generating perfect dependency sequence for Chemistry
2025-08-12 12:52:02,496 - app.new_score_oriented_tools - INFO - Fetching chapter flow for exam: JEE Mains, subject: Chemistry
2025-08-12 12:52:02,571 - app.new_score_oriented_tools - INFO - Fetching chapter weightage for exam: JEE Mains, subject: Chemistry
2025-08-12 12:52:02,648 - app.new_score_oriented_tools - INFO - Starting enhanced dependency resolution for Chemistry
2025-08-12 12:52:02,648 - app.new_score_oriented_tools - INFO - Flow data: 12 chapters with dependencies
2025-08-12 12:52:02,648 - app.new_score_oriented_tools - INFO - Weightage data: 12 chapters with priorities
2025-08-12 12:52:02,648 - app.enhanced_dependency_resolver - INFO - Building comprehensive dependency graph from Chapter_Flow and Chapter_Weightage tables
2025-08-12 12:52:02,649 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_1]' for chapter 'Chapter_3' not found in chapter list
2025-08-12 12:52:02,649 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_2]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 12:52:02,649 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_3]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 12:52:02,649 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_4]' for chapter 'Chapter_7' not found in chapter list
2025-08-12 12:52:02,649 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_6]' for chapter 'Chapter_10' not found in chapter list
2025-08-12 12:52:02,650 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_5]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 12:52:02,650 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_7]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 12:52:02,650 - app.enhanced_dependency_resolver - INFO - Dependency graph built: 12 chapters, 7 dependencies
2025-08-12 12:52:02,650 - app.enhanced_dependency_resolver - INFO - Starting strict dependency resolution for Chemistry
2025-08-12 12:52:02,650 - app.enhanced_dependency_resolver - WARNING - Some chapters could not be resolved due to dependency cycles: {'Chapter_10', 'Chapter_3', 'Chapter_7', 'Chapter_12', 'Chapter_5'}
2025-08-12 12:52:02,650 - app.enhanced_dependency_resolver - INFO - Strict dependency resolution completed for Chemistry: 12 chapters
2025-08-12 12:52:02,650 - app.enhanced_dependency_resolver - INFO - Enhanced dependency resolution completed for Chemistry: 12 chapters with strict dependency ordering
2025-08-12 12:52:02,650 - app.new_score_oriented_tools - INFO - Enhanced dependency resolution for Chemistry:
2025-08-12 12:52:02,650 - app.new_score_oriented_tools - INFO -   Total chapters: 12
2025-08-12 12:52:02,650 - app.new_score_oriented_tools - INFO -   Chapters with dependencies: 5
2025-08-12 12:52:02,651 - app.new_score_oriented_tools - INFO -   All dependencies satisfied: True
2025-08-12 12:52:02,651 - app.new_score_oriented_tools - INFO - Final chapter order (dependencies first):
2025-08-12 12:52:02,651 - app.new_score_oriented_tools - INFO -    1. Chapter_8 (no dependencies) - Priority: 42.4
2025-08-12 12:52:02,651 - app.new_score_oriented_tools - INFO -    2. Chapter_1 (no dependencies) - Priority: 37.0
2025-08-12 12:52:02,651 - app.new_score_oriented_tools - INFO -    3. Chapter_4 (no dependencies) - Priority: 20.0
2025-08-12 12:52:02,651 - app.new_score_oriented_tools - INFO -    4. Chapter_9 (no dependencies) - Priority: 15.8
2025-08-12 12:52:02,651 - app.new_score_oriented_tools - INFO -    5. Chapter_11 (no dependencies) - Priority: 6.0
2025-08-12 12:52:02,651 - app.new_score_oriented_tools - INFO -    6. Chapter_6 (no dependencies) - Priority: 2.3
2025-08-12 12:52:02,651 - app.new_score_oriented_tools - INFO -    7. Chapter_2 (no dependencies) - Priority: 0.6
2025-08-12 12:52:02,651 - app.new_score_oriented_tools - INFO -    8. Chapter_10 (depends on: [Chapter_6]) - Priority: 45.1
2025-08-12 12:52:02,651 - app.new_score_oriented_tools - INFO -    9. Chapter_3 (depends on: [Chapter_1]) - Priority: 33.9
2025-08-12 12:52:02,652 - app.new_score_oriented_tools - INFO -   10. Chapter_7 (depends on: [Chapter_4]) - Priority: 16.6
2025-08-12 12:52:02,652 - app.new_score_oriented_tools - INFO -   11. Chapter_12 (depends on: [Chapter_5], [Chapter_7]) - Priority: 3.1
2025-08-12 12:52:02,652 - app.new_score_oriented_tools - INFO -   12. Chapter_5 (depends on: [Chapter_2], [Chapter_3]) - Priority: 18.0
2025-08-12 12:52:02,652 - app.new_score_oriented_tools - INFO - Critical path: [Chapter_6] → Chapter_10
2025-08-12 12:52:02,652 - app.new_score_oriented_tools - INFO - Optimization suggestions:
2025-08-12 12:52:02,652 - app.new_score_oriented_tools - INFO -   • Consider parallel study tracks for efficiency: 3 groups of independent chapters identified
2025-08-12 12:52:02,652 - app.new_score_oriented_tools - INFO - ✅ All dependencies perfectly satisfied!
2025-08-12 12:52:02,652 - app.new_score_oriented_agents - INFO - Applying user preferences to dependency-resolved order for Chemistry
2025-08-12 12:52:02,652 - app.new_score_oriented_agents - INFO - User preferences applied to 12 chapters while maintaining dependencies
2025-08-12 12:52:02,652 - app.new_score_oriented_agents - INFO - Perfect dependency sequence generated for Chemistry: 12 chapters
2025-08-12 12:52:02,652 - app.new_score_oriented_agents - INFO - Dependency-first ordering applied successfully
2025-08-12 12:52:02,653 - app.new_score_oriented_agents - INFO - Ensuring 100% coverage for all chapters
2025-08-12 12:52:02,653 - app.new_score_oriented_agents - INFO - Processing complete syllabus for Mathematics
2025-08-12 12:52:02,654 - app.tools - INFO - Fetching chapter flow for exam: JEE Mains, subject: Mathematics
2025-08-12 12:52:02,734 - app.tools - INFO - Fetching chapter weightage for exam: JEE Mains, subject: Mathematics
2025-08-12 12:52:02,811 - app.new_score_oriented_agents - INFO - Generating perfect dependency sequence for Mathematics
2025-08-12 12:52:02,812 - app.new_score_oriented_tools - INFO - Fetching chapter flow for exam: JEE Mains, subject: Mathematics
2025-08-12 12:52:02,888 - app.new_score_oriented_tools - INFO - Fetching chapter weightage for exam: JEE Mains, subject: Mathematics
2025-08-12 12:52:02,954 - app.new_score_oriented_tools - INFO - Starting enhanced dependency resolution for Mathematics
2025-08-12 12:52:02,955 - app.new_score_oriented_tools - INFO - Flow data: 12 chapters with dependencies
2025-08-12 12:52:02,955 - app.new_score_oriented_tools - INFO - Weightage data: 12 chapters with priorities
2025-08-12 12:52:02,955 - app.enhanced_dependency_resolver - INFO - Building comprehensive dependency graph from Chapter_Flow and Chapter_Weightage tables
2025-08-12 12:52:02,955 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_1]' for chapter 'Chapter_3' not found in chapter list
2025-08-12 12:52:02,955 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_2]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 12:52:02,955 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_3]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 12:52:02,955 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_4]' for chapter 'Chapter_7' not found in chapter list
2025-08-12 12:52:02,955 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_6]' for chapter 'Chapter_10' not found in chapter list
2025-08-12 12:52:02,955 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_5]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 12:52:02,956 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_7]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 12:52:02,956 - app.enhanced_dependency_resolver - INFO - Dependency graph built: 12 chapters, 7 dependencies
2025-08-12 12:52:02,956 - app.enhanced_dependency_resolver - INFO - Starting strict dependency resolution for Mathematics
2025-08-12 12:52:02,956 - app.enhanced_dependency_resolver - WARNING - Some chapters could not be resolved due to dependency cycles: {'Chapter_10', 'Chapter_3', 'Chapter_7', 'Chapter_12', 'Chapter_5'}
2025-08-12 12:52:02,956 - app.enhanced_dependency_resolver - INFO - Strict dependency resolution completed for Mathematics: 12 chapters
2025-08-12 12:52:02,957 - app.enhanced_dependency_resolver - INFO - Enhanced dependency resolution completed for Mathematics: 12 chapters with strict dependency ordering
2025-08-12 12:52:02,957 - app.new_score_oriented_tools - INFO - Enhanced dependency resolution for Mathematics:
2025-08-12 12:52:02,957 - app.new_score_oriented_tools - INFO -   Total chapters: 12
2025-08-12 12:52:02,957 - app.new_score_oriented_tools - INFO -   Chapters with dependencies: 5
2025-08-12 12:52:02,957 - app.new_score_oriented_tools - INFO -   All dependencies satisfied: True
2025-08-12 12:52:02,957 - app.new_score_oriented_tools - INFO - Final chapter order (dependencies first):
2025-08-12 12:52:02,958 - app.new_score_oriented_tools - INFO -    1. Chapter_2 (no dependencies) - Priority: 42.9
2025-08-12 12:52:02,958 - app.new_score_oriented_tools - INFO -    2. Chapter_1 (no dependencies) - Priority: 37.5
2025-08-12 12:52:02,958 - app.new_score_oriented_tools - INFO -    3. Chapter_8 (no dependencies) - Priority: 34.2
2025-08-12 12:52:02,958 - app.new_score_oriented_tools - INFO -    4. Chapter_6 (no dependencies) - Priority: 32.3
2025-08-12 12:52:02,958 - app.new_score_oriented_tools - INFO -    5. Chapter_11 (no dependencies) - Priority: 21.0
2025-08-12 12:52:02,958 - app.new_score_oriented_tools - INFO -    6. Chapter_4 (no dependencies) - Priority: 16.5
2025-08-12 12:52:02,958 - app.new_score_oriented_tools - INFO -    7. Chapter_9 (no dependencies) - Priority: 15.8
2025-08-12 12:52:02,959 - app.new_score_oriented_tools - INFO -    8. Chapter_10 (depends on: [Chapter_6]) - Priority: 5.0
2025-08-12 12:52:02,959 - app.new_score_oriented_tools - INFO -    9. Chapter_3 (depends on: [Chapter_1]) - Priority: 12.6
2025-08-12 12:52:02,959 - app.new_score_oriented_tools - INFO -   10. Chapter_7 (depends on: [Chapter_4]) - Priority: 3.9
2025-08-12 12:52:02,959 - app.new_score_oriented_tools - INFO -   11. Chapter_12 (depends on: [Chapter_5], [Chapter_7]) - Priority: 2.1
2025-08-12 12:52:02,959 - app.new_score_oriented_tools - INFO -   12. Chapter_5 (depends on: [Chapter_2], [Chapter_3]) - Priority: 5.8
2025-08-12 12:52:02,959 - app.new_score_oriented_tools - INFO - Critical path: [Chapter_6] → Chapter_10
2025-08-12 12:52:02,959 - app.new_score_oriented_tools - INFO - Optimization suggestions:
2025-08-12 12:52:02,959 - app.new_score_oriented_tools - INFO -   • Consider parallel study tracks for efficiency: 3 groups of independent chapters identified
2025-08-12 12:52:02,959 - app.new_score_oriented_tools - INFO - ✅ All dependencies perfectly satisfied!
2025-08-12 12:52:02,960 - app.new_score_oriented_agents - INFO - Applying user preferences to dependency-resolved order for Mathematics
2025-08-12 12:52:02,960 - app.new_score_oriented_agents - INFO - User preferences applied to 12 chapters while maintaining dependencies
2025-08-12 12:52:02,960 - app.new_score_oriented_agents - INFO - Perfect dependency sequence generated for Mathematics: 12 chapters
2025-08-12 12:52:02,960 - app.new_score_oriented_agents - INFO - Dependency-first ordering applied successfully
2025-08-12 12:52:02,960 - app.new_score_oriented_agents - INFO - Ensuring 100% coverage for all chapters
2025-08-12 12:52:02,960 - app.new_score_oriented_agents - INFO - Distributing syllabus across 6 months (total: 7)
2025-08-12 12:52:02,960 - app.new_score_oriented_agents - INFO - Starting enhanced features generation...
2025-08-12 12:52:02,960 - app.new_score_oriented_agents - INFO - Generating enhanced features for new_score_oriented plan
2025-08-12 12:52:02,960 - app.new_score_oriented_agents - INFO - Monthly chapters data prepared: ['month_1', 'month_2', 'month_3', 'month_4', 'month_5', 'month_6']
2025-08-12 12:52:02,960 - app.new_score_oriented_agents - INFO - Sample month data structure: {'physics': ['Chapter_9', 'Chapter_8'], 'chemistry': ['Chapter_8', 'Chapter_1'], 'mathematics': ['Chapter_2', 'Chapter_1']}
2025-08-12 12:52:02,961 - app.enhanced_new_score_oriented_tools - INFO - Calculating monthly target scores for user target: 190/300
2025-08-12 12:52:03,456 - app.enhanced_new_score_oriented_tools - INFO - month_1: Achievable=80.75, Target=51.14
2025-08-12 12:52:03,909 - app.enhanced_new_score_oriented_tools - INFO - month_2: Achievable=51.24, Target=32.45
2025-08-12 12:52:04,307 - app.enhanced_new_score_oriented_tools - INFO - month_3: Achievable=30.37, Target=19.23
2025-08-12 12:52:04,699 - app.enhanced_new_score_oriented_tools - INFO - month_4: Achievable=54.45, Target=34.48
2025-08-12 12:52:05,088 - app.enhanced_new_score_oriented_tools - INFO - month_5: Achievable=36.66, Target=23.22
2025-08-12 12:52:05,478 - app.enhanced_new_score_oriented_tools - INFO - month_6: Achievable=45.21, Target=28.63
2025-08-12 12:52:05,478 - app.enhanced_new_score_oriented_tools - INFO - Monthly target calculation completed: 6 months processed
2025-08-12 12:52:05,479 - app.enhanced_new_score_oriented_tools - INFO - Generating extended months plan: 7 total, 6 for syllabus
2025-08-12 12:52:05,479 - app.enhanced_new_score_oriented_tools - INFO - Extended months plan generated: 1 months of intensive practice
2025-08-12 12:52:05,480 - app.enhanced_new_score_oriented_tools - INFO - Generating weekly topic breakdown for 6 months
2025-08-12 12:52:07,886 - app.enhanced_new_score_oriented_tools - INFO - Weekly topic breakdown generated for 6 months
2025-08-12 12:52:07,887 - app.enhanced_new_score_oriented_tools - INFO - Creating comprehensive weekend schedule for 7 months
2025-08-12 12:52:07,887 - app.enhanced_new_score_oriented_tools - INFO - Comprehensive weekend schedule created for 7 months
2025-08-12 12:52:07,887 - app.new_score_oriented_agents - INFO - Enhanced features generated successfully
2025-08-12 12:52:07,888 - app.new_score_oriented_agents - INFO - Enhanced features generated: ['monthly_target_scores', 'extended_months_plan', 'weekly_topic_breakdown', 'weekend_schedule', 'strategy_summary']
2025-08-12 12:52:07,888 - app.new_score_oriented_agents - INFO - RevisionFlow plan generated with 6 months for syllabus completion
2025-08-12 12:52:07,888 - app.new_score_oriented_graph - INFO - Generator Validator Agent executing
2025-08-12 12:52:07,889 - app.new_score_oriented_agents - INFO - Validating chapter coverage for new_score_oriented plan
2025-08-12 12:52:07,889 - app.new_score_oriented_graph - INFO - Topic Agent executing
2025-08-12 12:52:07,890 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_9
2025-08-12 12:52:07,951 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_8
2025-08-12 12:52:08,009 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_11
2025-08-12 12:52:08,076 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_4
2025-08-12 12:52:08,138 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_6
2025-08-12 12:52:08,208 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_1
2025-08-12 12:52:08,275 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_10
2025-08-12 12:52:08,333 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_2
2025-08-12 12:52:08,395 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_3
2025-08-12 12:52:08,457 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_7
2025-08-12 12:52:08,516 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_12
2025-08-12 12:52:08,572 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_5
2025-08-12 12:52:08,641 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_8
2025-08-12 12:52:08,704 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_1
2025-08-12 12:52:08,772 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_4
2025-08-12 12:52:08,845 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_9
2025-08-12 12:52:08,910 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_11
2025-08-12 12:52:08,981 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_6
2025-08-12 12:52:09,042 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_2
2025-08-12 12:52:09,105 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_10
2025-08-12 12:52:09,186 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_3
2025-08-12 12:52:09,260 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_7
2025-08-12 12:52:09,329 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_12
2025-08-12 12:52:09,399 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_5
2025-08-12 12:52:09,455 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_2
2025-08-12 12:52:09,510 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_1
2025-08-12 12:52:09,575 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_8
2025-08-12 12:52:09,631 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_6
2025-08-12 12:52:09,698 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_11
2025-08-12 12:52:09,783 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_4
2025-08-12 12:52:09,854 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_9
2025-08-12 12:52:09,915 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_10
2025-08-12 12:52:09,987 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_3
2025-08-12 12:52:10,045 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_7
2025-08-12 12:52:10,101 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_12
2025-08-12 12:52:10,161 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_5
2025-08-12 12:52:10,223 - app.new_score_oriented_graph - INFO - Topic Validator Agent executing
2025-08-12 12:52:10,223 - app.new_score_oriented_agents - INFO - Validating topic coverage for new_score_oriented plan
2025-08-12 12:52:10,224 - app.tools - INFO - Fetching syllabus for exam: JEE Mains
2025-08-12 12:52:10,290 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_9
2025-08-12 12:52:10,346 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_8
2025-08-12 12:52:10,404 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_11
2025-08-12 12:52:10,463 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_4
2025-08-12 12:52:10,523 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_6
2025-08-12 12:52:10,615 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_1
2025-08-12 12:52:10,680 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_10
2025-08-12 12:52:10,737 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_2
2025-08-12 12:52:10,836 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_3
2025-08-12 12:52:10,887 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_7
2025-08-12 12:52:10,943 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_12
2025-08-12 12:52:11,001 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_5
2025-08-12 12:52:11,066 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_8
2025-08-12 12:52:11,121 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_1
2025-08-12 12:52:11,177 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_4
2025-08-12 12:52:11,248 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_9
2025-08-12 12:52:11,341 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_11
2025-08-12 12:52:11,397 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_6
2025-08-12 12:52:11,473 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_2
2025-08-12 12:52:11,524 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_10
2025-08-12 12:52:11,577 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_3
2025-08-12 12:52:11,637 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_7
2025-08-12 12:52:11,714 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_12
2025-08-12 12:52:11,777 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_5
2025-08-12 12:52:11,851 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_2
2025-08-12 12:52:11,914 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_1
2025-08-12 12:52:11,970 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_8
2025-08-12 12:52:12,029 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_6
2025-08-12 12:52:12,083 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_11
2025-08-12 12:52:12,147 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_4
2025-08-12 12:52:12,210 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_9
2025-08-12 12:52:12,265 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_10
2025-08-12 12:52:12,331 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_3
2025-08-12 12:52:12,388 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_7
2025-08-12 12:52:12,446 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_12
2025-08-12 12:52:12,517 - app.tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_5
2025-08-12 12:52:12,579 - app.new_score_oriented_agents - INFO - Performing final syllabus compliance validation
2025-08-12 12:52:12,580 - app.new_score_oriented_graph - INFO - Supervisor Agent executing
2025-08-12 12:52:12,580 - app.new_score_oriented_agents - INFO - Supervising new_score_oriented plan for target achievement
2025-08-12 12:52:12,581 - app.new_score_oriented_graph - INFO - Finalizing new_score_oriented study plan with enhanced calendar features

================================================================================
🎯 NEW SCORE-ORIENTED STUDY PLAN - DETAILED BREAKDOWN
================================================================================
2025-08-12 to 2026-03-10 | Target: 190/300

7
Months
132
Study Days
56
PYQ Days
56
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
54.5
Total Achievable Score
34.5
Your Target Score
Efficiency Required
63.3%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_10', 'Chapter_2'], 'subject_weightage': 26.0, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_2', 'Chapter_10'], 'subject_weightage': 15.59, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_9', 'Chapter_10'], 'subject_weightage': 12.86, 'chapter_count': 2}

Month 5
63.3% of target
36.7
Total Achievable Score
23.2
Your Target Score
Efficiency Required
63.3%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_3', 'Chapter_7'], 'subject_weightage': 6.81, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_3', 'Chapter_7'], 'subject_weightage': 19.62, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_3', 'Chapter_7'], 'subject_weightage': 10.23, 'chapter_count': 2}

Month 6
63.3% of target
45.2
Total Achievable Score
28.6
Your Target Score
Efficiency Required
63.3%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_12', 'Chapter_5'], 'subject_weightage': 25.26, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_12', 'Chapter_5'], 'subject_weightage': 12.04, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_12', 'Chapter_5'], 'subject_weightage': 7.91, 'chapter_count': 2}

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
Chapter_5
  Topic_4
  Topic_6
  Topic_7
  Topic_3
  Topic_5
  Topic_1
  Topic_2
7 topics

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
Chapter_5
  Topic_1
  Topic_2
  Topic_5
  Topic_6
  Topic_3
  Topic_4
  Topic_7
7 topics

================================================================================
📋 JSON OUTPUT:
================================================================================
{
  "plan_info": {
    "start_date": "2025-08-12",
    "end_date": "2026-03-10",
    "target_score": "190/300",
    "total_months": 7,
    "syllabus_completion_months": 6,
    "study_days": 132,
    "pyq_days": 56,
    "weekend_sessions": 56,
    "dpp_sessions": 396,
    "Full_month_revision": 1
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
      "total_achievable_score": 54.45,
      "user_target_score": 34.48,
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
      "target_ratio": "63.3% of target",
      "total_achievable_score": 36.66,
      "user_target_score": 23.22,
      "efficiency_required": "63.3%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_3",
            "Chapter_7"
          ],
          "subject_weightage": 6.81,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_3",
            "Chapter_7"
          ],
          "subject_weightage": 19.62,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_3",
            "Chapter_7"
          ],
          "subject_weightage": 10.23,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 6": {
      "target_ratio": "63.3% of target",
      "total_achievable_score": 45.21,
      "user_target_score": 28.63,
      "efficiency_required": "63.3%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_12",
            "Chapter_5"
          ],
          "subject_weightage": 25.26,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_12",
            "Chapter_5"
          ],
          "subject_weightage": 12.04,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_12",
            "Chapter_5"
          ],
          "subject_weightage": 7.91,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 7": {
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
        "Chapter_2"
      ],
      "chemistry": [
        "Chapter_2",
        "Chapter_10"
      ]
    },
    "month_5": {
      "mathematics": [
        "Chapter_3",
        "Chapter_7"
      ],
      "physics": [
        "Chapter_3",
        "Chapter_7"
      ],
      "chemistry": [
        "Chapter_3",
        "Chapter_7"
      ]
    },
    "month_6": {
      "mathematics": [
        "Chapter_12",
        "Chapter_5"
      ],
      "physics": [
        "Chapter_12",
        "Chapter_5"
      ],
      "chemistry": [
        "Chapter_12",
        "Chapter_5"
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
            "total_topic_count": 19
          },
          "physics": {
            "chapters": {
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
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
            "total_topic_count": 19
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
            "total_topic_count": 19
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
            "total_topic_count": 19
          },
          "physics": {
            "chapters": {
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
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
            "total_topic_count": 19
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
            "total_topic_count": 19
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
            "total_topic_count": 19
          },
          "physics": {
            "chapters": {
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
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
            "total_topic_count": 19
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
            "total_topic_count": 19
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
            "total_topic_count": 19
          },
          "physics": {
            "chapters": {
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
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
            "total_topic_count": 19
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
            "total_topic_count": 19
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
            "total_topic_count": 19
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
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ]
            },
            "total_topic_count": 19
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
            "total_topic_count": 19
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
            "total_topic_count": 19
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
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ]
            },
            "total_topic_count": 19
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
            "total_topic_count": 19
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
            "total_topic_count": 19
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
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ]
            },
            "total_topic_count": 19
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
            "total_topic_count": 19
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
            "total_topic_count": 19
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
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ]
            },
            "total_topic_count": 19
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
            "total_topic_count": 19
          }
        }
      }
    }
  }
}

================================================================================
✅ NEW SCORE-ORIENTED PLAN DISPLAY COMPLETE
================================================================================

2025-08-12 12:52:12,642 - app.new_score_oriented_graph - INFO - New Score-Oriented Feedback Counsellor executing
2025-08-12 12:52:12,642 - app.new_score_oriented_graph - INFO - Processing user message: generate
2025-08-12 12:52:12,643 - app.new_score_oriented_graph - INFO - New Score-Oriented Feedback Counsellor Continue executing
2025-08-12 12:52:12,643 - app.new_score_oriented_graph - INFO - Feedback processed, finalizing plan
=== NEW SCORE ORIENTED PLAN DEBUG ===
Plan keys: ['user_id', 'target_score', 'exam_date', 'total_months', 'syllabus_completion_months', 'practice_months', 'monthly_plans', 'revision_flow_results', 'overall_strategy', 'dependency_analysis', 'coverage_validation', 'target_achievement_probability', 'enhanced_features', 'calendar_plan', 'monthly_targets_data', 'extended_months_plan', 'weekend_schedule', 'weekly_topic_breakdown', 'user_target_score', 'start_date', 'end_date', 'overall_summary']
Plan type: <class 'dict'>
Plan content preview: {'user_id': 'user_g0jpsqc1k', 'target_score': 190, 'exam_date': '2026-03-12', 'total_months': 7, 'syllabus_completion_months': 6, 'practice_months': 1, 'monthly_plans': [], 'revision_flow_results': {'physics': {'chapters': [{'chapter': 'Chapter_9', 'weightage': 14.77, 'category': 'High', 'coverage_percentage': 1.0, 'priority_reason': 'dependency_optimized', 'dependencies_satisfied': True, 'completion_order': 1, 'dependency_level': 0, 'dependencies': [], 'coverage_reason': 'complete_syllabus_cove...
=====================================
=== STUDY PLAN RESPONSE DEBUG ===
Response keys: ['insights', 'monthly_plan', 'weekly_plan', 'new_score_oriented_data']
Monthly plan keys: ['Month 1', 'Month 2', 'Month 3', 'Month 4', 'Month 5', 'Month 6']
====================================

================================================================================
🎯 NEW SCORE-ORIENTED STUDY PLAN - DETAILED BREAKDOWN
================================================================================
2025-08-12 to 2026-03-10 | Target: 190/300

7
Months
132
Study Days
56
PYQ Days
56
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
54.5
Total Achievable Score
34.5
Your Target Score
Efficiency Required
63.3%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_10', 'Chapter_2'], 'subject_weightage': 26.0, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_2', 'Chapter_10'], 'subject_weightage': 15.59, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_9', 'Chapter_10'], 'subject_weightage': 12.86, 'chapter_count': 2}

Month 5
63.3% of target
36.7
Total Achievable Score
23.2
Your Target Score
Efficiency Required
63.3%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_3', 'Chapter_7'], 'subject_weightage': 6.81, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_3', 'Chapter_7'], 'subject_weightage': 19.62, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_3', 'Chapter_7'], 'subject_weightage': 10.23, 'chapter_count': 2}

Month 6
63.3% of target
45.2
Total Achievable Score
28.6
Your Target Score
Efficiency Required
63.3%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_12', 'Chapter_5'], 'subject_weightage': 25.26, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_12', 'Chapter_5'], 'subject_weightage': 12.04, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_12', 'Chapter_5'], 'subject_weightage': 7.91, 'chapter_count': 2}

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
Chapter_5
  Topic_4
  Topic_6
  Topic_7
  Topic_3
  Topic_5
  Topic_1
  Topic_2
7 topics

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
Chapter_5
  Topic_1
  Topic_2
  Topic_5
  Topic_6
  Topic_3
  Topic_4
  Topic_7
7 topics

================================================================================
📋 JSON OUTPUT:
================================================================================
{
  "plan_info": {
    "start_date": "2025-08-12",
    "end_date": "2026-03-10",
    "target_score": "190/300",
    "total_months": 7,
    "syllabus_completion_months": 6,
    "study_days": 132,
    "pyq_days": 56,
    "weekend_sessions": 56,
    "dpp_sessions": 396,
    "Full_month_revision": 1
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
      "total_achievable_score": 54.45,
      "user_target_score": 34.48,
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
      "target_ratio": "63.3% of target",
      "total_achievable_score": 36.66,
      "user_target_score": 23.22,
      "efficiency_required": "63.3%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_3",
            "Chapter_7"
          ],
          "subject_weightage": 6.81,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_3",
            "Chapter_7"
          ],
          "subject_weightage": 19.62,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_3",
            "Chapter_7"
          ],
          "subject_weightage": 10.23,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 6": {
      "target_ratio": "63.3% of target",
      "total_achievable_score": 45.21,
      "user_target_score": 28.63,
      "efficiency_required": "63.3%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_12",
            "Chapter_5"
          ],
          "subject_weightage": 25.26,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_12",
            "Chapter_5"
          ],
          "subject_weightage": 12.04,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_12",
            "Chapter_5"
          ],
          "subject_weightage": 7.91,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 7": {
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
        "Chapter_2"
      ],
      "chemistry": [
        "Chapter_2",
        "Chapter_10"
      ]
    },
    "month_5": {
      "mathematics": [
        "Chapter_3",
        "Chapter_7"
      ],
      "physics": [
        "Chapter_3",
        "Chapter_7"
      ],
      "chemistry": [
        "Chapter_3",
        "Chapter_7"
      ]
    },
    "month_6": {
      "mathematics": [
        "Chapter_12",
        "Chapter_5"
      ],
      "physics": [
        "Chapter_12",
        "Chapter_5"
      ],
      "chemistry": [
        "Chapter_12",
        "Chapter_5"
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
            "total_topic_count": 19
          },
          "physics": {
            "chapters": {
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
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
            "total_topic_count": 19
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
            "total_topic_count": 19
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
            "total_topic_count": 19
          },
          "physics": {
            "chapters": {
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
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
            "total_topic_count": 19
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
            "total_topic_count": 19
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
            "total_topic_count": 19
          },
          "physics": {
            "chapters": {
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
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
            "total_topic_count": 19
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
            "total_topic_count": 19
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
            "total_topic_count": 19
          },
          "physics": {
            "chapters": {
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
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
            "total_topic_count": 19
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
            "total_topic_count": 19
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
            "total_topic_count": 19
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
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ]
            },
            "total_topic_count": 19
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
            "total_topic_count": 19
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
            "total_topic_count": 19
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
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ]
            },
            "total_topic_count": 19
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
            "total_topic_count": 19
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
            "total_topic_count": 19
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
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ]
            },
            "total_topic_count": 19
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
            "total_topic_count": 19
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
            "total_topic_count": 19
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
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ]
            },
            "total_topic_count": 19
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
            "total_topic_count": 19
          }
        }
      }
    }
  }
}

================================================================================
✅ NEW SCORE-ORIENTED PLAN DISPLAY COMPLETE
================================================================================

INFO:     127.0.0.1:64332 - "POST /chat HTTP/1.1" 200 OK
2025-08-12 12:52:27,913 - app.main - INFO - Received chat message from user: user_g0jpsqc1k
2025-08-12 12:52:27,914 - app.regen_tools - INFO - Checking if user exists: user_g0jpsqc1k
2025-08-12 12:52:28,077 - app.regen_tools - INFO - User user_g0jpsqc1k found in database
2025-08-12 12:52:28,078 - app.main - INFO - User existence check for user_g0jpsqc1k: exists=True, has_study_plan=False, treating_as_existing=False
2025-08-12 12:52:28,078 - app.main - INFO - New user detected: user_g0jpsqc1k - routing to normal flow
2025-08-12 12:52:28,198 - app.main - INFO - Retrieved stored form data for user: user_g0jpsqc1k
2025-08-12 12:52:28,199 - app.main - INFO - Using stored form data for user: user_g0jpsqc1k
2025-08-12 12:52:28,199 - app.new_score_oriented_tools - INFO - Exam date validation: {'is_valid': True, 'calculated_months': 7, 'exam_date': '2026-03-12', 'minimum_required': 6, 'message': 'Exam date is 7 months away. Valid for new_score_oriented plan.'}
2025-08-12 12:52:28,199 - app.main - INFO - Handling feedback for existing new_score_oriented plan: user_g0jpsqc1k
2025-08-12 12:52:28,200 - app.main - INFO - Processing new_score_oriented feedback: take every month 3 chapters
2025-08-12 12:52:28,200 - app.main - INFO - Routing to feedback_counsellor for user message: take every month 3 chapters
2025-08-12 12:52:28,201 - app.new_score_oriented_graph - INFO - Counsellor Generator Agent executing for new_score_oriented plan
2025-08-12 12:52:28,202 - app.new_score_oriented_tools - INFO - Exam date validation: {'is_valid': True, 'calculated_months': 7, 'exam_date': '2026-03-12', 'minimum_required': 6, 'message': 'Exam date is 7 months away. Valid for new_score_oriented plan.'}
2025-08-12 12:52:28,202 - app.new_score_oriented_graph - INFO - RevisionFlow Agent executing
2025-08-12 12:52:28,203 - app.new_score_oriented_agents - INFO - RevisionFlow Agent executing: Generating complete syllabus coverage plan
2025-08-12 12:52:28,203 - app.new_score_oriented_agents - INFO - Processing new_score_oriented plan for target: 190/300
2025-08-12 12:52:28,203 - app.new_score_oriented_agents - INFO - Processing complete syllabus for Physics
2025-08-12 12:52:28,203 - app.new_score_oriented_agents - INFO - Generating perfect dependency sequence for Physics
2025-08-12 12:52:28,205 - app.new_score_oriented_tools - INFO - Fetching chapter flow for exam: JEE Mains, subject: Physics
2025-08-12 12:52:28,354 - app.new_score_oriented_tools - INFO - Fetching chapter weightage for exam: JEE Mains, subject: Physics
2025-08-12 12:52:28,435 - app.new_score_oriented_tools - INFO - Starting enhanced dependency resolution for Physics
2025-08-12 12:52:28,436 - app.new_score_oriented_tools - INFO - Flow data: 12 chapters with dependencies
2025-08-12 12:52:28,436 - app.new_score_oriented_tools - INFO - Weightage data: 12 chapters with priorities
2025-08-12 12:52:28,436 - app.enhanced_dependency_resolver - INFO - Building comprehensive dependency graph from Chapter_Flow and Chapter_Weightage tables
2025-08-12 12:52:28,436 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_1]' for chapter 'Chapter_3' not found in chapter list
2025-08-12 12:52:28,437 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_2]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 12:52:28,437 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_3]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 12:52:28,437 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_4]' for chapter 'Chapter_7' not found in chapter list
2025-08-12 12:52:28,437 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_6]' for chapter 'Chapter_10' not found in chapter list
2025-08-12 12:52:28,437 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_5]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 12:52:28,438 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_7]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 12:52:28,438 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_1]' for chapter 'Chapter_2' not found in chapter list
2025-08-12 12:52:28,438 - app.enhanced_dependency_resolver - INFO - Dependency graph built: 12 chapters, 8 dependencies
2025-08-12 12:52:28,438 - app.enhanced_dependency_resolver - INFO - Starting strict dependency resolution for Physics
2025-08-12 12:52:28,439 - app.enhanced_dependency_resolver - WARNING - Some chapters could not be resolved due to dependency cycles: {'Chapter_10', 'Chapter_2', 'Chapter_3', 'Chapter_7', 'Chapter_12', 'Chapter_5'}
2025-08-12 12:52:28,439 - app.enhanced_dependency_resolver - INFO - Strict dependency resolution completed for Physics: 12 chapters
2025-08-12 12:52:28,439 - app.enhanced_dependency_resolver - INFO - Enhanced dependency resolution completed for Physics: 12 chapters with strict dependency ordering
2025-08-12 12:52:28,439 - app.new_score_oriented_tools - INFO - Enhanced dependency resolution for Physics:
2025-08-12 12:52:28,439 - app.new_score_oriented_tools - INFO -   Total chapters: 12
2025-08-12 12:52:28,439 - app.new_score_oriented_tools - INFO -   Chapters with dependencies: 6
2025-08-12 12:52:28,439 - app.new_score_oriented_tools - INFO -   All dependencies satisfied: True
2025-08-12 12:52:28,440 - app.new_score_oriented_tools - INFO - Final chapter order (dependencies first):
2025-08-12 12:52:28,440 - app.new_score_oriented_tools - INFO -    1. Chapter_9 (no dependencies) - Priority: 44.3
2025-08-12 12:52:28,440 - app.new_score_oriented_tools - INFO -    2. Chapter_8 (no dependencies) - Priority: 38.2
2025-08-12 12:52:28,440 - app.new_score_oriented_tools - INFO -    3. Chapter_11 (no dependencies) - Priority: 15.6
2025-08-12 12:52:28,440 - app.new_score_oriented_tools - INFO -    4. Chapter_4 (no dependencies) - Priority: 3.4
2025-08-12 12:52:28,440 - app.new_score_oriented_tools - INFO -    5. Chapter_6 (no dependencies) - Priority: 2.3
2025-08-12 12:52:28,440 - app.new_score_oriented_tools - INFO -    6. Chapter_1 (no dependencies) - Priority: 0.9
2025-08-12 12:52:28,440 - app.new_score_oriented_tools - INFO -    7. Chapter_10 (depends on: [Chapter_6]) - Priority: 22.6
2025-08-12 12:52:28,440 - app.new_score_oriented_tools - INFO -    8. Chapter_2 (depends on: [Chapter_1]) - Priority: 44.0
2025-08-12 12:52:28,440 - app.new_score_oriented_tools - INFO -    9. Chapter_3 (depends on: [Chapter_1]) - Priority: 0.9
2025-08-12 12:52:28,440 - app.new_score_oriented_tools - INFO -   10. Chapter_7 (depends on: [Chapter_4]) - Priority: 11.7
2025-08-12 12:52:28,440 - app.new_score_oriented_tools - INFO -   11. Chapter_12 (depends on: [Chapter_5], [Chapter_7]) - Priority: 22.6
2025-08-12 12:52:28,441 - app.new_score_oriented_tools - INFO -   12. Chapter_5 (depends on: [Chapter_2], [Chapter_3]) - Priority: 41.9
2025-08-12 12:52:28,441 - app.new_score_oriented_tools - INFO - Critical path: [Chapter_6] → Chapter_10
2025-08-12 12:52:28,441 - app.new_score_oriented_tools - INFO - Optimization suggestions:
2025-08-12 12:52:28,441 - app.new_score_oriented_tools - INFO -   • Consider parallel study tracks for efficiency: 3 groups of independent chapters identified
2025-08-12 12:52:28,441 - app.new_score_oriented_tools - INFO - ✅ All dependencies perfectly satisfied!
2025-08-12 12:52:28,441 - app.new_score_oriented_agents - INFO - Applying user preferences to dependency-resolved order for Physics
2025-08-12 12:52:28,441 - app.new_score_oriented_agents - INFO - User preferences applied to 12 chapters while maintaining dependencies
2025-08-12 12:52:28,441 - app.new_score_oriented_agents - INFO - Perfect dependency sequence generated for Physics: 12 chapters
2025-08-12 12:52:28,441 - app.new_score_oriented_agents - INFO - Dependency-first ordering applied successfully
2025-08-12 12:52:28,441 - app.new_score_oriented_agents - INFO - Ensuring 100% coverage for all chapters
2025-08-12 12:52:28,442 - app.new_score_oriented_agents - INFO - Processing complete syllabus for Chemistry
2025-08-12 12:52:28,442 - app.new_score_oriented_agents - INFO - Generating perfect dependency sequence for Chemistry
2025-08-12 12:52:28,443 - app.new_score_oriented_tools - INFO - Fetching chapter flow for exam: JEE Mains, subject: Chemistry
2025-08-12 12:52:28,506 - app.new_score_oriented_tools - INFO - Fetching chapter weightage for exam: JEE Mains, subject: Chemistry
2025-08-12 12:52:28,571 - app.new_score_oriented_tools - INFO - Starting enhanced dependency resolution for Chemistry
2025-08-12 12:52:28,571 - app.new_score_oriented_tools - INFO - Flow data: 12 chapters with dependencies
2025-08-12 12:52:28,571 - app.new_score_oriented_tools - INFO - Weightage data: 12 chapters with priorities
2025-08-12 12:52:28,571 - app.enhanced_dependency_resolver - INFO - Building comprehensive dependency graph from Chapter_Flow and Chapter_Weightage tables
2025-08-12 12:52:28,572 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_1]' for chapter 'Chapter_3' not found in chapter list
2025-08-12 12:52:28,572 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_2]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 12:52:28,572 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_3]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 12:52:28,572 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_4]' for chapter 'Chapter_7' not found in chapter list
2025-08-12 12:52:28,573 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_6]' for chapter 'Chapter_10' not found in chapter list
2025-08-12 12:52:28,573 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_5]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 12:52:28,573 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_7]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 12:52:28,573 - app.enhanced_dependency_resolver - INFO - Dependency graph built: 12 chapters, 7 dependencies
2025-08-12 12:52:28,573 - app.enhanced_dependency_resolver - INFO - Starting strict dependency resolution for Chemistry
2025-08-12 12:52:28,574 - app.enhanced_dependency_resolver - WARNING - Some chapters could not be resolved due to dependency cycles: {'Chapter_10', 'Chapter_3', 'Chapter_7', 'Chapter_12', 'Chapter_5'}
2025-08-12 12:52:28,574 - app.enhanced_dependency_resolver - INFO - Strict dependency resolution completed for Chemistry: 12 chapters
2025-08-12 12:52:28,574 - app.enhanced_dependency_resolver - INFO - Enhanced dependency resolution completed for Chemistry: 12 chapters with strict dependency ordering
2025-08-12 12:52:28,574 - app.new_score_oriented_tools - INFO - Enhanced dependency resolution for Chemistry:
2025-08-12 12:52:28,574 - app.new_score_oriented_tools - INFO -   Total chapters: 12
2025-08-12 12:52:28,575 - app.new_score_oriented_tools - INFO -   Chapters with dependencies: 5
2025-08-12 12:52:28,575 - app.new_score_oriented_tools - INFO -   All dependencies satisfied: True
2025-08-12 12:52:28,575 - app.new_score_oriented_tools - INFO - Final chapter order (dependencies first):
2025-08-12 12:52:28,575 - app.new_score_oriented_tools - INFO -    1. Chapter_8 (no dependencies) - Priority: 42.4
2025-08-12 12:52:28,575 - app.new_score_oriented_tools - INFO -    2. Chapter_1 (no dependencies) - Priority: 37.0
2025-08-12 12:52:28,575 - app.new_score_oriented_tools - INFO -    3. Chapter_4 (no dependencies) - Priority: 20.0
2025-08-12 12:52:28,575 - app.new_score_oriented_tools - INFO -    4. Chapter_9 (no dependencies) - Priority: 15.8
2025-08-12 12:52:28,576 - app.new_score_oriented_tools - INFO -    5. Chapter_11 (no dependencies) - Priority: 6.0
2025-08-12 12:52:28,576 - app.new_score_oriented_tools - INFO -    6. Chapter_6 (no dependencies) - Priority: 2.3
2025-08-12 12:52:28,576 - app.new_score_oriented_tools - INFO -    7. Chapter_2 (no dependencies) - Priority: 0.6
2025-08-12 12:52:28,576 - app.new_score_oriented_tools - INFO -    8. Chapter_10 (depends on: [Chapter_6]) - Priority: 45.1
2025-08-12 12:52:28,576 - app.new_score_oriented_tools - INFO -    9. Chapter_3 (depends on: [Chapter_1]) - Priority: 33.9
2025-08-12 12:52:28,577 - app.new_score_oriented_tools - INFO -   10. Chapter_7 (depends on: [Chapter_4]) - Priority: 16.6
2025-08-12 12:52:28,577 - app.new_score_oriented_tools - INFO -   11. Chapter_12 (depends on: [Chapter_5], [Chapter_7]) - Priority: 3.1
2025-08-12 12:52:28,577 - app.new_score_oriented_tools - INFO -   12. Chapter_5 (depends on: [Chapter_2], [Chapter_3]) - Priority: 18.0
2025-08-12 12:52:28,577 - app.new_score_oriented_tools - INFO - Critical path: [Chapter_6] → Chapter_10
2025-08-12 12:52:28,577 - app.new_score_oriented_tools - INFO - Optimization suggestions:
2025-08-12 12:52:28,577 - app.new_score_oriented_tools - INFO -   • Consider parallel study tracks for efficiency: 3 groups of independent chapters identified
2025-08-12 12:52:28,577 - app.new_score_oriented_tools - INFO - ✅ All dependencies perfectly satisfied!
2025-08-12 12:52:28,578 - app.new_score_oriented_agents - INFO - Applying user preferences to dependency-resolved order for Chemistry
2025-08-12 12:52:28,578 - app.new_score_oriented_agents - INFO - User preferences applied to 12 chapters while maintaining dependencies
2025-08-12 12:52:28,578 - app.new_score_oriented_agents - INFO - Perfect dependency sequence generated for Chemistry: 12 chapters
2025-08-12 12:52:28,578 - app.new_score_oriented_agents - INFO - Dependency-first ordering applied successfully
2025-08-12 12:52:28,578 - app.new_score_oriented_agents - INFO - Ensuring 100% coverage for all chapters
2025-08-12 12:52:28,578 - app.new_score_oriented_agents - INFO - Processing complete syllabus for Mathematics
2025-08-12 12:52:28,579 - app.new_score_oriented_agents - INFO - Generating perfect dependency sequence for Mathematics
2025-08-12 12:52:28,580 - app.new_score_oriented_tools - INFO - Fetching chapter flow for exam: JEE Mains, subject: Mathematics
2025-08-12 12:52:28,651 - app.new_score_oriented_tools - INFO - Fetching chapter weightage for exam: JEE Mains, subject: Mathematics
2025-08-12 12:52:28,712 - app.new_score_oriented_tools - INFO - Starting enhanced dependency resolution for Mathematics
2025-08-12 12:52:28,713 - app.new_score_oriented_tools - INFO - Flow data: 12 chapters with dependencies
2025-08-12 12:52:28,713 - app.new_score_oriented_tools - INFO - Weightage data: 12 chapters with priorities
2025-08-12 12:52:28,713 - app.enhanced_dependency_resolver - INFO - Building comprehensive dependency graph from Chapter_Flow and Chapter_Weightage tables
2025-08-12 12:52:28,713 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_1]' for chapter 'Chapter_3' not found in chapter list
2025-08-12 12:52:28,714 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_2]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 12:52:28,714 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_3]' for chapter 'Chapter_5' not found in chapter list
2025-08-12 12:52:28,714 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_4]' for chapter 'Chapter_7' not found in chapter list
2025-08-12 12:52:28,714 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_6]' for chapter 'Chapter_10' not found in chapter list
2025-08-12 12:52:28,714 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_5]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 12:52:28,715 - app.enhanced_dependency_resolver - WARNING - Dependency '[Chapter_7]' for chapter 'Chapter_12' not found in chapter list
2025-08-12 12:52:28,715 - app.enhanced_dependency_resolver - INFO - Dependency graph built: 12 chapters, 7 dependencies
2025-08-12 12:52:28,715 - app.enhanced_dependency_resolver - INFO - Starting strict dependency resolution for Mathematics
2025-08-12 12:52:28,715 - app.enhanced_dependency_resolver - WARNING - Some chapters could not be resolved due to dependency cycles: {'Chapter_10', 'Chapter_3', 'Chapter_7', 'Chapter_12', 'Chapter_5'}
2025-08-12 12:52:28,715 - app.enhanced_dependency_resolver - INFO - Strict dependency resolution completed for Mathematics: 12 chapters
2025-08-12 12:52:28,716 - app.enhanced_dependency_resolver - INFO - Enhanced dependency resolution completed for Mathematics: 12 chapters with strict dependency ordering
2025-08-12 12:52:28,716 - app.new_score_oriented_tools - INFO - Enhanced dependency resolution for Mathematics:
2025-08-12 12:52:28,716 - app.new_score_oriented_tools - INFO -   Total chapters: 12
2025-08-12 12:52:28,716 - app.new_score_oriented_tools - INFO -   Chapters with dependencies: 5
2025-08-12 12:52:28,716 - app.new_score_oriented_tools - INFO -   All dependencies satisfied: True
2025-08-12 12:52:28,716 - app.new_score_oriented_tools - INFO - Final chapter order (dependencies first):
2025-08-12 12:52:28,716 - app.new_score_oriented_tools - INFO -    1. Chapter_2 (no dependencies) - Priority: 42.9
2025-08-12 12:52:28,717 - app.new_score_oriented_tools - INFO -    2. Chapter_1 (no dependencies) - Priority: 37.5
2025-08-12 12:52:28,717 - app.new_score_oriented_tools - INFO -    3. Chapter_8 (no dependencies) - Priority: 34.2
2025-08-12 12:52:28,717 - app.new_score_oriented_tools - INFO -    4. Chapter_6 (no dependencies) - Priority: 32.3
2025-08-12 12:52:28,717 - app.new_score_oriented_tools - INFO -    5. Chapter_11 (no dependencies) - Priority: 21.0
2025-08-12 12:52:28,717 - app.new_score_oriented_tools - INFO -    6. Chapter_4 (no dependencies) - Priority: 16.5
2025-08-12 12:52:28,717 - app.new_score_oriented_tools - INFO -    7. Chapter_9 (no dependencies) - Priority: 15.8
2025-08-12 12:52:28,717 - app.new_score_oriented_tools - INFO -    8. Chapter_10 (depends on: [Chapter_6]) - Priority: 5.0
2025-08-12 12:52:28,718 - app.new_score_oriented_tools - INFO -    9. Chapter_3 (depends on: [Chapter_1]) - Priority: 12.6
2025-08-12 12:52:28,718 - app.new_score_oriented_tools - INFO -   10. Chapter_7 (depends on: [Chapter_4]) - Priority: 3.9
2025-08-12 12:52:28,718 - app.new_score_oriented_tools - INFO -   11. Chapter_12 (depends on: [Chapter_5], [Chapter_7]) - Priority: 2.1
2025-08-12 12:52:28,718 - app.new_score_oriented_tools - INFO -   12. Chapter_5 (depends on: [Chapter_2], [Chapter_3]) - Priority: 5.8
2025-08-12 12:52:28,718 - app.new_score_oriented_tools - INFO - Critical path: [Chapter_6] → Chapter_10
2025-08-12 12:52:28,719 - app.new_score_oriented_tools - INFO - Optimization suggestions:
2025-08-12 12:52:28,719 - app.new_score_oriented_tools - INFO -   • Consider parallel study tracks for efficiency: 3 groups of independent chapters identified
2025-08-12 12:52:28,719 - app.new_score_oriented_tools - INFO - ✅ All dependencies perfectly satisfied!
2025-08-12 12:52:28,719 - app.new_score_oriented_agents - INFO - Applying user preferences to dependency-resolved order for Mathematics
2025-08-12 12:52:28,719 - app.new_score_oriented_agents - INFO - User preferences applied to 12 chapters while maintaining dependencies
2025-08-12 12:52:28,719 - app.new_score_oriented_agents - INFO - Perfect dependency sequence generated for Mathematics: 12 chapters
2025-08-12 12:52:28,720 - app.new_score_oriented_agents - INFO - Dependency-first ordering applied successfully
2025-08-12 12:52:28,720 - app.new_score_oriented_agents - INFO - Ensuring 100% coverage for all chapters
2025-08-12 12:52:28,720 - app.new_score_oriented_agents - INFO - Distributing syllabus across 6 months (total: 7)
2025-08-12 12:52:28,720 - app.new_score_oriented_agents - INFO - Starting enhanced features generation...
2025-08-12 12:52:28,720 - app.new_score_oriented_agents - INFO - Generating enhanced features for new_score_oriented plan
2025-08-12 12:52:28,720 - app.new_score_oriented_agents - INFO - Monthly chapters data prepared: ['month_1', 'month_2', 'month_3', 'month_4', 'month_5', 'month_6']
2025-08-12 12:52:28,721 - app.new_score_oriented_agents - INFO - Sample month data structure: {'physics': ['Chapter_9', 'Chapter_8'], 'chemistry': ['Chapter_8', 'Chapter_1'], 'mathematics': ['Chapter_2', 'Chapter_1']}
2025-08-12 12:52:28,721 - app.enhanced_new_score_oriented_tools - INFO - Calculating monthly target scores for user target: 190/300
2025-08-12 12:52:29,135 - app.enhanced_new_score_oriented_tools - INFO - month_1: Achievable=80.75, Target=51.14
2025-08-12 12:52:29,552 - app.enhanced_new_score_oriented_tools - INFO - month_2: Achievable=51.24, Target=32.45
2025-08-12 12:52:29,982 - app.enhanced_new_score_oriented_tools - INFO - month_3: Achievable=30.37, Target=19.23
2025-08-12 12:52:30,399 - app.enhanced_new_score_oriented_tools - INFO - month_4: Achievable=54.45, Target=34.48
2025-08-12 12:52:30,786 - app.enhanced_new_score_oriented_tools - INFO - month_5: Achievable=36.66, Target=23.22
2025-08-12 12:52:31,167 - app.enhanced_new_score_oriented_tools - INFO - month_6: Achievable=45.21, Target=28.63
2025-08-12 12:52:31,167 - app.enhanced_new_score_oriented_tools - INFO - Monthly target calculation completed: 6 months processed
2025-08-12 12:52:31,168 - app.enhanced_new_score_oriented_tools - INFO - Generating extended months plan: 7 total, 6 for syllabus
2025-08-12 12:52:31,169 - app.enhanced_new_score_oriented_tools - INFO - Extended months plan generated: 1 months of intensive practice
2025-08-12 12:52:31,169 - app.enhanced_new_score_oriented_tools - INFO - Generating weekly topic breakdown for 6 months
2025-08-12 12:52:34,230 - app.enhanced_new_score_oriented_tools - INFO - Weekly topic breakdown generated for 6 months
2025-08-12 12:52:34,231 - app.enhanced_new_score_oriented_tools - INFO - Creating comprehensive weekend schedule for 7 months
2025-08-12 12:52:34,231 - app.enhanced_new_score_oriented_tools - INFO - Comprehensive weekend schedule created for 7 months
2025-08-12 12:52:34,231 - app.new_score_oriented_agents - INFO - Enhanced features generated successfully
2025-08-12 12:52:34,232 - app.new_score_oriented_agents - INFO - Enhanced features generated: ['monthly_target_scores', 'extended_months_plan', 'weekly_topic_breakdown', 'weekend_schedule', 'strategy_summary']
2025-08-12 12:52:34,232 - app.new_score_oriented_agents - INFO - RevisionFlow plan generated with 6 months for syllabus completion
2025-08-12 12:52:34,232 - app.new_score_oriented_graph - INFO - Generator Validator Agent executing
2025-08-12 12:52:34,233 - app.new_score_oriented_agents - INFO - Validating chapter coverage for new_score_oriented plan
2025-08-12 12:52:34,233 - app.new_score_oriented_graph - INFO - Topic Agent executing
2025-08-12 12:52:34,234 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_9
2025-08-12 12:52:34,315 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_8
2025-08-12 12:52:34,376 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_11
2025-08-12 12:52:34,453 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_4
2025-08-12 12:52:34,538 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_6
2025-08-12 12:52:34,599 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_1
2025-08-12 12:52:34,660 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_10
2025-08-12 12:52:34,721 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_2
2025-08-12 12:52:34,788 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_3
2025-08-12 12:52:34,859 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_7
2025-08-12 12:52:34,923 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_12
2025-08-12 12:52:34,993 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Physics, chapter: Chapter_5
2025-08-12 12:52:35,066 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_8
2025-08-12 12:52:35,144 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_1
2025-08-12 12:52:35,210 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_4
2025-08-12 12:52:35,282 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_9
2025-08-12 12:52:35,366 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_11
2025-08-12 12:52:35,427 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_6
2025-08-12 12:52:35,511 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_2
2025-08-12 12:52:35,581 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_10
2025-08-12 12:52:35,697 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_3
2025-08-12 12:52:35,764 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_7
2025-08-12 12:52:35,832 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_12
2025-08-12 12:52:35,894 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Chemistry, chapter: Chapter_5
2025-08-12 12:52:35,953 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_2
2025-08-12 12:52:36,016 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_1
2025-08-12 12:52:36,090 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_8
2025-08-12 12:52:36,168 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_6
2025-08-12 12:52:36,232 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_11
2025-08-12 12:52:36,296 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_4
2025-08-12 12:52:36,377 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_9
2025-08-12 12:52:36,448 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_10
2025-08-12 12:52:36,529 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_3
2025-08-12 12:52:36,592 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_7
2025-08-12 12:52:36,650 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_12
2025-08-12 12:52:36,708 - app.new_score_oriented_tools - INFO - Fetching topic priority for exam: JEE Mains, subject: Mathematics, chapter: Chapter_5
2025-08-12 12:52:36,778 - app.new_score_oriented_graph - INFO - Topic Validator Agent executing
2025-08-12 12:52:36,779 - app.new_score_oriented_agents - INFO - Validating topic coverage for new_score_oriented plan
2025-08-12 12:52:36,780 - app.new_score_oriented_agents - INFO - Performing final syllabus compliance validation
2025-08-12 12:52:36,781 - app.new_score_oriented_graph - INFO - Supervisor Agent executing
2025-08-12 12:52:36,781 - app.new_score_oriented_agents - INFO - Supervising new_score_oriented plan for target achievement
2025-08-12 12:52:36,781 - app.new_score_oriented_graph - INFO - Finalizing new_score_oriented study plan with enhanced calendar features

================================================================================
🎯 NEW SCORE-ORIENTED STUDY PLAN - DETAILED BREAKDOWN
================================================================================
2025-08-12 to 2026-03-10 | Target: 190/300

7
Months
132
Study Days
56
PYQ Days
56
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
54.5
Total Achievable Score
34.5
Your Target Score
Efficiency Required
63.3%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_10', 'Chapter_2'], 'subject_weightage': 26.0, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_2', 'Chapter_10'], 'subject_weightage': 15.59, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_9', 'Chapter_10'], 'subject_weightage': 12.86, 'chapter_count': 2}

Month 5
63.3% of target
36.7
Total Achievable Score
23.2
Your Target Score
Efficiency Required
63.3%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_3', 'Chapter_7'], 'subject_weightage': 6.81, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_3', 'Chapter_7'], 'subject_weightage': 19.62, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_3', 'Chapter_7'], 'subject_weightage': 10.23, 'chapter_count': 2}

Month 6
63.3% of target
45.2
Total Achievable Score
28.6
Your Target Score
Efficiency Required
63.3%
Subject Breakdown:
Physics:
{'chapters': ['Chapter_12', 'Chapter_5'], 'subject_weightage': 25.26, 'chapter_count': 2}
Chemistry:
{'chapters': ['Chapter_12', 'Chapter_5'], 'subject_weightage': 12.04, 'chapter_count': 2}
Mathematics:
{'chapters': ['Chapter_12', 'Chapter_5'], 'subject_weightage': 7.91, 'chapter_count': 2}

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
Chapter_5
  Topic_4
  Topic_6
  Topic_7
  Topic_3
  Topic_5
  Topic_1
  Topic_2
7 topics

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
Chapter_5
  Topic_1
  Topic_2
  Topic_5
  Topic_6
  Topic_3
  Topic_4
  Topic_7
7 topics

================================================================================
📋 JSON OUTPUT:
================================================================================
{
  "plan_info": {
    "start_date": "2025-08-12",
    "end_date": "2026-03-10",
    "target_score": "190/300",
    "total_months": 7,
    "syllabus_completion_months": 6,
    "study_days": 132,
    "pyq_days": 56,
    "weekend_sessions": 56,
    "dpp_sessions": 396,
    "Full_month_revision": 1
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
      "total_achievable_score": 54.45,
      "user_target_score": 34.48,
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
      "target_ratio": "63.3% of target",
      "total_achievable_score": 36.66,
      "user_target_score": 23.22,
      "efficiency_required": "63.3%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_3",
            "Chapter_7"
          ],
          "subject_weightage": 6.81,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_3",
            "Chapter_7"
          ],
          "subject_weightage": 19.62,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_3",
            "Chapter_7"
          ],
          "subject_weightage": 10.23,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 6": {
      "target_ratio": "63.3% of target",
      "total_achievable_score": 45.21,
      "user_target_score": 28.63,
      "efficiency_required": "63.3%",
      "subject_breakdown": {
        "physics": {
          "chapters": [
            "Chapter_12",
            "Chapter_5"
          ],
          "subject_weightage": 25.26,
          "chapter_count": 2,
          "Dpp": "Morning"
        },
        "chemistry": {
          "chapters": [
            "Chapter_12",
            "Chapter_5"
          ],
          "subject_weightage": 12.04,
          "chapter_count": 2,
          "Dpp": "Evening"
        },
        "mathematics": {
          "chapters": [
            "Chapter_12",
            "Chapter_5"
          ],
          "subject_weightage": 7.91,
          "chapter_count": 2,
          "Dpp": "Night"
        }
      }
    },
    "Month 7": {
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
        "Chapter_2"
      ],
      "chemistry": [
        "Chapter_2",
        "Chapter_10"
      ]
    },
    "month_5": {
      "mathematics": [
        "Chapter_3",
        "Chapter_7"
      ],
      "physics": [
        "Chapter_3",
        "Chapter_7"
      ],
      "chemistry": [
        "Chapter_3",
        "Chapter_7"
      ]
    },
    "month_6": {
      "mathematics": [
        "Chapter_12",
        "Chapter_5"
      ],
      "physics": [
        "Chapter_12",
        "Chapter_5"
      ],
      "chemistry": [
        "Chapter_12",
        "Chapter_5"
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
            "total_topic_count": 19
          },
          "physics": {
            "chapters": {
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
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
            "total_topic_count": 19
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
            "total_topic_count": 19
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
            "total_topic_count": 19
          },
          "physics": {
            "chapters": {
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
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
            "total_topic_count": 19
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
            "total_topic_count": 19
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
            "total_topic_count": 19
          },
          "physics": {
            "chapters": {
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
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
            "total_topic_count": 19
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
            "total_topic_count": 19
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
            "total_topic_count": 19
          },
          "physics": {
            "chapters": {
              "Chapter_3": [
                "Topic_3",
                "Topic_4",
                "Topic_5",
                "Topic_6",
                "Topic_1",
                "Topic_2",
                "Topic_7",
                "Topic_8"
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
            "total_topic_count": 19
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
            "total_topic_count": 19
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
            "total_topic_count": 19
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
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ]
            },
            "total_topic_count": 19
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
            "total_topic_count": 19
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
            "total_topic_count": 19
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
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ]
            },
            "total_topic_count": 19
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
            "total_topic_count": 19
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
            "total_topic_count": 19
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
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ]
            },
            "total_topic_count": 19
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
            "total_topic_count": 19
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
            "total_topic_count": 19
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
              "Chapter_5": [
                "Topic_4",
                "Topic_6",
                "Topic_7",
                "Topic_3",
                "Topic_5",
                "Topic_1",
                "Topic_2"
              ]
            },
            "total_topic_count": 19
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
            "total_topic_count": 19
          }
        }
      }
    }
  }
}

================================================================================
✅ NEW SCORE-ORIENTED PLAN DISPLAY COMPLETE
================================================================================

2025-08-12 12:52:36,830 - app.new_score_oriented_graph - INFO - New Score-Oriented Feedback Counsellor executing
2025-08-12 12:52:36,830 - app.new_score_oriented_graph - INFO - Processing user message: take every month 3 chapters
2025-08-12 12:52:36,831 - app.new_score_oriented_graph - INFO - New Score-Oriented Feedback Counsellor Continue executing
2025-08-12 12:52:36,831 - app.new_score_oriented_graph - INFO - Feedback processed, finalizing plan
INFO:     127.0.0.1:64336 - "POST /chat HTTP/1.1" 200 OK```

