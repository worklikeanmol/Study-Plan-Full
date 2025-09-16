import React, { useState } from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { Toaster, toast } from 'react-hot-toast'
import StudyPlanForm from './components/StudyPlanForm'
import ChatInterface from './components/ChatInterface'
import ScoreOrientedPlanView from './components/ScoreOrientedPlanView'
import StudyPlanView from './components/StudyPlanView'
import NewScoreOrientedPlanView from './components/NewScoreOrientedPlanView'
import Sidebar from './components/Sidebar'
import { StudyPlanProvider, useStudyPlan } from './context/StudyPlanContext'

function AppContent() {
  const [activeSection, setActiveSection] = useState('form')
  const { state, dispatch } = useStudyPlan()

  // Smart Plan View Component that routes based on plan type
  const SmartPlanView = () => {
    const { studyPlan, formData } = state
    
    if (!studyPlan) {
      return (
        <div className="flex items-center justify-center h-64">
          <div className="text-center">
            <p className="text-gray-500 mb-2">No study plan available</p>
            <p className="text-sm text-gray-400">Generate a plan first using the chat interface</p>
          </div>
        </div>
      )
    }

    // Determine plan type from multiple sources
    const planType = studyPlan.plan_type || 
                    formData.study_plan_type || 
                    'Custom'

    console.log('Plan type detected:', planType)
    console.log('Study plan data:', studyPlan)

    // Route to appropriate component based on plan type
    switch (planType.toLowerCase()) {
      case 'scoregeneric':
        return <NewScoreOrientedPlanView studyPlan={studyPlan} />
      
      case 'custom':
      default:
        return <StudyPlanView studyPlan={studyPlan} />
    }
  }

  // Handle form completion - redirect to chat
  const handleFormComplete = () => {
    setActiveSection('chat')
    toast.success('Form saved! Now chat with the AI to generate your study plan.')
  }

  return (
    <div className="flex h-screen bg-gray-50">
      <Sidebar activeSection={activeSection} setActiveSection={setActiveSection} />
      
      <div className="flex-1 flex flex-col overflow-hidden">
        <main className="flex-1 overflow-y-auto p-6">
          {activeSection === 'form' && (
            <StudyPlanForm onComplete={handleFormComplete} />
          )}
          {activeSection === 'chat' && <ChatInterface />}
          {activeSection === 'plan' && <SmartPlanView />}
        </main>
      </div>
      
      <Toaster 
        position="top-right"
        toastOptions={{
          duration: 4000,
          style: {
            background: '#363636',
            color: '#fff',
          },
        }}
      />
    </div>
  )
}

function App() {
  return (
    <StudyPlanProvider>
      <AppContent />
    </StudyPlanProvider>
  )
}

export default App