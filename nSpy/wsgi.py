import os
import sys
import environ

project_home = '/home/ekin4/nSpy'  # Change this to your project path
if project_home not in sys.path:
    sys.path.append(project_home)

from django.core.wsgi import get_wsgi_application

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()  # Reads the .env file

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nSpy.settings')

application = get_wsgi_application()
