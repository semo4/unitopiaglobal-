import sys
import os

# Add your app's directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import your Flask application
from main import app as application

# If your main file has a different name, adjust accordingly
# Example: from app import app as application
