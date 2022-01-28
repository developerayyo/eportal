#!/bin/bash

###################################################################
# Author: Peter Babalola
# Version: 0.0
# Date: 2020-09-12
# Description: script to restart the server after successful update
# Usage: ./after_updade_root.sh
###################################################################

command supervisorctl restart all
command service nginx restart