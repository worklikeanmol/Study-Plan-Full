import React from 'react'
import { Calendar, BookOpen, Clock, Target, Lightbulb } from 'lucide-react'
import { useStudyPlan } from '../context/StudyPlanContext'

export default function StudyPlanView() {
  const { state } = useStudyPlan()

  if (!state.studyPlan) {
    return (
      <div className="flex items-center justify-center h-full">
        <div className="text-center">
          <BookOpen className="h-16 w-16 text-gray-400 mx-auto mb-4" />
          <h3 className="text-lg font-medium text-gray-900 mb-2">
            No Study Plan Generated
          </h3>
          <p className="text-gray-600">
            Please complete the form and chat with the assistant to generate your study plan.
          </p>
        </div>
      </div>
    )
  }

  const getCoverageClass = (coverage) => {
    if (coverage >= 0.8) return 'bg-green-100 text-green-800 border-green-200'
    if (coverage >= 0.5) return 'bg-yellow-100 text-yellow-800 border-yellow-200'
    return 'bg-red-100 text-red-800 border-red-200'
  }

  const getCoverageIcon = (coverage) => {
    if (coverage >= 0.8) return '🟢'
    if (coverage >= 0.5) return '🟡'
    return '🔴'
  }

  return (
    <div className="max-w-6xl mx-auto">
      <div className="bg-white rounded-lg shadow-lg">
        {/* Header */}
        <div className="border-b border-gray-200 p-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center">
              <Target className="h-8 w-8 text-primary-600 mr-3" />
              <div>
                <h1 className="text-3xl font-bold text-gray-900">Your Study Plan</h1>
                <p className="text-gray-600 mt-1">
                  {state.formData.target_exam} • {state.formData.study_plan_type} Plan • {state.formData.preparation_type}
                </p>
              </div>
            </div>
            <div className="text-right">
              <div className="text-sm text-gray-600">Duration</div>
              <div className="text-2xl font-bold text-primary-600">
                {state.formData.number_of_months} months
              </div>
              <div className="text-sm text-gray-600">
                {state.formData.hours_per_day} hours/day
              </div>
            </div>
          </div>
        </div>

        {/* Plan Content */}
        <div className="p-6">
          {/* Insights */}
          {state.studyPlan.insights && (
            <div className="mb-8 bg-blue-50 border border-blue-200 rounded-lg p-4">
              <div className="flex items-start">
                <Lightbulb className="h-5 w-5 text-blue-600 mr-2 mt-0.5 flex-shrink-0" />
                <div>
                  <h3 className="font-medium text-blue-900 mb-2">Plan Insights</h3>
                  <p className="text-blue-800 text-sm leading-relaxed">
                    {state.studyPlan.insights}
                  </p>
                </div>
              </div>
            </div>
          )}

          {/* Target Score Display */}
          {state.formData.target_score && (
            <div className="mb-6 bg-green-50 border border-green-200 rounded-lg p-4">
              <div className="flex items-center">
                <Target className="h-5 w-5 text-green-600 mr-2" />
                <span className="font-medium text-green-900">
                  Target Score: {state.formData.target_score}/300
                </span>
              </div>
            </div>
          )}

          {/* Monthly Plan */}
          {state.studyPlan.monthly_plan && Object.keys(state.studyPlan.monthly_plan).length > 0 ? (
            <div className="space-y-8">
              {Object.entries(state.studyPlan.monthly_plan).map(([month, monthPlan]) => (
                <div key={month} className="border border-gray-200 rounded-lg overflow-hidden">
                  <div className="bg-gray-50 px-6 py-4 border-b border-gray-200">
                    <div className="flex items-center">
                      <Calendar className="h-5 w-5 text-gray-600 mr-2" />
                      <h2 className="text-xl font-semibold text-gray-900">{month}</h2>
                    </div>
                  </div>

                  <div className="p-6">
                    <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                      {['mathematics', 'physics', 'chemistry'].map(subject => {
                        const subjectData = monthPlan[subject]
                        if (!subjectData || subjectData.length === 0) return null

                        return (
                          <div key={subject} className="bg-gray-50 rounded-lg p-4">
                            <div className="flex items-center mb-4">
                              <BookOpen className="h-5 w-5 text-primary-600 mr-2" />
                              <h3 className="font-semibold text-gray-900 capitalize">
                                {subject}
                              </h3>
                            </div>

                            <div className="space-y-3">
                              {subjectData.map((chapterCoverage, index) => {
                                const coveragePercent = Math.round(chapterCoverage.coverage * 100)
                                const coverageClass = getCoverageClass(chapterCoverage.coverage)
                                const coverageIcon = getCoverageIcon(chapterCoverage.coverage)

                                return (
                                  <div
                                    key={index}
                                    className={`p-3 rounded-lg border ${coverageClass}`}
                                  >
                                    <div className="flex items-center justify-between">
                                      <div className="flex items-center">
                                        <span className="mr-2">{coverageIcon}</span>
                                        <span className="font-medium text-sm">
                                          {chapterCoverage.chapter}
                                        </span>
                                      </div>
                                      <div className="flex items-center">
                                        <Clock className="h-3 w-3 mr-1" />
                                        <span className="text-xs font-medium">
                                          {coveragePercent}%
                                        </span>
                                      </div>
                                    </div>
                                  </div>
                                )
                              })}
                            </div>
                          </div>
                        )
                      })}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div className="text-center py-12">
              <BookOpen className="h-16 w-16 text-gray-400 mx-auto mb-4" />
              <h3 className="text-lg font-medium text-gray-900 mb-2">
                No Monthly Plan Available
              </h3>
              <p className="text-gray-600">
                The study plan data appears to be incomplete. Please regenerate your plan.
              </p>
            </div>
          )}

          {/* Weekly Plan */}
          {state.studyPlan.weekly_plan && Object.keys(state.studyPlan.weekly_plan).length > 0 && (
            <div className="mt-8 border-t border-gray-200 pt-8">
              <h2 className="text-2xl font-bold text-gray-900 mb-6">Weekly Breakdown</h2>
              <div className="space-y-6">
                {Object.entries(state.studyPlan.weekly_plan).map(([week, weekPlan]) => (
                  <div key={week} className="border border-gray-200 rounded-lg overflow-hidden">
                    <div className="bg-gradient-to-r from-blue-50 to-indigo-50 px-6 py-4 border-b border-gray-200">
                      <div className="flex items-center">
                        <Calendar className="h-5 w-5 text-blue-600 mr-2" />
                        <h3 className="text-lg font-semibold text-gray-900 capitalize">
                          {week.replace('_', ' ')}
                        </h3>
                      </div>
                    </div>

                    <div className="p-6">
                      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                        {['mathematics', 'physics', 'chemistry'].map(subject => {
                          const subjectData = weekPlan[subject]
                          if (!subjectData || Object.keys(subjectData).length === 0) return null

                          return (
                            <div key={subject} className="bg-gray-50 rounded-lg p-4">
                              <div className="flex items-center mb-4">
                                <BookOpen className="h-5 w-5 text-primary-600 mr-2" />
                                <h4 className="font-semibold text-gray-900 capitalize">
                                  {subject}
                                </h4>
                              </div>

                              <div className="space-y-3">
                                {Object.entries(subjectData).map(([chapter, topics]) => (
                                  <div key={chapter} className="bg-white rounded-lg p-3 border border-gray-200">
                                    <div className="font-medium text-sm text-gray-900 mb-2">
                                      {chapter}
                                    </div>
                                    <div className="space-y-1">
                                      {topics.map((topic, topicIndex) => (
                                        <div key={topicIndex} className="flex items-center text-xs text-gray-600">
                                          <div className="w-2 h-2 bg-primary-400 rounded-full mr-2"></div>
                                          {topic}
                                        </div>
                                      ))}
                                    </div>
                                    <div className="mt-2 text-xs text-gray-500">
                                      {topics.length} topic{topics.length !== 1 ? 's' : ''}
                                    </div>
                                  </div>
                                ))}
                              </div>
                            </div>
                          )
                        })}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}