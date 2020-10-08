#!/bin/bash

###########################################################
# Author: Peter Babalola
# Version: 0.0
# Date: 2020-09-12
# Description: script to clean my project dir on the server
# Usage: ./pre_update.sh
###########################################################

command mv /home/ubuntu/eportal/env /home/ubuntu/temps/env
command mv /home/ubuntu/eportal/.env /home/ubuntu/temps/.env
command mv /home/ubuntu/eportal/media /home/ubuntu/temps/media
command rm -rf -v /home/ubuntu/eportal/*
command rm -rf -v /home/ubuntu/eportal/.*
command mv /home/ubuntu/temps/env /home/ubuntu/eportal/env
command mv /home/ubuntu/temps/.env /home/ubuntu/eportal/.env
command mv /home/ubuntu/temps/media /home/ubuntu/eportal/media
command echo "done"