"""Configuration de l'administration pour l'application lettings.

Ce module configure l'interface d'administration de Django pour l'application lettings,
permettant la gestion des modèles dans l'interface admin.
"""

from django.contrib import admin
from .models import Address, Letting

# Enregistrement des modèles Address et Letting dans l'interface d'administration de Django.
# Ceci permet de gérer ces modèles via l'interface d'administration.

admin.site.register(Address)
admin.site.register(Letting)
