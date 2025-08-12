# Custom Plan APIs Documentation

## Overview
Custom Plan APIs provide flexible study plan generation with two preparation types: **Syllabus Coverage** and **Revision**. These APIs support personalized learning through interactive chat-based planning.

---

## 📋 **Core APIs**

### 1. **Save Form Data**
**Endpoint:** `POST /save-form`

**Purpose:** Save user form data to database for later use in chat-based planning.

**Request Body:**
```json
{
  "user_id": "user_123456",
  "target_exam": "JEE Mains",
  "study_plan_type": "Custom",
  "preparation_type": "Syllabus Coverage",
  "syllabus": {
    "mathematics": ["Algebra", "Calculus", "Coordinate Geometry"],
    "physics": ["Mechanics", "Thermodynamics", "Waves"],
    "chemistry": ["Atomic Structure", "Chemical Bonding", "Thermodynamics"]
  },
  "number_of_months": 6,
  "hours_per_day": 6,
  "target_score": null,
  "exam_date": null
}
```

**Response:**
```json
{
  "success": true,
  "message": "Form data saved successfully",
  "user_id": "user_123456"
}
```

**Usage:**
- Store initial form configuration
- Enable chat-based personalization
- Support form validation and persistence

---

### 2. **Interactive Chat Planning**
**Endpoint:** `POST /chat`

**Purpose:** Interactive chat interface for personalized study plan generation with AI counsellor.

**Request Body:**
```json
{
  "user_id": "user_123456",
  "user_message": "I want to focus more on physics and prioritize mechanics chapter",
  "target_exam": "JEE Mains",
  "study_plan_type": "Custom",
  "preparation_type": "Syllabus Coverage",
  "syllabus": {
    "mathematics": ["Algebra", "Calculus"],
    "physics": ["Mechanics", "Thermodynamics"],
    "chemistry": ["Atomic Structure", "Chemical Bonding"]
  },
  "number_of_months": 6,
  "hours_per_day": 6,
  "target_score": null,
  "exam_date": null,
  "reset_chat": false
}
```

**Response (Conversation Phase):**
```json
{
  "user_id": "user_123456",
  "assistant_message": "Great! I understand you want to focus more on physics and prioritize the mechanics chapter. This will help build a strong foundation. Are there any other subjects or chapters you'd like to emphasize? When you're ready, just say 'generate' to create your plan.",
  "is_plan_generated": false,
  "study_plan": null,
  "chat_context": {
    "1": {
      "user_message": "I want to focus more on physics and prioritize mechanics chapter",
      "assistant_message": "Great! I understand you want to focus more on physics..."
    }
  }
}
```

**Response (Plan Generated):**
```json
{
  "user_id": "user_123456",
  "assistant_message": "🎉 Your personalized study plan has been generated!",
  "is_plan_generated": true,
  "study_plan": {
    "insights": "Your plan prioritizes physics with emphasis on mechanics...",
    "monthly_plan": {
      "Month 1": {
        "physics": [
          {"chapter": "Mechanics", "coverage": 1.0},
          {"chapter": "Thermodynamics", "coverage": 0.6}
        ],
        "mathematics": [
          {"chapter": "Algebra", "coverage": 0.8}
        ],
        "chemistry": [
          {"chapter": "Atomic Structure", "coverage": 0.7}
        ]
      }
    },
    "weekly_plan": {
      "week_1": {
        "physics": {
          "Mechanics": ["Kinematics", "Newton's Laws", "Work Energy"]
        },
        "mathematics": {
          "Algebra": ["Linear Equations", "Quadratic Equations"]
        }
      }
    }
  },
  "chat_context": {...}
}
```

**Usage:**
- Collect user preferences through natural conversation
- Generate personalized plans based on user input
- Support iterative refinement and feedback

---

### 3. **Legacy Direct Plan Generation**
**Endpoint:** `POST /generate-study-plan`

**Purpose:** Direct study plan generation without chat interface (legacy support).

**Request Body:**
```json
{
  "user_id": "user_123456",
  "target_exam": "JEE Mains",
  "study_plan_type": "Custom",
  "preparation_type": "Revision",
  "syllabus": {
    "mathematics": ["Algebra", "Calculus"],
    "physics": ["Mechanics", "Thermodynamics"],
    "chemistry": ["Atomic Structure"]
  },
  "number_of_months": 4,
  "hours_per_day": 8,
  "user_message": "Create a revision focused plan"
}
```

**Response:**
```json
{
  "insights": "Revision-focused plan prioritizing high-weightage topics...",
  "monthly_plan": {
    "month_1": {
      "physics": [{"chapter": "Mechanics", "coverage": 1.0}],
      "mathematics": [{"chapter": "Calculus", "coverage": 0.9}],
      "chemistry": [{"chapter": "Atomic Structure", "coverage": 0.8}]
    }
  },
  "weekly_plan": {...}
}
```

---

## 🎯 **Preparation Types**

### **1. Syllabus Coverage**
- **Purpose:** Complete learning approach for comprehensive preparation
- **Features:**
  - Logical chapter progression based on dependencies
  - Comprehensive topic coverage
  - Balanced time allocation across subjects
  - Sequential learning path

**Workflow:**
1. **Flow Agent** analyzes chapter dependencies
2. Applies user preferences (subject/chapter priorities)
3. Creates logical learning sequence
4. Generates comprehensive coverage plan

**Example Use Cases:**
- First-time learners
- Long-term preparation (6+ months)
- Complete syllabus mastery
- Foundation building

### **2. Revision**
- **Purpose:** Focused revision for exam preparation
- **Features:**
  - Weightage-based chapter prioritization
  - High-impact topic selection
  - Efficient time utilization
  - Score optimization focus

**Workflow:**
1. **Weightage Agent** prioritizes chapters by importance
2. Applies 3x/2x/1x multipliers (High/Medium/Low categories)
3. Optimizes for maximum score impact
4. Creates revision-focused plan

**Example Use Cases:**
- Short-term preparation (2-4 months)
- Pre-exam revision
- Weak area strengthening
- Score maximization

---

## 🔧 **Utility APIs**

### 4. **Get Chapters by Exam**
**Endpoint:** `GET /chapters/{exam}`

**Purpose:** Retrieve available chapters for a specific exam.

**Response:**
```json
{
  "exam": "JEE Mains",
  "subjects": {
    "mathematics": ["Algebra", "Calculus", "Coordinate Geometry"],
    "physics": ["Mechanics", "Thermodynamics", "Waves"],
    "chemistry": ["Atomic Structure", "Chemical Bonding"]
  },
  "total_chapters": 8,
  "source": "database"
}
```

### 5. **Chat History Management**
**Endpoint:** `GET /chat-history/{user_id}`

**Purpose:** Retrieve stored chat history for a user.

**Response:**
```json
{
  "user_id": "user_123456",
  "chat_key": "user_123456_JEE Mains_Custom",
  "total_turns": 3,
  "chat_history": {
    "1": {
      "user_message": "I want to focus on physics",
      "assistant_message": "Great choice! Physics focus noted..."
    }
  }
}
```

### 6. **Clear Chat History**
**Endpoint:** `DELETE /chat-history/{user_id}`

**Purpose:** Clear stored chat history for a user.

### 7. **Check User Status**
**Endpoint:** `POST /check-user-status`

**Purpose:** Check if user is new or existing (for regeneration routing).

---

## 📊 **Data Models**

### **UserData Model**
```python
{
  "user_id": str,
  "target_exam": str,
  "study_plan_type": str,  # "Custom"
  "preparation_type": str,  # "Syllabus Coverage" or "Revision"
  "syllabus": Dict[str, List[str]],
  "number_of_months": int,
  "hours_per_day": int,
  "target_score": Optional[int] = None,  # Not used for Custom
  "exam_date": Optional[str] = None      # Not used for Custom
}
```

### **StudyPlan Model**
```python
{
  "insights": str,
  "monthly_plan": Dict[str, MonthlySubjectPlan],
  "weekly_plan": Dict[str, WeeklySubjectPlan]
}
```

### **MonthlySubjectPlan Model**
```python
{
  "physics": List[ChapterCoverage],
  "chemistry": List[ChapterCoverage],
  "mathematics": List[ChapterCoverage]
}
```

### **ChapterCoverage Model**
```python
{
  "chapter": str,
  "coverage": float  # 0.0 to 1.0 (percentage)
}
```

---

## 🚀 **Usage Examples**

### **Example 1: Syllabus Coverage Plan**
```bash
# 1. Save form data
curl -X POST "http://localhost:8000/save-form" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "student_001",
    "target_exam": "JEE Mains",
    "study_plan_type": "Custom",
    "preparation_type": "Syllabus Coverage",
    "syllabus": {
      "mathematics": ["Algebra", "Calculus"],
      "physics": ["Mechanics", "Thermodynamics"],
      "chemistry": ["Atomic Structure"]
    },
    "number_of_months": 6,
    "hours_per_day": 6
  }'

# 2. Start chat conversation
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "student_001",
    "user_message": "I want to focus more on mathematics",
    "target_exam": "JEE Mains",
    "study_plan_type": "Custom",
    "preparation_type": "Syllabus Coverage",
    "syllabus": {...},
    "number_of_months": 6,
    "hours_per_day": 6
  }'

# 3. Generate plan
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "student_001",
    "user_message": "generate",
    ...
  }'
```

### **Example 2: Revision Plan**
```bash
# Generate revision-focused plan
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "student_002",
    "user_message": "Create a revision plan focusing on high-weightage chapters",
    "target_exam": "JEE Mains",
    "study_plan_type": "Custom",
    "preparation_type": "Revision",
    "syllabus": {...},
    "number_of_months": 3,
    "hours_per_day": 8
  }'
```

---

## ⚡ **Key Features**

### **Personalization**
- **Subject Priority:** Focus more time on specific subjects
- **Chapter Priority:** Emphasize particular chapters
- **Chapter Order:** Custom sequence for chapter coverage
- **Learning Preferences:** Adaptive to user's study style

### **Intelligent Routing**
- **Flow Agent:** For comprehensive syllabus coverage
- **Weightage Agent:** For revision and score optimization
- **Topic Agent:** Detailed weekly topic breakdown
- **Supervisor:** Quality validation and feedback

### **Feedback System**
- **Interactive Refinement:** Modify plans based on user feedback
- **Expert Analysis:** AI-powered pros/cons evaluation
- **Iterative Improvement:** Continuous plan enhancement
- **Finalization Support:** Lock in approved plans

### **Flexibility**
- **Multiple Preparation Types:** Syllabus Coverage vs Revision
- **Adaptive Time Allocation:** Based on user preferences
- **Comprehensive Coverage:** All subjects and topics included
- **Scalable Duration:** 2-12 months support

---

## 🔍 **Error Handling**

### **Common Error Responses**
```json
{
  "detail": "Error message describing the issue"
}
```

### **Validation Errors**
- Invalid user_id format
- Missing required fields
- Invalid preparation_type values
- Malformed syllabus structure

### **Processing Errors**
- Database connection issues
- Plan generation failures
- Chat context corruption
- Validation failures

---

## 📈 **Performance Considerations**

- **Chat History:** Stored in memory (Redis recommended for production)
- **Plan Generation:** 2-5 seconds typical response time
- **Database Queries:** Optimized for chapter/topic retrieval
- **Concurrent Users:** Supports multiple simultaneous conversations

---

This documentation covers all Custom Plan APIs with detailed examples and usage patterns. The system provides flexible, personalized study planning through intelligent conversation and adaptive algorithms.