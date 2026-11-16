@echo off
setlocal
title CALL OF DUTY // HQ LAUNCHER
echo [COD HQ] Initializing Call of Duty Tactical Headquarters...

cd /d "%~dp0\.."

REM Check for python
where pythonw >nul 2>nul
if %ERRORLEVEL% equ 0 (
    start "" pythonw main.py --desktop
    exit /b 0
)

where py >nul 2>nul
if %ERRORLEVEL% equ 0 (
    start "" py -3 main.py --desktop
    exit /b 0
)

where python >nul 2>nul
if %ERRORLEVEL% equ 0 (
    start "" python main.py --desktop
    exit /b 0
)

echo [ERROR] Python was not found in PATH.
echo Please install Python 3.10+ from https://www.python.org/downloads/
pause
