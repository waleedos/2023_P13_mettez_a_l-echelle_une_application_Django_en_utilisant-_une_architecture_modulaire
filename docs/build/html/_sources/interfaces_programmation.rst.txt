Les Interfaces de Programmation
-------------------------------


**Interfaces de Programmation pour l'application (oc_lettings_site)**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**1- Page d'Accueil :**

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

.. code-block:: html

    <html>
        <head>
            <title>Page d'Accueil</title>
        </head>
        <body>
            <h1>Bienvenue sur le site OC Lettings</h1>
        </body>
    </html>       


**2- Test d'Erreur 404 :**

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
        
.. code-block:: html

    <html>
        <head>
            <title>Erreur 404</title>
        </head>
        <body>
            <h1>Page non trouvée</h1>
        </body>
    </html>


**3- Test d'Erreur 500 :**

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

.. code-block:: html

    <html>
        <head>
            <title>Erreur 500</title>
        </head>
        <body>
            <h1>Erreur interne du serveur</h1>
        </body>
    </html>
                  


**Interfaces de Programmation pour l'application (lettings)**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**1- Endpoint /lettings/ (URL lettings_index):**

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



**2- Endpoint /lettings/<letting_id>/ (URL letting):**

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


**Interfaces de Programmation pour l'application (profiles)**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**1- Liste des Profils**

        +------------------+----------------------------------------------------------------------------------------------+
        | **URL et Méth.** | URL : /profiles/                                                                             |
        | **HTTP**         | Méthode : GET                                                                                |
        +------------------+----------------------------------------------------------------------------------------------+
        | **Description**  | Cette interface affiche une liste de tous les profils d'utilisateurs.                        |
        +------------------+----------------------------------------------------------------------------------------------+
        | **Rép. Att.**    | La réponse est une page HTML (profiles/index.html) affichant la liste des profils. Chaque    |
        |                  | profil est obtenu à partir du modèle Profile qui est lié au modèle utilisateur standard de   |
        |                  | Django.                                                                                      |
        +------------------+----------------------------------------------------------------------------------------------+

        Exemple de Code pour la Vue index dans views.py :

.. code:: shell

    def index(request):
        logger.info("Affichage de la liste des profils.")
        profiles_list = Profile.objects.all()
        context = {"profiles_list": profiles_list}
        return render(request, "profiles/index.html", context)


**2- Détails d'un Profil Spécifique**

        +------------------+----------------------------------------------------------------------------------------+
        | **URL et Méth.** | URL : /profiles/<username>/                                                            |
        | **HTTP**         | Méthode : GET                                                                          |
        +------------------+----------------------------------------------------------------------------------------+
        | **Description**  | Cette interface affiche les détails d'un profil utilisateur spécifique. Le username    |
        |                  | est passé en tant que paramètre dans l'URL.                                            |
        +------------------+----------------------------------------------------------------------------------------+
        | **Rép. Att.**    | La réponse est une page HTML (profiles/profile.html) affichant les détails du profil   |
        |                  | spécifié. Les détails incluent le nom d'utilisateur et la ville favorite.              |
        +------------------+----------------------------------------------------------------------------------------+

        Exemple de Code pour la Vue profile dans views.py :

.. code:: shell

    def profile(request, username):
        logger.info(f"Affichage du profil pour l'utilisateur : {username}")
        profile_instance = get_object_or_404(Profile, user__username=username)
        context = {"profile": profile_instance}
        return render(request, "profiles/profile.html", context)


**Conclusion sur les Interfaces de Programmation du Projet OC Lettings**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le projet OC Lettings, structuré autour des applications Django oc_lettings_site, lettings, et profiles, présente une architecture claire et modulaire, facilitant la compréhension et l'interaction avec ses différentes composantes. Chaque application encapsule des fonctionnalités spécifiques, exposées via des interfaces de programmation bien définies.

L'application oc_lettings_site sert de point d'entrée principal, orchestrant les interactions globales et dirigeant les utilisateurs vers les fonctionnalités pertinentes des applications lettings et profiles. L'application lettings gère efficacement les données relatives aux locations, offrant des interfaces pour afficher la liste des locations disponibles et les détails de chaque location. En parallèle, l'application profiles se concentre sur la gestion des profils utilisateurs, avec des interfaces pour visualiser la liste des profils et les détails spécifiques à chaque utilisateur.

La documentation des interfaces de ces applications met en lumière la manière dont elles interagissent avec les utilisateurs et les données. Les exemples de code fournis pour chaque endpoint illustrent concrètement comment les requêtes sont traitées et comment les réponses sont structurées, offrant ainsi une compréhension approfondie du fonctionnement interne de l'application.

En somme, ce projet démontre une application robuste et bien structurée de Django, où chaque composant joue un rôle clé dans la fourniture d'une expérience utilisateur fluide et cohérente. La clarté des interfaces de programmation et la modularité du code favorisent une maintenance aisée et une évolutivité efficace, éléments cruciaux pour le succès continu du projet OC Lettings.

.. Fin du document