#!/bin/bash

command /home/ubuntu/eportal/env/bin/activate
command pip3 install -r /home/ubuntu/eportal/requirements.txt
command cd eportal
command python3 manage.py makemigrations --settings=eportal.settings.pro
command python3 manage.py migrate --settings=eportal.settings.pro