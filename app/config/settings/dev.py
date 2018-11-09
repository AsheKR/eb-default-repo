from .base import *

DEV_JSON = json.load(open(os.path.join(SECRETS_DIR, 'dev.json')))
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

STATAICFILES_DIRS = [
    STATIC_DIR,
]

WSGI_APPLICATION = 'config.wsgi.dev.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = DEV_JSON['DATABASES']

AWS_STORAGE_BUCKET_NAME = DEV_JSON['AWS_STORAGE_BUCKET_NAME']