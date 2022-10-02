from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-k4+jlzp$w87j39_g)t(0l@k%^t401b!snuxlk%s=)ztl3lrsna'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
