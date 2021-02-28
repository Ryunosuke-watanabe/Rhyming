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

INSTALLED_APPS += (
    'score.apps.ScoreConfig',
)

LOGIN_URL = 'login' # ログインしていないときのリダイレクト先
LOGIN_REDIRECT_URL = 'index' # ログイン後のリダイレクト先
LOGOUT_REDIRECT_URL = 'index' # ログアウト後のリダイレクト先

AUTH_USER_MODEL = 'score.MyUser'
