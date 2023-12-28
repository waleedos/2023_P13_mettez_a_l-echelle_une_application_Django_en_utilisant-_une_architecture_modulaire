"""Module de vues pour l'application profiles.

Ce module contient les vues pour l'application profiles. Il définit les fonctions
qui prennent une requête web et retournent une réponse. Les vues interagissent
avec le modèle Profile pour récupérer et envoyer des données à l'utilisateur.
"""

import logging
from django.shortcuts import render, get_object_or_404
from .models import Profile

# Configuration du logger pour ce module.
logger = logging.getLogger(__name__)


def index(request):
    """Vue pour la page d'index de l'application profiles.

    Cette vue récupère tous les objets Profile et les transmet à un template pour
    affichage.

    Args:
        request: L'objet HttpRequest reçu.

    Returns:
        HttpResponse: La réponse HTTP contenant le rendu du template index.html
        avec la liste des profils.
    """
    logger.info("Affichage de la liste des profils.")
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """Vue pour la page de profil d'un utilisateur spécifique.

    Cette vue récupère un objet Profile basé sur le nom d'utilisateur et le transmet
    à un template pour affichage.

    Args:
        request: L'objet HttpRequest reçu.
        username (str): Le nom d'utilisateur pour lequel afficher le profil.

    Returns:
        HttpResponse: La réponse HTTP contenant le rendu du template profile.html
        avec les détails du profil demandé.
    """
    logger.info("Quelque chose s'est produit avec l'utilisateur : %s", username)
    profile_instance = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile_instance}
    return render(request, "profiles/profile.html", context)
