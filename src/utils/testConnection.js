// Test connection utility for debugging
export const testBackendConnection = async () => {
  const baseUrl = 'http://127.0.0.1:8000'
  
  console.log('Testing backend connection...')
  
  try {
    // Test 1: Basic connectivity
    const response = await fetch(`${baseUrl}/docs`)
    if (response.ok) {
      console.log('✅ Backend is accessible')
      return true
    } else {
      console.log('❌ Backend responded with error:', response.status)
      return false
    }
  } catch (error) {
    console.log('❌ Cannot connect to backend:', error.message)
    console.log('Make sure the backend is running on http://127.0.0.1:8000')
    return false
  }
}

// Test with sample data
export const testChatEndpoint = async () => {
  const baseUrl = 'http://127.0.0.1:8000'
  
  const testData = {
    user_id: 'test_user_frontend',
    user_message: 'hello',
    target_exam: 'JEE Mains',
    study_plan_type: 'Custom',
    preparation_type: 'Syllabus Coverage',
    syllabus: {
      mathematics: ['Algebra', 'Calculus'],
      physics: ['Mechanics', 'Thermodynamics'],
      chemistry: ['Atomic Structure', 'Chemical Bonding']
    },
    number_of_months: 6,
    hours_per_day: 6,
    target_score: null
  }
  
  try {
    const response = await fetch(`${baseUrl}/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(testData)
    })
    
    if (response.ok) {
      const data = await response.json()
      console.log('✅ Chat endpoint working:', data.assistant_message?.substring(0, 100))
      return true
    } else {
      console.log('❌ Chat endpoint error:', response.status, await response.text())
      return false
    }
  } catch (error) {
    console.log('❌ Chat endpoint error:', error.message)
    return false
  }
}