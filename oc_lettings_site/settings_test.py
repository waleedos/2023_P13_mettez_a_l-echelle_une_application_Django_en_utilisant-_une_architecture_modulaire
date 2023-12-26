"""
Configuration spécifique aux tests pour le projet oc_lettings_site.

Ce fichier de configuration étend la configuration par défaut de settings.py
pour l'environnement de test. Il désactive le mode DEBUG et configure la base
de données pour utiliser sqlite3, fournissant ainsi un environnement isolé
et rapide pour les tests.
"""

# pylint: disable=wildcard-import,unused-wildcard-import
from .settings import *  # noqa: F403, F401

# Désactivation du mode DEBUG pour les tests
DEBUG = False

# Configuration de la base de données pour les tests
# Utilisez sqlite3 pour un test rapide et isolé
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "test_database",
    }
}

ROOT_URLCONF = "oc_lettings_site.urls"
