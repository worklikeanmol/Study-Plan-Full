import React, { useState, useEffect } from 'react'
import { useForm } from 'react-hook-form'
import { toast } from 'react-hot-toast'
import { GraduationCap, Target, Clock, BookOpen, Plus, X } from 'lucide-react'
import { useStudyPlan } from '../context/StudyPlanContext'
import { saveFormData, getChaptersByExam } from '../services/api'

const defaultSyllabus = {
  mathematics: ['Algebra', 'Calculus', 'Coordinate Geometry', 'Trigonometry', 'Statistics', 'Probability', 'Vectors', 'Complex Numbers', 'Matrices', 'Sequences and Series'],
  physics: ['Mechanics', 'Thermodynamics', 'Waves and Oscillations', 'Electrostatics', 'Current Electricity', 'Magnetism', 'Electromagnetic Induction', 'Optics', 'Modern Physics', 'Atomic Structure'],
  chemistry: ['Atomic Structure', 'Chemical Bonding', 'Thermodynamics', 'Chemical Equilibrium', 'Ionic Equilibrium', 'Electrochemistry', 'Chemical Kinetics', 'Organic Chemistry', 'Coordination Compounds', 'Biomolecules']
}

export default function StudyPlanForm({ onComplete }) {
  const { state, dispatch } = useStudyPlan()
  const { register, handleSubmit, watch, setValue, formState: { errors } } = useForm({
    defaultValues: state.formData
  })

  const [syllabus, setSyllabus] = useState(state.formData.syllabus)
  const [customValidationErrors, setCustomValidationErrors] = useState({})

  // Watch form values for real-time validation
  const studyPlanType = watch('study_plan_type')
  const preparationType = watch('preparation_type')
  const targetScore = watch('target_score')
  const numberOfMonths = watch('number_of_months')
  const targetExam = watch('target_exam')

  // Generate random user ID on component mount
  useEffect(() => {
    if (!state.formData.user_id) {
      const randomId = 'user_' + Math.random().toString(36).substr(2, 9)
      setValue('user_id', randomId)
      dispatch({ type: 'UPDATE_FORM_DATA', payload: { user_id: randomId } })
    }
  }, [])

  // Load syllabus from database on mount
  useEffect(() => {
    const loadInitialSyllabus = async () => {
      if (Object.values(state.formData.syllabus).every(arr => arr.length === 0)) {
        try {
          const targetExam = state.formData.target_exam || 'JEE Mains'
          const chaptersData = await getChaptersByExam(targetExam)
          
          if (chaptersData.subjects && Object.keys(chaptersData.subjects).length > 0) {
            setSyllabus(chaptersData.subjects)
            dispatch({ type: 'SET_SYLLABUS', payload: chaptersData.subjects })
            toast.success(`Loaded ${chaptersData.total_chapters} chapters from database!`)
          } else {
            // Fallback to hardcoded default
            setSyllabus(defaultSyllabus)
            dispatch({ type: 'SET_SYLLABUS', payload: defaultSyllabus })
            toast.success('Loaded default syllabus')
          }
        } catch (error) {
          console.error('Error loading initial syllabus:', error)
          // Fallback to hardcoded default on error
          setSyllabus(defaultSyllabus)
          dispatch({ type: 'SET_SYLLABUS', payload: defaultSyllabus })
          toast.success('Loaded default syllabus')
        }
      }
    }
    
    loadInitialSyllabus()
  }, [])

  // Reload syllabus when target exam changes
  useEffect(() => {
    const reloadSyllabusForExam = async () => {
      if (targetExam && targetExam !== state.formData.target_exam) {
        try {
          toast.loading(`Loading syllabus for ${targetExam}...`)
          const chaptersData = await getChaptersByExam(targetExam)
          
          if (chaptersData.subjects && Object.keys(chaptersData.subjects).length > 0) {
            setSyllabus(chaptersData.subjects)
            dispatch({ type: 'SET_SYLLABUS', payload: chaptersData.subjects })
            toast.success(`Loaded ${chaptersData.total_chapters} chapters for ${targetExam}!`)
          } else {
            toast.warning(`No chapters found for ${targetExam}, keeping current syllabus`)
          }
        } catch (error) {
          console.error('Error reloading syllabus for exam change:', error)
          toast.error(`Failed to load syllabus for ${targetExam}`)
        }
      }
    }
    
    reloadSyllabusForExam()
  }, [targetExam])

  // Handle study plan type change
  useEffect(() => {
    if (studyPlanType === 'Generic') {
      // Target score is required for Generic plans
      setCustomValidationErrors(prev => ({
        ...prev,
        target_score: targetScore ? null : 'Target score is required for Generic plans'
      }))
    } else {
      // Clear target score for Custom plans
      setValue('target_score', null)
      setCustomValidationErrors(prev => ({
        ...prev,
        target_score: null
      }))
    }
  }, [studyPlanType, targetScore, setValue])

  // Handle preparation type change
  useEffect(() => {
    if (preparationType === 'Syllabus Coverage') {
      // Minimum 3 months required for Syllabus Coverage
      if (numberOfMonths && numberOfMonths < 3) {
        setValue('number_of_months', 3)
        toast.warning('Minimum 3 months required for Syllabus Coverage. Value adjusted to 3.')
      }
      setCustomValidationErrors(prev => ({
        ...prev,
        number_of_months: numberOfMonths && numberOfMonths < 3 ? 'Minimum 3 months required for Syllabus Coverage' : null
      }))
    } else {
      setCustomValidationErrors(prev => ({
        ...prev,
        number_of_months: null
      }))
    }
  }, [preparationType, numberOfMonths, setValue])

  // Validate target score range
  useEffect(() => {
    if (targetScore && (targetScore < 1 || targetScore > 300)) {
      setCustomValidationErrors(prev => ({
        ...prev,
        target_score: 'Target score must be between 1 and 300'
      }))
    } else if (studyPlanType === 'Generic' && !targetScore) {
      setCustomValidationErrors(prev => ({
        ...prev,
        target_score: 'Target score is required for Generic plans'
      }))
    } else {
      setCustomValidationErrors(prev => ({
        ...prev,
        target_score: null
      }))
    }
  }, [targetScore, studyPlanType])

  const addChapter = (subject) => {
    setSyllabus(prev => ({
      ...prev,
      [subject]: [...prev[subject], '']
    }))
  }

  const removeChapter = (subject, index) => {
    setSyllabus(prev => ({
      ...prev,
      [subject]: prev[subject].filter((_, i) => i !== index)
    }))
  }

  const updateChapter = (subject, index, value) => {
    setSyllabus(prev => ({
      ...prev,
      [subject]: prev[subject].map((chapter, i) => i === index ? value : chapter)
    }))
  }

  const loadDefaultSyllabus = async () => {
    try {
      const targetExam = watch('target_exam') || 'JEE Mains'
      toast.loading('Loading syllabus from database...')
      
      const chaptersData = await getChaptersByExam(targetExam)
      
      if (chaptersData.subjects && Object.keys(chaptersData.subjects).length > 0) {
        setSyllabus(chaptersData.subjects)
        dispatch({ type: 'SET_SYLLABUS', payload: chaptersData.subjects })
        toast.success(`Loaded ${chaptersData.total_chapters} chapters from database!`)
      } else {
        // Fallback to hardcoded default if no data from database
        setSyllabus(defaultSyllabus)
        dispatch({ type: 'SET_SYLLABUS', payload: defaultSyllabus })
        toast.success('Loaded default syllabus (database had no data)')
      }
    } catch (error) {
      console.error('Error loading syllabus from database:', error)
      // Fallback to hardcoded default on error
      setSyllabus(defaultSyllabus)
      dispatch({ type: 'SET_SYLLABUS', payload: defaultSyllabus })
      toast.error('Failed to load from database, using default syllabus')
    }
  }

  const validateSyllabus = () => {
    const subjects = ['mathematics', 'physics', 'chemistry']
    for (const subject of subjects) {
      const validChapters = syllabus[subject].filter(chapter => chapter.trim() !== '')
      if (validChapters.length === 0) {
        return `At least one chapter is required for ${subject}`
      }
    }
    return null
  }

  const onSubmit = async (data) => {
    // Validate syllabus
    const syllabusError = validateSyllabus()
    if (syllabusError) {
      toast.error(syllabusError)
      return
    }

    // Check for custom validation errors
    const hasCustomErrors = Object.values(customValidationErrors).some(error => error !== null)
    if (hasCustomErrors) {
      toast.error('Please fix the form errors before proceeding')
      return
    }

    // Clean syllabus data (remove empty chapters)
    const cleanSyllabus = {}
    Object.keys(syllabus).forEach(subject => {
      cleanSyllabus[subject] = syllabus[subject].filter(chapter => chapter.trim() !== '')
    })

    const formData = {
      ...data,
      syllabus: cleanSyllabus,
      target_score: studyPlanType === 'Generic' ? parseInt(data.target_score) : null
    }

    try {
      // Save form data to database first
      const loadingToast = toast.loading('Saving form data...')
      const saveResponse = await saveFormData(formData)
      toast.dismiss(loadingToast)
      
      if (saveResponse.success) {
        // Update local state
        dispatch({ type: 'UPDATE_FORM_DATA', payload: formData })
        dispatch({ type: 'SET_SYLLABUS', payload: cleanSyllabus })
        dispatch({ type: 'SET_FORM_VALIDITY', payload: true })
        
        toast.success('Form data saved! Proceeding to chat...')
        onComplete()
      } else {
        toast.error(`Failed to save form data: ${saveResponse.message}`)
        console.error('Save failed:', saveResponse)
      }
    } catch (error) {
      console.error('Error saving form data:', error)
      
      // Check if it's a network error (backend not running)
      if (error.message.includes('Network error') || error.message.includes('ECONNREFUSED')) {
        toast.error('Backend server is not running! Please start it first:\n1. Open terminal\n2. cd Study-Plan\n3. python -m uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload')
      } else {
        toast.error('Failed to save form data. You can still proceed to chat, but your data may not be persisted.')
      }
      
      // Still allow proceeding to chat even if save fails
      dispatch({ type: 'UPDATE_FORM_DATA', payload: formData })
      dispatch({ type: 'SET_SYLLABUS', payload: cleanSyllabus })
      dispatch({ type: 'SET_FORM_VALIDITY', payload: true })
      onComplete()
    }
  }

  return (
    <div className="max-w-4xl mx-auto">
      <div className="bg-white rounded-lg shadow-lg p-6">
        <div className="flex items-center mb-6">
          <GraduationCap className="h-8 w-8 text-primary-600 mr-3" />
          <h1 className="text-3xl font-bold text-gray-900">Create Study Plan</h1>
        </div>

        <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
          {/* Basic Information */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                User ID
              </label>
              <input
                {...register('user_id', { required: 'User ID is required' })}
                className={`form-input ${errors.user_id ? 'form-input-error' : ''}`}
                placeholder="Enter your user ID"
              />
              {errors.user_id && <p className="error-text">{errors.user_id.message}</p>}
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Target Exam
              </label>
              <select
                {...register('target_exam', { required: 'Target exam is required' })}
                className={`form-input ${errors.target_exam ? 'form-input-error' : ''}`}
              >
                <option value="JEE Mains">JEE Mains</option>
                <option value="JEE Advanced">JEE Advanced</option>
                <option value="NEET">NEET</option>
              </select>
              {errors.target_exam && <p className="error-text">{errors.target_exam.message}</p>}
            </div>
          </div>

          {/* Study Plan Configuration */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                <Target className="inline h-4 w-4 mr-1" />
                Study Plan Type
              </label>
              <select
                {...register('study_plan_type', { required: 'Study plan type is required' })}
                className={`form-input ${errors.study_plan_type ? 'form-input-error' : ''}`}
              >
                <option value="Custom">Custom</option>
                <option value="Generic">Generic</option>
              </select>
              {errors.study_plan_type && <p className="error-text">{errors.study_plan_type.message}</p>}
              {studyPlanType === 'Generic' && (
                <p className="text-blue-600 text-sm mt-1">
                  Generic plans require a target score for optimization
                </p>
              )}
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                <BookOpen className="inline h-4 w-4 mr-1" />
                Preparation Type
              </label>
              <select
                {...register('preparation_type', { required: 'Preparation type is required' })}
                className={`form-input ${errors.preparation_type ? 'form-input-error' : ''}`}
              >
                <option value="Syllabus Coverage">Syllabus Coverage</option>
                <option value="Revision">Revision</option>
              </select>
              {errors.preparation_type && <p className="error-text">{errors.preparation_type.message}</p>}
              {preparationType === 'Syllabus Coverage' && (
                <p className="warning-text">
                  Minimum 3 months required for Syllabus Coverage
                </p>
              )}
            </div>
          </div>

          {/* Target Score (conditional) */}
          {studyPlanType === 'Generic' && (
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                <Target className="inline h-4 w-4 mr-1" />
                Target Score (out of 300)
              </label>
              <input
                type="number"
                min="1"
                max="300"
                {...register('target_score', {
                  required: studyPlanType === 'Generic' ? 'Target score is required for Generic plans' : false,
                  min: { value: 1, message: 'Target score must be at least 1' },
                  max: { value: 300, message: 'Target score cannot exceed 300' }
                })}
                className={`form-input ${errors.target_score || customValidationErrors.target_score ? 'form-input-error' : ''}`}
                placeholder="e.g., 252"
              />
              {(errors.target_score || customValidationErrors.target_score) && (
                <p className="error-text">
                  {errors.target_score?.message || customValidationErrors.target_score}
                </p>
              )}
            </div>
          )}

          {/* Time Configuration */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                <Clock className="inline h-4 w-4 mr-1" />
                Number of Months
              </label>
              <input
                type="number"
                min={preparationType === 'Syllabus Coverage' ? 3 : 1}
                {...register('number_of_months', {
                  required: 'Number of months is required',
                  min: {
                    value: preparationType === 'Syllabus Coverage' ? 3 : 1,
                    message: preparationType === 'Syllabus Coverage' 
                      ? 'Minimum 3 months required for Syllabus Coverage'
                      : 'At least 1 month is required'
                  }
                })}
                className={`form-input ${errors.number_of_months || customValidationErrors.number_of_months ? 'form-input-error' : ''}`}
                placeholder="e.g., 6"
              />
              {(errors.number_of_months || customValidationErrors.number_of_months) && (
                <p className="error-text">
                  {errors.number_of_months?.message || customValidationErrors.number_of_months}
                </p>
              )}
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Hours per Day
              </label>
              <input
                type="number"
                min="1"
                max="24"
                {...register('hours_per_day', {
                  required: 'Hours per day is required',
                  min: { value: 1, message: 'At least 1 hour per day is required' },
                  max: { value: 24, message: 'Cannot exceed 24 hours per day' }
                })}
                className={`form-input ${errors.hours_per_day ? 'form-input-error' : ''}`}
                placeholder="e.g., 6"
              />
              {errors.hours_per_day && <p className="error-text">{errors.hours_per_day.message}</p>}
            </div>
          </div>

          {/* Syllabus Section */}
          <div>
            <div className="flex justify-between items-center mb-4">
              <h3 className="text-lg font-medium text-gray-900">Syllabus Configuration</h3>
              <button
                type="button"
                onClick={loadDefaultSyllabus}
                className="btn-secondary text-sm"
              >
                Load Syllabus from Database
              </button>
            </div>

            <div className="space-y-6">
              {Object.keys(syllabus).map(subject => (
                <div key={subject} className="border border-gray-200 rounded-lg p-4">
                  <div className="flex justify-between items-center mb-3">
                    <h4 className="text-md font-medium text-gray-800 capitalize">
                      {subject}
                    </h4>
                    <button
                      type="button"
                      onClick={() => addChapter(subject)}
                      className="flex items-center text-primary-600 hover:text-primary-700 text-sm"
                    >
                      <Plus className="h-4 w-4 mr-1" />
                      Add Chapter
                    </button>
                  </div>

                  <div className="space-y-2">
                    {syllabus[subject].map((chapter, index) => (
                      <div key={index} className="flex items-center space-x-2">
                        <input
                          type="text"
                          value={chapter}
                          onChange={(e) => updateChapter(subject, index, e.target.value)}
                          className="form-input flex-1"
                          placeholder="Chapter name"
                        />
                        <button
                          type="button"
                          onClick={() => removeChapter(subject, index)}
                          className="btn-danger p-2"
                        >
                          <X className="h-4 w-4" />
                        </button>
                      </div>
                    ))}
                  </div>

                  {syllabus[subject].filter(ch => ch.trim() !== '').length === 0 && (
                    <p className="error-text">At least one chapter is required for {subject}</p>
                  )}
                </div>
              ))}
            </div>
          </div>

          {/* Submit Button */}
          <div className="flex justify-end">
            <button
              type="submit"
              className="btn-primary px-8 py-3 text-lg"
            >
              Proceed to Chat
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}