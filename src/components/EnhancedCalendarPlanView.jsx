import React, { useState, useEffect } from 'react'
import { 
  Calendar, 
  Target, 
  TrendingUp, 
  BookOpen, 
  Clock, 
  CheckCircle,
  AlertCircle,
  BarChart3,
  Users,
  Award,
  PlayCircle,
  PauseCircle
} from 'lucide-react'

export default function EnhancedCalendarPlanView({ studyPlan }) {
  const [selectedMonth, setSelectedMonth] = useState(null)
  const [currentDate, setCurrentDate] = useState(new Date().toISOString().split('T')[0])

  // Extract calendar plan data
  const calendarPlan = studyPlan?.calendar_plan || {}
  const monthlyTargets = studyPlan?.monthly_targets_data?.monthly_targets || {}
  const overallSummary = studyPlan?.overall_summary || {}

  // Calculate months from exam date
  const calculateMonthsFromExamDate = () => {
    const examDate = studyPlan?.exam_date || studyPlan?.new_score_oriented_data?.exam_date
    const startDate = studyPlan?.start_date || new Date().toISOString().split('T')[0]
    
    if (examDate && startDate) {
      const start = new Date(startDate)
      const exam = new Date(examDate)
      const diffTime = Math.abs(exam - start)
      const diffMonths = Math.ceil(diffTime / (1000 * 60 * 60 * 24 * 30.44)) // Average days per month
      return diffMonths
    }
    
    return studyPlan?.total_months || 0
  }

  const totalMonths = calculateMonthsFromExamDate()
  const examDate = studyPlan?.exam_date || studyPlan?.new_score_oriented_data?.exam_date

  useEffect(() => {
    // Set first month as selected by default
    const firstMonth = Object.keys(calendarPlan)[0]
    if (firstMonth && !selectedMonth) {
      setSelectedMonth(firstMonth)
    }
  }, [calendarPlan, selectedMonth])

  if (!studyPlan?.calendar_plan) {
    return (
      <div className="text-center py-8">
        <p className="text-gray-500">No enhanced calendar plan data available</p>
      </div>
    )
  }

  const selectedMonthData = selectedMonth ? calendarPlan[selectedMonth] : null
  const selectedMonthTargets = selectedMonth ? monthlyTargets[selectedMonth] : null

  return (
    <div className="space-y-6">
      {/* Header with Overall Summary */}
      <div className="bg-gradient-to-r from-blue-600 to-purple-700 text-white rounded-lg p-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold flex items-center">
              <Calendar className="mr-2" />
              Enhanced Calendar Study Plan
            </h1>
            <p className="mt-2 opacity-90">
              {studyPlan.start_date} to {examDate ? new Date(examDate).toLocaleDateString() : studyPlan.end_date} | Target: {studyPlan.user_target_score}/300
            </p>
          </div>
          <div className="text-right">
            <div className="text-3xl font-bold">{examDate ? new Date(examDate).toLocaleDateString('en-US', { month: 'short', day: 'numeric' }) : totalMonths}</div>
            <div className="text-sm opacity-90">{examDate ? 'Exam Date' : 'Months'}</div>
            {examDate && (
              <div className="text-xs opacity-75 mt-1">
                {totalMonths} months prep
              </div>
            )}
          </div>
        </div>
        
        {/* Quick Stats */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-4">
          <div className="bg-white/10 rounded-lg p-3 text-center">
            <div className="text-lg font-bold">{overallSummary.total_study_days || 0}</div>
            <div className="text-xs opacity-80">Study Days</div>
          </div>
          <div className="bg-white/10 rounded-lg p-3 text-center">
            <div className="text-lg font-bold">{overallSummary.total_practice_days || 0}</div>
            <div className="text-xs opacity-80">PYQ Days</div>
          </div>
          <div className="bg-white/10 rounded-lg p-3 text-center">
            <div className="text-lg font-bold">{overallSummary.weekend_pyq_sessions || 0}</div>
            <div className="text-xs opacity-80">Weekend Sessions</div>
          </div>
          <div className="bg-white/10 rounded-lg p-3 text-center">
            <div className="text-lg font-bold">{overallSummary.daily_dpp_sessions || 0}</div>
            <div className="text-xs opacity-80">DPP Sessions</div>
          </div>
        </div>
      </div>

      {/* Month Selection Tabs */}
      <div className="bg-white rounded-lg shadow-lg p-4">
        <h2 className="text-lg font-semibold mb-4">Select Month</h2>
        <div className="flex flex-wrap gap-2">
          {Object.entries(calendarPlan).map(([monthKey, monthData]) => (
            <button
              key={monthKey}
              onClick={() => setSelectedMonth(monthKey)}
              className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                selectedMonth === monthKey
                  ? 'bg-blue-600 text-white'
                  : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
              }`}
            >
              Month {monthData.month_number}
              <div className="text-xs opacity-75">{monthData.month_name}</div>
            </button>
          ))}
        </div>
      </div>

      {/* Selected Month Details */}
      {selectedMonthData && (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          {/* Monthly Analysis */}
          <div className="bg-white rounded-lg shadow-lg p-6">
            <h3 className="text-xl font-semibold mb-4 flex items-center">
              <BarChart3 className="mr-2 text-green-600" />
              Monthly Analysis - {selectedMonthData.month_name}
            </h3>
            
            {selectedMonthData.monthly_analysis && (
              <div className="space-y-4">
                <div className="grid grid-cols-2 gap-4">
                  <div className="bg-green-50 rounded-lg p-4">
                    <div className="text-2xl font-bold text-green-700">
                      {selectedMonthData.monthly_analysis.total_achievable_score?.toFixed(1) || '0.0'}
                    </div>
                    <div className="text-sm text-green-600">Total Achievable Score</div>
                  </div>
                  <div className="bg-blue-50 rounded-lg p-4">
                    <div className="text-2xl font-bold text-blue-700">
                      {selectedMonthData.monthly_analysis.user_target_score?.toFixed(1) || '0.0'}
                    </div>
                    <div className="text-sm text-blue-600">Your Target Score</div>
                  </div>
                </div>
                
                <div className="bg-purple-50 rounded-lg p-4">
                  <div className="flex justify-between items-center">
                    <span className="text-sm text-purple-600">Efficiency Required</span>
                    <span className="text-lg font-bold text-purple-700">
                      {selectedMonthData.monthly_analysis.efficiency_required || 0}%
                    </span>
                  </div>
                  <div className="w-full bg-purple-200 rounded-full h-2 mt-2">
                    <div 
                      className="bg-purple-600 h-2 rounded-full transition-all duration-300"
                      style={{ width: `${Math.min(selectedMonthData.monthly_analysis.efficiency_required || 0, 100)}%` }}
                    ></div>
                  </div>
                </div>

                {/* Subject Breakdown */}
                {selectedMonthData.monthly_analysis.subject_breakdown && (
                  <div className="space-y-2">
                    <h4 className="font-medium text-gray-700">Subject Breakdown</h4>
                    {Object.entries(selectedMonthData.monthly_analysis.subject_breakdown).map(([subject, data]) => (
                      <div key={subject} className="flex justify-between items-center p-2 bg-gray-50 rounded">
                        <span className="font-medium">{subject}</span>
                        <div className="text-right">
                          <div className="text-sm font-bold">{data.subject_weightage?.toFixed(1) || '0.0'} marks</div>
                          <div className="text-xs text-gray-500">{data.chapter_count || 0} chapters</div>
                        </div>
                      </div>
                    ))}
                  </div>
                )}
              </div>
            )}
          </div>

          {/* Month Focus & Tags */}
          <div className="bg-white rounded-lg shadow-lg p-6">
            <h3 className="text-xl font-semibold mb-4 flex items-center">
              <Target className="mr-2 text-orange-600" />
              Month Focus & Schedule
            </h3>
            
            <div className="space-y-4">
              {/* Primary Focus */}
              <div className="bg-orange-50 rounded-lg p-4">
                <h4 className="font-medium text-orange-700 mb-2">Primary Focus</h4>
                <p className="text-orange-600">{selectedMonthData.primary_focus}</p>
              </div>

              {/* Tags */}
              <div>
                <h4 className="font-medium text-gray-700 mb-2">Tags</h4>
                <div className="flex flex-wrap gap-2">
                  {selectedMonthData.tags?.map((tag, index) => (
                    <span 
                      key={index}
                      className={`px-3 py-1 rounded-full text-xs font-medium ${
                        tag === 'PYQ' ? 'bg-red-100 text-red-700' :
                        tag === 'DPP' ? 'bg-blue-100 text-blue-700' :
                        tag === 'SYLLABUS' ? 'bg-green-100 text-green-700' :
                        'bg-gray-100 text-gray-700'
                      }`}
                    >
                      {tag}
                    </span>
                  ))}
                </div>
              </div>

              {/* Study Days Breakdown */}
              <div className="grid grid-cols-2 gap-4">
                <div className="text-center p-3 bg-blue-50 rounded-lg">
                  <div className="text-lg font-bold text-blue-700">
                    {selectedMonthData.study_days?.study_days || 0}
                  </div>
                  <div className="text-xs text-blue-600">Study Days</div>
                </div>
                <div className="text-center p-3 bg-red-50 rounded-lg">
                  <div className="text-lg font-bold text-red-700">
                    {selectedMonthData.study_days?.practice_days || 0}
                  </div>
                  <div className="text-xs text-red-600">Practice Days</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Weekly Pattern */}
      {selectedMonthData?.weekly_pattern && (
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h3 className="text-xl font-semibold mb-4 flex items-center">
            <Calendar className="mr-2 text-indigo-600" />
            Weekly Pattern - {selectedMonthData.month_name}
          </h3>
          
          <div className="grid grid-cols-1 md:grid-cols-7 gap-3">
            {Object.entries(selectedMonthData.weekly_pattern).map(([day, dayData]) => (
              <div 
                key={day}
                className={`p-4 rounded-lg border-2 ${
                  dayData.type === 'practice' 
                    ? 'border-red-200 bg-red-50' 
                    : dayData.type === 'study'
                    ? 'border-blue-200 bg-blue-50'
                    : 'border-green-200 bg-green-50'
                }`}
              >
                <div className="font-medium capitalize text-gray-800">{day}</div>
                <div className={`text-xs mt-1 ${
                  dayData.type === 'practice' ? 'text-red-600' :
                  dayData.type === 'study' ? 'text-blue-600' : 'text-green-600'
                }`}>
                  {dayData.type === 'practice' ? '🎯 PYQ' : 
                   dayData.type === 'study' ? '📚 Study + DPP' : '🔄 Revision'}
                </div>
                <div className="text-xs text-gray-600 mt-1">
                  {dayData.subject && <div>{dayData.subject}</div>}
                  <div className="truncate">{dayData.activity}</div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Daily Schedule Sample */}
      {selectedMonthData?.daily_schedule && (
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h3 className="text-xl font-semibold mb-4 flex items-center">
            <Clock className="mr-2 text-purple-600" />
            Sample Daily Schedule
          </h3>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {Object.entries(selectedMonthData.daily_schedule)
              .slice(0, 6) // Show first 6 days as sample
              .map(([dateKey, dayData]) => (
              <div key={dateKey} className="border rounded-lg p-4">
                <div className="flex justify-between items-center mb-2">
                  <div className="font-medium">{dayData.day_name}</div>
                  <span className={`px-2 py-1 rounded text-xs font-medium ${
                    dayData.tag === 'PYQ' ? 'bg-red-100 text-red-700' : 'bg-blue-100 text-blue-700'
                  }`}>
                    {dayData.tag}
                  </span>
                </div>
                
                <div className="text-sm text-gray-600 mb-2">
                  {dayData.primary_activity}
                </div>
                
                <div className="text-xs space-y-1">
                  {dayData.schedule && Object.entries(dayData.schedule).map(([time, activity]) => (
                    <div key={time} className="flex justify-between">
                      <span className="capitalize font-medium">{time}:</span>
                      <span className="text-gray-600 truncate ml-2">{activity}</span>
                    </div>
                  ))}
                </div>
                
                {dayData.dpp_details && (
                  <div className="mt-2 p-2 bg-blue-50 rounded text-xs">
                    <div className="font-medium text-blue-700">DPP: {dayData.dpp_details.subject}</div>
                    <div className="text-blue-600">{dayData.dpp_details.target_questions} questions</div>
                  </div>
                )}
              </div>
            ))}
          </div>
          
          <div className="mt-4 text-center">
            <p className="text-sm text-gray-500">
              Showing sample days. Full schedule available for all {selectedMonthData.total_days} days.
            </p>
          </div>
        </div>
      )}

      {/* Overall Strategy */}
      <div className="bg-white rounded-lg shadow-lg p-6">
        <h3 className="text-xl font-semibold mb-4 flex items-center">
          <BookOpen className="mr-2 text-green-600" />
          Overall Strategy
        </h3>
        
        <div className="prose max-w-none">
          <p className="text-gray-700 leading-relaxed">
            {overallSummary.overall_strategy || studyPlan.overall_strategy}
          </p>
        </div>
        
        {/* Key Features */}
        <div className="mt-6 grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="space-y-3">
            <h4 className="font-medium text-gray-800">✅ Key Features</h4>
            <ul className="space-y-2 text-sm text-gray-600">
              <li className="flex items-center">
                <CheckCircle className="w-4 h-4 text-green-500 mr-2" />
                Calendar-based planning from {studyPlan.start_date}
              </li>
              <li className="flex items-center">
                <CheckCircle className="w-4 h-4 text-green-500 mr-2" />
                Monthly analysis with achievable scores
              </li>
              <li className="flex items-center">
                <CheckCircle className="w-4 h-4 text-green-500 mr-2" />
                Weekend PYQ focus (Saturday & Sunday)
              </li>
              <li className="flex items-center">
                <CheckCircle className="w-4 h-4 text-green-500 mr-2" />
                Daily DPP for each subject
              </li>
            </ul>
          </div>
          
          <div className="space-y-3">
            <h4 className="font-medium text-gray-800">📊 Plan Statistics</h4>
            <div className="grid grid-cols-2 gap-3 text-sm">
              <div className="bg-gray-50 p-3 rounded">
                <div className="font-bold text-gray-800">{overallSummary.syllabus_completion_months || 6}</div>
                <div className="text-gray-600">Syllabus Months</div>
              </div>
              <div className="bg-gray-50 p-3 rounded">
                <div className="font-bold text-gray-800">{overallSummary.intensive_practice_months || 0}</div>
                <div className="text-gray-600">Practice Months</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}