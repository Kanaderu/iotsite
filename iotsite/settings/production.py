from .base import *
import os

DEBUG = False
ALLOWED_HOSTS = ['www.udsensors.tk', 'udsensors.tk']
SECRET_KEY = os.environ['SECRET_KEY']

# define webpack
# https://github.com/owais/django-webpack-loader
WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'dashboard/static/', # must end with '/'
        'STATS_FILE': os.path.join(BASE_DIR, 'dashboard', 'webpack-stats.json'),
    }
}

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
         'ENGINE': 'django.contrib.gis.db.backends.postgis',
         'NAME': os.environ['POSTGRES_NAME'],
         'USER': os.environ['POSTGRES_USER'],
         'PASSWORD': os.environ['POSTGRES_PASSWORD'],
         'HOST': os.environ['POSTGRES_HOST'],
         'PORT': os.environ['POSTGRES_PORT'],
    }
}
