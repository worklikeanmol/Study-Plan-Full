import React, { useState } from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { Toaster } from 'react-hot-toast'
import StudyPlanForm from './components/StudyPlanForm'
import ChatInterface from './components/ChatInterface'
import StudyPlanView from './components/StudyPlanView'
import Sidebar from './components/Sidebar'
import { StudyPlanProvider } from './context/StudyPlanContext'

function App() {
  const [activeSection, setActiveSection] = useState('form')

  return (
    <StudyPlanProvider>
      <div className="flex h-screen bg-gray-50">
        <Sidebar activeSection={activeSection} setActiveSection={setActiveSection} />
        
        <div className="flex-1 flex flex-col overflow-hidden">
          <main className="flex-1 overflow-y-auto p-6">
            {activeSection === 'form' && <StudyPlanForm onComplete={() => setActiveSection('chat')} />}
            {activeSection === 'chat' && <ChatInterface />}
            {activeSection === 'plan' && <StudyPlanView />}
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
    </StudyPlanProvider>
  )
}

export default App