#!/bin/bash

############################################################################
# Author: Peter Babalola
# Version: 0.0
# Date: 2020-09-12
# Description: script to run necessace commands after codebase update server
# Usage: ./after_update_usr.sh
############################################################################

command source /home/ubuntu/eportal/env/bin/activate
command pip3 install -r /home/ubuntu/eportal/requirements.txt
command cd /home/ubuntu/eportal
command export DJANGO_SETTIINGS_MODULE=eportal.settings.pro
command python3 manage.py makemigrations
command python3 manage.py migrate
command python3 manage.py collectstatic