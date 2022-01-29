from .base import *
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SERVER_EMAIL = "localhost@eportalproject.ml"

# local static settings 
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# local media settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

import django_heroku
django_heroku.settings(locals())
