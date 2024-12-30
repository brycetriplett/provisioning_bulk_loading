@echo off
set /p action="Would you like to add or delete SIM cards? (type 'add' or 'delete'): "

if /i "%action%"=="add" (
    call .venv\Scripts\activate
    python main.py
) else if /i "%action%"=="delete" (
    call .venv\Scripts\activate
    python delete.py
) else (
    echo Invalid input. Please type 'add' or 'delete'.
)
