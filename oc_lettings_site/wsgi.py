"""Module WSGI pour le projet oc_lettings_site.

Ce module configure l'interface WSGI pour le projet oc_lettings_site, permettant
de servir l'application via des serveurs web tels que Gunicorn ou uWSGI.
L'interface WSGI est une norme pour les applications web Python, facilitant la
communication entre le serveur web et l'application.
"""

import os
from django.core.wsgi import get_wsgi_application

# Configuration de la variable d'environnement pour le module de paramètres Django.
# Cela indique à Django quel fichier de paramètres doit être utilisé pour le projet.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")

# Création de l'application WSGI pour le projet oc_lettings_site.
# Cette application est utilisée par le serveur web pour gérer les requêtes.
application = get_wsgi_application()
