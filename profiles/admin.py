"""Module admin de l'application profiles.

Ce module permet de configurer les interfaces d'administration pour les modèles
de l'application profiles. Il utilise l'administration de Django pour
enregistrer les modèles et personnaliser l'affichage dans l'interface d'administration.
"""

from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    """Classe d'administration pour le modèle Profile.

    Cette classe permet de personnaliser l'interface d'administration pour le modèle Profile.
    Elle peut être étendue pour inclure des configurations spécifiques comme des filtres,
    des champs à afficher, des options de recherche, etc.
    """


# Enregistrement du modèle Profile avec sa classe d'administration correspondante
admin.site.register(Profile, ProfileAdmin)
