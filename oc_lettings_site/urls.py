"""Définition des URL pour le projet oc_lettings_site.

Ce module mappe les URL aux vues de l'application oc_lettings_site,
organisant les routes et les redirections au sein du projet.
"""

from django.contrib import admin
from django.urls import path, include
from . import views

# Liste des motifs d'URL pour le projet oc_lettings_site.
# Chaque motif d'URL est associé à une vue spécifique.
urlpatterns = [
    path("", views.index, name="index"),
    # La route racine "" est associée à la vue 'index' dans 'views.py'.
    path("lettings/", include("lettings.urls")),
    # Inclut les URL de l'application 'lettings'.
    # Toutes les URL commençant par 'lettings/' seront redirigées vers 'lettings.urls'.
    path("profiles/", include("profiles.urls")),
    # Inclut les URL de l'application 'profiles'.
    # Toutes les URL commençant par 'profiles/' seront redirigées vers 'profiles.urls'.
    path("admin/", admin.site.urls),
    # Le chemin 'admin/' est configuré pour les URL de l'interface d'administration Django.
]
