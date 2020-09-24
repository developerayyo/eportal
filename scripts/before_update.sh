#!/bin/bash

#####################################################################
# Author: Peter Babalola
# Version: 0.0
# Date: 2020-09-12
# Description: script to stop the server before updating the codebase
# Usage: ./before_update.sh
#####################################################################

command supervisorctl stop all
command service nginx stop


