import os

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY_PRODUCTION')
ALLOWED_HOSTS = [
    os.environ.get('HEROKU_HOST'),
]

Databases = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_PRODUCTION_NAME'),
        'USER': os.environ.get('DB_PRODUCTION_USER'),
        'PASSWORD': os.environ.get('DB_PRODUCTION_PASSWORD'),
        'HOST': os.environ.get('DB_PRODUCTION_HOST'),
        'PORT': os.environ.get('DB_PRODUCTION_PORT'),
    }
}
