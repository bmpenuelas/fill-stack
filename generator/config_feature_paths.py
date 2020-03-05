# CONFIG_FEATURE_PATHS
# Define needed directories and files for each feature to include.
# Directories are identified by ending with "/".
#   'features': List of features that require this file.
#   'binary': Is it a binary objet (False for source code).
#   'template': How to rename the file for the generated project.

config_feature_paths = {
    # common
    'docker-compose.yml': {
        'features': [
            ['common'],
        ],
        'binary': False,
        'template': r'docker-compose.yml',
    },
    '.env': {
        'features': [
            ['common'],
        ],
        'binary': False,
        'template': r'.env',
    },
    'README.md': {
        'features': [
            ['common'],
        ],
        'binary': False,
        'template': r'README.md',
    },
    '.dockerignore': {
        'features': [
            ['common'],
        ],
        'binary': False,
        'template': r'.dockerignore',
    },
    '.gitignore': {
        'features': [
            ['common'],
        ],
        'binary': False,
        'template': r'.gitignore',
    },

    # django
    'django/': {
        'features': [
            ['django'],
        ],
        'binary': False,
        'template': r'django/',
    },
    'django/requirements.txt': {
        'features': [
            ['django'],
        ],
        'binary': False,
        'template': r'django/requirements.txt',
    },
    'django/Dockerfile': {
        'features': [
            ['django'],
        ],
        'binary': False,
        'template': r'django/Dockerfile',
    },
    'django/manage.py': {
        'features': [
            ['django'],
        ],
        'binary': False,
        'template': r'django/manage.py',
    },
    'django/FS_DJANGO_PROJECT_NAME/': {
        'features': [
            ['django'],
        ],
        'binary': False,
        'template': r'django/{{ FS_DJANGO_PROJECT_NAME }}/',
    },
    'django/FS_DJANGO_PROJECT_NAME/__init__.py': {
        'features': [
            ['django'],
        ],
        'binary': False,
        'template': r'django/{{ FS_DJANGO_PROJECT_NAME }}/__init__.py',
    },
    'django/FS_DJANGO_PROJECT_NAME/settings.py': {
        'features': [
            ['django'],
        ],
        'binary': False,
        'template': r'django/{{ FS_DJANGO_PROJECT_NAME }}/settings.py',
    },
    'django/FS_DJANGO_PROJECT_NAME/urls.py': {
        'features': [
            ['django'],
        ],
        'binary': False,
        'template': r'django/{{ FS_DJANGO_PROJECT_NAME }}/urls.py',
    },
    'django/FS_DJANGO_PROJECT_NAME/wsgi.py': {
        'features': [
            ['django'],
        ],
        'binary': False,
        'template': r'django/{{ FS_DJANGO_PROJECT_NAME }}/wsgi.py',
    },
    'django/FS_DJANGO_APP_NAME/': {
        'features': [
            ['django'],
        ],
        'binary': False,
        'template': r'django/{{ FS_DJANGO_APP_NAME }}/',
    },
    'django/FS_DJANGO_APP_NAME/__init__.py': {
        'features': [
            ['django'],
        ],
        'binary': False,
        'template': r'django/{{ FS_DJANGO_APP_NAME }}/__init__.py',
    },
    'django/FS_DJANGO_APP_NAME/admin.py': {
        'features': [
            ['django'],
        ],
        'binary': False,
        'template': r'django/{{ FS_DJANGO_APP_NAME }}/admin.py',
    },
    'django/FS_DJANGO_APP_NAME/apps.py': {
        'features': [
            ['django'],
        ],
        'binary': False,
        'template': r'django/{{ FS_DJANGO_APP_NAME }}/apps.py',
    },
    'django/FS_DJANGO_APP_NAME/models.py': {
        'features': [
            ['django'],
        ],
        'binary': False,
        'template': r'django/{{ FS_DJANGO_APP_NAME }}/models.py',
    },
    'django/FS_DJANGO_APP_NAME/tests.py': {
        'features': [
            ['django'],
        ],
        'binary': False,
        'template': r'django/{{ FS_DJANGO_APP_NAME }}/tests.py',
    },
    'django/FS_DJANGO_APP_NAME/urls.py': {
        'features': [
            ['django'],
        ],
        'binary': False,
        'template': r'django/{{ FS_DJANGO_APP_NAME }}/urls.py',
    },
    'django/FS_DJANGO_APP_NAME/views.py': {
        'features': [
            ['django'],
        ],
        'binary': False,
        'template': r'django/{{ FS_DJANGO_APP_NAME }}/views.py',
    },
    'django/FS_DJANGO_APP_NAME/migrations/': {
        'features': [
            ['django'],
        ],
        'binary': False,
        'template': r'django/{{ FS_DJANGO_APP_NAME }}/migrations/',
    },
    'django/FS_DJANGO_APP_NAME/migrations/__init__.py': {
        'features': [
            ['django'],
        ],
        'binary': False,
        'template': r'django/{{ FS_DJANGO_APP_NAME }}/migrations/__init__.py',
    },
    'django/run_django.sh': {
        'features': [
            ['django'],
        ],
        'binary': False,
        'template': r'django/run_django.sh',
    },

    # django-celery
    'django/FS_DJANGO_PROJECT_NAME/celeryconf.py': {
        'features': [
            ['django-celery'],
        ],
        'binary': False,
        'template': r'django/{{ FS_DJANGO_PROJECT_NAME }}/celeryconf.py',
    },
    'django/FS_DJANGO_PROJECT_NAME/tasks.py': {
        'features': [
            ['django-celery'],
        ],
        'binary': False,
        'template': r'django/{{ FS_DJANGO_PROJECT_NAME }}/tasks.py',
    },
    'django/run_celery.sh': {
        'features': [
            ['django-celery'],
        ],
        'binary': False,
        'template': r'django/run_celery.sh',
    },

    # mongodb
    'mongo/': {
        'features': [
            ['mongodb'],
        ],
        'binary': False,
        'template': r'mongo/',
    },
    'mongo/Dockerfile': {
        'features': [
            ['mongodb'],
        ],
        'binary': False,
        'template': r'mongo/Dockerfile',
    },
    'mongo/init.js': {
        'features': [
            ['mongodb'],
        ],
        'binary': False,
        'template': r'mongo/init.js',
    },

    # nginx
    'nginx/': {
        'features': [
            ['nginx'],
        ],
        'binary': False,
        'template': r'nginx/',
    },
    'nginx/Dockerfile': {
        'features': [
            ['nginx'],
        ],
        'binary': False,
        'template': r'nginx/Dockerfile',
    },
    'nginx/nginx.conf': {
        'features': [
            ['nginx'],
        ],
        'binary': False,
        'template': r'nginx/nginx.conf',
    },
    'nginx/sites-enabled/': {
        'features': [
            ['nginx'],
        ],
        'binary': False,
        'template': r'nginx/sites-enabled/',
    },
    'nginx/sites-enabled/FS_DOMAIN': {
        'features': [
            ['nginx'],
        ],
        'binary': False,
        'template': r'nginx/sites-enabled/{{ FS_DOMAIN }}',
    },

    # dev
    'dev/': {
        'features': [
            ['dev-hosts'],
        ],
        'binary': False,
        'template': r'dev/',
    },
    'dev/set_dev_hosts.py': {
        'features': [
            ['dev-hosts'],
        ],
        'binary': False,
        'template': r'dev/set_dev_hosts.py',
    },

    # noip
    'noip/': {
        'features': [
            ['noip'],
        ],
        'binary': False,
        'template': r'noip/',
    },
    'noip/Dockerfile': {
        'features': [
            ['noip'],
        ],
        'binary': False,
        'template': r'noip/Dockerfile',
    },

    # vue
    'vue/': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'update_relevant': True,
        'template': r'vue/',
    },
    'vue/FS_VUE_PROJECT_NAME/': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'update_relevant': True,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/',
    },
    'vue/FS_VUE_PROJECT_NAME/.browserslistrc': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/.browserslistrc',
    },
    'vue/FS_VUE_PROJECT_NAME/.eslintrc.js': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/.eslintrc.js',
    },
    'vue/FS_VUE_PROJECT_NAME/.gitignore': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/.gitignore',
    },
    'vue/FS_VUE_PROJECT_NAME/babel.config.js': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/babel.config.js',
    },
    'vue/FS_VUE_PROJECT_NAME/package.json': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/package.json',
    },
    'vue/FS_VUE_PROJECT_NAME/package-lock.json': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/package-lock.json',
    },
    'vue/FS_VUE_PROJECT_NAME/postcss.config.js': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/postcss.config.js',
    },
    'vue/FS_VUE_PROJECT_NAME/README.md': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/README.md',
    },
    'vue/FS_VUE_PROJECT_NAME/public/': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/public/',
    },
    'vue/FS_VUE_PROJECT_NAME/public/favicon.ico': {
        'features': [
            ['vue'],
        ],
        'binary': True,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/public/favicon.ico',
    },
    'vue/FS_VUE_PROJECT_NAME/public/img/': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/public/img/',
    },
    'vue/FS_VUE_PROJECT_NAME/public/img/icons/': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/public/img/icons/',
    },
    'vue/FS_VUE_PROJECT_NAME/public/img/icons/android-chrome-192x192.png': {
        'features': [
            ['vue'],
        ],
        'binary': True,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/public/img/icons/android-chrome-192x192.png',
    },
    'vue/FS_VUE_PROJECT_NAME/public/img/icons/android-chrome-512x512.png': {
        'features': [
            ['vue'],
        ],
        'binary': True,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/public/img/icons/android-chrome-512x512.png',
    },
    'vue/FS_VUE_PROJECT_NAME/public/img/icons/apple-touch-icon-120x120.png': {
        'features': [
            ['vue'],
        ],
        'binary': True,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/public/img/icons/apple-touch-icon-120x120.png',
    },
    'vue/FS_VUE_PROJECT_NAME/public/img/icons/apple-touch-icon-152x152.png': {
        'features': [
            ['vue'],
        ],
        'binary': True,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/public/img/icons/apple-touch-icon-152x152.png',
    },
    'vue/FS_VUE_PROJECT_NAME/public/img/icons/apple-touch-icon-180x180.png': {
        'features': [
            ['vue'],
        ],
        'binary': True,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/public/img/icons/apple-touch-icon-180x180.png',
    },
    'vue/FS_VUE_PROJECT_NAME/public/img/icons/apple-touch-icon-60x60.png': {
        'features': [
            ['vue'],
        ],
        'binary': True,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/public/img/icons/apple-touch-icon-60x60.png',
    },
    'vue/FS_VUE_PROJECT_NAME/public/img/icons/apple-touch-icon-76x76.png': {
        'features': [
            ['vue'],
        ],
        'binary': True,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/public/img/icons/apple-touch-icon-76x76.png',
    },
    'vue/FS_VUE_PROJECT_NAME/public/img/icons/apple-touch-icon.png': {
        'features': [
            ['vue'],
        ],
        'binary': True,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/public/img/icons/apple-touch-icon.png',
    },
    'vue/FS_VUE_PROJECT_NAME/public/img/icons/favicon-16x16.png': {
        'features': [
            ['vue'],
        ],
        'binary': True,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/public/img/icons/favicon-16x16.png',
    },
    'vue/FS_VUE_PROJECT_NAME/public/img/icons/favicon-32x32.png': {
        'features': [
            ['vue'],
        ],
        'binary': True,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/public/img/icons/favicon-32x32.png',
    },
    'vue/FS_VUE_PROJECT_NAME/public/img/icons/msapplication-icon-144x144.png': {
        'features': [
            ['vue'],
        ],
        'binary': True,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/public/img/icons/msapplication-icon-144x144.png',
    },
    'vue/FS_VUE_PROJECT_NAME/public/img/icons/mstile-150x150.png': {
        'features': [
            ['vue'],
        ],
        'binary': True,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/public/img/icons/mstile-150x150.png',
    },
    'vue/FS_VUE_PROJECT_NAME/public/img/icons/safari-pinned-tab.svg': {
        'features': [
            ['vue'],
        ],
        'binary': True,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/public/img/icons/safari-pinned-tab.svg',
    },
    'vue/FS_VUE_PROJECT_NAME/public/index.html': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/public/index.html',
    },
    'vue/FS_VUE_PROJECT_NAME/public/manifest.json': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/public/manifest.json',
    },
    'vue/FS_VUE_PROJECT_NAME/public/robots.txt': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/public/robots.txt',
    },
    'vue/FS_VUE_PROJECT_NAME/tests/': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/tests/',
    },
    'vue/FS_VUE_PROJECT_NAME/tests/unit/': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/tests/unit/',
    },
    'vue/FS_VUE_PROJECT_NAME/tests/unit/.eslintrc.js': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/tests/unit/.eslintrc.js',
    },
    'vue/FS_VUE_PROJECT_NAME/tests/unit/example.spec.js': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/tests/unit/example.spec.js',
    },
    'vue/FS_VUE_PROJECT_NAME/src/': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'update_relevant': True,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/src/',
    },
    'vue/FS_VUE_PROJECT_NAME/src/App.vue': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'update_relevant': True,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/src/App.vue',
    },
    'vue/FS_VUE_PROJECT_NAME/src/main.js': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'update_relevant': True,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/src/main.js',
    },
    'vue/FS_VUE_PROJECT_NAME/src/registerServiceWorker.js': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/src/registerServiceWorker.js',
    },
    'vue/FS_VUE_PROJECT_NAME/src/router.js': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/src/router.js',
    },
    'vue/FS_VUE_PROJECT_NAME/src/store.js': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/src/store.js',
    },
    'vue/FS_VUE_PROJECT_NAME/src/assets/': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/src/assets/',
    },
    'vue/FS_VUE_PROJECT_NAME/src/assets/logo.png': {
        'features': [
            ['vue'],
        ],
        'binary': True,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/src/assets/logo.png',
    },
    'vue/FS_VUE_PROJECT_NAME/src/components/': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'update_relevant': True,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/src/components/',
    },
    'vue/FS_VUE_PROJECT_NAME/src/components/HelloWorld.vue': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/src/components/HelloWorld.vue',
    },
    'vue/FS_VUE_PROJECT_NAME/src/components/SocialLogin.vue': {
        'features': [
            ['vue', 'vue-socialauth'],
        ],
        'binary': False,
        'update_relevant': True,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/src/components/SocialLogin.vue',
    },
    'vue/FS_VUE_PROJECT_NAME/src/views/': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'update_relevant': True,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/src/views/',
    },
    'vue/FS_VUE_PROJECT_NAME/src/views/About.vue': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/src/views/About.vue',
    },
    'vue/FS_VUE_PROJECT_NAME/src/views/Home.vue': {
        'features': [
            ['vue'],
        ],
        'binary': False,
        'update_relevant': True,
        'template': r'vue/{{ FS_VUE_PROJECT_NAME }}/src/views/Home.vue',
    },
}
