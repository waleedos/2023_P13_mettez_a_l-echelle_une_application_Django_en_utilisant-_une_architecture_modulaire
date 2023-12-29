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

from django.test import TestCase
from django.urls import reverse


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
