from .base import *
import os


DEBUG = False
ALLOWED_HOSTS = ['www.ud-iot.ml','ud-iot.ml']
SECRET_KEY = os.environ['SECRET_KEY']
