#!/bin/sh

# wait for RabbitMQ server to start
sleep 10

# run Celery worker for our project with Celery configuration stored in Celeryconf
cd /django
su -m {{ FS_DOCKER_USERNAME }} -c "celery worker -A {{ FS_DJANGO_PROJECT_NAME }}.celeryconf -Q default -n default@%h"
