import React, { useState, useRef, useEffect } from 'react'
import { Send, Bot, User, RotateCcw, Loader, AlertCircle } from 'lucide-react'
import { toast } from 'react-hot-toast'
import { useStudyPlan } from '../context/StudyPlanContext'
import { sendChatMessage } from '../services/api'
import { testBackendConnection } from '../utils/testConnection'

export default function ChatInterface() {
  const { state, dispatch } = useStudyPlan()
  const [message, setMessage] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [backendConnected, setBackendConnected] = useState(null)
  const messagesEndRef = useRef(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [state.chatHistory])

  // Test backend connection on component mount
  useEffect(() => {
    const checkConnection = async () => {
      const isConnected = await testBackendConnection()
      setBackendConnected(isConnected)
      if (!isConnected) {
        toast.error('Cannot connect to backend. Please start the Study Plan API server.')
      }
    }
    checkConnection()
  }, [])

  useEffect(() => {
    // Add welcome message if no chat history and form is valid
    if (state.chatHistory.length === 0 && state.isFormValid && backendConnected) {
      const welcomeMessage = {
        type: 'assistant',
        content: `Great! I have your configuration:

📚 **Exam**: ${state.formData.target_exam}
📋 **Plan Type**: ${state.formData.study_plan_type}
🎯 **Preparation**: ${state.formData.preparation_type}
${state.formData.target_score ? `🎯 **Target Score**: ${state.formData.target_score}/300` : ''}
⏰ **Duration**: ${state.formData.number_of_months} months, ${state.formData.hours_per_day} hours/day

Now, tell me about your study preferences, weak areas, or any specific requirements you have. When you're ready, just say "generate" to create your study plan!`,
        timestamp: new Date().toISOString()
      }
      dispatch({ type: 'ADD_CHAT_MESSAGE', payload: welcomeMessage })
    }
  }, [state.isFormValid, state.formData, state.chatHistory.length, dispatch, backendConnected])

  const handleSendMessage = async () => {
    if (!message.trim()) return

    if (!state.isFormValid) {
      toast.error('Please fill out the form first before chatting.')
      return
    }

    if (backendConnected === false) {
      toast.error('Backend is not connected. Please start the API server first.')
      return
    }

    // Add user message
    const userMessage = {
      type: 'user',
      content: message.trim(),
      timestamp: new Date().toISOString()
    }
    dispatch({ type: 'ADD_CHAT_MESSAGE', payload: userMessage })
    setMessage('')
    setIsLoading(true)

    try {
      const requestData = {
        ...state.formData,
        user_message: message.trim(),
        reset_chat: false,
        // Ensure target_score is properly handled for Generic, Score-Oriented, and New Score-Oriented plans
        target_score: (state.formData.study_plan_type === 'Generic' || state.formData.study_plan_type === 'Score-Oriented' || state.formData.study_plan_type === 'new_score_oriented') ? state.formData.target_score : null
      }

      const response = await sendChatMessage(requestData)

      // Add assistant response
      const assistantMessage = {
        type: 'assistant',
        content: response.assistant_message,
        timestamp: new Date().toISOString()
      }
      dispatch({ type: 'ADD_CHAT_MESSAGE', payload: assistantMessage })

      // Check if study plan was generated
      if (response.is_plan_generated && response.study_plan) {
        // Enhanced plan data handling for different plan types
        const planData = {
          ...response.study_plan,
          plan_type: state.formData.study_plan_type,
          target_score: state.formData.target_score,
          exam_date: state.formData.exam_date,
          user_id: state.formData.user_id
        }
        
        dispatch({ type: 'SET_STUDY_PLAN', payload: planData })
        
        // Show appropriate success message based on plan type
        const planTypeName = state.formData.study_plan_type === 'new_score_oriented' 
          ? 'New Score-Oriented' 
          : state.formData.study_plan_type
        
        toast.success(`${planTypeName} study plan generated! Check the "View Plan" section.`)
      }

    } catch (error) {
      console.error('Error sending chat message:', error)
      const errorMessage = {
        type: 'assistant',
        content: 'Sorry, I encountered an error. Please try again or check if the API server is running.',
        timestamp: new Date().toISOString()
      }
      dispatch({ type: 'ADD_CHAT_MESSAGE', payload: errorMessage })
      toast.error('Failed to send message. Please check your connection and try again.')
    } finally {
      setIsLoading(false)
    }
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSendMessage()
    }
  }

  const resetChat = () => {
    if (window.confirm('Are you sure you want to reset the chat? This will clear all conversation history.')) {
      dispatch({ type: 'RESET_CHAT' })
      toast.success('Chat has been reset.')
    }
  }

  const formatMessage = (content) => {
    return content
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.*?)\*/g, '<em>$1</em>')
      .split('\n').map((line, index) => (
        <span key={index}>
          {line}
          {index < content.split('\n').length - 1 && <br />}
        </span>
      ))
  }

  if (!state.isFormValid) {
    return (
      <div className="flex items-center justify-center h-full">
        <div className="text-center">
          <Bot className="h-16 w-16 text-gray-400 mx-auto mb-4" />
          <h3 className="text-lg font-medium text-gray-900 mb-2">
            Complete the Form First
          </h3>
          <p className="text-gray-600">
            Please fill out the study plan form before starting the chat.
          </p>
        </div>
      </div>
    )
  }

  if (backendConnected === false) {
    return (
      <div className="flex items-center justify-center h-full">
        <div className="text-center">
          <AlertCircle className="h-16 w-16 text-red-400 mx-auto mb-4" />
          <h3 className="text-lg font-medium text-gray-900 mb-2">
            Backend Connection Failed
          </h3>
          <p className="text-gray-600 mb-4">
            Cannot connect to the Study Plan API server.
          </p>
          <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4 text-left">
            <h4 className="font-medium text-yellow-800 mb-2">To fix this:</h4>
            <ol className="text-sm text-yellow-700 space-y-1">
              <li>1. Open a terminal in the Study-Plan directory</li>
              <li>2. Backend is deployed at: <code className="bg-green-100 px-1 rounded">AWS Lambda</code></li>
              <li>3. Check your internet connection</li>
              <li>4. Contact support if the issue persists</li>
            </ol>
          </div>
          <button
            onClick={() => window.location.reload()}
            className="mt-4 btn-primary"
          >
            Retry Connection
          </button>
        </div>
      </div>
    )
  }

  return (
    <div className="flex flex-col h-full max-w-4xl mx-auto">
      {/* Header */}
      <div className="bg-white rounded-t-lg shadow-sm border-b p-4 flex justify-between items-center">
        <div className="flex items-center">
          <Bot className="h-6 w-6 text-primary-600 mr-2" />
          <h2 className="text-xl font-semibold text-gray-900">Chat Assistant</h2>
        </div>
        <button
          onClick={resetChat}
          className="flex items-center text-gray-600 hover:text-gray-800 transition-colors"
        >
          <RotateCcw className="h-4 w-4 mr-1" />
          Reset Chat
        </button>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto bg-gray-50 p-4 space-y-4">
        {state.chatHistory.map((msg, index) => (
          <div
            key={index}
            className={`flex ${msg.type === 'user' ? 'justify-end' : 'justify-start'}`}
          >
            <div
              className={`max-w-3xl rounded-lg p-4 ${
                msg.type === 'user'
                  ? 'bg-primary-600 text-white'
                  : 'bg-white text-gray-900 shadow-sm border'
              }`}
            >
              <div className="flex items-start space-x-2">
                {msg.type === 'assistant' && (
                  <Bot className="h-5 w-5 text-primary-600 mt-0.5 flex-shrink-0" />
                )}
                {msg.type === 'user' && (
                  <User className="h-5 w-5 text-white mt-0.5 flex-shrink-0" />
                )}
                <div className="flex-1">
                  <div className="prose prose-sm max-w-none">
                    {typeof msg.content === 'string' ? (
                      <div dangerouslySetInnerHTML={{ __html: msg.content.replace(/\n/g, '<br>') }} />
                    ) : (
                      formatMessage(msg.content)
                    )}
                  </div>
                  <div className={`text-xs mt-2 ${msg.type === 'user' ? 'text-primary-200' : 'text-gray-500'}`}>
                    {new Date(msg.timestamp).toLocaleTimeString()}
                  </div>
                </div>
              </div>
            </div>
          </div>
        ))}
        
        {isLoading && (
          <div className="flex justify-start">
            <div className="bg-white text-gray-900 shadow-sm border rounded-lg p-4">
              <div className="flex items-center space-x-2">
                <Bot className="h-5 w-5 text-primary-600" />
                <Loader className="h-4 w-4 animate-spin text-primary-600" />
                <span className="text-sm text-gray-600">Assistant is typing...</span>
              </div>
            </div>
          </div>
        )}
        
        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <div className="bg-white rounded-b-lg shadow-sm border-t p-4">
        <div className="flex space-x-4">
          <textarea
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Type your message here... (Press Enter to send)"
            className="flex-1 resize-none border border-gray-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            rows="2"
            disabled={isLoading}
          />
          <button
            onClick={handleSendMessage}
            disabled={!message.trim() || isLoading}
            className="btn-primary px-6 py-2 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <Send className="h-4 w-4" />
          </button>
        </div>
      </div>
    </div>
  )
}