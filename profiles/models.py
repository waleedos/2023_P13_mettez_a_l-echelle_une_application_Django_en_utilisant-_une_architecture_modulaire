"""Module de modèles pour l'application profiles.

Ce module définit les modèles de données pour l'application profiles.
Il inclut le modèle Profile qui est lié au modèle utilisateur standard de Django.
"""

from django.db import models
from django.contrib.auth import get_user_model

# Obtention du modèle User actuel de Django.
# Cela permet d'utiliser le modèle User standard ou un modèle personnalisé, si configuré.
User = get_user_model()


class Profile(models.Model):
    """Modèle représentant le profil d'un utilisateur.

    Ce modèle étend le modèle User standard de Django en ajoutant des informations
    supplémentaires spécifiques à l'utilisateur, telles que sa ville favorite.

    Attributs:
        user (OneToOneField): Un lien un-à-un vers le modèle User standard de Django.
            Lorsqu'un utilisateur est supprimé, son profil associé est également supprimé.
        favorite_city (CharField): Un champ pour stocker la ville favorite de l'utilisateur.
            Ce champ est facultatif et peut être laissé vide.
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profiles_profile"
    )
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """Renvoie une représentation en chaîne de caractères du profil.

        Cette méthode est utilisée pour afficher une représentation lisible du profil,
        qui, dans ce cas, est le nom d'utilisateur associé au profil.

        Retourne:
            str: Le nom d'utilisateur du profil.
        """
        return self.user.username
