"""Module de modèles pour l'application lettings.

Ce module définit les modèles de données pour l'application lettings, représentant les structures
de données nécessaires pour la gestion des locations.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Modèle de données pour une adresse.

    Cette classe modélise une adresse avec des champs tels que le numéro,
    la rue, la ville, l'État, le code postal et le code ISO du pays.

    Attributes:
        number (PositiveIntegerField): Le numéro de l'adresse.
        street (CharField): Le nom de la rue.
        city (CharField): Le nom de la ville.
        state (CharField): L'État ou la province.
        zip_code (PositiveIntegerField): Le code postal.
        country_iso_code (CharField): Le code ISO du pays.

    Methods:
        __str__(): Renvoie une représentation textuelle de l'adresse.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        """
        Renvoie une représentation textuelle de l'adresse.

        Returns:
            str: Une chaîne représentant l'adresse sous la forme "numéro rue".
        """
        return f"{self.number} {self.street}"

    class Meta:
        app_label = 'lettings'
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Modèle de données pour une annonce de location (letting).

    Cette classe modélise une annonce de location avec un titre et une
    référence à une adresse.

    Attributes:
        title (CharField): Le titre de l'annonce.
        address (OneToOneField): Une référence à l'adresse associée à cette annonce.

    Methods:
        __str__(): Renvoie une représentation textuelle de l'annonce.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Renvoie une représentation textuelle de l'annonce.

        Returns:
            str: Le titre de l'annonce.
        """
        return self.title

    class Meta:
        app_label = 'lettings'
