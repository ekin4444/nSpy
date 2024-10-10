import os
import tempfile

import environ
from pathlib import Path

from virtualenv.activation.python import activate_this

env = environ.Env()
environ.Env.read_env()

tempfile.tempdir = '/tmp'
BASE_DIR = Path(
    __file__).resolve().parent.parentactivate_this = '/home/ekin4/.venv/Scripts/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))


# Quick-start development settings - unsuitable for production
DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'ekin4.pythonanywhere.com']
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'machine_learning',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'nSpy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'nSpy.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Istanbul'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Change STATIC_ROOT to ensure it doesn't conflict with STATICFILES_DIRS
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Collect static files here

# Update the STATICFILES_DIRS
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Your static files for development
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "ekinfilizatass@gmail.com"
EMAIL_HOST_PASSWORD = "zznm fcmc glwk qxps"  # Make sure to handle sensitive data properly
EMAIL_USE_TLS = True

# Stripe keys
STRIPE_PUBLIC_KEY = 'your-public-key'
STRIPE_SECRET_KEY = 'your-secret-key'
print(ALLOWED_HOSTS)
