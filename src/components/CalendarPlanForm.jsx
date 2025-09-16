import React, { useState, useEffect } from 'react'
import { Calendar, Target, Clock, BookOpen, AlertCircle, CheckCircle } from 'lucide-react'

export default function CalendarPlanForm({ onGeneratePlan, isLoading = false }) {
  const [formData, setFormData] = useState({
    exam: 'JEE Mains',
    user_target_score: 250,
    total_months: 6,
    start_date: '',
    use_sample_chapters: true
  })
  
  const [validation, setValidation] = useState({
    isValid: true,
    errors: {}
  })

  // Set default start date to today
  useEffect(() => {
    const today = new Date().toISOString().split('T')[0]
    setFormData(prev => ({ ...prev, start_date: today }))
  }, [])

  const handleInputChange = (e) => {
    const { name, value, type, checked } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }))
    
    // Clear validation errors when user starts typing
    if (validation.errors[name]) {
      setValidation(prev => ({
        ...prev,
        errors: { ...prev.errors, [name]: null }
      }))
    }
  }

  const validateForm = () => {
    const errors = {}
    
    if (!formData.exam.trim()) {
      errors.exam = 'Exam is required'
    }
    
    if (!formData.user_target_score || formData.user_target_score < 1 || formData.user_target_score > 300) {
      errors.user_target_score = 'Target score must be between 1 and 300'
    }
    
    if (!formData.total_months || formData.total_months < 1 || formData.total_months > 24) {
      errors.total_months = 'Total months must be between 1 and 24'
    }
    
    if (!formData.start_date) {
      errors.start_date = 'Start date is required'
    } else {
      const startDate = new Date(formData.start_date)
      const today = new Date()
      today.setHours(0, 0, 0, 0)
      
      if (startDate < today) {
        errors.start_date = 'Start date cannot be in the past'
      }
    }
    
    const isValid = Object.keys(errors).length === 0
    setValidation({ isValid, errors })
    return isValid
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    
    if (!validateForm()) {
      return
    }
    
    try {
      // Calculate end date for display
      const startDate = new Date(formData.start_date)
      const endDate = new Date(startDate)
      endDate.setMonth(endDate.getMonth() + parseInt(formData.total_months))
      
      const planData = {
        ...formData,
        user_target_score: parseInt(formData.user_target_score),
        total_months: parseInt(formData.total_months),
        end_date: endDate.toISOString().split('T')[0]
      }
      
      await onGeneratePlan(planData)
    } catch (error) {
      console.error('Error generating calendar plan:', error)
    }
  }

  const calculateEndDate = () => {
    if (formData.start_date && formData.total_months) {
      const startDate = new Date(formData.start_date)
      const endDate = new Date(startDate)
      endDate.setMonth(endDate.getMonth() + parseInt(formData.total_months))
      return endDate.toISOString().split('T')[0]
    }
    return ''
  }

  return (
    <div className="bg-white rounded-lg shadow-lg p-6">
      <div className="flex items-center mb-6">
        <Calendar className="w-6 h-6 text-blue-600 mr-2" />
        <h2 className="text-xl font-semibold text-gray-800">Generate Calendar-Based Study Plan</h2>
      </div>
      
      <form onSubmit={handleSubmit} className="space-y-6">
        {/* Exam Selection */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            <BookOpen className="w-4 h-4 inline mr-1" />
            Target Exam
          </label>
          <select
            name="exam"
            value={formData.exam}
            onChange={handleInputChange}
            className={`w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 ${
              validation.errors.exam ? 'border-red-500' : 'border-gray-300'
            }`}
          >
            <option value="JEE Mains">JEE Mains</option>
            <option value="JEE Advanced">JEE Advanced</option>
            <option value="NEET">NEET</option>
          </select>
          {validation.errors.exam && (
            <p className="text-red-500 text-xs mt-1 flex items-center">
              <AlertCircle className="w-3 h-3 mr-1" />
              {validation.errors.exam}
            </p>
          )}
        </div>

        {/* Target Score */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            <Target className="w-4 h-4 inline mr-1" />
            Target Score (out of 300)
          </label>
          <input
            type="number"
            name="user_target_score"
            value={formData.user_target_score}
            onChange={handleInputChange}
            min="1"
            max="300"
            className={`w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 ${
              validation.errors.user_target_score ? 'border-red-500' : 'border-gray-300'
            }`}
            placeholder="Enter your target score"
          />
          {validation.errors.user_target_score && (
            <p className="text-red-500 text-xs mt-1 flex items-center">
              <AlertCircle className="w-3 h-3 mr-1" />
              {validation.errors.user_target_score}
            </p>
          )}
        </div>

        {/* Date Range */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              <Calendar className="w-4 h-4 inline mr-1" />
              Start Date
            </label>
            <input
              type="date"
              name="start_date"
              value={formData.start_date}
              onChange={handleInputChange}
              className={`w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 ${
                validation.errors.start_date ? 'border-red-500' : 'border-gray-300'
              }`}
            />
            {validation.errors.start_date && (
              <p className="text-red-500 text-xs mt-1 flex items-center">
                <AlertCircle className="w-3 h-3 mr-1" />
                {validation.errors.start_date}
              </p>
            )}
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              <Clock className="w-4 h-4 inline mr-1" />
              Total Months
            </label>
            <input
              type="number"
              name="total_months"
              value={formData.total_months}
              onChange={handleInputChange}
              min="1"
              max="24"
              className={`w-full px-3 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 ${
                validation.errors.total_months ? 'border-red-500' : 'border-gray-300'
              }`}
              placeholder="Number of months"
            />
            {validation.errors.total_months && (
              <p className="text-red-500 text-xs mt-1 flex items-center">
                <AlertCircle className="w-3 h-3 mr-1" />
                {validation.errors.total_months}
              </p>
            )}
          </div>
        </div>

        {/* Calculated End Date Display */}
        {calculateEndDate() && (
          <div className="bg-blue-50 rounded-lg p-4">
            <div className="flex items-center">
              <CheckCircle className="w-5 h-5 text-blue-600 mr-2" />
              <div>
                <div className="font-medium text-blue-800">Plan Duration</div>
                <div className="text-sm text-blue-600">
                  {formData.start_date} to {calculateEndDate()} ({formData.total_months} months)
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Use Sample Chapters Option */}
        <div className="flex items-center">
          <input
            type="checkbox"
            name="use_sample_chapters"
            checked={formData.use_sample_chapters}
            onChange={handleInputChange}
            className="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
          />
          <label className="ml-2 block text-sm text-gray-700">
            Use sample chapter distribution (recommended for testing)
          </label>
        </div>

        {/* Features List */}
        <div className="bg-gray-50 rounded-lg p-4">
          <h3 className="font-medium text-gray-800 mb-3">✨ Enhanced Calendar Features</h3>
          <ul className="space-y-2 text-sm text-gray-600">
            <li className="flex items-center">
              <CheckCircle className="w-4 h-4 text-green-500 mr-2" />
              Monthly analysis with total achievable score and user targets
            </li>
            <li className="flex items-center">
              <CheckCircle className="w-4 h-4 text-green-500 mr-2" />
              Calendar-based daily scheduling starting from your chosen date
            </li>
            <li className="flex items-center">
              <CheckCircle className="w-4 h-4 text-green-500 mr-2" />
              Weekend PYQ focus (Saturday & Sunday dedicated to Previous Year Questions)
            </li>
            <li className="flex items-center">
              <CheckCircle className="w-4 h-4 text-green-500 mr-2" />
              Daily DPP (Daily Practice Papers) for each subject on weekdays
            </li>
            <li className="flex items-center">
              <CheckCircle className="w-4 h-4 text-green-500 mr-2" />
              Proper PYQ and DPP tags for easy identification
            </li>
            <li className="flex items-center">
              <CheckCircle className="w-4 h-4 text-green-500 mr-2" />
              Extended months planning for intensive practice phase
            </li>
          </ul>
        </div>

        {/* Submit Button */}
        <button
          type="submit"
          disabled={isLoading || !validation.isValid}
          className={`w-full py-3 px-4 rounded-lg font-medium transition-colors ${
            isLoading || !validation.isValid
              ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
              : 'bg-blue-600 text-white hover:bg-blue-700'
          }`}
        >
          {isLoading ? (
            <div className="flex items-center justify-center">
              <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2"></div>
              Generating Calendar Plan...
            </div>
          ) : (
            <div className="flex items-center justify-center">
              <Calendar className="w-4 h-4 mr-2" />
              Generate Enhanced Calendar Plan
            </div>
          )}
        </button>
      </form>
    </div>
  )
}