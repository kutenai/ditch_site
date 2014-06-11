
print ("Running Development Settings.")

from .base import *

USE_LESS = True
LESS_POLL = 2000

try:
    from local_settings import *
except ImportError:
    print("Failed to load local_settings.")
