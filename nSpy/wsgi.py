import os
import environ

from django.core.wsgi import get_wsgi_application

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()  # Reads the .env file

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nSpy.settings')

application = get_wsgi_application()
