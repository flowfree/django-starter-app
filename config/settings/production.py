import os
from .base import *

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = [os.getenv('BACKEND_HOSTNAME')]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD')
    }
}

# Disable DRF's browsable API
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

CORS_ALLOWED_ORIGINS = [
    'http://' + os.getenv('FRONTEND_HOSTNAME'),
    'https://' + os.getenv('FRONTEND_HOSTNAME'),
]

