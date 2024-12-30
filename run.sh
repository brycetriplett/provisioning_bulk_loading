#!/bin/bash

# Activate the virtual environment
source .venv/bin/activate

# Prompt the user for input
read -p "Would you like to add or delete SIM cards? (type 'add' or 'delete'): " action

# Run the appropriate script based on user input
if [ "$action" == "add" ]; then
    python main.py
elif [ "$action" == "delete" ]; then
    python delete.py
else
    echo "Invalid input. Please type 'add' or 'delete'."
fi