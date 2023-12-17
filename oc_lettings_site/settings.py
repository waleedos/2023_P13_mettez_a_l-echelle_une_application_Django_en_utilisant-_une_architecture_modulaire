"""Configuration des paramètres pour le projet oc_lettings_site.

Ce module définit les configurations globales du projet Django,
incluant les réglages de base de données, les configurations de sécurité,
et d'autres paramètres importants.
"""
import os
from pathlib import Path

# Chemin de base du projet Django.
# Utilisé pour construire des chemins de fichiers relatifs au projet.
BASE_DIR = Path(__file__).resolve().parent.parent

# Paramètres de développement rapide - inadaptés à la production
# Voir https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# AVERTISSEMENT DE SÉCURITÉ : garder la clé secrète utilisée en production secrète!
SECRET_KEY = "fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s"

# AVERTISSEMENT DE SÉCURITÉ : ne pas exécuter avec debug activé en production!
DEBUG = True

ALLOWED_HOSTS = []

# Définition de l'application

# Liste des applications installées dans ce projet Django.
# Chaque application ajoute une fonctionnalité ou des fonctionnalités au projet.
INSTALLED_APPS = [
    # ... (liste des applications)
]

# Middleware

# Liste des middleware utilisés par ce projet Django.
# Chaque middleware est un traitement effectué sur la requête/réponse.
MIDDLEWARE = [
    # ... (liste des middleware)
]

ROOT_URLCONF = "oc_lettings_site.urls"

# Configuration des templates

# Configuration des moteurs de templates utilisés dans ce projet Django.
TEMPLATES = [
    # ... (configuration des templates)
]

# Configuration de l'application WSGI

# Chemin vers l'application WSGI utilisée pour servir le projet.
WSGI_APPLICATION = "oc_lettings_site.wsgi.application"

# Base de données

# Configuration de la base de données pour ce projet Django.
# Voir https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    "default": {
        # ... (configuration de la base de données)
    }
}

# Validation des mots de passe

# Configuration des validateurs de mot de passe pour ce projet Django.
AUTH_PASSWORD_VALIDATORS = [
    # ... (liste des validateurs de mot de passe)
]

# Internationalisation

# Configuration de la langue, du fuseau horaire, et de la localisation.
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Fichiers statiques (CSS, JavaScript, Images)

# Configuration des fichiers statiques pour ce projet Django.
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Champ auto-id par défaut

# Configuration du champ auto-id par défaut pour les modèles.
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
