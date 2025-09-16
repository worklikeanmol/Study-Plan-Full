import React from 'react'
import { GraduationCap, MessageCircle, FileText, FormInput, CheckCircle, Circle } from 'lucide-react'
import { useStudyPlan } from '../context/StudyPlanContext'

const navigationItems = [
  { id: 'form', label: 'Study Plan Form', icon: FormInput, step: 1 },
  { id: 'chat', label: 'Chat Assistant', icon: MessageCircle, step: 2 },
  { id: 'plan', label: 'View Plan', icon: FileText, step: 3 },
]

export default function Sidebar({ activeSection, setActiveSection }) {
  const { state } = useStudyPlan()
  
  // Determine workflow progress
  const isFormComplete = state.isFormValid
  const hasPlan = state.studyPlan !== null
  
  const getStepStatus = (stepId) => {
    switch (stepId) {
      case 'form':
        return isFormComplete ? 'completed' : (activeSection === 'form' ? 'active' : 'pending')
      case 'chat':
        return hasPlan ? 'completed' : (activeSection === 'chat' ? 'active' : (isFormComplete ? 'available' : 'disabled'))
      case 'plan':
        return activeSection === 'plan' ? 'active' : (hasPlan ? 'available' : 'disabled')
      default:
        return 'pending'
    }
  }
  return (
    <div className="w-64 bg-gradient-to-b from-primary-600 to-primary-700 text-white flex flex-col">
      {/* Header */}
      <div className="p-6 border-b border-primary-500">
        <div className="flex items-center">
          <GraduationCap className="h-8 w-8 mr-3" />
          <h2 className="text-xl font-bold">Study Planner</h2>
        </div>
      </div>

      {/* Navigation */}
      <nav className="flex-1 p-4">
        {/* Workflow Progress */}
        <div className="mb-6">
          <h3 className="text-sm font-medium text-primary-200 mb-3">Workflow Progress</h3>
          <div className="space-y-1">
            {navigationItems.map((item, index) => {
              const status = getStepStatus(item.id)
              const isDisabled = status === 'disabled'
              
              return (
                <div key={item.id} className="flex items-center text-sm">
                  <div className="flex items-center mr-2">
                    {status === 'completed' ? (
                      <CheckCircle className="h-4 w-4 text-green-400" />
                    ) : (
                      <Circle className={`h-4 w-4 ${
                        status === 'active' ? 'text-blue-400' : 
                        status === 'available' ? 'text-primary-300' : 'text-primary-500'
                      }`} />
                    )}
                  </div>
                  <span className={`${
                    status === 'completed' ? 'text-green-300' :
                    status === 'active' ? 'text-blue-300' :
                    status === 'available' ? 'text-primary-200' : 'text-primary-400'
                  }`}>
                    Step {item.step}: {item.label}
                  </span>
                </div>
              )
            })}
          </div>
        </div>

        {/* Navigation Buttons */}
        <div className="space-y-2">
          {navigationItems.map((item) => {
            const Icon = item.icon
            const status = getStepStatus(item.id)
            const isDisabled = status === 'disabled'
            
            return (
              <button
                key={item.id}
                onClick={() => !isDisabled && setActiveSection(item.id)}
                disabled={isDisabled}
                className={`w-full flex items-center px-4 py-3 rounded-lg transition-colors duration-200 ${
                  activeSection === item.id
                    ? 'bg-primary-500 text-white'
                    : isDisabled
                    ? 'text-primary-400 cursor-not-allowed opacity-50'
                    : 'text-primary-100 hover:bg-primary-500 hover:text-white'
                }`}
              >
                <Icon className="h-5 w-5 mr-3" />
                <div className="flex-1 text-left">
                  <div>{item.label}</div>
                  {isDisabled && (
                    <div className="text-xs text-primary-400 mt-1">
                      {item.id === 'chat' ? 'Complete form first' : 'Generate plan first'}
                    </div>
                  )}
                </div>
                {status === 'completed' && (
                  <CheckCircle className="h-4 w-4 text-green-400" />
                )}
              </button>
            )
          })}
        </div>
      </nav>

      {/* Footer */}
      <div className="p-4 border-t border-primary-500">
        <p className="text-primary-200 text-sm text-center">
          AI-Powered Study Planning
        </p>
      </div>
    </div>
  )
}