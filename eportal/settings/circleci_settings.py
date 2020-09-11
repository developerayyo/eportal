from . base import *
# Use the following live settings to build on Travis CI
SECRET_KEY = config("SECRET_KEY")
DEBUG = False
TEMPLATE_DEBUG = True
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
