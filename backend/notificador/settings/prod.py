from decouple import config, Csv  # type: ignore
from pathlib import Path
from notificador.settings.base import *

SECRET_KEY = config("SECRET_KEY")  # type: ignore
DEBUG = config("DEBUG", default=False, cast=bool)  # type: ignore
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())  # type: ignore
CSRF_TRUSTED_ORIGINS = config("CSRF_TRUSTED_ORIGINS", cast=Csv())  # type: ignore
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # type: ignore

# Mail
EMAIL_HOST = config("EMAIL_HOST")  # type: ignore
EMAIL_PORT = config("EMAIL_PORT")  # type: ignore
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")  # type: ignore
EMAIL_HOST_USER = config("EMAIL_HOST_USER")  # type: ignore
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")  # type: ignore
EMAIL_USE_TLS = config("DEBUG", default=True, cast=bool)  # type: ignore
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"  # type: ignore
FAKE_MAIL=config("FAKE_MAIL", default=False, cast=bool)  # type: ignore

CORS_ALLOWED_ORIGINS = config("CSRF_TRUSTED_ORIGINS", cast=Csv())  # type: ignore

DATABASES = {  # type: ignore
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_DATABASE_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST", default="localhost"),
        "PORT": config("DB_PORT", default=5432, cast=int),
    }
}
