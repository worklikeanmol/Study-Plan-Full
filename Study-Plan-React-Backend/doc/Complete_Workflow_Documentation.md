# Study Plan Generator - Complete Workflow Documentation

## Overview

The Study Plan Generator is an AI-powered system that creates personalized study plans for competitive exams like JEE Mains. It uses a sophisticated multi-agent workflow with LangGraph to provide intelligent conversation, plan generation, validation, and iterative refinement based on user feedback.

## Architecture Overview

### Technology Stack
- **FastAPI**: Web framework for REST API
- **LangGraph**: Multi-agent workflow orchestration
- **LangChain**: LLM integration and tooling
- **Google Gemini**: Underlying language model
- **Supabase**: Database for syllabus data and finalized plans
- **Pydantic**: Data validation and modeling

### Core Components

1. **Multi-Agent System**: Specialized agents for different tasks
2. **Conversation Management**: Auto-managed chat history
3. **Plan Generation**: Intelligent study plan creation
4. **Validation System**: Quality assurance with feedback loops
5. **Database Integration**: Persistent storage of finalized plans

## Workflow Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           STUDY PLAN GENERATOR WORKFLOW                          │
└─────────────────────────────────────────────────────────────────────────────────┘

Phase 1: Initial Conversation & Plan Generation
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Counsellor  │───▶│ Generator   │───▶│ Flow/Weight │───▶│ Topic       │
│ Node        │    │ Node        │    │ age Node    │    │ Node        │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
      │                    │                    │                    │
      ▼                    ▼                    ▼                    ▼
 Collect user         Extract user        Apply priorities     Generate weekly
 preferences          preferences        & generate plan      topic breakdown

┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Generator   │───▶│ Supervisor  │───▶│ Feedback    │
│ Collate     │    │ Node        │    │ Counsellor  │
└─────────────┘    └─────────────┘    └─────────────┘
      │                    │                    │
      ▼                    ▼                    ▼
 Create final plan    Validate plan      Present plan &
 with metadata       against intent     collect feedback

Phase 2: Feedback Loop & Refinement
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Feedback    │───▶│ Feedback    │───▶│ Generator   │
│ Counsellor  │    │ Supervisor  │    │ (Re-edit)   │
└─────────────┘    └─────────────┘    └─────────────┘
      │                    │                    │
      ▼                    ▼                    ▼
 Capture change      Provide expert      Regenerate plan
 requests           analysis & pros/cons  with changes

Phase 3: Finalization & Storage
┌─────────────┐    ┌─────────────┐
│ Feedback    │───▶│ Database    │
│ Counsellor  │    │ Storage     │
└─────────────┘    └─────────────┘
      │                    │
      ▼                    ▼
 User says "finalize"   Save to User_Table
```

## Detailed Agent Descriptions

### 1. Counsellor Agent
**Purpose**: Initial conversation and preference collection
**Responsibilities**:
- Greet users and explain the process
- Collect study preferences (subject priorities, chapter preferences)
- Guide users through the conversation flow
- Handle finalization requests

**Key Features**:
- Focuses only on additional preferences (basic info already provided)
- Recognizes generation triggers: "generate", "create plan", etc.
- Handles finalization triggers: "finalize", "yes this is final", etc.
- Prevents infinite loops with re-edit detection

### 2. Generator Agent
**Purpose**: Extract user preferences and route to appropriate planning agents
**Responsibilities**:
- Parse conversation to extract structured preferences
- Validate preferences against actual syllabus data
- Route to Flow Agent (syllabus coverage) or Weightage Agent (priority-based)

**Extraction Capabilities**:
- **Subject Priority**: "focus on mathematics" → `subject_priority: ["mathematics"]`
- **Chapter Priority**: "more time on Chapter_3" → `chapter_priority: {"physics": ["Chapter_3"]}`
- **Chapter Order**: "do Chapter_3 first" → `chapter_coverage_order: {"physics": ["Chapter_3"]}`

### 3. Flow Agent
**Purpose**: Create study plans based on logical chapter dependencies
**Responsibilities**:
- Fetch chapter flow data from database
- Apply user preferences to chapter ordering
- Calculate time allocation with priority multipliers
- Generate monthly coverage plans

**Priority Application**:
- Subject priority: 1.5x multiplier for single subject, 1.25x for two subjects
- Chapter priority: 1.5x time multiplier for prioritized chapters
- Custom chapter ordering overrides default flow

### 4. Weightage Agent
**Purpose**: Create study plans based on chapter importance/weightage
**Responsibilities**:
- Fetch chapter weightage data from database
- Apply priority-based unit calculations
- Sort chapters by importance and user preferences
- Generate time-optimized study plans

### 5. Topic Agent
**Purpose**: Break down first month into weekly topic-level plans
**Responsibilities**:
- Fetch topic priority data for first month chapters
- Create detailed weekly breakdown
- Apply topic-level priority weighting (High: 3x, Medium: 2x, Low: 1x)
- Generate actionable weekly study schedules

### 6. Supervisor Agent
**Purpose**: Validate generated plans against user intent
**Responsibilities**:
- Analyze user intent vs. extracted preferences
- Validate implementation of preferences in the plan
- Provide detailed feedback for regeneration if needed
- Ensure quality and accuracy of plans

**Validation Criteria**:
- Intent matching: User said "focus on math" → subject_priority contains "mathematics"
- Implementation checking: Preferences were actually applied in the plan
- Metadata verification: Plan statistics confirm proper application

### 7. Feedback Counsellor Agent
**Purpose**: Handle post-generation user feedback and refinement
**Responsibilities**:
- Present generated plans to users
- Collect change requests and feedback
- Guide users through refinement process
- Handle finalization and database saving

**Key Features**:
- Distinguishes between feedback collection and implementation
- Routes to Feedback Supervisor for expert analysis
- Handles "re-edit" triggers for plan regeneration
- Manages finalization and database storage

### 8. Feedback Supervisor Agent
**Purpose**: Provide expert analysis of user change requests
**Responsibilities**:
- Analyze impact of requested changes
- Provide pros/cons analysis
- Make recommendations
- Guide users toward informed decisions

## Database Schema

### User_Table
```sql
CREATE TABLE public."User_Table" (
  user_id text NOT NULL,
  state_msg jsonb NOT NULL,
  study_plan jsonb NULL,
  created_at timestamp with time zone NOT NULL DEFAULT now(),
  CONSTRAINT User_Table_pkey PRIMARY KEY (user_id)
);
```

**Fields**:
- `user_id`: Unique identifier for the user
- `state_msg`: Complete conversation state and metadata (JSONB)
- `study_plan`: Finalized study plan with monthly/weekly schedules (JSONB)
- `created_at`: Timestamp of plan finalization

### Supporting Tables
- **Syllabus**: Exam subjects, chapters, and topics
- **Chapter_Flow**: Chapter dependencies and required hours
- **Chapter_Weightage**: Chapter importance and categories
- **Topic_Priority**: Topic-level priorities within chapters

## API Endpoints

### POST /chat
**Purpose**: Main conversational endpoint for study plan generation

**Request Body**:
```json
{
  "user_id": "string",
  "user_message": "string",
  "target_exam": "string",
  "study_plan_type": "string",
  "preparation_type": "string",
  "syllabus": {
    "mathematics": ["Chapter_1", "Chapter_2", ...],
    "physics": ["Chapter_1", "Chapter_2", ...],
    "chemistry": ["Chapter_1", "Chapter_2", ...]
  },
  "number_of_months": "integer",
  "hours_per_day": "integer",
  "reset_chat": "boolean (optional)"
}
```

**Response**:
```json
{
  "user_id": "string",
  "assistant_message": "string",
  "is_plan_generated": "boolean",
  "study_plan": "StudyPlan object or null",
  "chat_context": "object"
}
```

### GET /chat-history/{user_id}
**Purpose**: Retrieve stored chat history for a user

### DELETE /chat-history/{user_id}
**Purpose**: Clear stored chat history for a user

### GET /chat-storage-status
**Purpose**: Get overview of all stored chat histories

## Conversation Flow Examples

### Phase 1: Initial Plan Generation

1. **User Greeting**
   ```
   User: "hi"
   System: Greets and asks for preferences
   ```

2. **Preference Collection**
   ```
   User: "I am weak at mathematics so please focus more on it"
   System: Acknowledges and asks for more details
   ```

3. **Plan Generation Trigger**
   ```
   User: "generate"
   System: Creates complete study plan with mathematics prioritized
   ```

### Phase 2: Feedback and Refinement

4. **Change Request**
   ```
   User: "The plan looks good but I want more time for physics and less for chemistry"
   System: Acknowledges request and provides expert analysis
   ```

5. **Additional Requests**
   ```
   User: "Can we do physics Chapter_3 before Chapter_1?"
   System: Provides dependency analysis and recommendations
   ```

6. **Implementation**
   ```
   User: "re-edit the plan"
   System: Implements changes and shows updated plan
   ```

### Phase 3: Finalization

7. **Plan Approval**
   ```
   User: "finalize" or "yes this is final"
   System: Saves plan to database and provides confirmation
   ```

## Key Features

### 1. Intelligent Preference Extraction
- Natural language processing of user preferences
- Pattern recognition for different types of requests
- Validation against actual syllabus data

### 2. Multi-Agent Validation
- Generator-Supervisor feedback loop
- Quality assurance with regeneration capability
- Intent verification and implementation checking

### 3. Flexible Planning Algorithms
- Flow-based planning (dependency-driven)
- Weightage-based planning (importance-driven)
- Priority application with multipliers

### 4. Comprehensive Metadata
- Chapter-wise coverage tracking
- Time allocation per subject/chapter
- User preference application tracking
- Plan statistics and insights

### 5. Iterative Refinement
- Expert analysis of change requests
- Pros/cons evaluation
- Guided decision making
- Loop prevention mechanisms

### 6. Persistent Storage
- Complete conversation state preservation
- Finalized plan storage
- User history management

## Error Handling

### 1. Infinite Loop Prevention
- Re-edit cycle detection with flags
- Maximum regeneration attempts (3)
- Circuit breaker patterns

### 2. Database Fallbacks
- Mock data when Supabase unavailable
- Graceful degradation
- Error logging and recovery

### 3. Validation Failures
- Detailed feedback for regeneration
- User intent analysis
- Preference extraction error handling

## Performance Considerations

### 1. Chat History Management
- Auto-managed storage per user
- Efficient context building
- Memory optimization

### 2. Database Optimization
- Efficient syllabus queries
- Indexed lookups
- Connection pooling

### 3. LLM Optimization
- Structured output parsing
- Prompt optimization
- Response caching where appropriate

## Security & Privacy

### 1. Data Protection
- User data encryption
- Secure database connections
- API key management

### 2. Input Validation
- Pydantic model validation
- SQL injection prevention
- XSS protection

## Monitoring & Logging

### 1. Comprehensive Logging
- Agent execution tracking
- User interaction logging
- Error tracking and debugging

### 2. Performance Metrics
- Response time monitoring
- Success rate tracking
- User satisfaction metrics

## Future Enhancements

### 1. Advanced Features
- Multi-exam support
- Collaborative planning
- Progress tracking integration

### 2. AI Improvements
- Better intent recognition
- Smarter preference extraction
- Enhanced validation logic

### 3. User Experience
- Real-time collaboration
- Mobile optimization
- Offline capability

---

This documentation provides a comprehensive overview of the Study Plan Generator system. For specific implementation details, refer to the source code and API documentation.