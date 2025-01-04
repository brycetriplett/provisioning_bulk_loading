#!/bin/bash

# Activate the virtual environment
source .venv/bin/activate

# Run the main.py script with an optional file name parameter
if [ -z "$1" ]; then
    python add.py
else
    python add.py "$1"
fi