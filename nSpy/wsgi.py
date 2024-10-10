import os
import sys

# Add your project directory to the sys.path
sys.path.append('/home/ekin4/nSpy')  # Update 'yourusername' with your actual PythonAnywhere username

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'nSpy.settings')  # Update this if your settings file is named differently

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
