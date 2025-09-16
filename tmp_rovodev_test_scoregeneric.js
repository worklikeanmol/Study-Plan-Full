// Test script for ScoreGeneric frontend integration
const API_BASE_URL = 'http://127.0.0.1:8000'

async function testBackendConnection() {
  try {
    const response = await fetch(`${API_BASE_URL}/`)
    if (response.ok) {
      console.log('✅ Backend connection successful')
      return true
    } else {
      console.log('❌ Backend responded with error:', response.status)
      return false
    }
  } catch (error) {
    console.log('❌ Backend connection failed:', error.message)
    return false
  }
}

async function testScoreGenericChat() {
  const testPayload = {
    user_id: 'test_user_scoregeneric',
    target_exam: 'JEE Mains',
    study_plan_type: 'ScoreGeneric',
    exam_date: '2024-12-15',
    target_score: 252,
    user_message: 'I want to focus on Physics and Chemistry. Generate my study plan.'
  }

  try {
    console.log('🧪 Testing ScoreGeneric chat API...')
    console.log('Payload:', JSON.stringify(testPayload, null, 2))
    
    const response = await fetch(`${API_BASE_URL}/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(testPayload)
    })

    if (response.ok) {
      const data = await response.json()
      console.log('✅ ScoreGeneric chat API successful')
      console.log('Response:', JSON.stringify(data, null, 2))
      
      if (data.is_plan_generated && data.study_plan) {
        console.log('✅ Study plan generated successfully')
        console.log('Plan type:', data.study_plan.plan_type)
        console.log('Monthly plans count:', Object.keys(data.study_plan.monthly_plans || {}).length)
        console.log('Weekly plans count:', Object.keys(data.study_plan.weekly_plans || {}).length)
      } else {
        console.log('ℹ️ Chat response received, but no plan generated yet')
      }
      
      return data
    } else {
      const errorData = await response.text()
      console.log('❌ ScoreGeneric chat API failed:', response.status, errorData)
      return null
    }
  } catch (error) {
    console.log('❌ ScoreGeneric chat API error:', error.message)
    return null
  }
}

async function testFormSave() {
  const formPayload = {
    user_id: 'test_user_scoregeneric',
    target_exam: 'JEE Mains',
    study_plan_type: 'ScoreGeneric',
    exam_date: '2024-12-15',
    target_score: 252
  }

  try {
    console.log('🧪 Testing ScoreGeneric form save API...')
    console.log('Payload:', JSON.stringify(formPayload, null, 2))
    
    const response = await fetch(`${API_BASE_URL}/save-form`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formPayload)
    })

    if (response.ok) {
      const data = await response.json()
      console.log('✅ ScoreGeneric form save successful')
      console.log('Response:', JSON.stringify(data, null, 2))
      return data
    } else {
      const errorData = await response.text()
      console.log('❌ ScoreGeneric form save failed:', response.status, errorData)
      return null
    }
  } catch (error) {
    console.log('❌ ScoreGeneric form save error:', error.message)
    return null
  }
}

async function runTests() {
  console.log('🚀 Starting ScoreGeneric Frontend Integration Tests\n')
  
  // Test 1: Backend Connection
  console.log('=== Test 1: Backend Connection ===')
  const isConnected = await testBackendConnection()
  if (!isConnected) {
    console.log('❌ Cannot proceed with tests - backend is not running')
    console.log('Please start the backend with: python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload')
    return
  }
  console.log('')

  // Test 2: Form Save
  console.log('=== Test 2: ScoreGeneric Form Save ===')
  await testFormSave()
  console.log('')

  // Test 3: Chat API
  console.log('=== Test 3: ScoreGeneric Chat API ===')
  await testScoreGenericChat()
  console.log('')

  console.log('🎉 Tests completed!')
  console.log('\n📋 Next Steps:')
  console.log('1. Start the React frontend: npm run dev')
  console.log('2. Fill out the form with ScoreGeneric plan type')
  console.log('3. Test the chat interface')
  console.log('4. Verify the plan view displays correctly')
}

// Run tests if this script is executed directly
if (typeof window === 'undefined') {
  // Node.js environment
  const fetch = require('node-fetch')
  runTests()
} else {
  // Browser environment
  window.runScoreGenericTests = runTests
  console.log('ScoreGeneric test functions loaded. Run window.runScoreGenericTests() to start.')
}