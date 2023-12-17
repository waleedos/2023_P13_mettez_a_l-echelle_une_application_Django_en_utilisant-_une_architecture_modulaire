"""Module de définition des URL pour l'application profiles.

Ce module définit les chemins d'URL (routes) pour l'application profiles.
Chaque chemin est associé à une vue spécifique pour gérer les requêtes correspondantes.

Attributes:
    app_name (str): Un nom d'application qui est utilisé pour organiser les URL au niveau de
    l'application.
"""

from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path(
        "", views.index, name="profiles_index"
    ),  # Mise à jour de profiles_index en index
    # Chemin pour la page d'index de l'application profiles.
    path("<str:username>/", views.profile, name="profile"),
    # Chemin pour afficher le profil d'un utilisateur spécifique.
]
