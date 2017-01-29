from __future__ import absolute_import, unicode_literals

from .base import *

# Sensitive and machine-specific info (e.g. database password)
from .local_production import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PWD,
        'HOST': 'localhost',
        'PORT': '',
    }
}

try:
    from .local import *
except ImportError:
    pass
