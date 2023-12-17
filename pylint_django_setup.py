"""Configuration spécifique pour l'exécution de Pylint sur un projet Django.

Ce module configure l'environnement nécessaire pour que Pylint puisse
correctement analyser un projet Django.
"""
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")
django.setup()
