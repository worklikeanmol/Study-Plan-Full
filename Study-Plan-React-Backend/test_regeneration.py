#!/usr/bin/env python3
"""
Test script for the regeneration flow
This script tests the complete regeneration workflow
"""

import requests
import json
import time

# Configuration
BASE_URL = "http://localhost:8000"
TEST_USER_ID = "test_regen_user_001"

def test_user_status_check():
    """Test user status checking"""
    print("🔍 Testing user status check...")
    
    response = requests.post(f"{BASE_URL}/check-user-status", params={"user_id": TEST_USER_ID})
    if response.status_code == 200:
        data = response.json()
        print(f"✅ User status: {data}")
        return data.get("is_existing_user", False)
    else:
        print(f"❌ Error checking user status: {response.status_code}")
        return False

def test_normal_flow():
    """Test normal flow for new user"""
    print("\n📚 Testing normal flow (new user)...")
    
    chat_request = {
        "user_id": TEST_USER_ID,
        "user_message": "Hi, I want to create a study plan",
        "target_exam": "JEE Mains",
        "study_plan_type": "Custom",
        "preparation_type": "Syllabus Coverage",
        "syllabus": {
            "Physics": ["Chapter_1", "Chapter_2", "Chapter_3"],
            "Chemistry": ["Chapter_1", "Chapter_2", "Chapter_3"],
            "Mathematics": ["Chapter_1", "Chapter_2", "Chapter_3"]
        },
        "number_of_months": 8,
        "hours_per_day": 6,
        "reset_chat": True
    }
    
    response = requests.post(f"{BASE_URL}/chat", json=chat_request)
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Normal flow response: {data['assistant_message'][:200]}...")
        return True
    else:
        print(f"❌ Error in normal flow: {response.status_code}")
        return False

def test_plan_generation():
    """Test plan generation in normal flow"""
    print("\n🎯 Testing plan generation...")
    
    chat_request = {
        "user_id": TEST_USER_ID,
        "user_message": "I want to focus on physics and generate my plan",
        "target_exam": "JEE Mains",
        "study_plan_type": "Custom",
        "preparation_type": "Syllabus Coverage",
        "syllabus": {
            "Physics": ["Chapter_1", "Chapter_2", "Chapter_3"],
            "Chemistry": ["Chapter_1", "Chapter_2", "Chapter_3"],
            "Mathematics": ["Chapter_1", "Chapter_2", "Chapter_3"]
        },
        "number_of_months": 8,
        "hours_per_day": 6
    }
    
    response = requests.post(f"{BASE_URL}/chat", json=chat_request)
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Plan generation response: {data['assistant_message'][:200]}...")
        print(f"📊 Plan generated: {data['is_plan_generated']}")
        return data['is_plan_generated']
    else:
        print(f"❌ Error in plan generation: {response.status_code}")
        return False

def test_plan_finalization():
    """Test plan finalization"""
    print("\n✅ Testing plan finalization...")
    
    chat_request = {
        "user_id": TEST_USER_ID,
        "user_message": "finalize",
        "target_exam": "JEE Mains",
        "study_plan_type": "Custom",
        "preparation_type": "Syllabus Coverage",
        "syllabus": {
            "Physics": ["Chapter_1", "Chapter_2", "Chapter_3"],
            "Chemistry": ["Chapter_1", "Chapter_2", "Chapter_3"],
            "Mathematics": ["Chapter_1", "Chapter_2", "Chapter_3"]
        },
        "number_of_months": 8,
        "hours_per_day": 6
    }
    
    response = requests.post(f"{BASE_URL}/chat", json=chat_request)
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Finalization response: {data['assistant_message'][:200]}...")
        return True
    else:
        print(f"❌ Error in finalization: {response.status_code}")
        return False

def test_regeneration_info():
    """Test regeneration info endpoint"""
    print("\n📈 Testing regeneration info...")
    
    response = requests.get(f"{BASE_URL}/regeneration-info/{TEST_USER_ID}")
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Regeneration info: {json.dumps(data, indent=2)}")
        return True
    elif response.status_code == 404:
        print("ℹ️ User not found (expected for new user)")
        return True
    else:
        print(f"❌ Error getting regeneration info: {response.status_code}")
        return False

def test_regeneration_flow():
    """Test regeneration flow for existing user"""
    print("\n🔄 Testing regeneration flow (existing user)...")
    
    chat_request = {
        "user_id": TEST_USER_ID,
        "user_message": "Hi, I'm back after my first month",
        "target_exam": "JEE Mains",
        "study_plan_type": "Custom",
        "preparation_type": "Syllabus Coverage",
        "syllabus": {
            "Physics": ["Chapter_1", "Chapter_2", "Chapter_3"],
            "Chemistry": ["Chapter_1", "Chapter_2", "Chapter_3"],
            "Mathematics": ["Chapter_1", "Chapter_2", "Chapter_3"]
        },
        "number_of_months": 8,
        "hours_per_day": 6,
        "reset_chat": True
    }
    
    response = requests.post(f"{BASE_URL}/chat", json=chat_request)
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Regeneration flow response: {data['assistant_message'][:200]}...")
        return True
    else:
        print(f"❌ Error in regeneration flow: {response.status_code}")
        return False

def test_chat_storage_status():
    """Test chat storage status"""
    print("\n💾 Testing chat storage status...")
    
    response = requests.get(f"{BASE_URL}/chat-storage-status")
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Chat storage status: {json.dumps(data, indent=2)}")
        return True
    else:
        print(f"❌ Error getting chat storage status: {response.status_code}")
        return False

def main():
    """Run all tests"""
    print("🚀 Starting Regeneration Flow Tests")
    print("=" * 50)
    
    try:
        # Test 1: Check initial user status (should be new)
        is_existing = test_user_status_check()
        
        if not is_existing:
            # Test 2: Normal flow for new user
            test_normal_flow()
            
            # Test 3: Generate plan
            plan_generated = test_plan_generation()
            
            if plan_generated:
                # Test 4: Finalize plan
                test_plan_finalization()
                
                # Wait a bit for database operations
                time.sleep(2)
                
                # Test 5: Check user status again (should be existing now)
                print("\n🔄 Checking user status after plan creation...")
                is_existing_after = test_user_status_check()
                
                if is_existing_after:
                    # Test 6: Get regeneration info
                    test_regeneration_info()
                    
                    # Test 7: Test regeneration flow
                    test_regeneration_flow()
        else:
            print("ℹ️ User already exists, testing regeneration flow directly...")
            test_regeneration_info()
            test_regeneration_flow()
        
        # Test 8: Chat storage status
        test_chat_storage_status()
        
        print("\n" + "=" * 50)
        print("✅ All tests completed!")
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()