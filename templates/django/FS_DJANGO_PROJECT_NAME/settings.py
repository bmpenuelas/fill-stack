"""
Django settings for {{ FS_DJANGO_PROJECT_NAME }} project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

from kombu import Exchange, Queue


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['ENV_DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.environ['ENV_DJANGO_DEBUG'].lower() == 'true' else False

ALLOWED_HOSTS = ['0.0.0.0', '.{{ FS_DOMAIN }}']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    {% if render_features['django-socialauth'] %}
    'oauth2_provider',
    'social_django',
    'rest_framework_social_oauth2',
    {% endif %}

    '{{ FS_DJANGO_APP_NAME }}.apps.{{ FS_DJANGO_APP_NAME_CONFIG }}',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '{{ FS_DJANGO_PROJECT_NAME }}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                {% if render_features['django-socialauth'] %}
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                {% endif %}
            ],
        },
    },
]

WSGI_APPLICATION = '{{ FS_DJANGO_PROJECT_NAME }}.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        {% if render_features['django-postgresql'] %}
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['ENV_POSTGRES_DB_NAME'],
            'USER': os.environ['ENV_POSTGRES_DB_USER'],
            'PASSWORD': os.environ['ENV_POSTGRES_DB_PASSWORD'],
            'HOST': 'postgres',
            'PORT': 5432,
        {% endif %}
    },
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# REST framework

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        {% if render_features['django-jwt'] %}
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        {% endif %}
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        {% if render_features['django-socialauth'] %}
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
        {% endif %}
    ),
}

AUTHENTICATION_BACKENDS = (
    {% if render_features['django-socialauth'] %}
    # Facebook
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',

    'rest_framework_social_oauth2.backends.DjangoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    {% endif %}
)

{% if render_features['django-socialauth'] %}
# Social Auth

DRFSO2_URL_NAMESPACE = 'django-socialauth'

# Social Auth providers

# Facebook
SOCIAL_AUTH_FACEBOOK_KEY = '{{ FS_DJANGO_SOCIALAUTH_FACEBOOK_APP_ID }}'
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ['ENV_DJANGO_SOCIALAUTH_FACEBOOK_APP_SECRET']
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}
{% endif %}

{% if render_features['django-jwt'] %}
# JWT authentication

JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True,
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}
{% endif %}


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = '/django/static/'
STATIC_URL = '/{{ FS_API_PATH }}/django/static/'


{% if render_features['django-redis-rabbit'] %}
# Redis
# https://redis.io/

REDIS_PORT = {{ FS_REDIS_PORT }}
REDIS_DB = 0
REDIS_HOST = 'redis'

RABBIT_HOSTNAME = 'rabbit'

if RABBIT_HOSTNAME.startswith('tcp://'):
    RABBIT_HOSTNAME = RABBIT_HOSTNAME.split('//')[1]

BROKER_URL = os.environ.get('BROKER_URL', '')
if not BROKER_URL:
    BROKER_URL = 'amqp://{user}:{password}@{hostname}/{vhost}/'.format(
        user=os.environ['ENV_RABBIT_USER'],
        password=os.environ['ENV_RABBIT_PASSWORD'],
        hostname=RABBIT_HOSTNAME,
        vhost='')

# Negotiate using heartbeats, so as not to have dead connections stored on rabbitmq
BROKER_HEARTBEAT = '?heartbeat=30'
if not BROKER_URL.endswith(BROKER_HEARTBEAT):
    BROKER_URL += BROKER_HEARTBEAT

BROKER_POOL_LIMIT = 1
BROKER_CONNECTION_TIMEOUT = 15
{% endif %}


{% if render_features['django-celery'] %}
# Celery configuration
# http://docs.celeryproject.org/en/3.1/configuration.html

CELERY_DEFAULT_QUEUE = 'default'
CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
)

# Sensible settings for celery
CELERY_ALWAYS_EAGER = False
CELERY_ACKS_LATE = True
CELERY_TASK_PUBLISH_RETRY = True
CELERY_DISABLE_RATE_LIMITS = False

# By default we will ignore result
# If you want to see results and try out tasks interactively, change it to False
# Or change this setting on tasks level
CELERY_IGNORE_RESULT = True
CELERY_SEND_TASK_ERROR_EMAILS = False
CELERY_TASK_RESULT_EXPIRES = 600

# Set redis as celery result backend
CELERY_RESULT_BACKEND = 'redis://%s:%d/%d' % (REDIS_HOST, REDIS_PORT, REDIS_DB)
CELERY_REDIS_MAX_CONNECTIONS = 1

CELERY_TASK_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ['application/json']

CELERYD_HIJACK_ROOT_LOGGER = False
CELERYD_PREFETCH_MULTIPLIER = 1
CELERYD_MAX_TASKS_PER_CHILD = 1000
{% endif %}