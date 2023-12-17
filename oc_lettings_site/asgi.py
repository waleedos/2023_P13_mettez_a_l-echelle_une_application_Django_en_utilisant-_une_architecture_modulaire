"""Module ASGI pour le projet oc_lettings_site.

Ce module configure l'interface ASGI pour le projet oc_lettings_site, permettant
de servir l'application via des serveurs ASGI modernes comme Daphne ou Hypercorn.
L'interface ASGI est une norme émergente pour les applications web Python asynchrones.
"""

import os
from django.core.asgi import get_asgi_application

# Configuration de la variable d'environnement pour le module de paramètres Django.
# Cela indique à Django quel fichier de paramètres doit être utilisé.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")

# Création de l'application ASGI pour le projet oc_lettings_site.
# Cette application est ensuite utilisée par le serveur ASGI pour gérer les requêtes.
application = get_asgi_application()
