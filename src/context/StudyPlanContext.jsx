import React, { createContext, useContext, useReducer } from 'react'

const StudyPlanContext = createContext()

const initialState = {
  formData: {
    user_id: '',
    target_exam: 'JEE Mains',
    study_plan_type: 'Custom',
    preparation_type: 'Syllabus Coverage',
    syllabus: {
      mathematics: [],
      physics: [],
      chemistry: []
    },
    // Custom plan specific fields
    number_of_months: 3,
    hours_per_day: 6,
    // ScoreGeneric plan specific fields
    target_score: null,
    exam_date: null
  },
  chatHistory: [],
  studyPlan: null,
  isFormValid: false,
  isExistingUser: false,
  // Add validation state for different plan types
  validationErrors: {},
  isSubmitting: false
}

function studyPlanReducer(state, action) {
  switch (action.type) {
    case 'UPDATE_FORM_DATA':
      return {
        ...state,
        formData: { ...state.formData, ...action.payload }
      }
    case 'SET_SYLLABUS':
      return {
        ...state,
        formData: {
          ...state.formData,
          syllabus: action.payload
        }
      }
    case 'ADD_CHAT_MESSAGE':
      return {
        ...state,
        chatHistory: [...state.chatHistory, action.payload]
      }
    case 'SET_CHAT_HISTORY':
      return {
        ...state,
        chatHistory: action.payload
      }
    case 'SET_STUDY_PLAN':
      return {
        ...state,
        studyPlan: action.payload
      }
    case 'SET_FORM_VALIDITY':
      return {
        ...state,
        isFormValid: action.payload
      }
    case 'SET_USER_STATUS':
      return {
        ...state,
        isExistingUser: action.payload
      }
    case 'SET_VALIDATION_ERRORS':
      return {
        ...state,
        validationErrors: action.payload
      }
    case 'SET_SUBMITTING':
      return {
        ...state,
        isSubmitting: action.payload
      }
    case 'RESET_CHAT':
      return {
        ...state,
        chatHistory: []
      }
    case 'RESET_FORM':
      return {
        ...state,
        formData: initialState.formData,
        validationErrors: {},
        isFormValid: false
      }
    default:
      return state
  }
}

export function StudyPlanProvider({ children }) {
  const [state, dispatch] = useReducer(studyPlanReducer, initialState)

  return (
    <StudyPlanContext.Provider value={{ state, dispatch }}>
      {children}
    </StudyPlanContext.Provider>
  )
}

export function useStudyPlan() {
  const context = useContext(StudyPlanContext)
  if (!context) {
    throw new Error('useStudyPlan must be used within a StudyPlanProvider')
  }
  return context
}