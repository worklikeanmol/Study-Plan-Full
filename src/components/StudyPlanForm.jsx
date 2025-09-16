import React, { useState, useEffect } from 'react'
import { useForm } from 'react-hook-form'
import { toast } from 'react-hot-toast'
import { GraduationCap, Target, Clock, BookOpen, Plus, X } from 'lucide-react'
import { useStudyPlan } from '../context/StudyPlanContext'
import { saveFormData, getChaptersByExam, validateExamDate } from '../services/api'

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
  const examDate = watch('exam_date')

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
    if (studyPlanType === 'ScoreGeneric') {
      // Target score and exam date are required for ScoreGeneric plans
      // No preparation type needed for ScoreGeneric
      setValue('preparation_type', '')
      setCustomValidationErrors(prev => ({
        ...prev,
        target_score: null, // Clear any previous errors - let form validation handle it
        exam_date: null // Clear any previous errors - let form validation handle it
      }))
    } else if (studyPlanType === 'Score-Oriented') {
      // Target score and exam date are required for Score-Oriented plans
      // Force preparation type to revision
      setValue('preparation_type', 'revision')
      setCustomValidationErrors(prev => ({
        ...prev,
        target_score: null, // Clear any previous errors - let form validation handle it
        exam_date: null // Clear any previous errors - let form validation handle it
      }))
    } else if (studyPlanType === 'new_score_oriented') {
      // Target score and exam date are required for New Score-Oriented plans
      // Force preparation type to revision & syllabus coverage
      setValue('preparation_type', 'revision & syllabus coverage')
      setCustomValidationErrors(prev => ({
        ...prev,
        target_score: null, // Clear any previous errors - let form validation handle it
        exam_date: null // Clear any previous errors - let form validation handle it
      }))
    } else if (studyPlanType === 'Generic') {
      // Target score is required for Generic plans
      setValue('exam_date', null)
      setCustomValidationErrors(prev => ({
        ...prev,
        target_score: targetScore ? null : 'Target score is required for Generic plans',
        exam_date: null
      }))
    } else {
      // Clear target score and exam date for Custom plans
      setValue('target_score', null)
      setValue('exam_date', null)
      setCustomValidationErrors(prev => ({
        ...prev,
        target_score: null,
        exam_date: null
      }))
    }
  }, [studyPlanType, targetScore, examDate, setValue])

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
    } else if ((studyPlanType === 'ScoreGeneric' || studyPlanType === 'Generic' || studyPlanType === 'Score-Oriented') && !targetScore) {
      setCustomValidationErrors(prev => ({
        ...prev,
        target_score: `Target score is required for ${studyPlanType} plans`
      }))
    } else {
      setCustomValidationErrors(prev => ({
        ...prev,
        target_score: null
      }))
    }
  }, [targetScore, studyPlanType])

  // Validate exam date for ScoreGeneric, Score-Oriented and New Score-Oriented plans
  useEffect(() => {
    const validateDate = async () => {
      if ((studyPlanType === 'ScoreGeneric' || studyPlanType === 'Score-Oriented' || studyPlanType === 'new_score_oriented') && examDate) {
        try {
          // First do client-side validation
          const examDateTime = new Date(examDate)
          const today = new Date()
          const timeDiff = examDateTime - today
          const monthsAvailable = timeDiff / (1000 * 60 * 60 * 24 * 30.44)
          
          const minMonths = studyPlanType === 'ScoreGeneric' ? 6 : 3
          const planTypeName = studyPlanType === 'ScoreGeneric' ? 'ScoreGeneric' : 'Custom'
          
          if (monthsAvailable < minMonths) {
            setCustomValidationErrors(prev => ({
              ...prev,
              exam_date: `Exam date is only ${monthsAvailable.toFixed(1)} months away. Minimum ${minMonths} months required for ${planTypeName} plans.`
            }))
            return
          }
          
          // If client-side validation passes, call API
          const validation = await validateExamDate(examDate)
          if (!validation.is_valid) {
            setCustomValidationErrors(prev => ({
              ...prev,
              exam_date: validation.message
            }))
          } else {
            setCustomValidationErrors(prev => ({
              ...prev,
              exam_date: null
            }))
            // Update number of months based on exam date
            setValue('number_of_months', validation.calculated_months)
            toast.success(`Exam date validated! ${validation.months_available} months available for preparation.`)
          }
        } catch (error) {
          console.error('Exam date validation error:', error)
          // Fallback to client-side validation if API fails
          try {
            const examDateTime = new Date(examDate)
            const today = new Date()
            const timeDiff = examDateTime - today
            const monthsAvailable = timeDiff / (1000 * 60 * 60 * 24 * 30.44)
            
            const minMonths = studyPlanType === 'ScoreGeneric' ? 6 : 3
            const planTypeName = studyPlanType === 'ScoreGeneric' ? 'ScoreGeneric' : 'Custom'
            
            if (monthsAvailable < minMonths) {
              setCustomValidationErrors(prev => ({
                ...prev,
                exam_date: `Exam date is only ${monthsAvailable.toFixed(1)} months away. Minimum ${minMonths} months required for ${planTypeName} plans.`
              }))
            } else {
              setCustomValidationErrors(prev => ({
                ...prev,
                exam_date: null
              }))
              const calculatedMonths = Math.min(Math.floor(monthsAvailable), 12)
              setValue('number_of_months', calculatedMonths)
              toast.success(`Exam date validated! ${monthsAvailable.toFixed(1)} months available for preparation.`)
            }
          } catch (dateError) {
            setCustomValidationErrors(prev => ({
              ...prev,
              exam_date: 'Invalid date format. Please use YYYY-MM-DD format.'
            }))
          }
        }
      } else if (studyPlanType === 'ScoreGeneric' && !examDate) {
        const planTypeName = 'ScoreGeneric'
        setCustomValidationErrors(prev => ({
          ...prev,
          exam_date: `Exam date is required for ${planTypeName} plans`
        }))
      } else {
        setCustomValidationErrors(prev => ({
          ...prev,
          exam_date: null
        }))
      }
    }

    if (studyPlanType === 'ScoreGeneric' && examDate) {
      const timeoutId = setTimeout(validateDate, 500) // Debounce validation
      return () => clearTimeout(timeoutId)
    } else {
      validateDate()
    }
  }, [examDate, studyPlanType, setValue])

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
    // Skip syllabus validation for Score-Oriented plans
    if (studyPlanType === 'Score-Oriented') {
      return null
    }
    
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

    // Clean syllabus data (remove empty chapters) - Skip for Score-Oriented
    let cleanSyllabus = {}
    if (studyPlanType === 'Score-Oriented') {
      // For Score-Oriented plans, syllabus is auto-selected by the system
      cleanSyllabus = {
        mathematics: ['Auto-Selected'],
        physics: ['Auto-Selected'],
        chemistry: ['Auto-Selected']
      }
    } else {
      Object.keys(syllabus).forEach(subject => {
        cleanSyllabus[subject] = syllabus[subject].filter(chapter => chapter.trim() !== '')
      })
    }

    const formData = {
      ...data,
      syllabus: cleanSyllabus,
      target_score: (studyPlanType === 'Generic' || studyPlanType === 'Score-Oriented' || studyPlanType === 'new_score_oriented') ? parseInt(data.target_score) : null,
      exam_date: (studyPlanType === 'Score-Oriented' || studyPlanType === 'new_score_oriented') ? data.exam_date : null,
      // Set default values for Score-Oriented and New Score-Oriented plans
      number_of_months: (studyPlanType === 'Score-Oriented' || studyPlanType === 'new_score_oriented') ? numberOfMonths : data.number_of_months,
      hours_per_day: (studyPlanType === 'Score-Oriented' || studyPlanType === 'new_score_oriented') ? 8 : data.hours_per_day // Default 8 hours for score-oriented plans
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
                <option value="ScoreGeneric">ScoreGeneric</option>
              </select>
              {errors.study_plan_type && <p className="error-text">{errors.study_plan_type.message}</p>}
              {studyPlanType === 'Custom' && (
                <p className="text-blue-600 text-sm mt-1">
                  📚 Custom plans provide personalized study schedules based on your preferences and available time
                </p>
              )}
              {studyPlanType === 'ScoreGeneric' && (
                <p className="text-indigo-600 text-sm mt-1">
                  🎯 ScoreGeneric plans provide comprehensive score-oriented study plans with priority-based chapter distribution (minimum 6 months required)
                </p>
              )}
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                <BookOpen className="inline h-4 w-4 mr-1" />
                Preparation Type
              </label>
              <select
                {...register('preparation_type', { required: studyPlanType !== 'ScoreGeneric' ? 'Preparation type is required' : false })}
                className={`form-input ${errors.preparation_type ? 'form-input-error' : ''}`}
                disabled={studyPlanType === 'ScoreGeneric' || studyPlanType === 'Score-Oriented' || studyPlanType === 'new_score_oriented'}
              >
                <option value="Syllabus Coverage">Syllabus Coverage</option>
                <option value="revision">Revision</option>
                <option value="revision & syllabus coverage">Revision & Syllabus Coverage</option>
              </select>
              {errors.preparation_type && <p className="error-text">{errors.preparation_type.message}</p>}
              {preparationType === 'Syllabus Coverage' && (
                <p className="warning-text">
                  Minimum 3 months required for Syllabus Coverage
                </p>
              )}
            </div>
          </div>

          {/* Target Score and Exam Date (conditional) */}
          {(studyPlanType === 'ScoreGeneric' || studyPlanType === 'Generic' || studyPlanType === 'Score-Oriented' || studyPlanType === 'new_score_oriented') && (
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
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
                    required: (studyPlanType === 'ScoreGeneric' || studyPlanType === 'Generic' || studyPlanType === 'Score-Oriented' || studyPlanType === 'new_score_oriented') ? `Target score is required for ${studyPlanType === 'new_score_oriented' ? 'New Score-Oriented' : studyPlanType} plans` : false,
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

              {(studyPlanType === 'ScoreGeneric' || studyPlanType === 'Score-Oriented' || studyPlanType === 'new_score_oriented') && (
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    📅 Exam Date
                  </label>
                  <input
                    type="date"
                    {...register('exam_date', {
                      required: (studyPlanType === 'ScoreGeneric' || studyPlanType === 'Score-Oriented' || studyPlanType === 'new_score_oriented') ? `Exam date is required for ${studyPlanType === 'ScoreGeneric' ? 'ScoreGeneric' : (studyPlanType === 'new_score_oriented' ? 'New Score-Oriented' : studyPlanType)} plans` : false
                    })}
                    className={`form-input ${errors.exam_date || customValidationErrors.exam_date ? 'form-input-error' : ''}`}
                    min={new Date().toISOString().split('T')[0]} // Minimum today's date
                  />
                  {(errors.exam_date || customValidationErrors.exam_date) && (
                    <p className="error-text">
                      {errors.exam_date?.message || customValidationErrors.exam_date}
                    </p>
                  )}
                  <p className="text-sm text-gray-500 mt-1">
                    ⚠️ Minimum {studyPlanType === 'ScoreGeneric' || studyPlanType === 'new_score_oriented' ? '6' : '5'} months required from today for {studyPlanType === 'ScoreGeneric' ? 'ScoreGeneric' : (studyPlanType === 'new_score_oriented' ? 'New Score-Oriented' : 'Score-Oriented')} plans
                  </p>
                </div>
              )}
            </div>
          )}

          {/* Time Configuration - Hidden for ScoreGeneric, Score-Oriented and New Score-Oriented */}
          {studyPlanType !== 'ScoreGeneric' && studyPlanType !== 'Score-Oriented' && studyPlanType !== 'new_score_oriented' && (
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
                    required: studyPlanType !== 'Score-Oriented' ? 'Number of months is required' : false,
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
                    required: studyPlanType !== 'Score-Oriented' && studyPlanType !== 'new_score_oriented' ? 'Hours per day is required' : false,
                    min: { value: 1, message: 'At least 1 hour per day is required' },
                    max: { value: 24, message: 'Cannot exceed 24 hours per day' }
                  })}
                  className={`form-input ${errors.hours_per_day ? 'form-input-error' : ''}`}
                  placeholder="e.g., 6"
                />
                {errors.hours_per_day && <p className="error-text">{errors.hours_per_day.message}</p>}
              </div>
            </div>
          )}

          {/* New Score-Oriented Info Display */}
          {studyPlanType === 'new_score_oriented' && (
            <div className="bg-purple-50 border border-purple-200 rounded-lg p-4">
              <h3 className="text-lg font-semibold text-purple-800 mb-2">🆕 New Score-Oriented Configuration</h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm text-purple-700">
                <div>
                  <strong>📚 Complete Coverage:</strong>
                  <ul className="mt-1 ml-4 list-disc">
                    <li>100% syllabus coverage</li>
                    <li>All chapters completed fully</li>
                    <li>Dependency-aware sequencing</li>
                  </ul>
                </div>
                <div>
                  <strong>🎯 Target Strategy:</strong>
                  <ul className="mt-1 ml-4 list-disc">
                    <li>6-month syllabus completion</li>
                    <li>Saturday: PYQ Practice</li>
                    <li>Sunday: DPP Practice</li>
                    <li>Force-fit for target achievement</li>
                  </ul>
                </div>
              </div>
              {examDate && (
                <p className="mt-2 text-sm text-purple-600">
                  ⏱️ Months calculated automatically from exam date: <strong>{numberOfMonths} months</strong>
                  <br />
                  📅 Syllabus completion target: <strong>{Math.min(numberOfMonths, 6)} months</strong>
                  {numberOfMonths > 6 && <span> + {numberOfMonths - 6} months intensive practice</span>}
                </p>
              )}
            </div>
          )}

          {/* Score-Oriented Info Display */}
          {studyPlanType === 'Score-Oriented' && (
            <div className="bg-green-50 border border-green-200 rounded-lg p-4">
              <h3 className="text-lg font-semibold text-green-800 mb-2">🎯 Score-Oriented Configuration</h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm text-green-700">
                <div>
                  <strong>📅 Study Schedule:</strong>
                  <ul className="mt-1 ml-4 list-disc">
                    <li>Monday-Friday: Chapter Study</li>
                    <li>Saturday: PYQ Practice</li>
                    <li>Sunday: DPP Practice</li>
                  </ul>
                </div>
                <div>
                  <strong>🎯 Optimization:</strong>
                  <ul className="mt-1 ml-4 list-disc">
                    <li>High-weightage chapters prioritized</li>
                    <li>Monthly score targets</li>
                    <li>Dependency-aware sequencing</li>
                  </ul>
                </div>
              </div>
              {examDate && (
                <p className="mt-2 text-sm text-green-600">
                  ⏱️ Months calculated automatically from exam date: <strong>{numberOfMonths} months</strong>
                </p>
              )}
            </div>
          )}

          {/* Syllabus Section - Hidden for Score-Oriented and New Score-Oriented */}
          {studyPlanType !== 'Score-Oriented' && studyPlanType !== 'new_score_oriented' && (
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
          )}

          {/* Score-Oriented Syllabus Info */}
          {studyPlanType === 'Score-Oriented' && (
            <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
              <h3 className="text-lg font-semibold text-blue-800 mb-2">📚 Automatic Syllabus Selection</h3>
              <p className="text-blue-700 text-sm">
                For Score-Oriented plans, the system automatically selects the most optimal chapters based on:
              </p>
              <ul className="mt-2 ml-4 list-disc text-sm text-blue-600">
                <li><strong>Chapter Weightage:</strong> High-scoring chapters prioritized</li>
                <li><strong>Dependencies:</strong> Prerequisite chapters included automatically</li>
                <li><strong>Target Score:</strong> Optimal selection to achieve your {targetScore || 'target'} marks</li>
                <li><strong>Time Constraints:</strong> Chapters that fit within your exam timeline</li>
              </ul>
            </div>
          )}

          {/* New Score-Oriented Syllabus Info */}
          {studyPlanType === 'new_score_oriented' && (
            <div className="bg-green-50 border border-green-200 rounded-lg p-4">
              <h3 className="text-lg font-semibold text-green-800 mb-2">🎯 Complete Syllabus Coverage</h3>
              <p className="text-green-700 text-sm">
                For New Score-Oriented plans, the system provides complete syllabus coverage with:
              </p>
              <ul className="mt-2 ml-4 list-disc text-sm text-green-600">
                <li><strong>100% Syllabus Coverage:</strong> All chapters completed in one go</li>
                <li><strong>Dependency Resolution:</strong> Prerequisites completed before dependent chapters</li>
                <li><strong>Priority-Based Sequencing:</strong> High-weightage chapters prioritized</li>
                <li><strong>Revision Focus:</strong> Always revision & syllabus coverage type</li>
                <li><strong>Practice Schedule:</strong> Saturday (PYQ) + Sunday (DPP) practice</li>
                <li><strong>Target Achievement:</strong> Force-fit strategy to achieve your {targetScore || 'target'} marks</li>
                <li><strong>6-Month Completion:</strong> Syllabus completed within 6 months maximum</li>
              </ul>
            </div>
          )}

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