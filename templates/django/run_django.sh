#!/bin/sh

{% if render_features['django-postgresql'] %}
# wait for PostgresSQL server to start
sleep 5
{% endif %}

cd /django
# prepare init migration
su -m {{ FS_DOCKER_USERNAME }} -c "python3 ./manage.py makemigrations {{ FS_DJANGO_APP_NAME }}"
# migrate db, so we have the latest db schema
su -m {{ FS_DOCKER_USERNAME }} -c "python3 ./manage.py migrate"
# generate static files
python3 ./manage.py collectstatic --no-input
# create django admin
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('$ENV_DJANGO_ADMIN_USER', '$ENV_DJANGO_ADMIN_EMAIL', '$ENV_DJANGO_ADMIN_PASSWORD')" | python3 manage.py shell
{% if render_features['django-socialauth'] %}
python3 ./manage.py createapp -ci $ENV_DJANGO_SOCIALAUTH_CLIENT_ID -cs $ENV_DJANGO_SOCIALAUTH_CLIENT_SECRET
{% endif %}
{% if render_features['django-gunicorn'] %}
# start development server on public ip interface, on port 8000
su -m {{ FS_DOCKER_USERNAME }} -c "gunicorn {{ FS_DJANGO_PROJECT_NAME }}.wsgi:application --bind 0.0.0.0:8000"
{% endif %}
