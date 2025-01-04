@echo off

:: Activate the virtual environment
call .venv\Scripts\activate

:: Run the delete.py script with an optional file name parameter
if "%1"=="" (
    python delete.py
) else (
    python delete.py %1
)