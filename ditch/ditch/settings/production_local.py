
print ("Running Production Local Settings.")

from .base import *

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = '/Users/kutenai/proj/bondiproj/ditch_site/collectedstatic'

#DEBUG = True
#TEMPLATE_DEBUG = DEBUG

#USE_LESS = True
#LESS_POLL = 2000

ALLOWED_HOSTS = (
    '127.0.0.1',
)

