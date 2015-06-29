from __future__ import absolute_import
# Django settings for ditch project.

from os.path import abspath
from unipath import Path
from celery.schedules import crontab
from datetime import timedelta

DJANGO_ROOT = Path(abspath(__file__)).ancestor(3)
print("File:%s" % __file__)

SITE_ROOT = DJANGO_ROOT.ancestor(1)
print("Site root:%s" % SITE_ROOT)
print("Django Root:%s" % DJANGO_ROOT)

ADMINS = (
    ('Ed Henderson', 'kutenai@me.com'),
)

LOGIN_URL = '/account/login/'

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'bondinorth_ditch',                      # Or path to database file if using sqlite3.
        'USER': 'gb_user',                      # Not used with sqlite3.
        'PASSWORD': 'aj-vic-gik-du-i',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

API_VERSION = 'v1'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'US/Mountain'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1
SITE_NAME = "Boise Ditch Company"

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/site_media/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    DJANGO_ROOT.child('static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Set your DSN value
RAVEN_CONFIG = {
    'dsn': 'https://2ebc4238aa3d493ba1621ad15097a158:6e84b01224fa441fb7eee42620e6b2c2@app.getsentry.com/26472',
    }

# Make this unique, and don't share it with anybody.
SECRET_KEY = ')#w(pmjx(&+1q&yfz&d=)@2ut1q^gkkq^rco77o!_9#b&7!2uz'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

########## TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'ws4redis.context_processors.default',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'account.context_processors.account',
    'pinax_theme_bootstrap.context_processors.theme',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'ditchlib.context_processors.gardenbuzz_ctx',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'ditch.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ditch.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    DJANGO_ROOT.child('templates'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.webdesign',

    'django_forms_bootstrap',
    'pinax_theme_bootstrap',
    'bootstrapform',

    'rest_framework',
    'account',
    'bootstrap',

    'ditch',
    'ditchdb',
    'ditchmon',
    'ditchctrl',

    'dbtasks',
    'ditchtasks',

    # Web sockets
    'ws4redis',

    #'messages',
    'raven.contrib.django.raven_compat',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 10
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

USE_LESS = False
LESS_POLL = 20000

# Web Sockets
WEBSOCKET_URL = '/ws/'

WS4REDIS_CONNECTION = {
    'host': 'gardenbuzz.com',
    'port': 6379,
    'db': 4, # For production
    #'password': 'verysecret',
}
WS4REDIS_EXPIRE = 7200

# Use a different prefix for dev
WS4REDIS_PREFIX = 'ws'
#WS4REDIS_SUBSCRIBER = 'myapp.redis_store.RedisSubscriber'
WSGI_APPLICATION = 'ws4redis.django_runserver.application'

# Redis Sessions
SESSION_ENGINE = 'redis_sessions.session'

SESSION_REDIS_HOST = 'gardenbuzz.com'
SESSION_REDIS_PORT = 6379
SESSION_REDIS_DB = 5
#SESSION_REDIS_PASSWORD = 'password'
SESSION_REDIS_PREFIX = 'ditch'

# If you prefer domain socket connection, you can just add this line instead of SESSION_REDIS_HOST and SESSION_REDIS_PORT.

#SESSION_REDIS_UNIX_DOMAIN_SOCKET_PATH = '/var/run/redis/redis.sock'

# Celery
BROKER_URL = 'redis://gardenbuzz.com:6379/0'
CELERY_RESULT_BACKEND = 'redis://gardenbuzz.com:6379/1'

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'US/Mountain'
CELERY_ENABLE_UTC = False
CELERYD_CONCURRENCY = 1
CELERY_TASK_RESULT_EXPIRES=60
CELERY_DISABLE_RATE_LIMITS = True

CELERY_ROUTES = {
    'dbtasks.tasks.onstatus': {'queue': 'db'}
}

CELERYBEAT_SCHEDULE = {
    'update-ditch-db' : {
        'task' : 'dbtasks.tasks.update_database',
        'schedule' : crontab(minute='*/1')
    },
    'update_status' : {
        'task' : 'ditchtasks.tasks.status',
        'schedule' : timedelta(seconds=10)
    }
}

DITCH_POLL_RATE = 2000

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc --clean-css --clean-option=--keep-line-breaks {infile} {outfile}'),
)

