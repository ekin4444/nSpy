import os
import sys
import environ
from waitress import serve
from django.core.wsgi import get_wsgi_application

# Change this to your project path
project_home = 'C:\\Users\\ekinf\\PycharmProjects\\nSpy'  # Windows path
if project_home not in sys.path:
    sys.path.append(project_home)

# Initialize environment variables
env = environ.Env()
environ.Env.read_env('C:\\Users\\ekinf\\PycharmProjects\\nSpy\\.env')  # Windows path to .env file

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nSpy.settings')

application = get_wsgi_application()

# Start the server using Waitress
if __name__ == "__main__":
    serve(application, host='0.0.0.0', port=8000)
