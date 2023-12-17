"""Module de vues pour l'application lettings.

Ce module contient les vues pour l'application lettings, définissant comment les données
sont présentées à l'utilisateur dans les templates HTML.
"""

from django.shortcuts import render
from .models import Letting


def index(request):
    """
    View function for displaying a list of lettings.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page displaying a list of lettings.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    View function for displaying the details of a specific letting.

    Parameters:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The ID of the specific letting to display.

    Returns:
        HttpResponse: The rendered HTML page displaying the details of the letting.
    """
    specific_letting = Letting.objects.get(id=letting_id)
    context = {
        "title": specific_letting.title,
        "address": specific_letting.address,
    }
    return render(request, "lettings/letting.html", context)
