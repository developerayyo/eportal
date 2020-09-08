from .base import *

DEBUG = False
ADMINS = [('Peter B', 'server-admin@eportalproject.ml'),]

ALLOWED_HOSTS = ['*']

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': 'eportal',
         'USER': 'postgres',
         'PASSWORD': config('PASSWORD'),
         'HOST': config('HOST'),
         'PORT': config('PORT'),
     }
 }

SERVER_EMAIL = "server@eportalproject.ml"

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True