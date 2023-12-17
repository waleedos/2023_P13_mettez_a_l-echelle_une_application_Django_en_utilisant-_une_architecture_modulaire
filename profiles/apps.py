"""Module de configuration de l'application profiles.

Ce module définit la configuration spécifique à l'application profiles.
Il est utilisé par Django pour configurer divers aspects de l'application,
comme le nom de l'application et le type de champ d'identifiant automatique par défaut.
"""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """Configuration de l'application profiles.

    Cette classe hérite de AppConfig et définit les paramètres de configuration
    pour l'application profiles. Elle spécifie le nom de l'application et le type
    de champ d'identifiant automatique par défaut à utiliser pour les modèles de cette application.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "profiles"
