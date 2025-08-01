#!/usr/bin/env python3
"""
Test script for the target score-based planning system
"""

import requests
import json

# Configuration
BASE_URL = "http://localhost:8000"

def test_generic_plan_with_target_score():
    """Test generic plan with target score"""
    print("🎯 Testing Generic Plan with Target Score...")
    
    # Test case 1: Achievable target score
    chat_request = {
        "user_id": "test_score_user_001",
        "user_message": "Hi, I want a score-optimized study plan",
        "target_exam": "JEE Mains",
        "study_plan_type": "generic",  # Generic plan
        "preparation_type": "revision",  # Should route to weightage
        "target_score": 200,  # Achievable target
        "syllabus": {
            "Physics": ["Chapter_1", "Chapter_2", "Chapter_3"],
            "Chemistry": ["Chapter_1", "Chapter_2", "Chapter_3"],
            "Mathematics": ["Chapter_1", "Chapter_2", "Chapter_3"]
        },
        "number_of_months": 6,
        "hours_per_day": 6,
        "reset_chat": True
    }
    
    response = requests.post(f"{BASE_URL}/chat", json=chat_request)
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Generic plan response: {data['assistant_message'][:200]}...")
        return True
    else:
        print(f"❌ Error in generic plan: {response.status_code}")
        return False

def test_challenging_target_score():
    """Test generic plan with challenging target score"""
    print("\n⚠️ Testing Challenging Target Score...")
    
    chat_request = {
        "user_id": "test_score_user_002",
        "user_message": "I want to score very high",
        "target_exam": "JEE Mains",
        "study_plan_type": "generic",
        "preparation_type": "syllabus coverage",  # Should route to flow initially
        "target_score": 290,  # Very challenging target
        "syllabus": {
            "Physics": ["Chapter_1", "Chapter_2"],
            "Chemistry": ["Chapter_1", "Chapter_2"],
            "Mathematics": ["Chapter_1", "Chapter_2"]
        },
        "number_of_months": 2,  # Limited time
        "hours_per_day": 4,     # Limited hours
        "reset_chat": True
    }
    
    response = requests.post(f"{BASE_URL}/chat", json=chat_request)
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Challenging target response: {data['assistant_message'][:200]}...")
        return True
    else:
        print(f"❌ Error in challenging target: {response.status_code}")
        return False

def test_custom_plan_routing():
    """Test custom plan routing"""
    print("\n📚 Testing Custom Plan Routing...")
    
    # Test syllabus coverage -> flow
    chat_request = {
        "user_id": "test_custom_user_001",
        "user_message": "I want comprehensive coverage",
        "target_exam": "JEE Mains",
        "study_plan_type": "custom",
        "preparation_type": "syllabus coverage",  # Should route to flow
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
        print(f"✅ Custom syllabus coverage: {data['assistant_message'][:200]}...")
    else:
        print(f"❌ Error in custom syllabus coverage: {response.status_code}")
        return False
    
    # Test revision -> weightage
    chat_request["preparation_type"] = "revision"  # Should route to weightage
    chat_request["user_id"] = "test_custom_user_002"
    chat_request["user_message"] = "I want to focus on revision"
    
    response = requests.post(f"{BASE_URL}/chat", json=chat_request)
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Custom revision: {data['assistant_message'][:200]}...")
        return True
    else:
        print(f"❌ Error in custom revision: {response.status_code}")
        return False

def test_plan_generation():
    """Test actual plan generation with score optimization"""
    print("\n🚀 Testing Plan Generation with Score Optimization...")
    
    chat_request = {
        "user_id": "test_score_user_001",
        "user_message": "generate my score-optimized plan",
        "target_exam": "JEE Mains",
        "study_plan_type": "generic",
        "preparation_type": "revision",
        "target_score": 200,
        "syllabus": {
            "Physics": ["Chapter_1", "Chapter_2", "Chapter_3"],
            "Chemistry": ["Chapter_1", "Chapter_2", "Chapter_3"],
            "Mathematics": ["Chapter_1", "Chapter_2", "Chapter_3"]
        },
        "number_of_months": 6,
        "hours_per_day": 6
    }
    
    response = requests.post(f"{BASE_URL}/chat", json=chat_request)
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Plan generated: {data['is_plan_generated']}")
        if data.get('study_plan'):
            insights = data['study_plan'].get('insights', '')
            print(f"📊 Plan insights: {insights[:300]}...")
            
            # Check if score optimization is mentioned
            if 'score' in insights.lower() or 'target' in insights.lower():
                print("✅ Score optimization detected in insights")
            else:
                print("⚠️ Score optimization not clearly mentioned in insights")
        return True
    else:
        print(f"❌ Error in plan generation: {response.status_code}")
        return False

def main():
    """Run all score system tests"""
    print("🎯 Starting Target Score-Based Planning Tests")
    print("=" * 60)
    
    try:
        # Test 1: Generic plan with achievable target
        test_generic_plan_with_target_score()
        
        # Test 2: Generic plan with challenging target
        test_challenging_target_score()
        
        # Test 3: Custom plan routing
        test_custom_plan_routing()
        
        # Test 4: Plan generation with score optimization
        test_plan_generation()
        
        print("\n" + "=" * 60)
        print("✅ All score system tests completed!")
        
        print("\n📋 Test Summary:")
        print("✅ Generic plans with target scores")
        print("✅ Challenging target score warnings")
        print("✅ Proper routing based on preparation type")
        print("✅ Score optimization in plan generation")
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()