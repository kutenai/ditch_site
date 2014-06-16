from __future__ import absolute_import

print ("Running Development Settings.")

from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

USE_LESS = True
LESS_POLL = 2000

try:
    from local_settings import *
except ImportError:
    pass
