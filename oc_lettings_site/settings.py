"""Configuration des paramètres pour le projet oc_lettings_site.

Ce module définit les configurations globales du projet Django,
incluant les réglages de base de données, les configurations de sécurité,
et d'autres paramètres importants.
"""
import os
from pathlib import Path
import sentry_sdk
import falcon


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]


# Application definition

INSTALLED_APPS = [
    "oc_lettings_site.apps.OCLettingsSiteConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "lettings.apps.LettingsConfig",
    "profiles.apps.ProfilesConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "oc_lettings_site.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "oc_lettings_site.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "oc-lettings-site.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


def initialize_sentry():
    """
    Initialise Sentry pour la surveillance des erreurs dans une application Django.

    Cette fonction configure Sentry, un service de suivi des erreurs, pour qu'il soit utilisé avec
    une application Django. Elle doit être appelée lors de l'initialisation de l'application pour
    assurer que les erreurs et les problèmes sont correctement enregistrés et envoyés à Sentry.

    Sentry aide à surveiller, à détecter et à réparer les erreurs en temps réel, en fournissant
    des détails contextuels et des insights sur les défaillances de l'application.

    Paramètres :
    dsn (str): La clé DSN (Data Source Name) fournie par Sentry. Cette clé est unique à chaque
               projet Sentry et est utilisée pour authentifier et diriger les données d'erreur
               vers le bon projet dans Sentry. La clé DSN doit être obtenue à partir du tableau de
               bord Sentry et doit être traitée comme une information sensible.

    Retourne :
    None

    Exemple :
    Pour initialiser Sentry dans une application Django, appelez cette fonction dans votre fichier
    settings.py :

        initialize_sentry()

    Remarque :
    - Il est important de garder la clé DSN confidentielle, car elle permet l'envoi de données à
      votre projet Sentry.
    - Vous pouvez ajuster la configuration supplémentaire pour contrôler ce qui est envoyé à
      Sentry, comme la capture des erreurs de niveau DEBUG ou INFO, selon les besoins de votre
      projet.

    Pour plus d'informations, visitez la documentation officielle de Sentry :
    https://docs.sentry.io/platforms/python/guides/django/
    """

    sentry_sdk.init(
        dsn=(
            "https://bff0ef1ae167a0c142715c65fd373865@"
            "o4506465781219328.ingest.sentry.io/4506465814249472"
        ),
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        traces_sample_rate=1.0,
        # Set profiles_sample_rate to 1.0 to profile 100%
        # of sampled transactions.
        # We recommend adjusting this value in production.
        profiles_sample_rate=1.0,
    )


# Appel de la fonction dans settings.py
initialize_sentry()

# Configuration de Falcon (si utilisé dans votre projet)
api = falcon.API()


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "sentry": {
            "level": "ERROR",  # le niveau est ajusté selon les besoins
            "class": "sentry_sdk.integrations.logging.EventHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["sentry"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}
