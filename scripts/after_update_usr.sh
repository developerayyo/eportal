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
command chmod +x manage.py --settings=eportal.settings.pro
command ./manage.py makemigrations --settings=eportal.settings.pro
command ./manage.py migrate --settings=eportal.settings.pro
# command ./manage.py loaddata dbback3.json --settings=eportal.settings.pro
command ./manage.py collectstatic --settings=eportal.settings.pro
