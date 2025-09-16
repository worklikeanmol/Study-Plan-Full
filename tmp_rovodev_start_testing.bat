@echo off
echo ========================================
echo  ScoreGeneric Frontend Testing Setup
echo ========================================
echo.

echo 1. Checking if backend is running...
curl -s http://127.0.0.1:8000/ >nul 2>&1
if %errorlevel% == 0 (
    echo ✅ Backend is running on port 8000
) else (
    echo ❌ Backend is not running!
    echo.
    echo Please start the backend first:
    echo   cd Study-Plan
    echo   python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    echo.
    pause
    exit /b 1
)

echo.
echo 2. Starting React frontend...
echo.
echo Frontend will be available at: http://localhost:5173
echo.
echo 📋 Testing Checklist:
echo   □ Fill form with ScoreGeneric plan type
echo   □ Set exam date (minimum 6 months from today)
echo   □ Set target score (1-300)
echo   □ Chat with AI and say "generate"
echo   □ Check plan view for ScoreGeneric features
echo.

npm run dev