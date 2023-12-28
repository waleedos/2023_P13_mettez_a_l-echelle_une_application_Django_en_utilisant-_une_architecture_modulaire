"""Définition des URL pour l'application lettings.

Ce module définit les chemins d'URL pour l'application lettings, associant les vues aux URL
correspondantes.
"""

from django.urls import path
from . import views

app_name = "lettings"

urlpatterns = [
    path("", views.index, name="lettings_index"),
    path("<int:letting_id>/", views.letting, name="letting"),
]
