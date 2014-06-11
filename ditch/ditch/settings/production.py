
print ("Running Production Settings.")

from .base import *

try:
    from local_settings import *
except ImportError:
    print("Failed to load local_settings.")
