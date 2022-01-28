from .base import *

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID_BUCKET') 
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY_BUCKET')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN='%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {    
     'CacheControl': 'max-age=86400',
}
AWS_DEFAULT_ACL = 'None'

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

# s3 static settings
STATIC_LOCATION = 'static'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
STATICFILES_STORAGE = 'eportal.storage_backends.StaticStorage'
# s3 public media settings
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = 'eportal.storage_backends.PublicMediaStorage'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'


SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
