"""Module de vues pour l'application oc_lettings_site.

Ce module définit les vues principales de l'application oc_lettings_site,
en déterminant comment les données sont présentées à l'utilisateur.
"""
from django.shortcuts import render


def index(request):
    """Vue pour la page d'accueil du site.

    Cette fonction gère la requête pour la page d'accueil ('/') du site.
    Elle rend le template 'index.html', qui est la page d'entrée de l'application.

    Args:
        request: L'objet HttpRequest reçu.

    Returns:
        HttpResponse: La réponse HTTP avec le template 'index.html' rendu.
    """
    return render(request, "index.html")
