# 🧪 Testing Score-Oriented Study Plans

## 🚀 **How to Test the Implementation**

### **Step 1: Start the Servers**

**Backend:**
```bash
cd Study-Plan-Full/Study-Plan-React-Backend
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

**Frontend:**
```bash
cd Study-Plan-Full/Study-Plan-React-Frontend
npm run dev
```

### **Step 2: Test Score-Oriented Plan Creation**

1. **Open the Frontend**: Navigate to `http://localhost:5173`

2. **Fill the Form**:
   - **User ID**: `test_score_user_123`
   - **Target Exam**: `JEE Mains`
   - **Study Plan Type**: `Score-Oriented` ⭐
   - **Target Score**: `200` (out of 300)
   - **Exam Date**: `2026-04-15` (should be 16+ months away)

3. **Notice the Changes**:
   - ✅ Preparation type automatically set to "revision" (disabled)
   - ✅ Number of months and hours per day fields hidden
   - ✅ Syllabus selection hidden
   - ✅ Green info box showing Score-Oriented configuration
   - ✅ Blue info box explaining automatic syllabus selection

4. **Submit the Form**: Click "Create Study Plan"

### **Step 3: Generate the Plan**

1. **Chat Interface**: You'll be taken to the chat interface
2. **Type**: `generate` or `generate my plan`
3. **Expected Response**: 
   ```
   🎯 Score-Oriented Study Plan Generated!
   
   📊 Monthly Score Targets:
   Month 1 (December 2024): 12.5 marks
   Month 2 (January 2025): 12.5 marks
   ...
   
   ✅ Your plan is ready! Check the 'View Plan' section for detailed breakdown.
   ```

### **Step 4: View the Score-Oriented Plan**

1. **Click "View Plan"** in the sidebar
2. **Expected Display**:
   - 🎯 Score-Oriented header with target score and success ratio
   - 📊 Monthly score targets with progress cards
   - 📅 Weekly schedule (Mon-Fri study, Sat-Sun practice)
   - 📈 Score progression tracking
   - 📚 Strategy overview
   - 🔢 Key metrics dashboard

## 🎯 **Expected Behavior**

### **Score Calculation Example**
```
Target Score: 200/300
Exam Date: 2026-04-15 (16 months away)
Monthly Requirement: 200/16 = 12.5 marks/month
Score Ratio: 200/300 = 66.7%
```

### **Chapter Selection**
- System automatically selects high-weightage chapters
- Includes prerequisite chapters based on dependencies
- Optimizes for achieving 200+ marks within 16 months

### **Weekly Schedule**
- **Monday-Friday**: Chapter study (5 days)
- **Saturday**: PYQ (Previous Year Questions)
- **Sunday**: DPP (Daily Practice Problems)

### **Monthly Targets**
Each month should show:
- Target marks for that month (12.5)
- Cumulative target (Month 1: 12.5, Month 2: 25.0, etc.)
- Chapters to cover
- Estimated score from those chapters

## 🔍 **Validation Tests**

### **Test 1: Exam Date Validation**
- Try date less than 5 months away → Should show error
- Try date 5+ months away → Should validate successfully

### **Test 2: Target Score Validation**
- Try score < 1 → Should show error
- Try score > 300 → Should show error
- Try score 1-300 → Should validate successfully

### **Test 3: Form Behavior**
- Select Score-Oriented → Should hide hours/months/syllabus
- Select Custom → Should show all fields
- Select Generic → Should show target score only

### **Test 4: Plan Generation**
- Score-Oriented plan → Should use new score engine
- Custom/Generic plan → Should use normal workflow

## 🐛 **Common Issues & Solutions**

### **Issue 1: API Endpoint Not Found**
```
Error: POST /score/validate-exam-date 404
```
**Solution**: Ensure backend server is running and score_router is included

### **Issue 2: Score Engine Import Error**
```
ImportError: cannot import name 'score_engine'
```
**Solution**: Check if score_calculation_engine.py is in the correct location

### **Issue 3: Plan Not Displaying**
```
No score-oriented plan data available
```
**Solution**: Check if score_oriented_data is included in the response

### **Issue 4: Exam Date Validation Failing**
```
Error validating exam date
```
**Solution**: Use YYYY-MM-DD format and ensure date is 5+ months away

## ✅ **Success Criteria**

The implementation is working correctly if:

1. ✅ **Form Validation**: Score-Oriented plans require only target score and exam date
2. ✅ **Auto-Configuration**: Months calculated from exam date, preparation type set to revision
3. ✅ **Plan Generation**: "generate" command creates score-oriented plan immediately
4. ✅ **Plan Display**: Specialized view shows monthly targets and weekly schedule
5. ✅ **Score Logic**: Monthly targets calculated as target_score/months
6. ✅ **Practice Days**: Saturday/Sunday reserved for PYQ/DPP
7. ✅ **Chapter Selection**: High-weightage chapters prioritized automatically

## 📊 **Test Data Examples**

### **Test Case 1: High Achiever**
- Target Score: 280/300
- Exam Date: 2026-06-15
- Expected: Aggressive monthly targets, most chapters selected

### **Test Case 2: Moderate Target**
- Target Score: 200/300
- Exam Date: 2026-04-15
- Expected: Balanced approach, selective chapter coverage

### **Test Case 3: Conservative Target**
- Target Score: 150/300
- Exam Date: 2026-08-15
- Expected: Focused on highest-weightage chapters only

## 🎉 **Expected Results**

After successful testing, you should see:
- Clean, intuitive Score-Oriented form interface
- Real-time validation and auto-calculation
- Immediate plan generation with score optimization
- Beautiful, informative plan display with progress tracking
- Monthly score targets that add up to your goal
- Practical weekly schedule with dedicated practice days

The system should feel like a sophisticated, AI-powered score optimization tool that takes the guesswork out of exam preparation!