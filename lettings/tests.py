"""Tests for the lettings app."""

# Imports de bibliothèques tierces
from django.core.exceptions import ValidationError
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

# Imports de votre application
from lettings.models import Address, Letting
from lettings.views import index


class AddressModelTestCase(TestCase):
    """
    Classe de test pour le modèle Address.

    Cette classe définit des tests pour le modèle Address, notamment
    la création d'une instance d'adresse et la validation du code postal.
    """

    def test_create_address_instance(self):
        """
        Teste la création d'une instance d'adresse.

        Cette méthode crée une instance d'adresse avec des données fictives
        et vérifie si l'instance est correctement créée en comparant ses
        attributs aux valeurs attendues.
        """
        # Créez une instance d'adresse
        address = Address(
            number=123,
            street="Main Street",
            city="Cityville",
            state="ST",
            zip_code=12345,
            country_iso_code="ABC",
        )

        # Vérifiez si l'instance est correctement créée
        self.assertEqual(address.number, 123)
        self.assertEqual(address.street, "Main Street")
        self.assertEqual(address.city, "Cityville")
        self.assertEqual(address.state, "ST")
        self.assertEqual(address.zip_code, 12345)
        self.assertEqual(address.country_iso_code, "ABC")

    def test_zip_code_validation(self):
        """
        Teste la validation du code postal lors de la création d'une adresse.

        Cette méthode crée une instance d'adresse avec un code postal invalide
        (trop long) et vérifie si une exception ValidationError est levée
        lors de la validation.
        """
        # Essayez de créer une adresse avec un code postal invalide (trop long)
        address = Address(
            number=123,
            street="Main Street",
            city="Cityville",
            state="ST",
            zip_code=123456,  # Code postal invalide
            country_iso_code="ABC",
        )

        # Vérifiez si une exception ValidationError est levée lors de la création
        with self.assertRaises(ValidationError):
            address.full_clean()

    def test_address_number_validation(self):
        """
        Teste la validation du numéro dans le modèle Address.

        Vérifie si une exception ValidationError est levée lors de la saisie d'un numéro invalide.
        """
        with self.assertRaises(ValidationError):
            address = Address(
                number=10000,  # Numéro invalide (supérieur à 9999)
                street="Main Street",
                city="Cityville",
                state="ST",
                zip_code=12345,
                country_iso_code="ABC",
            )
            address.full_clean()

    def test_address_state_country_iso_code_validation(self):
        """
        Teste la validation des champs 'state' et 'country_iso_code' dans le modèle Address.

        Vérifie si une exception ValidationError est levée pour des valeurs invalides.
        """
        # Test pour 'state'
        with self.assertRaises(ValidationError):
            address = Address(
                number=123,
                street="Main Street",
                city="Cityville",
                state="A",  # Longueur invalide
                zip_code=12345,
                country_iso_code="ABC",
            )
            address.full_clean()

        # Test pour 'country_iso_code'
        with self.assertRaises(ValidationError):
            address.country_iso_code = "AB"  # Longueur invalide
            address.full_clean()


class LettingsViewTestCase(TestCase):
    """
    Classe de test pour les vues de l'application lettings.

    Cette classe teste le fonctionnement des vues, notamment le rendu des templates,
    les codes de statut HTTP, et le contexte des vues.
    """

    def test_index_view(self):
        """
        Teste la vue index de l'application lettings.

        Vérifie que la vue renvoie un code de statut HTTP 200 et utilise
        le bon template.
        """
        # Utilisez le bon nom d'URL
        response = self.client.get(reverse("lettings:lettings_index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/index.html")


class LettingsURLsTestCase(SimpleTestCase):
    """
    Classe de test pour les URLs de l'application lettings.

    Cette classe teste si les URLs sont correctement résolues et renvoient
    les bons codes de statut HTTP.
    """

    def test_index_url_resolves(self):
        """
        Teste si l'URL de la vue index est correctement résolue.
        """
        # Utilisez le bon nom d'URL
        url = reverse("lettings:lettings_index")
        self.assertEqual(resolve(url).func, index)


class LettingViewTestCase(TestCase):
    """
    Classe de test pour les vues détaillées de l'application lettings.
    """

    @classmethod
    def setUpTestData(cls):
        # Créer des données de test
        cls.address = Address.objects.create(
            number=123,
            street="Main Street",
            city="Cityville",
            state="ST",
            zip_code=12345,
            country_iso_code="ABC",
        )
        cls.letting = Letting.objects.create(title="Test Letting", address=cls.address)

    def test_letting_view_context(self):
        """
        Teste si la vue letting renvoie le bon contexte.
        """
        response = self.client.get(reverse("lettings:letting", args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["title"], self.letting.title)
        self.assertEqual(response.context["address"], self.letting.address)

    def setUp(self):
        """
        Fonction de configuration pour créer un objet Address avant chaque test.
        """
        Address.objects.create(
            number=123,
            street="Main Street",
            city="Anytown",
            state="AT",
            zip_code=12345,
            country_iso_code="USA",
        )

    def test_address_str(self):
        """
        Teste la méthode __str__ du modèle Address.

        Vérifie que la méthode __str__ renvoie une chaîne formatée correctement
        représentant l'adresse.
        """
        address = Address.objects.get(id=1)
        self.assertEqual(str(address), "123 Main Street")

    def test_letting_str(self):
        """
        Teste la méthode __str__ du modèle Letting.

        Vérifie que la méthode __str__ renvoie correctement le titre de l'annonce
        de location.
        """
        letting = Letting.objects.get(id=1)
        self.assertEqual(str(letting), "Test Letting")
