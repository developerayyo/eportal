from .base import *

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn=config('dsn'),
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)


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