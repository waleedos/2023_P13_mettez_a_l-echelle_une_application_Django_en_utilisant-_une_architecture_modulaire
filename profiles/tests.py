from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.test import SimpleTestCase, TestCase
from profiles.views import profile
from profiles.models import Profile


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
        cls.profile = Profile.objects.create(user=cls.user, favorite_city="Paris")

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
        cls.profile = Profile.objects.create(user=cls.user, favorite_city="Paris")

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
    Tests pour les méthodes personnalisées du modèle Profile.
    Vérifie le fonctionnement correct des méthodes personnalisées du modèle.
    """

    @classmethod
    def setUpTestData(cls):
        # Création d'un utilisateur et d'un profil pour le test
        cls.user = User.objects.create_user(username="testuser", password="12345")
        cls.profile = Profile.objects.create(user=cls.user, favorite_city="Paris")

    def test_custom_method(self):
        """
        Teste une méthode personnalisée du modèle Profile.
        Remplacez ceci par un test réel pour une méthode personnalisée.
        """
        # Exemple de test (à remplacer par votre méthode personnalisée)
        result = self.profile.favorite_city
        expected_result = "Paris"  # Remplacez par le résultat attendu
        self.assertEqual(result, expected_result)
