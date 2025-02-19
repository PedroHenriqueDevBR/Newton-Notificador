import os
from pathlib import Path
from datetime import timedelta
from typing import Any, Dict, List

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY: str = ""
DEBUG: bool = True
ALLOWED_HOSTS: List[str] = []
CSRF_TRUSTED_ORIGINS: List[str] = []

# Application definition
INSTALLED_APPS: List[str] = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # libs de terceiros
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    # Apps
    "provedor",
    "core",
]

MIDDLEWARE: List[str] = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

REST_FRAMEWORK: Dict[str, Any] = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
}

CORS_ALLOWED_ORIGINS: List[str] = []

SIMPLE_JWT: Dict[str, Any] = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME': timedelta(days=30),
    'SLIDING_TOKEN_REFRESH_LIFETIME_LATE_USER': timedelta(days=1),
    'SLIDING_TOKEN_LIFETIME_LATE_USER': timedelta(days=30),
}


# Mail
EMAIL_HOST: str = ""
EMAIL_PORT: str = ""
DEFAULT_FROM_EMAIL: str = ""
EMAIL_HOST_USER: str = ""
EMAIL_HOST_PASSWORD: str = ""
EMAIL_USE_TLS: str = ""
EMAIL_BACKEND: str = "django.core.mail.backends.smtp.EmailBackend"
FAKE_MAIL: bool = False

# Auth
LOGIN_URL: str = "/admin/"
LOGOUT_REDIRECT_URL: str = "/admin/"
LOGIN_REDIRECT_URL: str = "/"

ROOT_URLCONF: str = "notificador.urls"

TEMPLATES: List[Dict[str, Any]] = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION: str = "notificador.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES: Dict[str, Any] = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
N1 = "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
N2 = "django.contrib.auth.password_validation.MinimumLengthValidator"
N3 = "django.contrib.auth.password_validation.CommonPasswordValidator"
N4 = "django.contrib.auth.password_validation.NumericPasswordValidator"

AUTH_PASSWORD_VALIDATORS: List[Dict[str, Any]] = [
    {"NAME": N1},
    {"NAME": N2},
    {"NAME": N3},
    {"NAME": N4},
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGE_CODE: str = "pt-br"
TIME_ZONE: str = "America/Fortaleza"
USE_I18N: bool = True
USE_TZ: bool = True
USE_L10N: bool = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL: str = "static/"
STATIC_ROOT: str = os.path.join("staticfiles")
MEDIA_URL: str = "media/"
MEDIA_ROOT: str = os.path.join("mediafiles")


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD: str = "django.db.models.BigAutoField"
