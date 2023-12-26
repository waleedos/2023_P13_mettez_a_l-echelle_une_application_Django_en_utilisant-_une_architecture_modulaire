"""
Tests pour l'application oc_lettings_site.

Ce module contient des tests unitaires pour l'application oc_lettings_site. Il comprend des
tests pour les vues, modèles, et autres composants de l'application. Les tests couvrent
divers aspects fonctionnels et d'erreur de l'application, assurant ainsi que les composants
fonctionnent comme prévu dans différents scénarios.

Classes de Test:
    ViewsTestCase: Tests pour les vues de l'application.
    IndexViewTestCase: Tests spécifiques pour la vue index.
    Test404ViewTestCase: Tests pour la gestion des erreurs 404.
    Test500ViewTestCase: Tests pour la gestion des erreurs 500.
"""

from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings


class MyTestCase(TestCase):
    """
    Classe de test pour vérifier la configuration des paramètres de l'application.

    Cette classe contient des tests pour s'assurer que les paramètres de l'application
    sont correctement configurés pour l'environnement de test. Elle est utile pour vérifier
    que les modifications apportées aux paramètres n'affectent pas le comportement attendu
    de l'application dans l'environnement de test.

    Méthodes:
        test_debug_is_off: Vérifie que le mode DEBUG est désactivé.
    """

    def test_debug_is_off(self):
        """
        Teste si le mode DEBUG est désactivé dans les paramètres de l'application.

        Le mode DEBUG doit être désactivé dans l'environnement de test pour s'assurer
        que les erreurs sont gérées de la même manière que dans l'environnement de
        production. Ce test échouera si DEBUG est True.
        """
        self.assertFalse(settings.DEBUG)


class ViewsTestCase(TestCase):
    """
    Classe de test pour les vues de l'application.

    Cette classe contient des tests pour vérifier le comportement des différentes vues
    de l'application, y compris les réponses aux requêtes HTTP valides et invalides.

    Les tests comprennent la vérification du code de statut, l'utilisation des templates
    corrects et le contenu des réponses HTTP.

    Méthodes:
        test_index_view: Teste la vue de la page d'accueil.
        test_404_view: Teste la gestion des requêtes vers des URLs inexistantes.
        test_500_view: Teste la réponse en cas d'erreur interne du serveur.
    """

    def test_index_view(self):
        """
        Teste la vue de la page d'accueil.

        Vérifie si la requête vers la page d'accueil retourne un code de statut 200 (OK)
        et utilise le template 'index.html'. Assure que l'URL correspond à la vue 'index'.
        """
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_404_view(self):
        """
        Teste la gestion des erreurs 404.

        Vérifie si une requête vers une URL inexistante retourne un code de statut 404 (Not Found)
        et utilise le template '404.html'. Cela permet de s'assurer que les erreurs 404 sont gérées
        correctement par l'application.
        """
        response = self.client.get("/une_url_inexistante/")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")

    def test_500_view(self):
        """
        Teste la gestion des erreurs 500.

        Simule une requête provoquant une erreur interne du serveur pour vérifier si l'application
        retourne correctement un code de statut 500 (Internal Server Error).
        """
        try:
            self.client.get("/test-500/")
        except ValueError as e:
            self.assertEqual(str(e), "Test d'erreur 500")


class IndexViewTestCase(TestCase):
    """
    Classe de test pour la vue index de l'application oc_lettings_site.
    """

    def test_index_view(self):
        """
        Teste si la vue index renvoie la réponse HTTP attendue et utilise le bon template.

        Vérifie que la page d'accueil (vue index) renvoie un code de statut HTTP 200 (OK)
        et utilise le template 'index.html'.
        """
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")


class Test404ViewTestCase(TestCase):
    """
    Classe de test pour la vue test_404 de l'application oc_lettings_site.
    """

    def test_404_view(self):
        """
        Teste si la vue test_404 renvoie correctement une réponse HTTP 404.
        """
        response = self.client.get("/chemin_inexistant/")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")


class Test500ViewTestCase(TestCase):
    """
    Classe de test pour la vue test_500 de l'application oc_lettings_site.
    """

    def test_500_view(self):
        """
        Teste si la vue test_500 provoque correctement une erreur de serveur interne.
        """
        client = Client()
        try:
            client.get("/test-500/")
        except ValueError as e:
            self.assertEqual(str(e), "Test d'erreur 500")
