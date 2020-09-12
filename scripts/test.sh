#!/bin/bash

# command service supervisorctl stop all
mv /home/ayo/Repos/eportal/config /home/ayo/Repos/config
mv /home/ayo/Repos/eportal/.git /home/ayo/Repos/.git
mv /home/ayo/Repos/eportal/.env /home/ayo/Repos/.env
rm -rf /home/ayo/Repos/eportal/*
rm -rf /home/ayo/Repos/eportal/.*
mv /home/ayo/Repos/config /home/ayo/Repos/eportal/config
mv /home/ayo/Repos/.env /home/ayo/Repos/eportal/.env
mv /home/ayo/Repos/.git /home/ayo/Repos/eportal/.git
echo "done"