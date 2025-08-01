# Target Score-Based Study Plan System - Complete Workflow Documentation

## Overview

The Target Score-Based Study Plan System is an intelligent planning framework that creates optimized study plans based on user's target scores, available time, and preparation preferences. It supports both comprehensive coverage and score-optimized approaches with automatic routing and validation.

## System Architecture

### Study Plan Types
1. **Generic Plans**: Score-optimized plans with target score requirements
2. **Custom Plans**: Traditional comprehensive coverage plans

### Preparation Types
1. **Syllabus Coverage**: Comprehensive topic coverage following logical flow
2. **Revision**: High-impact topic prioritization for score maximization

## Workflow Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    TARGET SCORE-BASED PLANNING WORKFLOW                          │
└─────────────────────────────────────────────────────────────────────────────────┘

Phase 1: User Input & Validation
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ User Request    │───▶│ Input Validation│───▶│ Score Analysis  │
│ + Target Score  │    │ & Type Detection│    │ & Time Check    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │                        │
                              ▼                        ▼
                       ┌─────────────┐         ┌─────────────┐
                       │ Generic     │         │ Custom      │
                       │ (Score-Based)│         │ (Coverage)  │
                       └─────────────┘         └─────────────┘

Phase 2: Intelligent Routing
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Counsellor      │───▶│ Generator       │───▶│ Smart Router    │
│ (Preferences)   │    │ (Requirements)  │    │ (Agent Selection)│
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Score Context   │    │ Time Validation │    │ Route Decision  │
│ Collection      │    │ & Optimization  │    │ Flow/Weightage  │
└─────────────────┘    └─────────────────┘    └─────────────────┘

Phase 3: Plan Generation
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Flow Agent      │───▶│ Topic Agent     │───▶│ Generator       │
│ (Dependencies)  │    │ (Weekly Plan)   │    │ Collate         │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Weightage Agent │    │ Score           │    │ Plan Metadata   │
│ (Score Priority)│    │ Calculation     │    │ & Insights      │
└─────────────────┘    └─────────────────┘    └─────────────────┘

Phase 4: Validation & Finalization
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Supervisor      │───▶│ Score Validation│───▶│ Final Plan      │
│ (Quality Check) │    │ & Warnings      │    │ Presentation    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Agent Roles & Responsibilities

### 1. Counsellor Agent
**Role**: Initial user interaction and preference collection

**Responsibilities**:
- Collect additional study preferences beyond form data
- Detect score-based plans and explain optimization features
- Guide users through preference selection
- Trigger plan generation when ready

**For Generic Plans**:
- Acknowledge target score (e.g., "252/300")
- Explain score optimization approach
- Highlight high-weightage chapter focus
- Collect subject/chapter preferences

**For Custom Plans**:
- Focus on comprehensive coverage preferences
- Collect study constraints and special requirements
- Guide through traditional preference selection

**Key Behaviors**:
- Encouraging and supportive tone
- Focus on personalization, not basic info collection
- Wait for generation trigger words ("generate", "create plan")

### 2. Generator Agent
**Role**: Requirement extraction and intelligent routing

**Responsibilities**:
- Extract user preferences from conversation
- Validate target score feasibility
- Perform time sufficiency analysis
- Route to appropriate agent (Flow/Weightage)

**Score-Based Logic**:
```python
if study_plan_type == "generic" and target_score:
    time_needed = calculate_time_for_target(target_score)
    if available_time < time_needed:
        warn_user()
        route_to_weightage()  # Score optimization
    else:
        route_by_preparation_type()
```

**Routing Rules**:
- **Generic + Insufficient Time** → Weightage Agent (score optimization)
- **Generic + Sufficient Time** → Based on preparation_type
- **Custom Plans** → Based on preparation_type
- **Syllabus Coverage** → Flow Agent
- **Revision** → Weightage Agent

### 3. Flow Agent
**Role**: Dependency-based comprehensive planning

**Responsibilities**:
- Create plans based on logical chapter flow
- Maintain proper learning dependencies
- Ensure comprehensive syllabus coverage
- Balance coverage with score considerations (for generic plans)

**For Syllabus Coverage**:
- Follow chapter dependencies strictly
- Ensure all topics are covered systematically
- Maintain proper learning progression

**For Generic Plans with Scores**:
- Follow logical flow but prioritize high-weightage chapters
- Calculate expected score with flow-based approach
- Warn if flow approach won't achieve target score

**Key Features**:
- Chapter dependency analysis
- Comprehensive coverage guarantee
- Score impact calculation (for generic plans)

### 4. Weightage Agent
**Role**: Score-optimized priority-based planning

**Responsibilities**:
- Prioritize chapters by score impact
- Apply category multipliers (High=3x, Medium=2x, Low=1x)
- Optimize for target score achievement
- Calculate score efficiency (marks per hour)

**Priority Logic**:
1. **Average Weightage** (Primary factor)
2. **Chapter Category** (High/Medium/Low multipliers)
3. **Topic Priority** (High/Medium/Low within chapters)

**For Generic Plans**:
- Calculate expected score with weightage approach
- Warn if target not achievable
- Suggest time extensions or target adjustments
- Focus on high-impact chapters

**For Revision Preparation**:
- Maximize score impact per hour
- Focus on high-weightage topics only
- Optimize for exam efficiency

### 5. Topic Agent
**Role**: Weekly topic breakdown and scheduling

**Responsibilities**:
- Break down monthly plans into weekly topics
- Prioritize topics within chapters
- Create detailed study schedules
- Consider topic priorities and dependencies

**Score-Based Enhancements**:
- Prioritize high-priority topics first
- Calculate topic-level score contributions
- Optimize weekly schedules for score impact

### 6. Generator Collate Agent
**Role**: Plan assembly and insight generation

**Responsibilities**:
- Combine monthly and weekly plans
- Generate comprehensive insights
- Include score analysis and predictions
- Create plan metadata for validation

**Score-Based Features**:
- Calculate expected score vs target
- Generate score optimization insights
- Include achievement probability
- Provide score gap analysis

### 7. Supervisor Agent
**Role**: Quality validation and score verification

**Responsibilities**:
- Validate plan quality and completeness
- Verify score calculations and predictions
- Check preference implementation
- Provide feedback for regeneration if needed

**Score Validation**:
- Verify expected score calculations
- Check target score achievability
- Validate time allocation efficiency
- Ensure proper priority implementation

## Score Optimization Logic

### Priority Calculation Formula
```
For Generic Plans:
Chapter Priority Score = (Average Weightage × 0.5) + 
                        (Category Multiplier × 5 × 0.3) + 
                        (Efficiency Score × 10 × 0.2)

Where:
- Category Multiplier: High=3, Medium=2, Low=1
- Efficiency Score: Average Weightage / Required Hours
```

### Time Validation Process
```
1. Calculate total available hours: months × 30 × daily_hours
2. Estimate required hours for target score
3. Compare available vs required
4. If insufficient:
   - Generate warning message
   - Suggest options (extend time, adjust target, use revision)
   - Route to weightage agent for optimization
```

### Score Prediction Algorithm
```
Expected Score = Σ(Chapter Weightage × Coverage Percentage)

For each subject:
  For each chapter:
    if chapter in plan:
      expected_score += chapter.average_weightage × coverage_percentage
```

## Regeneration Flow Integration

### Score Progress Analysis
- Calculate current score from completed topics
- Determine remaining score needed for target
- Analyze pending topic importance
- Suggest regeneration approach

### Updated Target Support
- Allow users to modify target scores
- Recalculate feasibility with new targets
- Adjust regeneration strategy accordingly

## Warning and Recommendation System

### Time Warnings
```
⚠️ Target score 252/300 requires ~1200 hours, but you have 1080 hours available.

Options:
1. Extend study time to 1200 hours (add 120 hours)
2. Adjust target score to achievable range (~230/300)
3. Focus on high-weightage topics only (revision approach)
```

### Score Warnings
```
⚠️ Flow-based approach may not achieve target 252/300. Expected: 240/300

Recommendations:
- Consider switching to weightage-based optimization
- Focus on high-priority chapters first
- Add 1-2 months for comprehensive coverage
```

## API Integration Points

### Input Validation
- Validate target_score (1-300 for JEE Mains)
- Check study_plan_type ("generic" or "custom")
- Verify preparation_type ("syllabus coverage" or "revision")

### Response Enhancement
- Include score analysis in all responses
- Provide achievement probability
- Show time vs score trade-offs

## Error Handling

### Invalid Target Scores
- Scores > 300: Adjust to maximum possible
- Scores < 50: Warn about low targets
- Missing scores for generic plans: Request clarification

### Insufficient Data
- Missing weightage data: Use default values
- Incomplete syllabus: Warn and proceed with available data
- Database errors: Fallback to mock data with warnings

## Performance Metrics

### Success Indicators
- Target score achievement rate
- User satisfaction with score predictions
- Plan completion rates
- Time estimation accuracy

### Monitoring Points
- Score prediction accuracy
- Route decision effectiveness
- Warning system utilization
- User preference implementation success

This comprehensive workflow ensures intelligent, score-optimized study plan generation with proper validation, warnings, and user guidance throughout the process.