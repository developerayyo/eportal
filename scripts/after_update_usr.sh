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
command sudo ./manage.py makemigrations
command sudo ./manage.py migrate
command sudo ./manage.py loaddata dbback3.json
command sudo ./manage.py collectstatic
