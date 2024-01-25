Documentation des Interfaces de Programmation
---------------------------------------------


#. **Interfaces de Programmation pour l'application (oc_lettings_site)**

    A- Page d'Accueil :

        +-------------------+------------------------------------------------+
        | **Description**   | Affiche la page d'accueil du site.             |
        +-------------------+------------------------------------------------+
        | **URL et Params** | /                                              |
        +-------------------+------------------------------------------------+
        | **Méthode HTTP**  | GET                                            |
        +-------------------+------------------------------------------------+
        | **Données Req.**  | Aucune                                         |
        +-------------------+------------------------------------------------+
        | **Réponse Att.**  | Page HTML de l'accueil                         |
        +-------------------+------------------------------------------------+

        Exemple de Réponse:
        .. code:: shell

            <html>
            <head>
                <title>Page d'Accueil</title>
            </head>
            <body>
                <h1>Bienvenue sur le site OC Lettings</h1>
            </body>
            </html>       

    B- Test d'Erreur 404 :

        +-------------------+------------------------------------------------------------------+
        | **Description**   | Provoque intentionnellement une erreur 404 pour tester la        |
        |                   | gestion des erreurs.                                             |
        +-------------------+------------------------------------------------------------------+
        | **URL et Params** | /test-404/                                                       |
        +-------------------+------------------------------------------------------------------+
        | **Méthode HTTP**  | GET                                                              |
        +-------------------+------------------------------------------------------------------+
        | **Données Req.**  | Aucune                                                           |
        +-------------------+------------------------------------------------------------------+
        | **Réponse Att.**  | Statut: 404 Non Trouvé                                           |
        |                   | Contenu: Page d'erreur personnalisée.                            |
        +-------------------+------------------------------------------------------------------+

        Exemple de Réponse:
        .. code:: shell

           <html>
           <head>
               <title>Erreur 404</title>
           </head>
           <body>
               <h1>Page non trouvée</h1>
           </body>
           </html>

    C- Test d'Erreur 500 :

        +-------------------+------------------------------------------------------------------+
        | **Description**   | Provoque intentionnellement une erreur 500 pour tester la        |
        |                   | gestion des erreurs.                                             |
        +-------------------+------------------------------------------------------------------+
        | **URL et Params** | /test-500/                                                       |
        +-------------------+------------------------------------------------------------------+
        | **Méthode HTTP**  | GET                                                              |
        +-------------------+------------------------------------------------------------------+
        | **Données Req.**  | Aucune                                                           |
        +-------------------+------------------------------------------------------------------+
        | **Réponse Att.**  | Statut: 500 Erreur Interne du Serveur                            |
        |                   | Contenu: Page d'erreur personnalisée.                            |
        +-------------------+------------------------------------------------------------------+

        Exemple de Réponse:
        .. code:: shell

           <html>
           <head>
               <title>Erreur 500</title>
           </head>
           <body>
               <h1>Erreur interne du serveur</h1>
           </body>
           </html>
                  

#. **Interfaces de Programmation pour l'application (lettings)**

    A- Endpoint /lettings/ (URL lettings_index):

        +-------------------+------------------------------------------------------------------+
        | **Description**   | Cette vue affiche une liste de toutes les locations disponibles. |
        |                   | Elle  récupère  toutes les instances  de Letting et les transmet |
        |                   | au template pour affichage.                                      |
        +-------------------+------------------------------------------------------------------+
        | **URL et Params** | /lettings/                                                       |
        +-------------------+------------------------------------------------------------------+
        | **Méthode HTTP**  | GET                                                              |
        +-------------------+------------------------------------------------------------------+
        | **Données Req.**  | Aucune donnée de requête nécessaire.                             |
        +-------------------+------------------------------------------------------------------+
        | **Réponse Att.**  | Structure: Une page HTML rendue affichant une liste des          |
        |                   | locations (lettings).                                            |
        +-------------------+------------------------------------------------------------------+

        Exemple de Réponse:
        .. code:: shell

           lettings_list = Letting.objects.all()
           context = {"lettings_list": lettings_list}
           return render(request, "lettings/index.html", context)
        

    B- Endpoint /lettings/<letting_id>/ (URL letting):

        +-------------------+----------------------------------------------------------------------------------------+
        | **Description**   | Cette vue affiche les détails d'une location spécifique. Elle récupère une instance    |
        |                   | de Letting basée sur l'id fourni et transmet les détails au template.                  |
        +-------------------+----------------------------------------------------------------------------------------+
        | **URL et Params** | /lettings/<letting_id>/ (où letting_id est un entier représentant l'ID du letting).    |
        +-------------------+----------------------------------------------------------------------------------------+
        | **Méthode HTTP**  | GET                                                                                    |
        +-------------------+----------------------------------------------------------------------------------------+
        | **Données Req.**  | letting_id (ID de la location à afficher).                                             |
        +-------------------+----------------------------------------------------------------------------------------+
        | **Réponse Att.**  | Structure: Une page HTML rendue affichant les détails de la location spécifiée.        |
        +-------------------+----------------------------------------------------------------------------------------+

        Exemple de Réponse:
        .. code:: shell

           specific_letting = get_object_or_404(Letting, id=letting_id)
           context = {"title": specific_letting.title, "address": specific_letting.address}
           return render(request, "lettings/letting.html", context)

        Ces informations détaillées permettront une meilleure compréhension de l'interaction avec l'application lettings via ses interfaces. La gestion des erreurs, comme la gestion des cas où un letting spécifique n'est pas trouvé (get_object_or_404), est également intégrée dans les vues.


        