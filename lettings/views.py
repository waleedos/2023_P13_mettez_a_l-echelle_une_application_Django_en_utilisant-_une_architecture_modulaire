"""Module de vues pour l'application lettings.

Ce module contient les vues pour l'application lettings, définissant comment les données
sont présentées à l'utilisateur dans les templates HTML.
"""

import logging
from django.shortcuts import render, get_object_or_404
from .models import Letting

# Configuration du logger pour ce module.
logger = logging.getLogger(__name__)


def index(request):
    """
    Fonction de vue pour afficher une liste de lettings.

    Paramètres :
        request (HttpRequest) : L'objet de requête HTTP.

    Retourne :
        HttpResponse : La page HTML rendue affichant une liste de lettings.
    """
    logger.info("Affichage de la liste des lettings.")
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Fonction de vue pour afficher les détails d'un letting spécifique.

    Paramètres :
        request (HttpRequest) : L'objet de requête HTTP.
        letting_id (int) : L'ID du letting spécifique à afficher.

    Retourne :
        HttpResponse : La page HTML rendue affichant les détails du letting.
    """
    specific_letting = get_object_or_404(Letting, id=letting_id)
    context = {"title": specific_letting.title, "address": specific_letting.address}
    return render(request, "lettings/letting.html", context)
