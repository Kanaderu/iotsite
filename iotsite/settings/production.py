from .base import *
import os

DEBUG = False
ALLOWED_HOSTS = ['www.udsensors.tk', 'udsensors.tk']
SECRET_KEY = os.environ['SECRET_KEY']
