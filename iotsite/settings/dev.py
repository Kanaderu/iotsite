from .base import *

DEBUG = True
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1']
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '65=fldls_qvn(tvd3a@3&b=_#@s_bz1&55))2zjw@&-8whjdz&'

# define webpack
# https://github.com/owais/django-webpack-loader
WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'dist/', # must end with '/'
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
    }
}

