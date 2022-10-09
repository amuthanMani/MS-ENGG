import os
from .common import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']


ALLOWED_HOSTS = ['127.0.0.1', 'fathomless-spire-24787.herokuapp.com']
