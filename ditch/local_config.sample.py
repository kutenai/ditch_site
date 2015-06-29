# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import

import sys
print("Bootstrap from {}".format(__file__))

if sys.argv[1] == 'test':
    print("Running test mode..")
    from ditch.settings.testing import *
else:
    from ditch.settings.dev import *

    # Then, you are able to override or extend existing data structure.
    # For example:
    DATABASES['default']['HOST'] = 'localhost'
    DATABASES['default']['NAME'] = ''
    DATABASES['default']['USER'] = ''
    DATABASES['default']['PASSWORD'] = ''

    DEBUG = True
    TEMPLATE_DEBUG = DEBUG


if USE_LESS:
    COMPRESS_PRECOMPILERS = [
        p for p in COMPRESS_PRECOMPILERS if not p[0] == 'text/less'
    ]

#set this up to send confirm email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_USE_TLS = True
