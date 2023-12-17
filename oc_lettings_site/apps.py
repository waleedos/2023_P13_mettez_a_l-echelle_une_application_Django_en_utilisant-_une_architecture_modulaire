"""Configuration de l'application oc_lettings_site.

Ce module définit la configuration spécifique de l'application oc_lettings_site
dans le cadre Django. Il hérite de AppConfig pour intégrer l'application
dans le projet Django global.
"""

from django.apps import AppConfig


class OCLettingsSiteConfig(AppConfig):
    """Configuration spécifique pour l'application oc_lettings_site.

    Cette classe hérite de AppConfig et est utilisée pour configurer divers aspects
    de l'application oc_lettings_site, comme son nom et d'autres comportements
    d'initialisation.

    Attributs:
        name (str): Nom officiel de l'application utilisé dans les configurations Django.
            Cela aide Django à identifier et à utiliser l'application dans le projet global.
    """

    name = "oc_lettings_site"
