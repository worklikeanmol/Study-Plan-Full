# Study Plan Regeneration - Complete Workflow Documentation

## Overview

The Study Plan Regeneration system is designed for existing users who return after completing their first month of study. It analyzes their progress, performance data, and provides flexible options for continuing their preparation with a regenerated study plan.

## Architecture Overview

### Regeneration Flow Components

1. **User Detection System**: Automatically detects existing vs new users
2. **Performance Analysis**: Comprehensive analysis of completed and pending topics
3. **Regeneration Counsellor**: Guides users through regeneration options
4. **Regeneration Generator**: Extracts regeneration preferences and requirements
5. **Regeneration Flow/Weightage**: Creates regenerated plans based on progress
6. **Regeneration Supervisor**: Validates regenerated plans
7. **Database Integration**: Saves regenerated plans and updates performance data

## Database Schema

### User_Table
```sql
create table public."User_Table" (
  user_id text not null,
  state_msg jsonb not null,
  study_plan jsonb null,
  created_at timestamp with time zone not null default now(),
  constraint User_Table_pkey primary key (user_id)
) TABLESPACE pg_default;
```

### User_Performance
```sql
create table public."User_Performance" (
  user_id text not null,
  completed_topics jsonb not null default '{}'::jsonb,
  not_completed_topics jsonb not null default '{}'::jsonb,
  overall_progress_percentage numeric(5, 2) null default 0.0,
  subject_wise_progress jsonb null default '{}'::jsonb,
  performance_metrics jsonb null default '{}'::jsonb,
  last_updated timestamp with time zone null default now(),
  created_at timestamp with time zone null default now(),
  constraint user_performance_pkey primary key (user_id),
  constraint user_performance_user_id_fkey foreign KEY (user_id) references "User_Table" (user_id) on delete CASCADE
) TABLESPACE pg_default;
```

## Regeneration Workflow

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           REGENERATION WORKFLOW                                  │
└─────────────────────────────────────────────────────────────────────────────────┘

Phase 1: User Detection & Routing
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   User Request  │───▶│ Check User Exists│───▶│ Route to Flow   │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │                        │
                              ▼                        ▼
                       ┌─────────────┐         ┌─────────────┐
                       │ New User    │         │ Existing    │
                       │ Normal Flow │         │ Regen Flow  │
                       └─────────────┘         └─────────────┘

Phase 2: Regeneration Analysis & Guidance
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Regen Counsellor│───▶│ Performance     │───▶│ Topic Importance│
│                 │    │ Analysis        │    │ Analysis        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Progress        │    │ Insights        │    │ Recommendations │
│ Insights        │    │ Generation      │    │ & Options       │
└─────────────────┘    └─────────────────┘    └─────────────────┘

Phase 3: Regeneration Plan Creation
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Regen Generator │───▶│ Regen Flow/     │───▶│ Regen Topic     │
│                 │    │ Weightage       │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Extract Regen   │    │ Create Plan     │    │ Weekly Topics   │
│ Preferences     │    │ with Context    │    │ Breakdown       │
└─────────────────┘    └─────────────────┘    └─────────────────┘

Phase 4: Validation & Finalization
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Regen Supervisor│───▶│ Validation      │───▶│ Final Counsellor│
│                 │    │ & Feedback      │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Progress        │    │ Plan Quality    │    │ Finalization    │
│ Integration     │    │ Check           │    │ & Save          │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Key Features

### 1. Automatic User Detection
- **New Users**: Routed to normal study plan generation flow
- **Existing Users**: Routed to regeneration flow automatically
- **Database Check**: Uses `check_user_exists` tool to determine user status

### 2. Comprehensive Performance Analysis
- **Progress Tracking**: Overall and subject-wise progress percentages
- **Topic Analysis**: Completed vs not-completed topics breakdown
- **Performance Metrics**: Study consistency, weak/strong areas identification
- **Importance Scoring**: Critical, important, and moderate topic classification

### 3. Flexible Regeneration Options
- **Extend Plan**: Continue with remaining topics from original plan
- **Create New**: Fresh start focusing on not-completed topics
- **Hybrid Approach**: Combine important pending topics with new content
- **Time Adjustments**: Modify daily hours or extend timeline
- **Priority Changes**: Shift focus based on performance insights

### 4. User-Centric Approach
- **Complete Flexibility**: Users can choose any regeneration approach
- **No Restrictions**: System provides suggestions but doesn't force decisions
- **Intelligent Guidance**: Highlights importance of pending topics
- **Parallel Planning**: Suggests adding important topics alongside new content

## Regeneration Agents

### 1. Regeneration Counsellor
**Role**: Analyzes performance and guides regeneration process

**Capabilities**:
- Performance data analysis
- Progress insights generation
- Topic importance highlighting
- Regeneration options presentation
- User preference collection

**Tools Used**:
- `check_user_exists`
- `get_user_performance`
- `analyze_topic_importance`
- `generate_progress_insights`

### 2. Regeneration Generator
**Role**: Extracts regeneration preferences and routes to appropriate flow

**Capabilities**:
- Conversation analysis for regeneration preferences
- Requirement extraction
- Flow routing (regen-flow vs regen-weightage)
- Preference validation

### 3. Regeneration Flow/Weightage Agents
**Role**: Create regenerated plans considering previous progress

**Capabilities**:
- Previous progress integration
- Gap analysis and coverage
- Time allocation adjustment
- Priority-based planning with regeneration context

### 4. Regeneration Topic Agent
**Role**: Creates weekly breakdown avoiding duplication

**Capabilities**:
- Completed topic filtering
- Not-completed topic inclusion
- New topic integration
- Efficient time utilization

### 5. Regeneration Supervisor
**Role**: Validates regenerated plans against regeneration requirements

**Capabilities**:
- Progress integration validation
- Gap coverage verification
- Regeneration preference implementation check
- Time allocation realism assessment

## API Endpoints

### 1. Main Chat Endpoint (Enhanced)
```
POST /chat
```
- **Auto-Detection**: Automatically routes new vs existing users
- **Dual Flow Support**: Handles both normal and regeneration flows
- **Separate Storage**: Maintains separate chat histories for each flow

### 2. User Status Check
```
POST /check-user-status
```
- **Purpose**: Check if user is new or existing
- **Returns**: User status, flow type, previous plan existence

### 3. Regeneration Information
```
GET /regeneration-info/{user_id}
```
- **Purpose**: Get comprehensive regeneration data for existing users
- **Returns**: Previous plan, performance data, progress metrics

### 4. Chat Storage Status (Enhanced)
```
GET /chat-storage-status
```
- **Purpose**: Overview of all chat histories
- **Returns**: Normal vs regeneration conversation counts

## Regeneration Process Flow

### Step 1: User Detection
1. User sends message to `/chat` endpoint
2. System calls `check_user_exists` tool
3. Routes to appropriate flow:
   - **New User** → Normal Flow
   - **Existing User** → Regeneration Flow

### Step 2: Performance Analysis
1. Regeneration counsellor retrieves user data
2. Analyzes performance metrics and progress
3. Generates comprehensive insights
4. Evaluates importance of not-completed topics

### Step 3: Regeneration Guidance
1. Presents progress analysis to user
2. Highlights critical pending topics
3. Explains regeneration options
4. Collects user preferences with complete flexibility

### Step 4: Plan Generation
1. Extracts regeneration preferences from conversation
2. Routes to appropriate regeneration flow
3. Creates plan considering:
   - Previous progress
   - Not-completed topics
   - User preferences
   - Time adjustments

### Step 5: Validation & Finalization
1. Validates regenerated plan quality
2. Ensures proper integration of previous progress
3. Verifies gap coverage and preference implementation
4. Saves regenerated plan to database

## Key Considerations

### 1. Topic Importance Analysis
- **Critical Topics**: Must complete before proceeding (Score: 8-10)
- **Important Topics**: Should complete in parallel (Score: 6-7)
- **Moderate Topics**: Can be deferred if needed (Score: 1-5)

### 2. Regeneration Strategies
- **Conservative**: Focus on completing all pending topics
- **Balanced**: Include critical topics, defer moderate ones
- **Aggressive**: Skip some topics to maintain timeline

### 3. Time Management
- **Extension Options**: Add more months or increase daily hours
- **Efficiency Focus**: Optimize time allocation based on performance
- **Parallel Learning**: Combine pending topics with new content

### 4. User Flexibility
- **No Forced Decisions**: Users can choose any approach
- **Intelligent Suggestions**: System provides recommendations
- **Consequence Awareness**: Users understand impact of their choices

## Benefits

1. **Personalized Regeneration**: Based on actual performance data
2. **Flexible Approach**: User-centric with complete freedom of choice
3. **Intelligent Analysis**: Comprehensive topic importance evaluation
4. **Seamless Integration**: Automatic detection and routing
5. **Progress Preservation**: Builds on previous achievements
6. **Gap Addressing**: Systematically handles knowledge gaps

This regeneration system ensures that returning users get the most effective and personalized study plan based on their actual progress and preferences, while maintaining complete flexibility in their approach to continuing their preparation.