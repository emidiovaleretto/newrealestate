from decouple import config
from .settings import BASE_DIR

DEBUG = True
SECRET_KEY = config('SECRET_KEY_DEVELOPMENT')

ALLOWED_HOSTS = [
    "localhost",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
