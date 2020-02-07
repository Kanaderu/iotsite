from .base import *

DEBUG = True
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', '10.0.2.2']
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '65=fldls_qvn(tvd3a@3&b=_#@s_bz1&55))2zjw@&-8whjdz&'

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
         'NAME': 'geodjango',
         'USER': 'geo',
         'PASSWORD': 'geo',
         'HOST': 'postgis',
         'PORT': '5432',
    }
}

# setup sql explorer
INSTALLED_APPS += [
    'explorer',
]
EXPLORER_CONNECTIONS = { 'Default': 'default' }
EXPLORER_DEFAULT_CONNECTION = 'default'

# Simple JWT Signing Key
SIMPLE_JWT['SIGNING_KEY'] = SECRET_KEY
