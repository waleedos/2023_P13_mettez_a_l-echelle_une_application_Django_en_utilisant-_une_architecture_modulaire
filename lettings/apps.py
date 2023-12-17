"""Configuration de l'application lettings.

Ce module définit la configuration spécifique de l'application lettings dans le projet Django.
"""

from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """
    Configuration de l'application Lettings.

    Cette classe de configuration permet de spécifier la configuration
    de l'application Lettings, notamment le champ par défaut pour les clés
    étrangères (default_auto_field) et le nom de l'application.

    Attributes:
        default_auto_field (str): Le nom de la classe de champ à utiliser pour
            les clés étrangères automatiques.
        name (str): Le nom de l'application.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "lettings"
