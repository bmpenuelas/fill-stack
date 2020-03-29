# AVAILABLE_FEATURES
# Features that can be selected by the user to be included
# Set dependencies with the 'force_if' field.

available_features = {
    # django
    'django':{
        'force_if': [],
    },
    'django-gunicorn':{
        'force_if': ['django'],
    },
    'django-postgresql':{
        'force_if': [],
    },
    'django-jwt':{
        'force_if': [],
    },
    'django-socialauth':{
        'force_if': [],
    },
    'django-celery':{
        'force_if': [],
    },
    'django-redis-rabbit':{
        'force_if': [
            ['django-celery']
        ],
    },

    # postgresql
    'postgresql': {
        'force_if': [
            ['django-postgresql'],
        ],
    },

    # celery
    'celery': {
        'force_if': [
            ['django-celery'],
        ],
    },

    # redis, rabbitmq
    'redis-rabbit': {
        'force_if': [
            ['django-redis-rabbit'],
        ],
    },

    # mongodb
    'mongodb': {
        'force_if': [
            [],
        ],
    },
    'mongo-express': {
        'force_if': [
            [],
        ],
    },

    # nginx
    'nginx': {
        'force_if': [
            [],
        ],
    },

    # https-portal
    'https-portal': {
        'force_if': [
            [],
        ],
    },

    # dev-hosts
    'dev-hosts': {
        'force_if': [
            [],
        ],
    },

    # noip
    'noip': {
        'force_if': [
            [],
        ],
    },

    # vue
    'vue': {
        'force_if': [
            [],
        ],
    },
    'vue-socialauth': {
        'force_if': [
            [],
        ],
    },

    # aws
    'aws-docker-machine': {
        'force_if': [
            [],
        ],
    },
}


# CONFIG_FEATURE_KEYWORDS
# Keywords provided by the user for the selected features,
# these are replaced in the templates.
#   'features': Features that require this keyword to be set.
#   'environment': Is it an environment variable.
#   'secret': To be set only offline.
#   'name': Name in natural language, to be shown to the user.
#   'description': Short description.
#   'default': Default value.
#   'sanitize': A regex describing a valid value for the keyword.

config_feature_keywords = {
    # common
    'FS_PRODUCT_NAME': {
        'features': [
            ['common'],
        ],
        'environment': False,
        'secret': False,
        'name': 'Product name',
        'description': 'The name for your app or product.',
        'default': 'mywebapp',
        'sanitize': r'^\w+$',
    },
    'FS_DOMAIN': {
        'features': [
            ['common'],
        ],
        'environment': False,
        'secret': False,
        'name': 'Main domain name',
        'description': 'The domain of your webapp (your-name.com).',
        'default': 'mywebapp.com',
        'sanitize': r'^(((?!-))(xn--|_{1,1})?[a-z0-9-]{0,61}[a-z0-9]{1,1}\.)*(xn--)?([a-z0-9][a-z0-9\-]{0,60}|[a-z0-9-]{1,30}\.[a-z]{2,})$',
    },
    'FS_DOCKER_USERNAME': {
        'features': [
            ['common'],
        ],
        'environment': False,
        'secret': False,
        'name': 'Docker username.',
        'description': 'Username to run the docker commands.',
        'default': 'dockeruser',
        'sanitize': r'^[a-z][-a-z0-9_]*$',
    },


    # django
    'FS_ENV_DJANGO_DEBUG': {
        'features': [
            ['django'],
        ],
        'environment': True,
        'secret': False,
        'name': 'Django debug mode.',
        'description': 'Set to put Django in DEBUG mode. DO NOT SET IN PRODUCTION!',
        'default': 'True',
        'sanitize': r'(True|true|False|false)$',
    },
    'FS_ENV_DJANGO_SECRET_KEY': {
        'features': [
            ['django'],
        ],
        'environment': True,
        'secret': True,
        'name': 'Django secret key.',
        'description': 'Secret key for Django production. KEEP SECRET!',
        'default': 'CHANGE_ME!!!',
        'sanitize': r'^.+$',
    },
    'FS_ENV_DJANGO_ADMIN_USER': {
        'features': [
            ['django'],
        ],
        'environment': True,
        'secret': True,
        'name': 'Admin username',
        'description': 'Django superuser (admin) username.',
        'default': 'djangoadmin',
        'sanitize': r'^.+$',
    },
    'FS_ENV_DJANGO_ADMIN_EMAIL': {
        'features': [
            ['django'],
        ],
        'environment': True,
        'secret': True,
        'name': 'Admin email',
        'description': 'Django superuser (admin) email.',
        'default': 'my@email.com',
        'sanitize': r'^.+$',
    },
    'FS_ENV_DJANGO_ADMIN_PASSWORD': {
        'features': [
            ['django'],
        ],
        'environment': True,
        'secret': True,
        'name': 'Admin password',
        'description': 'Django superuser (admin) password.',
        'default': 'CHANGE_ME!!!',
        'sanitize': r'^.+$',
    },
    'FS_DJANGO_PROJECT_NAME': {
        'features': [
            ['django'],
        ],
        'environment': False,
        'secret': False,
        'name': 'Django project name',
        'description': 'Name of your Django project.',
        'default': 'myproject',
        'sanitize': r'^\w+$',
    },
    'FS_DJANGO_APP_NAME': {
        'features': [
            ['django'],
        ],
        'environment': False,
        'secret': False,
        'name': 'Django app name',
        'description': 'Name of your Django app.',
        'default': 'myapp',
        'sanitize': r'^\w+$',
    },


    # django-socialauth
    'FS_ENV_DJANGO_SOCIALAUTH_CLIENT_ID': {
        'features': [
            ['django-socialauth'],
        ],
        'environment': True,
        'secret': True,
        'name': 'Client ID',
        'description': 'Social Authentication chosen client_id.',
        'default': 'CLIENT_ID',
        'sanitize': r'^.+$',
    },
    'FS_ENV_DJANGO_SOCIALAUTH_CLIENT_SECRET': {
        'features': [
            ['django-socialauth'],
        ],
        'environment': True,
        'secret': True,
        'name': 'Client Secret',
        'description': 'Social Authentication chosen client_secret.',
        'default': 'CHANGE_ME!!!',
        'sanitize': r'^.+$',
    },
    'FS_DJANGO_SOCIALAUTH_FACEBOOK_APP_ID': {
        'features': [
            ['django-socialauth'],
        ],
        'environment': False,
        'secret': False,
        'name': 'App ID',
        'description': 'Facebook App ID - Get one at developers.facebook.com/apps/ or add any number now and replace it with the real one later.',
        'default': 'FB_APP_ID',
        'sanitize': r'^\d+$',
    },
    'FS_ENV_DJANGO_SOCIALAUTH_FACEBOOK_APP_SECRET': {
        'features': [
            ['django-socialauth'],
        ],
        'environment': True,
        'secret': True,
        'name': 'App Secret',
        'description': 'Social Authentication - Facebook App Secret.',
        'default': 'FB_APP_SECRET',
        'sanitize': r'^.+$',
    },


    # postgresql
    'FS_ENV_POSTGRES_DB_NAME': {
        'features': [
            ['postgresql'],
        ],
        'environment': True,
        'secret': True,
        'name': 'DB Name',
        'description': 'Postgresql database name.',
        'default': 'postgresdb',
        'sanitize': r'^\w+$',
    },
    'FS_ENV_POSTGRES_DB_USER': {
        'features': [
            ['postgresql'],
        ],
        'environment': True,
        'secret': True,
        'name': 'DB User',
        'description': 'Postgresql database user.',
        'default': 'postgresuser',
        'sanitize': r'^\w+$',
    },
    'FS_ENV_POSTGRES_DB_PASSWORD': {
        'features': [
            ['postgresql'],
        ],
        'environment': True,
        'secret': True,
        'name': 'DB Password',
        'description': 'Postgresql database password.',
        'default': 'CHANGE_ME!!!',
        'sanitize': r'^.+$',
    },


    # redis-rabbit
    'FS_ENV_RABBIT_USER': {
        'features': [
            ['redis-rabbit'],
        ],
        'environment': True,
        'secret': True,
        'name': 'Admin username.',
        'description': 'Rabbit Admin user.',
        'default': 'rabbituser',
        'sanitize': r'^\w+$',
    },
    'FS_ENV_RABBIT_PASSWORD': {
        'features': [
            ['redis-rabbit'],
        ],
        'environment': True,
        'secret': True,
        'name': 'Admin password.',
        'description': 'Rabbit Admin password.',
        'default': 'CHANGE_ME!!!',
        'sanitize': r'^.+$',
    },
    'FS_REDIS_PORT': {
        'features': [
            ['redis-rabbit'],
        ],
        'environment': False,
        'secret': False,
        'name': 'Port for Redis.',
        'description': 'Redis port number.',
        'default': '6379',
        'sanitize': r'^\d+$',
    },


    # mongodb
    'FS_ENV_MONGO_ROOT_USERNAME': {
        'features': [
            ['mongodb'],
        ],
        'environment': True,
        'secret': True,
        'name': 'mongodb root username.',
        'description': 'MongoDB root user.',
        'default': 'mongouser',
        'sanitize': r'^\w+$',
    },
    'FS_ENV_MONGO_ROOT_PASSWORD': {
        'features': [
            ['mongodb'],
        ],
        'environment': True,
        'secret': True,
        'name': 'mongodb root password.',
        'description': 'MongoDB root password.',
        'default': 'CHANGE_ME!!!',
        'sanitize': r'^.+$',
    },
    'FS_ENV_MONGO_DATABASE_NAME': {
        'features': [
            ['mongodb'],
        ],
        'environment': True,
        'secret': True,
        'name': 'MongoDB database name.',
        'description': 'Create a mongodb database with this name.',
        'default': 'mongodb',
        'sanitize': r'^\w+$',
    },
    'FS_MONGO_EXAMPLE_COLLECTION': {
        'features': [
            ['mongodb'],
        ],
        'environment': False,
        'secret': False,
        'name': 'MongoDB example collection.',
        'description': 'Create a collection in the mongodb database.',
        'default': 'mycollection',
        'sanitize': r'^\w+$',
    },
    'FS_MONGO_EXAMPLE_FIELD': {
        'features': [
            ['mongodb'],
        ],
        'environment': False,
        'secret': False,
        'name': 'MongoDB example field.',
        'description': 'Create a field in the mongodb example collection.',
        'default': 'myfield',
        'sanitize': r'^\w+$',
    },
    'FS_MONGO_EXAMPLE_VALUE': {
        'features': [
            ['mongodb'],
        ],
        'environment': False,
        'secret': False,
        'name': 'MongoDB example value.',
        'description': 'Value of the mongodb example field.',
        'default': 'myvalue',
        'sanitize': r'^\w+$',
    },


    # mongo-express
    'FS_ENV_MONGO_EXPRESS_USERNAME': {
        'features': [
            ['mongo-express'],
        ],
        'environment': True,
        'secret': True,
        'name': 'Mongo-express admin panel username.',
        'description': 'Mongo-express admin panel user.',
        'default': 'mongoexpressuser',
        'sanitize': r'^\w+$',
    },
    'FS_ENV_MONGO_EXPRESS_PASSWORD': {
        'features': [
            ['mongo-express'],
        ],
        'environment': True,
        'secret': True,
        'name': 'Mongo-express admin panel password.',
        'description': 'Mongo-express admin panel password.',
        'default': 'CHANGE_ME!!!',
        'sanitize': r'^.+$',
    },


    # vue
    'FS_VUE_PROJECT_NAME': {
        'features': [
            ['vue'],
        ],
        'environment': False,
        'secret': False,
        'name': 'Vue project name.',
        'description': 'Name for the Vue.js frontend project.',
        'default': 'mywebapp',
        'sanitize': r'^\w+$',
    },


    # nginx
    'FS_API_PATH': {
        'features': [
            ['nginx'],
        ],
        'environment': False,
        'secret': False,
        'name': 'API path',
        'description': 'Path to the API (my_api would make your API available in mydomain.com/my_api/',
        'default': 'api',
        'sanitize': r'^\w+$',
    },


    # https-portal
    'FS_ENV_HTTPS_PORTAL_STAGE': {
        'features': [
            ['https-portal'],
        ],
        'environment': True,
        'secret': False,
        'name': 'https certificates stage',
        'description': 'Use real, staging or self-signed SSL/TLS certificates (to avoid rate-limit).',
        'choices': ['local', 'staging', 'production'],
        'default': 'local',
        'sanitize': r'^\w+$',
    },


    # noip
    'FS_ENV_NOIP_USER': {
        'features': [
            ['noip'],
        ],
        'environment': True,
        'secret': True,
        'name': 'No-IP User.',
        'description': 'Username of your noip.com account.',
        'default': 'myNoIPuser',
        'sanitize': r'^\w+$',
    },
    'FS_ENV_NOIP_PASSWORD': {
        'features': [
            ['noip'],
        ],
        'environment': True,
        'secret': True,
        'name': 'No-IP Password.',
        'description': 'Password of your noip.com account.',
        'default': 'CHANGE_ME!!!',
        'sanitize': r'^.+$',
    },
    'FS_ENV_NOIP_INTERVAL': {
        'features': [
            ['noip'],
        ],
        'environment': True,
        'secret': False,
        'name': 'No-IP Interval.',
        'description': 'Time between DDNS IP updates.',
        'default': '5m',
        'sanitize': r'^\w+$',
    },

}


# CONFIG_FEATURE_KEYWORDS_DERIVED
# Keywords derived from the user input.

config_feature_keywords_derived = {
    'FS_DJANGO_APP_NAME_CONFIG':
        lambda selected_keywords:
            (selected_keywords['FS_DJANGO_APP_NAME'][0].upper() \
            + selected_keywords['FS_DJANGO_APP_NAME'][1:].lower() \
            + 'Config'),
}
