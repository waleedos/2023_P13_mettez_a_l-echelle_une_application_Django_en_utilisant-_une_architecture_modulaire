"""Script de gestion pour le projet Django.

Ce script est utilisé pour exécuter diverses commandes de gestion de Django
depuis la ligne de commande.
"""

import os
import sys
from django.core.management import execute_from_command_line

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")


def main():
    """Fonction principale du script de gestion."""
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
