from .common import *
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
ALLOWED_HOSTS = ['*']
import dj_database_url
DATABASES = {
    'default': dj_database_url.config()
}

BROKER_URL = os.environ.get('REDISTOGO_URL')
