import React, { useState } from 'react'
import { 
  Target, 
  Calendar, 
  BookOpen, 
  Clock, 
  TrendingUp, 
  CheckCircle,
  Award,
  BarChart3,
  ChevronDown,
  ChevronRight,
  Star,
  Zap,
  Brain,
  Trophy
} from 'lucide-react'

export default function NewScoreOrientedPlanView({ studyPlan }) {
  const [selectedMonth, setSelectedMonth] = useState(1)
  const [expandedSubjects, setExpandedSubjects] = useState({})
  const [activeTab, setActiveTab] = useState('overview')

  if (!studyPlan) {
    return (
      <div className="flex items-center justify-center h-64">
        <p className="text-gray-500">No study plan available</p>
      </div>
    )
  }

  // Detect plan type and extract data accordingly
  const planType = studyPlan.plan_type || 'new_score_oriented'
  const isScoreGeneric = planType.toLowerCase() === 'scoregeneric'
  
  // Extract data based on plan type
  let monthlyPlan, weeklyPlan, insights, monthlyTargets, practiceSchedule, overallScoreDistribution
  
  if (isScoreGeneric) {
    // ScoreGeneric structure
    monthlyPlan = studyPlan.monthly_plans || {}
    weeklyPlan = studyPlan.weekly_plans || {}
    insights = studyPlan.insights || ''
    overallScoreDistribution = studyPlan.overall_score_distribution || {}
    practiceSchedule = studyPlan.practice_summary || {}
    
    // Extract monthly targets from monthly plans
    monthlyTargets = {}
    Object.keys(monthlyPlan).forEach(month => {
      const plan = monthlyPlan[month]
      if (plan.score_target) {
        monthlyTargets[month] = {
          total_achievable_score: plan.score_target.total_achievable_score,
          user_target_for_month: plan.score_target.user_target_for_month
        }
      }
    })
  } else {
    // New Score-Oriented structure
    const newScoreData = studyPlan.new_score_oriented_data || {}
    monthlyPlan = studyPlan.monthly_plan || {}
    weeklyPlan = studyPlan.weekly_plan || {}
    insights = studyPlan.insights || ''
    
    // Extract enhanced features if available
    const enhancedFeatures = newScoreData.enhanced_features || {}
    monthlyTargets = enhancedFeatures.monthly_target_scores || {}
    const extendedPlan = enhancedFeatures.extended_months_plan || {}
    const weekendSchedule = enhancedFeatures.weekend_schedule || {}
    
    // Extract revision flow results
    const revisionFlow = newScoreData.revision_flow_results || {}
    const monthlyDistribution = newScoreData.monthly_distribution || {}
  }

  const toggleSubject = (subject) => {
    setExpandedSubjects(prev => ({
      ...prev,
      [subject]: !prev[subject]
    }))
  }

  const renderOverviewTab = () => (
    <div className="space-y-6">
      {/* Plan Summary */}
      <div className="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-xl p-6 border border-blue-200">
        <div className="flex items-center mb-4">
          <Trophy className="h-6 w-6 text-blue-600 mr-2" />
          <h3 className="text-xl font-bold text-blue-900">
            {isScoreGeneric ? 'ScoreGeneric Plan Summary' : 'New Score-Oriented Plan Summary'}
          </h3>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="bg-white rounded-lg p-4 border border-blue-100">
            <div className="flex items-center">
              <Target className="h-5 w-5 text-blue-600 mr-2" />
              <span className="text-sm font-medium text-gray-600">Target Score</span>
            </div>
            <p className="text-2xl font-bold text-blue-900 mt-1">
              {isScoreGeneric 
                ? (studyPlan.target_score || 'N/A')
                : (studyPlan.target_score || newScoreData.target_score || 'N/A')
              }/300
            </p>
          </div>
          
          <div className="bg-white rounded-lg p-4 border border-blue-100">
            <div className="flex items-center">
              <Calendar className="h-5 w-5 text-green-600 mr-2" />
              <span className="text-sm font-medium text-gray-600">Total Duration</span>
            </div>
            <p className="text-2xl font-bold text-green-900 mt-1">
              {isScoreGeneric 
                ? (studyPlan.total_months || Object.keys(monthlyPlan).length || 'N/A')
                : (newScoreData.total_months || Object.keys(monthlyPlan).length || 'N/A')
              } months
            </p>
          </div>
          
          <div className="bg-white rounded-lg p-4 border border-blue-100">
            <div className="flex items-center">
              <BookOpen className="h-5 w-5 text-purple-600 mr-2" />
              <span className="text-sm font-medium text-gray-600">Syllabus Target</span>
            </div>
            <p className="text-2xl font-bold text-purple-900 mt-1">
              {isScoreGeneric 
                ? (studyPlan.coverage_months || 6)
                : (newScoreData.syllabus_completion_months || 6)
              } months
            </p>
          </div>
        </div>
      </div>

      {/* Key Features */}
      <div className="bg-white rounded-xl p-6 border border-gray-200">
        <h3 className="text-lg font-bold text-gray-900 mb-4 flex items-center">
          <Star className="h-5 w-5 text-yellow-500 mr-2" />
          Key Features
        </h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="flex items-start space-x-3">
            <CheckCircle className="h-5 w-5 text-green-500 mt-0.5" />
            <div>
              <p className="font-medium text-gray-900">Complete Syllabus Coverage</p>
              <p className="text-sm text-gray-600">100% chapter completion ensuring strong foundation</p>
            </div>
          </div>
          <div className="flex items-start space-x-3">
            <CheckCircle className="h-5 w-5 text-green-500 mt-0.5" />
            <div>
              <p className="font-medium text-gray-900">Dependency Management</p>
              <p className="text-sm text-gray-600">Chapters ordered based on prerequisites</p>
            </div>
          </div>
          <div className="flex items-start space-x-3">
            <CheckCircle className="h-5 w-5 text-green-500 mt-0.5" />
            <div>
              <p className="font-medium text-gray-900">Score Optimization</p>
              <p className="text-sm text-gray-600">High-weightage chapters prioritized</p>
            </div>
          </div>
          <div className="flex items-start space-x-3">
            <CheckCircle className="h-5 w-5 text-green-500 mt-0.5" />
            <div>
              <p className="font-medium text-gray-900">Practice Integration</p>
              <p className="text-sm text-gray-600">Saturday (PYQ) + Sunday (DPP) schedule</p>
            </div>
          </div>
        </div>
      </div>

      {/* Insights */}
      {insights && (
        <div className="bg-white rounded-xl p-6 border border-gray-200">
          <h3 className="text-lg font-bold text-gray-900 mb-4 flex items-center">
            <Brain className="h-5 w-5 text-blue-500 mr-2" />
            Plan Insights
          </h3>
          <div className="prose prose-sm max-w-none">
            {insights.split('\n').map((line, index) => (
              <p key={index} className="text-gray-700 mb-2">
                {line}
              </p>
            ))}
          </div>
        </div>
      )}

      {/* ScoreGeneric Practice Schedule */}
      {isScoreGeneric && practiceSchedule && Object.keys(practiceSchedule).length > 0 && (
        <div className="bg-white rounded-xl p-6 border border-gray-200">
          <h3 className="text-lg font-bold text-gray-900 mb-4 flex items-center">
            <Zap className="h-5 w-5 text-yellow-500 mr-2" />
            Practice Schedule Summary
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="bg-blue-50 rounded-lg p-4">
              <h4 className="font-semibold text-blue-900 mb-2">DPP Schedule</h4>
              <p className="text-sm text-blue-700">
                Daily Practice Problems - Monday through Friday
              </p>
              <p className="text-xs text-blue-600 mt-1">
                Subject rotation: Physics → Chemistry → Mathematics
              </p>
            </div>
            <div className="bg-green-50 rounded-lg p-4">
              <h4 className="font-semibold text-green-900 mb-2">PYQ Schedule</h4>
              <p className="text-sm text-green-700">
                Previous Year Questions - Weekends
              </p>
              <p className="text-xs text-green-600 mt-1">
                Saturday & Sunday: All subjects combined practice
              </p>
            </div>
          </div>
        </div>
      )}

      {/* ScoreGeneric Score Distribution */}
      {isScoreGeneric && overallScoreDistribution && Object.keys(overallScoreDistribution).length > 0 && (
        <div className="bg-white rounded-xl p-6 border border-gray-200">
          <h3 className="text-lg font-bold text-gray-900 mb-4 flex items-center">
            <BarChart3 className="h-5 w-5 text-purple-500 mr-2" />
            Overall Score Distribution
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {Object.entries(overallScoreDistribution).map(([subject, score]) => (
              <div key={subject} className="bg-gray-50 rounded-lg p-4">
                <h4 className="font-semibold text-gray-900 capitalize mb-1">{subject}</h4>
                <p className="text-2xl font-bold text-purple-600">{score}</p>
                <p className="text-xs text-gray-600">Expected Score</p>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )

  const renderMonthlyPlanTab = () => (
    <div className="space-y-6">
      {/* Month Selection */}
      <div className="bg-white rounded-xl p-6 border border-gray-200">
        <h3 className="text-lg font-bold text-gray-900 mb-4">Select Month</h3>
        <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-2">
          {Object.keys(monthlyPlan).map((monthKey, index) => {
            const monthNum = index + 1
            return (
              <button
                key={monthKey}
                onClick={() => setSelectedMonth(monthNum)}
                className={`p-3 rounded-lg border text-center transition-colors ${
                  selectedMonth === monthNum
                    ? 'bg-blue-500 text-white border-blue-500'
                    : 'bg-gray-50 text-gray-700 border-gray-200 hover:bg-gray-100'
                }`}
              >
                <div className="text-sm font-medium">Month {monthNum}</div>
              </button>
            )
          })}
        </div>
      </div>

      {/* Selected Month Details */}
      {selectedMonth && monthlyPlan[`Month ${selectedMonth}`] && (
        <div className="bg-white rounded-xl p-6 border border-gray-200">
          <h3 className="text-lg font-bold text-gray-900 mb-4 flex items-center">
            <Calendar className="h-5 w-5 text-blue-500 mr-2" />
            Month {selectedMonth} Plan
          </h3>
          
          <div className="space-y-4">
            {isScoreGeneric ? (
              // ScoreGeneric structure: chapters are objects with chapter priorities
              monthlyPlan[`Month ${selectedMonth}`]?.chapters && 
              Object.entries(monthlyPlan[`Month ${selectedMonth}`].chapters).map(([subject, chapterList]) => {
                if (!chapterList || chapterList.length === 0) return null
                
                return (
                  <div key={subject} className="border border-gray-200 rounded-lg">
                    <button
                      onClick={() => toggleSubject(subject)}
                      className="w-full flex items-center justify-between p-4 text-left hover:bg-gray-50"
                    >
                      <div className="flex items-center">
                        <BookOpen className="h-5 w-5 text-blue-500 mr-3" />
                        <span className="font-medium text-gray-900 capitalize">{subject}</span>
                        <span className="ml-2 text-sm text-gray-500">
                          ({chapterList.length} chapters)
                        </span>
                      </div>
                      {expandedSubjects[subject] ? (
                        <ChevronDown className="h-5 w-5 text-gray-400" />
                      ) : (
                        <ChevronRight className="h-5 w-5 text-gray-400" />
                      )}
                    </button>
                    
                    {expandedSubjects[subject] && (
                      <div className="px-4 pb-4">
                        <div className="space-y-2">
                          {chapterList.map((chapterObj, index) => (
                            <div key={index} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                              <div className="flex items-center">
                                <div className={`w-2 h-2 rounded-full mr-3 ${
                                  chapterObj.priority_level === 'High' ? 'bg-red-500' :
                                  chapterObj.priority_level === 'Medium' ? 'bg-yellow-500' : 'bg-green-500'
                                }`} />
                                <span className="text-sm font-medium text-gray-900">{chapterObj.chapter}</span>
                              </div>
                              <div className="flex items-center space-x-2">
                                <span className={`px-2 py-1 text-xs rounded-full ${
                                  chapterObj.priority_level === 'High' ? 'bg-red-100 text-red-800' :
                                  chapterObj.priority_level === 'Medium' ? 'bg-yellow-100 text-yellow-800' : 'bg-green-100 text-green-800'
                                }`}>
                                  {chapterObj.priority_level}
                                </span>
                                <span className="text-xs text-gray-500">
                                  {chapterObj.weightage}% weightage
                                </span>
                              </div>
                            </div>
                          ))}
                        </div>
                      </div>
                    )}
                  </div>
                )
              })
            ) : (
              // New Score-Oriented structure: chapters are simple arrays
              Object.entries(monthlyPlan[`Month ${selectedMonth}`]).map(([subject, chapters]) => {
                if (!chapters || chapters.length === 0) return null
                
                return (
                  <div key={subject} className="border border-gray-200 rounded-lg">
                    <button
                      onClick={() => toggleSubject(subject)}
                      className="w-full flex items-center justify-between p-4 text-left hover:bg-gray-50"
                    >
                      <div className="flex items-center">
                        <BookOpen className="h-5 w-5 text-blue-500 mr-3" />
                        <span className="font-medium text-gray-900 capitalize">{subject}</span>
                        <span className="ml-2 text-sm text-gray-500">
                          ({chapters.length} chapters)
                        </span>
                      </div>
                      {expandedSubjects[subject] ? (
                        <ChevronDown className="h-5 w-5 text-gray-400" />
                      ) : (
                        <ChevronRight className="h-5 w-5 text-gray-400" />
                      )}
                    </button>
                  
                    {expandedSubjects[subject] && (
                      <div className="px-4 pb-4">
                        <div className="space-y-2">
                          {chapters.map((chapterInfo, index) => (
                            <div key={index} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                              <span className="text-gray-900">{chapterInfo.chapter}</span>
                              <div className="flex items-center">
                                <div className="w-16 bg-gray-200 rounded-full h-2 mr-2">
                                  <div 
                                    className="bg-green-500 h-2 rounded-full" 
                                    style={{ width: `${(chapterInfo.coverage || 1) * 100}%` }}
                                  ></div>
                                </div>
                                <span className="text-sm text-gray-600">
                                  {Math.round((chapterInfo.coverage || 1) * 100)}%
                                </span>
                              </div>
                            </div>
                          ))}
                        </div>
                      </div>
                    )}
                  </div>
                )
              })
            )}
          </div>
        </div>
      )}
    </div>
  )

  const renderWeeklyPlanTab = () => (
    <div className="space-y-6">
      <div className="bg-white rounded-xl p-6 border border-gray-200">
        <h3 className="text-lg font-bold text-gray-900 mb-4 flex items-center">
          <Clock className="h-5 w-5 text-green-500 mr-2" />
          Weekly Breakdown (Month 1)
        </h3>
        
        <div className="space-y-4">
          {Object.entries(weeklyPlan).map(([weekKey, weekData]) => (
            <div key={weekKey} className="border border-gray-200 rounded-lg p-4">
              <h4 className="font-medium text-gray-900 mb-3 capitalize">
                {weekKey.replace('_', ' ')}
              </h4>
              
              <div className="space-y-3">
                {Object.entries(weekData).map(([subject, chapters]) => {
                  if (!chapters || Object.keys(chapters).length === 0) return null
                  
                  return (
                    <div key={subject} className="bg-gray-50 rounded-lg p-3">
                      <h5 className="font-medium text-gray-800 capitalize mb-2">{subject}</h5>
                      <div className="space-y-2">
                        {Object.entries(chapters).map(([chapter, topics]) => (
                          <div key={chapter} className="text-sm">
                            <span className="font-medium text-gray-700">{chapter}:</span>
                            <div className="ml-4 mt-1">
                              {topics.slice(0, 3).map((topic, index) => (
                                <div key={index} className="text-gray-600">• {topic}</div>
                              ))}
                              {topics.length > 3 && (
                                <div className="text-gray-500 italic">
                                  ... and {topics.length - 3} more topics
                                </div>
                              )}
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                  )
                })}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )

  const renderEnhancedFeaturesTab = () => (
    <div className="space-y-6">
      {/* Monthly Target Scores */}
      {monthlyTargets && Object.keys(monthlyTargets).length > 0 && (
        <div className="bg-white rounded-xl p-6 border border-gray-200">
          <h3 className="text-lg font-bold text-gray-900 mb-4 flex items-center">
            <Target className="h-5 w-5 text-red-500 mr-2" />
            Monthly Target Scores
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {Object.entries(monthlyTargets).map(([month, data]) => (
              <div key={month} className="bg-gradient-to-r from-red-50 to-pink-50 rounded-lg p-4 border border-red-200">
                <h4 className="font-medium text-gray-900 mb-2">{month}</h4>
                <div className="space-y-1 text-sm">
                  <div className="flex justify-between">
                    <span className="text-gray-600">Target:</span>
                    <span className="font-medium">{data.user_target_score || 'N/A'}</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-gray-600">Max Achievable:</span>
                    <span className="font-medium">{data.total_achievable_score || 'N/A'}</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-gray-600">Efficiency:</span>
                    <span className="font-medium">{data.efficiency_required || 'N/A'}%</span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Weekend Schedule */}
      {weekendSchedule && Object.keys(weekendSchedule).length > 0 && (
        <div className="bg-white rounded-xl p-6 border border-gray-200">
          <h3 className="text-lg font-bold text-gray-900 mb-4 flex items-center">
            <Award className="h-5 w-5 text-purple-500 mr-2" />
            Weekend Practice Schedule
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="bg-blue-50 rounded-lg p-4 border border-blue-200">
              <h4 className="font-medium text-blue-900 mb-2 flex items-center">
                <Calendar className="h-4 w-4 mr-1" />
                Saturday - PYQ Practice
              </h4>
              <p className="text-sm text-blue-700">
                Previous Year Questions focused practice sessions
              </p>
            </div>
            <div className="bg-green-50 rounded-lg p-4 border border-green-200">
              <h4 className="font-medium text-green-900 mb-2 flex items-center">
                <BarChart3 className="h-4 w-4 mr-1" />
                Sunday - DPP Practice
              </h4>
              <p className="text-sm text-green-700">
                Daily Practice Problems for concept reinforcement
              </p>
            </div>
          </div>
        </div>
      )}

      {/* Extended Months Plan */}
      {extendedPlan && Object.keys(extendedPlan).length > 0 && (
        <div className="bg-white rounded-xl p-6 border border-gray-200">
          <h3 className="text-lg font-bold text-gray-900 mb-4 flex items-center">
            <TrendingUp className="h-5 w-5 text-orange-500 mr-2" />
            Extended Practice Phase
          </h3>
          <div className="bg-orange-50 rounded-lg p-4 border border-orange-200">
            <p className="text-orange-800 mb-2">
              <strong>Intensive Practice & Revision Phase</strong>
            </p>
            <p className="text-sm text-orange-700">
              After completing the syllabus, focus on intensive practice sessions, 
              mock tests, and targeted revision of weak areas.
            </p>
          </div>
        </div>
      )}
    </div>
  )

  return (
    <div className="max-w-7xl mx-auto p-6">
      {/* Header */}
      <div className="mb-8">
        <div className="flex items-center mb-2">
          <Zap className="h-8 w-8 text-blue-600 mr-3" />
          <h1 className="text-3xl font-bold text-gray-900">New Score-Oriented Study Plan</h1>
        </div>
        <p className="text-gray-600">
          Complete syllabus coverage with strategic score optimization
        </p>
      </div>

      {/* Tab Navigation */}
      <div className="mb-6">
        <div className="border-b border-gray-200">
          <nav className="-mb-px flex space-x-8">
            {[
              { id: 'overview', label: 'Overview', icon: Target },
              { id: 'monthly', label: 'Monthly Plan', icon: Calendar },
              { id: 'weekly', label: 'Weekly Plan', icon: Clock },
              { id: 'enhanced', label: 'Enhanced Features', icon: Star }
            ].map(({ id, label, icon: Icon }) => (
              <button
                key={id}
                onClick={() => setActiveTab(id)}
                className={`flex items-center py-2 px-1 border-b-2 font-medium text-sm ${
                  activeTab === id
                    ? 'border-blue-500 text-blue-600'
                    : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                }`}
              >
                <Icon className="h-4 w-4 mr-2" />
                {label}
              </button>
            ))}
          </nav>
        </div>
      </div>

      {/* Tab Content */}
      {activeTab === 'overview' && renderOverviewTab()}
      {activeTab === 'monthly' && renderMonthlyPlanTab()}
      {activeTab === 'weekly' && renderWeeklyPlanTab()}
      {activeTab === 'enhanced' && renderEnhancedFeaturesTab()}
    </div>
  )
}