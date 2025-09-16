import React, { useState } from 'react'
import { Target, Calendar, TrendingUp, BookOpen, Clock, BarChart3, Users } from 'lucide-react'
import EnhancedCalendarPlanView from './EnhancedCalendarPlanView'

export default function ScoreOrientedPlanView({ studyPlan }) {
  const [viewMode, setViewMode] = useState('standard') // 'standard' or 'enhanced'

  if (!studyPlan?.score_oriented_data && !studyPlan?.calendar_plan) {
    return (
      <div className="text-center py-8">
        <p className="text-gray-500">No score-oriented plan data available</p>
      </div>
    )
  }

  // Check if we have enhanced calendar data
  const hasEnhancedData = studyPlan?.calendar_plan || studyPlan?.monthly_targets_data
  const scoreData = studyPlan.score_oriented_data

  // If we have enhanced calendar data, show the enhanced view
  if (hasEnhancedData && viewMode === 'enhanced') {
    return <EnhancedCalendarPlanView studyPlan={studyPlan} />
  }

  return (
    <div className="space-y-6">
      {/* View Mode Toggle */}
      {hasEnhancedData && (
        <div className="bg-white rounded-lg shadow-lg p-4">
          <div className="flex items-center justify-between">
            <h3 className="text-lg font-semibold">Plan View Mode</h3>
            <div className="flex bg-gray-100 rounded-lg p-1">
              <button
                onClick={() => setViewMode('standard')}
                className={`px-4 py-2 rounded-md text-sm font-medium transition-colors ${
                  viewMode === 'standard'
                    ? 'bg-white text-blue-600 shadow-sm'
                    : 'text-gray-600 hover:text-gray-800'
                }`}
              >
                Standard View
              </button>
              <button
                onClick={() => setViewMode('enhanced')}
                className={`px-4 py-2 rounded-md text-sm font-medium transition-colors ${
                  viewMode === 'enhanced'
                    ? 'bg-white text-blue-600 shadow-sm'
                    : 'text-gray-600 hover:text-gray-800'
                }`}
              >
                📅 Enhanced Calendar View
              </button>
            </div>
          </div>
          <p className="text-sm text-gray-600 mt-2">
            Switch between standard score view and enhanced calendar view with daily scheduling
          </p>
        </div>
      )}

      {/* Header */}
      <div className="bg-gradient-to-r from-green-500 to-blue-600 text-white rounded-lg p-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold flex items-center">
              <Target className="mr-2" />
              Score-Oriented Study Plan
            </h1>
            <p className="mt-2 opacity-90">
              Target: {scoreData?.target_score || studyPlan?.user_target_score}/300 marks | {scoreData?.total_months || studyPlan?.total_months} months
            </p>
          </div>
          <div className="text-right">
            <div className="text-3xl font-bold">{scoreData ? (scoreData.score_ratio * 100).toFixed(1) : '0.0'}%</div>
            <div className="text-sm opacity-90">Success Ratio</div>
          </div>
        </div>
      </div>

      {/* Enhanced Monthly Analysis */}
      {studyPlan?.monthly_targets_data && (
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h2 className="text-xl font-semibold mb-4 flex items-center">
            <BarChart3 className="mr-2 text-purple-600" />
            Enhanced Monthly Analysis
          </h2>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-6">
            {Object.entries(studyPlan.monthly_targets_data.monthly_targets || {}).map(([monthKey, monthData]) => (
              <div key={monthKey} className="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow">
                <div className="flex items-center justify-between mb-3">
                  <h3 className="font-semibold text-gray-800">Month {monthKey.split('_')[1]}</h3>
                  <span className="text-xs bg-blue-100 text-blue-800 px-2 py-1 rounded">
                    {monthData.target_ratio}% of target
                  </span>
                </div>
                
                <div className="space-y-3">
                  <div className="bg-green-50 rounded-lg p-3">
                    <div className="text-lg font-bold text-green-700">
                      {monthData.total_achievable_score?.toFixed(1) || '0.0'}
                    </div>
                    <div className="text-xs text-green-600">Total Achievable Score</div>
                  </div>
                  
                  <div className="bg-blue-50 rounded-lg p-3">
                    <div className="text-lg font-bold text-blue-700">
                      {monthData.user_target_score?.toFixed(1) || '0.0'}
                    </div>
                    <div className="text-xs text-blue-600">Your Target Score</div>
                  </div>
                  
                  <div className="bg-purple-50 rounded-lg p-3">
                    <div className="flex justify-between items-center">
                      <span className="text-xs text-purple-600">Efficiency Required</span>
                      <span className="text-sm font-bold text-purple-700">
                        {monthData.efficiency_required || 0}%
                      </span>
                    </div>
                    <div className="w-full bg-purple-200 rounded-full h-1.5 mt-1">
                      <div 
                        className="bg-purple-600 h-1.5 rounded-full transition-all duration-300"
                        style={{ width: `${Math.min(monthData.efficiency_required || 0, 100)}%` }}
                      ></div>
                    </div>
                  </div>

                  {/* Subject Breakdown */}
                  {monthData.subject_breakdown && (
                    <div className="space-y-1">
                      <div className="text-xs font-medium text-gray-600">Subject Breakdown:</div>
                      {Object.entries(monthData.subject_breakdown).map(([subject, subjectData]) => (
                        <div key={subject} className="flex justify-between text-xs">
                          <span>{subject}:</span>
                          <span className="font-medium">{subjectData.subject_weightage?.toFixed(1) || '0.0'}</span>
                        </div>
                      ))}
                    </div>
                  )}
                </div>
              </div>
            ))}
          </div>

          {/* Overall Summary */}
          {studyPlan.monthly_targets_data.overall_summary && (
            <div className="bg-gradient-to-r from-indigo-50 to-purple-50 rounded-lg p-4">
              <h3 className="font-semibold text-indigo-800 mb-3">Overall Target Summary</h3>
              <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                <div className="text-center">
                  <div className="text-xl font-bold text-indigo-700">
                    {studyPlan.monthly_targets_data.total_achievable_score?.toFixed(1) || '0.0'}
                  </div>
                  <div className="text-xs text-indigo-600">Total Achievable</div>
                </div>
                <div className="text-center">
                  <div className="text-xl font-bold text-purple-700">
                    {studyPlan.monthly_targets_data.total_user_target?.toFixed(1) || '0.0'}
                  </div>
                  <div className="text-xs text-purple-600">Total Target</div>
                </div>
                <div className="text-center">
                  <div className="text-xl font-bold text-green-700">
                    {studyPlan.monthly_targets_data.overall_efficiency_required?.toFixed(1) || '0.0'}%
                  </div>
                  <div className="text-xs text-green-600">Overall Efficiency</div>
                </div>
                <div className="text-center">
                  <div className={`text-xl font-bold ${
                    studyPlan.monthly_targets_data.target_achievability?.is_achievable 
                      ? 'text-green-700' : 'text-red-700'
                  }`}>
                    {studyPlan.monthly_targets_data.target_achievability?.is_achievable ? '✅' : '⚠️'}
                  </div>
                  <div className="text-xs text-gray-600">Achievable</div>
                </div>
              </div>
            </div>
          )}
        </div>
      )}

      {/* Monthly Score Targets */}
      {scoreData?.monthly_plans && (
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h2 className="text-xl font-semibold mb-4 flex items-center">
            <TrendingUp className="mr-2 text-green-600" />
            Monthly Score Targets
          </h2>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {scoreData.monthly_plans?.map((plan, index) => (
              <div key={index} className="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow">
                <div className="flex items-center justify-between mb-2">
                  <h3 className="font-semibold text-gray-800">Month {plan.month_number}</h3>
                  <span className="text-sm text-gray-500">{plan.month_name}</span>
                </div>
                
                <div className="space-y-2">
                  <div className="flex justify-between">
                    <span className="text-sm text-gray-600">Target:</span>
                    <span className="font-medium text-green-600">
                      {plan.score_target.target_score_for_month?.toFixed(1) || '0.0'} marks
                    </span>
                  </div>
                  
                  <div className="flex justify-between">
                    <span className="text-sm text-gray-600">Cumulative:</span>
                    <span className="font-medium text-blue-600">
                      {plan.score_target.cumulative_target?.toFixed(1) || '0.0'} marks
                    </span>
                  </div>
                  
                  <div className="mt-3">
                    <div className="text-xs text-gray-500 mb-1">
                      Chapters with Coverage:
                      {plan.score_target.practice_focus_percentage && (
                        <span className="ml-2 px-2 py-1 bg-blue-100 text-blue-800 rounded text-xs">
                          Practice: {plan.score_target.practice_focus_percentage}%
                        </span>
                      )}
                      {plan.score_target.syllabus_completion_percentage && (
                        <span className="ml-1 px-2 py-1 bg-green-100 text-green-800 rounded text-xs">
                          Syllabus: {plan.score_target.syllabus_completion_percentage}%
                        </span>
                      )}
                    </div>
                    <div className="text-xs bg-gray-50 rounded p-2 max-h-32 overflow-y-auto space-y-1">
                      {plan.score_target.chapter_coverage_details?.length > 0 ? (
                        plan.score_target.chapter_coverage_details.map((coverage, idx) => (
                          <div key={idx} className="flex items-center justify-between p-1 bg-white rounded border">
                            <div className="flex-1">
                              <span className="font-medium text-gray-700">
                                {coverage.subject} - {coverage.chapter_name}
                              </span>
                              {coverage.is_dependency && (
                                <span className="ml-1 px-1 py-0.5 bg-yellow-100 text-yellow-700 rounded text-xs">
                                  Dep: {coverage.dependency_for}
                                </span>
                              )}
                            </div>
                            <div className="flex items-center space-x-2">
                              <span className="px-2 py-1 bg-blue-100 text-blue-800 rounded text-xs font-medium">
                                {coverage.coverage_percentage}%
                              </span>
                              <span className="px-2 py-1 bg-green-100 text-green-800 rounded text-xs font-medium">
                                {coverage.estimated_marks} marks
                              </span>
                            </div>
                          </div>
                        ))
                      ) : (
                        // Fallback to legacy format
                        plan.score_target.chapters_to_cover?.length > 0 ? (
                          plan.score_target.chapters_to_cover.map((chapter, idx) => (
                            <div key={idx} className="truncate">{chapter}</div>
                          ))
                        ) : (
                          <div className="text-gray-400">No chapters assigned</div>
                        )
                      )}
                    </div>
                  </div>
                </div>
              </div>
          ))}
        </div>
      )}

      {/* Weekly Schedule */}
      {scoreData?.practice_configuration && (
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h2 className="text-xl font-semibold mb-4 flex items-center">
            <Calendar className="mr-2 text-blue-600" />
            Weekly Schedule Template
          </h2>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Study Days */}
            <div className="bg-blue-50 rounded-lg p-4">
              <h3 className="font-semibold text-blue-800 mb-3">📚 Study Days</h3>
              <div className="space-y-2">
                {scoreData.practice_configuration?.study_days?.map((day, index) => (
                  <div key={index} className="flex items-center justify-between py-2 px-3 bg-white rounded border">
                    <span className="font-medium">{day}</span>
                    <span className="text-sm text-blue-600">Chapter Study</span>
                  </div>
                ))}
              </div>
            </div>

            {/* Practice Days */}
            <div className="bg-green-50 rounded-lg p-4">
              <h3 className="font-semibold text-green-800 mb-3">🎯 Practice Days</h3>
              <div className="space-y-2">
                {scoreData.practice_configuration?.practice_days?.map((day, index) => (
                  <div key={index} className="flex items-center justify-between py-2 px-3 bg-white rounded border">
                    <span className="font-medium">{day}</span>
                    <span className="text-sm text-green-600">
                      {day === 'Saturday' ? 'PYQ Practice' : 'DPP Practice'}
                    </span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Score Tracking */}
      {scoreData?.score_tracking && (
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h2 className="text-xl font-semibold mb-4 flex items-center">
            <Clock className="mr-2 text-purple-600" />
            Score Progression Tracking
          </h2>
          
          <div className="space-y-3">
            {Object.entries(scoreData.score_tracking || {}).map(([month, score], index) => {
              const percentage = (score / scoreData.target_score) * 100
              return (
                <div key={index} className="flex items-center space-x-4">
                  <div className="w-20 text-sm font-medium text-gray-600">{month}</div>
                  <div className="flex-1 bg-gray-200 rounded-full h-4 relative">
                    <div 
                      className="bg-gradient-to-r from-green-400 to-green-600 h-4 rounded-full transition-all duration-300"
                      style={{ width: `${Math.min(percentage, 100)}%` }}
                    ></div>
                    <div className="absolute inset-0 flex items-center justify-center text-xs font-medium text-white">
                      {score?.toFixed(1) || '0.0'} / {scoreData.target_score}
                    </div>
                  </div>
                  <div className="w-16 text-sm text-gray-600">{percentage?.toFixed(1) || '0.0'}%</div>
                </div>
              )
            })}
          </div>
        </div>
      )}

      {/* Strategy Summary */}
      {scoreData?.overall_strategy && (
        <div className="bg-white rounded-lg shadow-lg p-6">
          <h2 className="text-xl font-semibold mb-4 flex items-center">
            <BookOpen className="mr-2 text-indigo-600" />
            Strategy Overview
          </h2>
          
          <div className="prose max-w-none">
            <div className="whitespace-pre-line text-gray-700 leading-relaxed">
              {scoreData.overall_strategy}
            </div>
          </div>
        </div>
      )}

      {/* Key Metrics */}
      {scoreData && (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="bg-gradient-to-br from-blue-500 to-blue-600 text-white rounded-lg p-4">
            <div className="text-2xl font-bold">{scoreData.monthly_score_requirement?.toFixed(1) || '0.0'}</div>
            <div className="text-sm opacity-90">Marks per Month</div>
          </div>
          
          <div className="bg-gradient-to-br from-green-500 to-green-600 text-white rounded-lg p-4">
            <div className="text-2xl font-bold">{scoreData.total_months || 0}</div>
            <div className="text-sm opacity-90">Total Months</div>
          </div>
          
          <div className="bg-gradient-to-br from-purple-500 to-purple-600 text-white rounded-lg p-4">
            <div className="text-2xl font-bold">5/7</div>
            <div className="text-sm opacity-90">Study Days per Week</div>
          </div>
        </div>
      )}
    </div>
  )
}