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


DEBUG = config('DEBUG', cast=bool)

USE_AWS = True

ADMINS = [('Peter B', 'server-admin@eportalproject.ml'),]

ALLOWED_HOSTS = config('HEROKU_HOSTS', cast=Csv())

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

# REDIS CONFIG
REDIS_URL = config('REDIS_URL', 'redis://127.0.0.1:6379')
BROKER_CONNECTION_MAX_RETRIES = config('BROKER_CONNECTION_MAX_RETRIES', None)
BROKER_POOL_LIMIT = config('BROKER_POOL_LIMIT', None)

# CELERY CONFIG
CELERY_BROKER_URL = config('CELERY_BROKER_URL', REDIS_URL)
CELERY_RESULT_BACKEND = config('CELERY_RESULT_BACKEND', REDIS_URL)
CELERY_REDIS_MAX_CONNECTIONS = config('CELERY_REDIS_MAX_CONNECTIONS', 5)
CELERYD_CONCURRENCY = config('CELERYD_CONCURRENCY', 1)

# Activate Django-Heroku.
django_heroku.settings(locals())