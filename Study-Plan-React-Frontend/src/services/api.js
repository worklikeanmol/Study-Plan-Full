import axios from 'axios'

const API_BASE_URL = 'http://127.0.0.1:8000'

// Create axios instance with default config
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 30000, // 30 seconds timeout
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

export default api