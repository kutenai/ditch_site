from __future__ import absolute_import

print ("Running Development Settings.")

from .base import *

STATIC_ROOT = SITE_ROOT.child('collectedstatic')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

USE_LESS = True
LESS_POLL = 2000

ALLOWED_HOSTS = (
    '127.0.0.1',
)

try:
    from local_settings import *
except ImportError:
    pass
