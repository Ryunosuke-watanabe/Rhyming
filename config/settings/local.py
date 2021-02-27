from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rhyme',
        'USER': 'ryu',
        'PASSWORD' : 'ryunosuke0904',
        'HOST' : 'localhost',
        'PORT' : 5432,
    }
}
