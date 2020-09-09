from . base import *
# Use the following live settings to build on Travis CI
SECRET_KEY = config("SECRET_KEY")
DEBUG = False
TEMPLATE_DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'travis_ci_db',
        'USER': 'travis',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
    }
}
