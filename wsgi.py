import os
import sys
import environ
from waitress import serve
from django.core.wsgi import get_wsgi_application

# Get the project directory dynamically
project_home = os.path.dirname(os.path.abspath(__file__))  # Use the current script's path
if project_home not in sys.path:
    sys.path.append(project_home)

# Initialize environment variables
env = environ.Env()
env.read_env(os.path.join(project_home, 'nSpy/.env'))  # Using a cross-platform way to access .env

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nSpy.settings')

# Get the WSGI application
application = get_wsgi_application()

# Start the server using Waitress
if __name__ == "__main__":
    serve(application, host='0.0.0.0', port=8000)
