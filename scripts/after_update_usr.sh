#!/bin/bash

command /home/ubuntu/eportal/env/bin/activate
command pip install -r /home/ubuntu/eportal/requirements.txt
command python manage.py makemigrations --settings=eportal.settings.pro
command python manage.py migrate --settings=eportal.settings.pro