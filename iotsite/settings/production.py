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

