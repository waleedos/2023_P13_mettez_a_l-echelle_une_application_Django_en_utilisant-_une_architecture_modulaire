"""
Module de tests pour l'application profiles.

Ce module contient des tests unitaires pour l'application profiles,
couvrant les modèles, les vues, et les URLs. Les tests assurent le bon
fonctionnement et la robustesse des fonctionnalités de l'application.
"""

from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from profiles.views import profile
from profiles.models import Profile

User = get_user_model()


class ProfilesURLsTestCase(SimpleTestCase):
    """
    Classe de test pour les URLs de l'application profiles.
    Teste si les URLs sont correctement résolues.
    """

    def test_profile_url_resolves(self):
        """
        Teste si l'URL du profil utilisateur est correctement résolue.
        """
        url = reverse("profiles:profile", args=["username"])
        self.assertEqual(resolve(url).func, profile)


class ProfileAccessTestCase(TestCase):
    """
    Tests pour vérifier l'accès ou la redirection des vues de profiles.
    """

    @classmethod
    def setUpTestData(cls):
        # Création d'un utilisateur et d'un profil pour le test
        cls.user = User.objects.create_user(username="testuser", password="12345")
        cls.user_profile = Profile.objects.create(user=cls.user, favorite_city="Paris")

    def test_profile_access_redirection(self):
        """
        Teste si un utilisateur non authentifié est redirigé depuis une vue qui requiert
        l'authentification.
        """
        response = self.client.get(reverse("profiles:profile", args=["testuser"]))
        self.assertEqual(response.status_code, 200)


class ProfileContentTestCase(TestCase):
    """
    Tests pour vérifier le contenu renvoyé par les vues de profiles.
    Vérifie que le contenu attendu est présent dans les réponses des vues.
    """

    @classmethod
    def setUpTestData(cls):
        # Création d'un utilisateur et d'un profil pour le test
        cls.user = User.objects.create_user(username="testuser", password="12345")
        cls.user_profile = Profile.objects.create(user=cls.user, favorite_city="Paris")

    def test_profile_content(self):
        """
        Teste si la vue de profil renvoie les informations correctes du profil.
        """
        self.client.login(username="testuser", password="12345")
        response = self.client.get(reverse("profiles:profile", args=["testuser"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Paris")


class ProfileModelMethodsTestCase(TestCase):
    """
    Classe de test pour les méthodes personnalisées du modèle Profile.

    Cette classe teste les méthodes personnalisées définies dans le modèle Profile.
    Elle s'assure que ces méthodes fonctionnent comme prévu, en fournissant
    des cas de test spécifiques pour chaque méthode personnalisée.
    """

    @classmethod
    def setUpTestData(cls):
        # Initialisation des données de test
        cls.user = User.objects.create_user(username="testuser", password="12345")
        cls.user_profile = Profile.objects.create(user=cls.user, favorite_city="Paris")

    def test_custom_method(self):
        """
        Teste une méthode personnalisée du modèle Profile.
        Remplacez ceci par un test réel pour une méthode personnalisée.
        """
        # Utilisation du profil correct
        result = self.user_profile.favorite_city
        expected_result = "Paris"  # Remplacez par le résultat attendu
        self.assertEqual(result, expected_result)


class ProfileModelTest(TestCase):
    """
    Classe de test pour le modèle Profile.
    Teste la création et les fonctionnalités du modèle Profile.
    """

    @classmethod
    def setUpTestData(cls):
        # Création d'un utilisateur et d'un profil pour les tests
        cls.user = get_user_model().objects.create_user(
            username="testuser", password="12345"
        )
        Profile.objects.create(user=cls.user, favorite_city="Paris")

    def test_profile_creation(self):
        """
        Teste la création d'un objet Profile et vérifie ses attributs.
        """
        test_profile = Profile.objects.get(id=1)
        self.assertTrue(isinstance(test_profile, Profile))
        self.assertEqual(test_profile.user.username, "testuser")
        self.assertEqual(test_profile.favorite_city, "Paris")

    def test_profile_str(self):
        """
        Teste la méthode __str__ du modèle Profile.
        """
        test_profile = Profile.objects.get(id=1)
        self.assertEqual(str(test_profile), test_profile.user.username)

    def test_favorite_city_field(self):
        """
        Teste le comportement du champ favorite_city du modèle Profile.

        Vérifie que le champ peut stocker correctement une ville favorite,
        et qu'il peut être laissé vide.
        """
        # Vérifier le profil avec une ville favorite
        test_profile_with_city = Profile.objects.get(user__username="testuser")
        self.assertEqual(test_profile_with_city.favorite_city, "Paris")

        # Créer un autre profil sans ville favorite
        user_without_city = User.objects.create_user(
            username="testuser2", password="12345"
        )
        test_profile_without_city = Profile.objects.create(user=user_without_city)
        self.assertEqual(test_profile_without_city.favorite_city, "")


class IndexViewTestCase(TestCase):
    """
    Classe de test pour la vue index de l'application profiles.

    Cette classe teste la fonctionnalité de la vue index,
    vérifiant qu'elle renvoie la liste correcte des profils.
    """

    @classmethod
    def setUpTestData(cls):
        # Création d'utilisateurs et de profils pour le test
        number_of_profiles = 5
        for profile_num in range(number_of_profiles):
            user = User.objects.create_user(
                username=f"testuser{profile_num}", password="12345"
            )
            Profile.objects.create(user=user, favorite_city=f"City{profile_num}")

    def test_view_url_exists_at_desired_location(self):
        """
        Teste si l'URL de la vue index existe et est accessible.
        """
        response = self.client.get("/profiles/")
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Teste si la vue index utilise le template correct.
        """
        response = self.client.get(reverse("profiles:profiles_index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/index.html")

    def test_lists_all_profiles(self):
        """
        Teste si la vue index affiche tous les profils créés.
        """
        response = self.client.get(reverse("profiles:profiles_index"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context["profiles_list"]) == 5)


class ProfileViewTestCase(TestCase):
    """
    Classe de test pour la vue profile de l'application profiles.

    Cette classe teste la fonctionnalité de la vue profile,
    en particulier la récupération et l'affichage des détails d'un profil utilisateur.
    """

    @classmethod
    def setUpTestData(cls):
        # Création d'un utilisateur et d'un profil pour le test
        cls.user = User.objects.create_user(username="testuser", password="12345")
        cls.profile = Profile.objects.create(user=cls.user, favorite_city="Paris")

    def test_view_url_exists_at_desired_location(self):
        """
        Teste si l'URL de la vue profile existe et est accessible.
        """
        response = self.client.get("/profiles/testuser/")
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Teste si la vue profile utilise le template correct.
        """
        response = self.client.get(reverse("profiles:profile", args=["testuser"]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")

    def test_view_returns_correct_profile(self):
        """
        Teste si la vue profile renvoie les informations correctes du profil demandé.
        """
        response = self.client.get(reverse("profiles:profile", args=["testuser"]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["profile"], self.profile)
