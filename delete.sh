#!/bin/bash

# Activate the virtual environment
source .venv/bin/activate

# Run the delete.py script with an optional file name parameter
if [ -z "$1" ]; then
    python delete.py
else
    python delete.py "$1"
fi