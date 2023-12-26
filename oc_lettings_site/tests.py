from django.test import TestCase, RequestFactory
from django.urls import reverse
from .views import test_500


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
        retourne correctement un code de statut 500 (Internal Server Error) et si le contenu de la
        réponse contient le message d'erreur attendu. Utilise RequestFactory pour simuler la
        requête.
        """
        request = RequestFactory().get("/chemin_qui_provoque_erreur/")
        response = test_500(request)
        self.assertEqual(response.status_code, 500)
        self.assertIn("500 - Internal Server Error", response.content.decode())


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
        Teste si la vue test_500 renvoie correctement une réponse HTTP 500.
        """
        response = self.client.get("/test-500/")
        self.assertEqual(response.status_code, 500)
        self.assertTemplateUsed(response, "500.html")
