# New Score-Oriented Plan APIs Documentation

## Overview
New Score-Oriented Plan APIs provide advanced study plan generation focused on achieving specific target scores with **complete syllabus coverage**. These plans use sophisticated algorithms for dependency management, score optimization, and enhanced features like weekend practice schedules.

**Key Characteristics:**
- **Preparation Type:** Always **Revision** (forced)
- **Syllabus Coverage:** Always **Complete** (100% coverage mandatory)
- **Minimum Duration:** 6 months minimum
- **Target Score:** Required (1-300 for JEE Mains)
- **Exam Date:** Required (YYYY-MM-DD format)

---

## 📋 **Core APIs**

### 1. **Save Form Data (New Score-Oriented)**
**Endpoint:** `POST /save-form`

**Purpose:** Save new score-oriented form data with target score and exam date validation.

**Request Body:**
```json
{
  "user_id": "user_789012",
  "target_exam": "JEE Mains",
  "study_plan_type": "new_score_oriented",
  "preparation_type": "revision",
  "syllabus": {
    "mathematics": ["Algebra", "Calculus", "Coordinate Geometry", "Trigonometry"],
    "physics": ["Mechanics", "Thermodynamics", "Waves", "Electrostatics"],
    "chemistry": ["Atomic Structure", "Chemical Bonding", "Thermodynamics"]
  },
  "number_of_months": 8,
  "hours_per_day": 8,
  "target_score": 250,
  "exam_date": "2024-04-15"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Form data saved successfully",
  "user_id": "user_789012"
}
```

**Validation Rules:**
- `target_score`: Required, 1-300 range
- `exam_date`: Required, minimum 6 months from today
- `preparation_type`: Automatically set to "revision"
- `number_of_months`: Auto-calculated from exam date

---

### 2. **Interactive Chat Planning (New Score-Oriented)**
**Endpoint:** `POST /chat`

**Purpose:** Advanced chat interface with requirement collection and enhanced plan generation.

**Request Body:**
```json
{
  "user_id": "user_789012",
  "user_message": "I want to achieve 250 marks and focus more on physics",
  "target_exam": "JEE Mains",
  "study_plan_type": "new_score_oriented",
  "preparation_type": "revision",
  "syllabus": {...},
  "number_of_months": 8,
  "hours_per_day": 8,
  "target_score": 250,
  "exam_date": "2024-04-15",
  "reset_chat": false
}
```

**Response (Requirement Collection Phase):**
```json
{
  "user_id": "user_789012",
  "assistant_message": "Great! I understand you want to achieve 250 marks with a focus on physics. For your New Score-Oriented plan, I'll ensure complete syllabus coverage with strategic prioritization. Are there any specific chapters in physics you'd like to emphasize? When ready, say 'generate' to create your comprehensive plan.",
  "is_plan_generated": false,
  "study_plan": null,
  "chat_context": {...}
}
```

**Response (Plan Generated):**
```json
{
  "user_id": "user_789012",
  "assistant_message": "🎯 New Score-Oriented study plan generated successfully!",
  "is_plan_generated": true,
  "study_plan": {
    "insights": "🎯 NEW SCORE-ORIENTED STUDY PLAN\n\nTarget Achievement Strategy: Your plan is designed to achieve 250/300 marks within 8 months through complete syllabus coverage...",
    "monthly_plan": {
      "Month 1": {
        "physics": [
          {"chapter": "Mechanics", "coverage": 1.0},
          {"chapter": "Thermodynamics", "coverage": 1.0}
        ],
        "mathematics": [
          {"chapter": "Algebra", "coverage": 1.0}
        ],
        "chemistry": [
          {"chapter": "Atomic Structure", "coverage": 1.0}
        ]
      }
    },
    "weekly_plan": {...},
    "new_score_oriented_data": {
      "revision_flow_results": {
        "physics": {
          "chapters": [...],
          "total_weightage": 120.5,
          "dependency_chains": {...}
        }
      },
      "monthly_distribution": {
        "month_1": {
          "month_number": 1,
          "subjects": {
            "physics": {
              "chapters": [
                {"chapter": "Mechanics", "coverage_percentage": 1.0, "weightage": 35.2}
              ]
            }
          }
        }
      },
      "enhanced_features": {
        "monthly_target_scores": {
          "Month 1": {
            "user_target_score": 31.25,
            "total_achievable_score": 45.8,
            "efficiency_required": 68.2
          }
        },
        "weekend_schedule": {
          "saturday": {"type": "PYQ", "focus": "Previous Year Questions"},
          "sunday": {"type": "DPP", "focus": "Daily Practice Problems"}
        },
        "extended_months_plan": {
          "months_7_8": {
            "focus": "Intensive Practice & Revision",
            "type": "PYQ & DPP Focus"
          }
        }
      }
    }
  },
  "chat_context": {...}
}
```

**Usage:**
- Collects user requirements without immediate generation
- Validates target score achievability
- Generates comprehensive plans with enhanced features
- Supports feedback and plan modifications

---

### 3. **Validate Exam Date**
**Endpoint:** `POST /new_score_oriented/validate-exam-date`

**Purpose:** Validate if exam date meets minimum 6-month requirement for new score-oriented plans.

**Request Body:**
```json
{
  "exam_date": "2024-04-15"
}
```

**Response (Valid):**
```json
{
  "is_valid": true,
  "calculated_months": 8,
  "message": "Exam date is valid. You have 8 months for preparation.",
  "exam_date": "2024-04-15",
  "start_date": "2023-08-15"
}
```

**Response (Invalid):**
```json
{
  "is_valid": false,
  "calculated_months": 4,
  "message": "❌ New Score-Oriented plans require minimum 6 months. You have only 4 months until 2024-04-15.",
  "exam_date": "2024-04-15",
  "start_date": "2023-12-15"
}
```

---

### 4. **Generate Revision Flow**
**Endpoint:** `POST /new_score_oriented/generate-revision-flow`

**Purpose:** Generate comprehensive revision flow with dependency management and score optimization.

**Request Body:**
```json
{
  "exam": "JEE Mains",
  "target_score": 250,
  "available_months": 8
}
```

**Response:**
```json
{
  "exam": "JEE Mains",
  "target_score": 250,
  "available_months": 8,
  "subjects": {
    "physics": {
      "weightage_data": [
        {
          "chapter": "Mechanics",
          "average_weightage": 35.2,
          "chapter_category": "High",
          "dependencies": null
        }
      ],
      "flow_data": [
        {
          "chapter": "Mechanics",
          "required_hours": 45,
          "difficulty_level": "Medium",
          "prerequisites": []
        }
      ],
      "total_chapters": 12
    },
    "chemistry": {...},
    "mathematics": {...}
  }
}
```

---

### 5. **Calculate Progress**
**Endpoint:** `POST /new_score_oriented/calculate-progress`

**Purpose:** Calculate study progress and remaining targets for new score-oriented plans.

**Request Body:**
```json
{
  "user_id": "user_789012",
  "exam": "JEE Mains",
  "target_score": 250,
  "completed_chapters": {
    "physics": ["Mechanics", "Thermodynamics"],
    "mathematics": ["Algebra"],
    "chemistry": ["Atomic Structure"]
  }
}
```

**Response:**
```json
{
  "user_id": "user_789012",
  "overall_progress": 35.7,
  "subject_progress": {
    "physics": {
      "completed_chapters": 2,
      "total_chapters": 12,
      "progress_percentage": 16.7,
      "score_achieved": 42.3,
      "remaining_score": 77.7
    }
  },
  "target_achievement": {
    "current_projected_score": 89.5,
    "target_score": 250,
    "achievement_probability": 78.2,
    "remaining_effort_required": "High"
  },
  "recommendations": [
    "Focus on high-weightage chapters in remaining subjects",
    "Increase practice frequency for completed topics"
  ]
}
```

---

### 6. **Validate Syllabus Coverage**
**Endpoint:** `POST /new_score_oriented/validate-syllabus`

**Purpose:** Validate that planned chapters provide complete syllabus coverage.

**Request Body:**
```json
{
  "exam": "JEE Mains",
  "planned_chapters": {
    "physics": ["Mechanics", "Thermodynamics", "Waves"],
    "mathematics": ["Algebra", "Calculus"],
    "chemistry": ["Atomic Structure", "Chemical Bonding"]
  }
}
```

**Response:**
```json
{
  "exam": "JEE Mains",
  "validation_result": {
    "is_complete": false,
    "coverage_percentage": 67.5,
    "missing_chapters": {
      "physics": ["Electrostatics", "Optics", "Modern Physics"],
      "mathematics": ["Coordinate Geometry", "Trigonometry"],
      "chemistry": ["Thermodynamics", "Chemical Kinetics"]
    },
    "recommendations": [
      "Add missing chapters for complete coverage",
      "Prioritize high-weightage missing chapters"
    ]
  }
}
```

---

### 7. **Get Complete Syllabus**
**Endpoint:** `GET /new_score_oriented/syllabus/{exam}`

**Purpose:** Retrieve complete syllabus for validation and planning.

**Response:**
```json
{
  "exam": "JEE Mains",
  "complete_syllabus": {
    "physics": [
      {
        "chapter": "Mechanics",
        "topics": ["Kinematics", "Newton's Laws", "Work Energy"],
        "weightage": 35.2,
        "category": "High"
      }
    ],
    "mathematics": [...],
    "chemistry": [...]
  },
  "total_chapters": 36,
  "total_topics": 324
}
```

---

### 8. **Generate Enhanced Plan**
**Endpoint:** `POST /new_score_oriented/generate_enhanced_plan`

**Purpose:** Generate comprehensive enhanced score-oriented plan with all features.

**Request Body:**
```json
{
  "exam": "JEE Mains",
  "target_score": "250/300",
  "exam_date": "2024-04-15",
  "start_date": "2023-08-15"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Enhanced score-oriented plan generated successfully",
  "data": {
    "plan_info": {
      "exam": "JEE Mains",
      "target_score": 250,
      "total_months": 8,
      "syllabus_completion_target": 6,
      "practice_months": 2
    },
    "monthly_breakdown": {
      "month_1": {
        "month_number": 1,
        "month_name": "August 2023",
        "target_score": 31.25,
        "chapters_to_complete": 4,
        "subjects": {
          "physics": {
            "chapters": [
              {
                "chapter": "Mechanics",
                "weightage": 35.2,
                "completion_target": 100,
                "estimated_hours": 45
              }
            ]
          }
        }
      }
    },
    "enhanced_features": {
      "monthly_target_scores": {
        "Month 1": {
          "user_target_score": 31.25,
          "total_achievable_score": 45.8,
          "efficiency_required": 68.2,
          "subject_breakdown": {...}
        }
      },
      "weekend_schedule": {
        "saturday": {
          "type": "PYQ",
          "focus": "Previous Year Questions",
          "duration": "3-4 hours",
          "subjects_rotation": ["Physics", "Chemistry", "Mathematics"]
        },
        "sunday": {
          "type": "DPP",
          "focus": "Daily Practice Problems",
          "duration": "2-3 hours",
          "mixed_topics": true
        }
      },
      "extended_months_plan": {
        "months_7_8": {
          "tag": "PYQ & DPP Focus",
          "focus_type": "Intensive Practice",
          "intensity_level": "High",
          "daily_targets": {
            "pyq_questions": 50,
            "dpp_problems": 30,
            "revision_hours": 4
          }
        }
      }
    }
  }
}
```

---

## 🎯 **New Score-Oriented Characteristics**

### **Mandatory Features**
- **Complete Syllabus Coverage:** 100% of all chapters must be included
- **Revision Focus:** Always uses revision-based approach
- **Dependency Management:** Chapters ordered by prerequisites
- **Score Optimization:** High-weightage chapters prioritized within logical flow
- **6-Month Minimum:** Ensures adequate time for complete coverage

### **Enhanced Features**
- **Monthly Target Scores:** Specific score goals for each month
- **Weekend Practice Schedule:** Saturday (PYQ) + Sunday (DPP)
- **Extended Practice Phase:** Additional months for intensive practice
- **Dependency Resolution:** Automatic prerequisite handling
- **Force-Fit Strategy:** Adjustments to ensure target achievement

---

## 📊 **Data Models**

### **NewScoreOrientedUserData Model**
```python
{
  "user_id": str,
  "target_exam": str,
  "study_plan_type": "new_score_oriented",
  "preparation_type": "revision",  # Always revision
  "syllabus_coverage": "complete",  # Always complete
  "target_score": int,  # Required, 1-300
  "exam_date": str,     # Required, YYYY-MM-DD
  "number_of_months": int  # Auto-calculated
}
```

### **NewScoreOrientedStudyPlan Model**
```python
{
  "user_id": str,
  "target_score": int,
  "exam_date": str,
  "total_months": int,
  "syllabus_completion_months": int,  # Max 6
  "practice_months": int,
  "monthly_plans": List[MonthlyRevisionPlan],
  "revision_flow_results": Dict[str, RevisionFlowPlan],
  "overall_strategy": str,
  "dependency_analysis": Dict,
  "coverage_validation": Dict,
  "target_achievement_probability": float,
  "enhanced_features": EnhancedFeatures
}
```

### **EnhancedFeatures Model**
```python
{
  "monthly_target_scores": Dict[str, Any],
  "extended_months_plan": Dict[str, Any],
  "weekly_topic_breakdown": Dict[str, Any],
  "weekend_schedule": Dict[str, Any],
  "strategy_summary": Dict[str, Any]
}
```

### **RevisionFlowPlan Model**
```python
{
  "subject": str,
  "chapters": List[ChapterWithDependencies],
  "total_chapters": int,
  "total_weightage": float,
  "dependency_chains": Dict[str, List[str]],
  "completion_sequence": List[str]
}
```

---

## 🚀 **Usage Examples**

### **Example 1: Complete New Score-Oriented Workflow**
```bash
# 1. Validate exam date
curl -X POST "http://localhost:8000/new_score_oriented/validate-exam-date" \
  -H "Content-Type: application/json" \
  -d '{"exam_date": "2024-04-15"}'

# 2. Save form data
curl -X POST "http://localhost:8000/save-form" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "student_nso_001",
    "target_exam": "JEE Mains",
    "study_plan_type": "new_score_oriented",
    "preparation_type": "revision",
    "syllabus": {...},
    "number_of_months": 8,
    "hours_per_day": 8,
    "target_score": 250,
    "exam_date": "2024-04-15"
  }'

# 3. Start requirement collection
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "student_nso_001",
    "user_message": "I want to achieve 250 marks with focus on physics",
    "target_exam": "JEE Mains",
    "study_plan_type": "new_score_oriented",
    "preparation_type": "revision",
    "target_score": 250,
    "exam_date": "2024-04-15",
    ...
  }'

# 4. Generate plan
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "student_nso_001",
    "user_message": "generate",
    ...
  }'
```

### **Example 2: Progress Tracking**
```bash
# Track progress
curl -X POST "http://localhost:8000/new_score_oriented/calculate-progress" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "student_nso_001",
    "exam": "JEE Mains",
    "target_score": 250,
    "completed_chapters": {
      "physics": ["Mechanics", "Thermodynamics"],
      "mathematics": ["Algebra"],
      "chemistry": ["Atomic Structure"]
    }
  }'
```

### **Example 3: Enhanced Plan Generation**
```bash
# Generate enhanced plan directly
curl -X POST "http://localhost:8000/new_score_oriented/generate_enhanced_plan" \
  -H "Content-Type: application/json" \
  -d '{
    "exam": "JEE Mains",
    "target_score": "250/300",
    "exam_date": "2024-04-15",
    "start_date": "2023-08-15"
  }'
```

---

## ⚡ **Key Differentiators**

### **vs Custom Plans**
| Feature | Custom Plans | New Score-Oriented |
|---------|-------------|-------------------|
| **Preparation Type** | Syllabus Coverage OR Revision | Always Revision |
| **Syllabus Coverage** | Flexible | Always 100% Complete |
| **Target Score** | Optional | Required |
| **Exam Date** | Optional | Required |
| **Minimum Duration** | Any | 6 months minimum |
| **Dependency Management** | Basic | Advanced with prerequisites |
| **Enhanced Features** | None | Monthly targets, weekend schedule |
| **Practice Integration** | Basic | Structured PYQ/DPP schedule |

### **Advanced Algorithms**
- **Revision Flow Agent:** Complete syllabus with dependency resolution
- **Score Optimization:** Target achievement with force-fit strategy
- **Enhanced Validation:** Multi-layer syllabus compliance checking
- **Supervisor Analysis:** Target achievement probability calculation

### **Enhanced Features**
- **Monthly Target Scores:** Specific score goals for each month
- **Weekend Practice:** Saturday (PYQ) + Sunday (DPP) schedule
- **Extended Practice Phase:** Additional months for intensive practice
- **Weekly Topic Breakdown:** Detailed topic distribution
- **Strategy Summary:** Comprehensive preparation strategy

---

## 🔍 **Error Handling**

### **Validation Errors**
```json
{
  "detail": "❌ Target score is required for New Score-Oriented study plans. Please provide a target score between 1-300."
}
```

```json
{
  "detail": "❌ New Score-Oriented plans require minimum 6 months. You have only 4 months until 2024-04-15."
}
```

### **Processing Errors**
```json
{
  "status": "error",
  "message": "Validation error in enhanced plan generation: Invalid exam date format"
}
```

---

## 📈 **Performance Considerations**

- **Plan Generation:** 5-10 seconds for complete analysis
- **Dependency Resolution:** Advanced algorithms for prerequisite handling
- **Memory Usage:** Enhanced features require additional storage
- **Database Queries:** Optimized for complete syllabus retrieval
- **Validation Overhead:** Multiple validation layers for quality assurance

---

## 🎯 **Best Practices**

### **For API Consumers**
1. **Always validate exam date** before plan generation
2. **Use requirement collection phase** for better personalization
3. **Monitor progress** using progress tracking APIs
4. **Leverage enhanced features** for comprehensive planning
5. **Handle validation errors** gracefully

### **For Plan Generation**
1. **Complete syllabus coverage** is mandatory
2. **6-month minimum** ensures quality planning
3. **Target score validation** prevents unrealistic goals
4. **Dependency resolution** ensures logical learning progression
5. **Enhanced features** provide comprehensive preparation strategy

---

This documentation covers all New Score-Oriented Plan APIs with their advanced features, enhanced algorithms, and comprehensive planning capabilities. The system ensures complete syllabus coverage while optimizing for target score achievement through sophisticated dependency management and score optimization strategies.