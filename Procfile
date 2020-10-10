release: python manage.py migrate
web: gunicorn eportal.wsgi --log-file -
worker: celery worker -A eportal -l info