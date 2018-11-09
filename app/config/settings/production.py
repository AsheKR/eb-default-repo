from .base import *

PRODUCTION_JSON = json.load(open(os.path.join(SECRETS_DIR, 'production.json')))
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

WSGI_APPLICATION = 'config.wsgi.production.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = PRODUCTION_JSON['DATABASES']

AWS_STORAGE_BUCKET_NAME = PRODUCTION_JSON['AWS_STORAGE_BUCKET_NAME']

LOG_DIR = os.path.join(ROOT_DIR, '.log')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR, exist_ok=True)

LOGGING = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(levelname)s] %(name)s (%(asctime)s)\n\t%(message)s',
        }
    },
    'handlers': {
        'file_error': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'formatter': 'default',
            # 최대 1MB를 넘게되면 새 파일을 만들어 저장
            'maxBytes': 1048576,
            # 최대 파일은 10개
            'backupCount': 10,
        },
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file_error', 'console'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}