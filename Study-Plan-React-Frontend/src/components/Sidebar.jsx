import React from 'react'
import { GraduationCap, MessageCircle, FileText, Settings } from 'lucide-react'

const navigationItems = [
  { id: 'form', label: 'Create Plan', icon: Settings },
  { id: 'chat', label: 'Chat Assistant', icon: MessageCircle },
  { id: 'plan', label: 'View Plan', icon: FileText },
]

export default function Sidebar({ activeSection, setActiveSection }) {
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
        <div className="space-y-2">
          {navigationItems.map((item) => {
            const Icon = item.icon
            return (
              <button
                key={item.id}
                onClick={() => setActiveSection(item.id)}
                className={`w-full flex items-center px-4 py-3 rounded-lg transition-colors duration-200 ${
                  activeSection === item.id
                    ? 'bg-primary-500 text-white'
                    : 'text-primary-100 hover:bg-primary-500 hover:text-white'
                }`}
              >
                <Icon className="h-5 w-5 mr-3" />
                {item.label}
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