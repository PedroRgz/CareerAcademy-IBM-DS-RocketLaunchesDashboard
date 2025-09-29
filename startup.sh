#!/bin/bash
# Azure Web App startup script for Python Dash application

# Install dependencies
pip install -r requirements.txt

# Start the Dash application using Gunicorn
exec gunicorn --bind 0.0.0.0:8000 --workers 1 --timeout 600 main:server