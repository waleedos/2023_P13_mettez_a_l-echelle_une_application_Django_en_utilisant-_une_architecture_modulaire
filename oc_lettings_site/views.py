"""Module de vues pour l'application oc_lettings_site.

Ce module définit les vues principales de l'application oc_lettings_site,
en déterminant comment les données sont présentées à l'utilisateur.
"""
import logging
from django.shortcuts import render
from django.http import HttpResponseNotFound

# Configuration du logger pour ce module.
logger = logging.getLogger(__name__)


def index(request):
    """
    Vue pour la page d'accueil du site.

    Cette fonction gère la requête pour la page d'accueil ('/') du site.
    Elle rend le template 'index.html', qui est la page d'entrée de l'application.

    Args:
        request: L'objet HttpRequest reçu.

    Returns:
        HttpResponse: La réponse HTTP avec le template 'index.html' rendu.
    """
    logger.info("Affichage de la page d'accueil.")
    return render(request, "index.html")


def test_404(request):
    """
    Renvoie une réponse HTTP 404 (Non trouvé) avec la page de rendu "404.html".

    Cette fonction est utilisée pour tester la gestion des erreurs 404 dans l'application.
    Elle renvoie une réponse HTTP 404 avec le contenu de la page "404.html" rendue
    à l'aide de la bibliothèque de rendu Django.

    Args:
        request (HttpRequest): L'objet de requête HTTP reçu.

    Returns:
        HttpResponseNotFound: Une réponse HTTP 404 contenant le contenu de la page "404.html".
    """
    logger.warning("Page 404 demandée.")
    return HttpResponseNotFound(render(request, "404.html"))


def test_500(request):
    """
    Provoque une erreur de serveur interne pour tester la gestion des erreurs 500.

    Args:
        request (HttpRequest): L'objet de requête HTTP reçu.
    """
    logger.error("Erreur interne du serveur déclenchée.")
    raise ValueError("Test d'erreur 500")
