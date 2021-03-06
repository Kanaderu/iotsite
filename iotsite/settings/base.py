from __future__ import print_function
from datetime import timedelta

import os
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)
eprint('PROJECT_DIR = {}'.format(PROJECT_DIR))
eprint('BASE_DIR = {}'.format(BASE_DIR))

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',   # geodjango

    'django_extensions',    # django extension utilities
    'webpack_loader',       # react webpack integration
    'rest_framework',       # rest framework library
    'thorn.django',         # webhooks library
    'django_filters',       # field filtering for REST
    'drf_extra_fields',     # drf add-ons
    'graphene_django',      # GraphQL support
    'rest_framework_simplejwt.token_blacklist', # JWT Blacklist
    'channels',             # channels

    'rest_framework_gis',
    'djgeojson',
    'leaflet',

    # custom apps
    'geo',
    'sensors',
    'dashboard',
    'users',
    'setup',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'iotsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'iotsite.wsgi.application'

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True

REST_FRAMEWORK = {
    'PAGE_SIZE': 50,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_csv.renderers.CSVRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework_csv.parsers.CSVParser'
    ],
    'DEFAULT_METADATA_CLASS': 'rest_framework.metadata.SimpleMetadata',

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),

    'ORDERING_PARAM': 'sort',

    #'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',
    #'DEFAULT_FILTER_BACKENDS': (
    #    'rest_framework_json_api.filters.QueryParameterValidationFilter',
    #    'rest_framework_json_api.filters.OrderingFilter',
    #    'rest_framework_json_api.django_filters.DjangoFilterBackend',
    #    'rest_framework.filters.SearchFilter',
    #),
    #'SEARCH_PARAM': 'filter[search]',
    #'TEST_REQUEST_RENDERER_CLASSES': (
    #    'rest_framework_json_api.renderers.JSONRenderer',
    #),
    #'TEST_REQUEST_DEFAULT_FORMAT': 'vnd.api+json'
}

THORN_HMAC_SIGNER = 'thorn.utils.hmac:sign'

STATIC_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# DarkSky API CONF
if 'DARKSKY_KEY' in os.environ and os.environ['DARKSKY_KEY']:
    DARKSKY_KEY = os.environ['DARKSKY_KEY']
else:
    eprint('DARKSKY_KEY Environment Variable is NOT set! Ignoring...')
    DARKSKY_KEY = None

DARKSKY_LAT = 39.758949
DARKSKY_LON = -84.191605
DARKSKY_THRESH = 96.0 # seconds before fetching new darksky data

# GeoDjango
GEOIP_PATH = os.path.join(BASE_DIR, 'utils', 'geodjango', 'geoip2', 'GeoLite2'),

# Leaflet
LEAFLET_CONFIG = {
}

# Accounts
AUTH_USER_MODEL = 'users.Account'


LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'

# GraphQL
GRAPHENE = {
    'SCHEMA': 'iotsite.schema.schema'
}

# JSON Web Tokens
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',
                           'rest_framework_simplejwt.tokens.SlidingToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(days=365),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=365 * 2),
}

# Channels
REDIS_HOST = os.environ['REDIS_HOST'] if 'REDIS_HOST' in os.environ and os.environ['REDIS_HOST'] else 'localhost'
ASGI_APPLICATION = 'iotsite.routing.application'
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(REDIS_HOST, 6379)],
        },
    },
}
