import axios from 'axios'

const API_BASE_URL = 'http://127.0.0.1:8000'

// Create axios instance with default config
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 150000, // 30 seconds timeout
  withCredentials: false, // Disable credentials for CORS
})

// Request interceptor for logging
api.interceptors.request.use(
  (config) => {
    console.log(`Making ${config.method?.toUpperCase()} request to ${config.url}`)
    return config
  },
  (error) => {
    console.error('Request error:', error)
    return Promise.reject(error)
  }
)

// Response interceptor for error handling
api.interceptors.response.use(
  (response) => {
    return response
  },
  (error) => {
    console.error('Response error:', error)
    
    if (error.code === 'ECONNABORTED') {
      throw new Error('Request timeout. Please try again.')
    }
    
    if (error.response) {
      // Server responded with error status
      const status = error.response.status
      const message = error.response.data?.detail || error.response.data?.message || 'An error occurred'
      
      switch (status) {
        case 400:
          throw new Error(`Bad Request: ${message}`)
        case 404:
          throw new Error(`Not Found: ${message}`)
        case 500:
          throw new Error(`Server Error: ${message}`)
        default:
          throw new Error(`Error ${status}: ${message}`)
      }
    } else if (error.request) {
      // Network error
      throw new Error('Network error. Please check if the API server is running.')
    } else {
      throw new Error('An unexpected error occurred.')
    }
  }
)

// API functions
export const sendChatMessage = async (requestData) => {
  try {
    const response = await api.post('/chat', requestData)
    return response.data
  } catch (error) {
    console.error('Error in sendChatMessage:', error)
    throw error
  }
}

// Validate exam date for Score-Oriented plans
export const validateExamDate = async (examDate) => {
  try {
    const response = await api.post('/score/validate-exam-date', { exam_date: examDate })
    return response.data
  } catch (error) {
    console.error('Error in validateExamDate:', error)
    throw error
  }
}

export const checkUserStatus = async (userId) => {
  try {
    const response = await api.post('/check-user-status', { user_id: userId })
    return response.data
  } catch (error) {
    console.error('Error in checkUserStatus:', error)
    throw error
  }
}

export const getChatHistory = async (userId, targetExam = 'JEE Mains', studyPlanType = 'Custom') => {
  try {
    const params = new URLSearchParams({
      target_exam: targetExam,
      study_plan_type: studyPlanType
    })
    const response = await api.get(`/chat-history/${userId}?${params}`)
    return response.data
  } catch (error) {
    console.error('Error in getChatHistory:', error)
    throw error
  }
}

export const clearChatHistory = async (userId, targetExam = 'JEE Mains', studyPlanType = 'Custom') => {
  try {
    const params = new URLSearchParams({
      target_exam: targetExam,
      study_plan_type: studyPlanType
    })
    const response = await api.delete(`/chat-history/${userId}?${params}`)
    return response.data
  } catch (error) {
    console.error('Error in clearChatHistory:', error)
    throw error
  }
}

export const getRegenerationInfo = async (userId) => {
  try {
    const response = await api.get(`/regeneration-info/${userId}`)
    return response.data
  } catch (error) {
    console.error('Error in getRegenerationInfo:', error)
    throw error
  }
}

export const getChatStorageStatus = async () => {
  try {
    const response = await api.get('/chat-storage-status')
    return response.data
  } catch (error) {
    console.error('Error in getChatStorageStatus:', error)
    throw error
  }
}

// Save form data to database
export const saveFormData = async (formData) => {
  try {
    const response = await api.post('/save-form', formData)
    return response.data
  } catch (error) {
    console.error('Error in saveFormData:', error)
    throw error
  }
}

// Get chapters for a specific exam from database
export const getChaptersByExam = async (exam) => {
  try {
    const response = await api.get(`/chapters/${encodeURIComponent(exam)}`)
    return response.data
  } catch (error) {
    console.error('Error in getChaptersByExam:', error)
    throw error
  }
}

// Legacy endpoint for direct study plan generation
export const generateStudyPlan = async (requestData) => {
  try {
    const response = await api.post('/generate-study-plan', requestData)
    return response.data
  } catch (error) {
    console.error('Error in generateStudyPlan:', error)
    throw error
  }
}

// Enhanced Calendar API Functions

// Generate calendar-based study plan
export const generateCalendarStudyPlan = async (planData) => {
  try {
    const response = await api.post('/enhanced_calendar/generate-calendar-plan', planData)
    return response.data
  } catch (error) {
    console.error('Error in generateCalendarStudyPlan:', error)
    throw error
  }
}

// Get monthly analysis with total_achievable_score and user_target
export const getMonthlyAnalysis = async (analysisData) => {
  try {
    const response = await api.post('/enhanced_calendar/monthly-analysis', analysisData)
    return response.data
  } catch (error) {
    console.error('Error in getMonthlyAnalysis:', error)
    throw error
  }
}

// Calculate monthly target scores
export const calculateMonthlyTargets = async (targetData) => {
  try {
    const response = await api.post('/enhanced_calendar/calculate-monthly-targets', targetData)
    return response.data
  } catch (error) {
    console.error('Error in calculateMonthlyTargets:', error)
    throw error
  }
}

// Generate extended months plan (beyond 6 months)
export const generateExtendedPlan = async (extendedData) => {
  try {
    const response = await api.post('/enhanced_calendar/extended-months-plan', extendedData)
    return response.data
  } catch (error) {
    console.error('Error in generateExtendedPlan:', error)
    throw error
  }
}

// Create weekend schedule with PYQ focus
export const createWeekendSchedule = async (scheduleData) => {
  try {
    const response = await api.post('/enhanced_calendar/weekend-schedule', scheduleData)
    return response.data
  } catch (error) {
    console.error('Error in createWeekendSchedule:', error)
    throw error
  }
}

// Generate weekly topic breakdown
export const generateWeeklyTopics = async (topicData) => {
  try {
    const response = await api.post('/enhanced_calendar/weekly-topic-breakdown', topicData)
    return response.data
  } catch (error) {
    console.error('Error in generateWeeklyTopics:', error)
    throw error
  }
}

// Get current date for calendar planning
export const getCurrentDate = async () => {
  try {
    const response = await api.get('/enhanced_calendar/current-date')
    return response.data
  } catch (error) {
    console.error('Error in getCurrentDate:', error)
    throw error
  }
}

// Validate study plan dates
export const validateStudyDates = async (startDate, totalMonths) => {
  try {
    const response = await api.post('/enhanced_calendar/validate-dates', {
      start_date: startDate,
      total_months: totalMonths
    })
    return response.data
  } catch (error) {
    console.error('Error in validateStudyDates:', error)
    throw error
  }
}

// Get sample monthly chapters for testing
export const getSampleMonthlyChapters = async (exam, totalMonths = 6) => {
  try {
    const response = await api.get(`/enhanced_calendar/sample-monthly-chapters/${encodeURIComponent(exam)}?total_months=${totalMonths}`)
    return response.data
  } catch (error) {
    console.error('Error in getSampleMonthlyChapters:', error)
    throw error
  }
}

// New Score-Oriented API Functions

// Validate exam date for new score-oriented plans (minimum 6 months)
export const validateNewScoreOrientedExamDate = async (examDate) => {
  try {
    const response = await api.post('/new_score_oriented/validate-exam-date', { exam_date: examDate })
    return response.data
  } catch (error) {
    console.error('Error in validateNewScoreOrientedExamDate:', error)
    throw error
  }
}

// Generate enhanced score-oriented study plan
export const generateEnhancedScoreOrientedPlan = async (planData) => {
  try {
    const response = await api.post('/new_score_oriented/generate_enhanced_plan', planData)
    return response.data
  } catch (error) {
    console.error('Error in generateEnhancedScoreOrientedPlan:', error)
    throw error
  }
}

// Get complete syllabus for new score-oriented validation
export const getNewScoreOrientedSyllabus = async (exam) => {
  try {
    const response = await api.get(`/new_score_oriented/syllabus/${encodeURIComponent(exam)}`)
    return response.data
  } catch (error) {
    console.error('Error in getNewScoreOrientedSyllabus:', error)
    throw error
  }
}

// Calculate progress for new score-oriented plan
export const calculateNewScoreOrientedProgress = async (progressData) => {
  try {
    const response = await api.post('/new_score_oriented/calculate-progress', progressData)
    return response.data
  } catch (error) {
    console.error('Error in calculateNewScoreOrientedProgress:', error)
    throw error
  }
}

// Get revision flow for new score-oriented plans
export const getNewScoreOrientedRevisionFlow = async (revisionData) => {
  try {
    const response = await api.post('/new_score_oriented/revision-flow', revisionData)
    return response.data
  } catch (error) {
    console.error('Error in getNewScoreOrientedRevisionFlow:', error)
    throw error
  }
}

// Validate syllabus coverage for new score-oriented plans
export const validateNewScoreOrientedSyllabus = async (syllabusData) => {
  try {
    const response = await api.post('/new_score_oriented/validate-syllabus', syllabusData)
    return response.data
  } catch (error) {
    console.error('Error in validateNewScoreOrientedSyllabus:', error)
    throw error
  }
}

export default api