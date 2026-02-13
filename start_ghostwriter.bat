@echo off
title GhostWriter Server
cd /d "%~dp0"

REM Activate venv if it exists
if exist ".venv\Scripts\activate.bat" (
    call ".venv\Scripts\activate.bat"
)

cd /d "%~dp0ghostwriter"
echo ==========================================
echo    GhostWriter - Launching Server...
echo ==========================================
python server.py
if %ERRORLEVEL% neq 0 (
    echo.
    echo [ERROR] Server crashed or failed to start.
    pause
)
