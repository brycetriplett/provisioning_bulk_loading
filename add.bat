@echo off

:: Activate the virtual environment
call .venv\Scripts\activate

:: Run the add.py script with an optional file name parameter
if "%1"=="" (
    python add.py
) else (
    python add.py %1
)