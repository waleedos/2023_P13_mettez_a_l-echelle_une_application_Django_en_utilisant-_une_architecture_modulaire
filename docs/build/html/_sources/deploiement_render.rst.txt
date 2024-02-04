Déploiement Render
------------------

Dans la mission de ce projet, l'auteur nous a donné la possibilité de déployer ce dernier sur des plateforme gratuite comme Render, AWS webapp, Azure, etc...

Nous avons fait le choix de la plateforme `Render <https://dashboard.render.com//>`_ 

Le déploiement d'un projet Django sur Render, après avoir configuré l'intégration continue (CI) et la conteneurisation avec Docker via CircleCI, implique plusieurs étapes et concepts clés. Voici un guide détaillé pour comprendre et exécuter ce processus.


**Prérequis**

- Projet Django : Un projet Django fonctionnel, de préférence versionné avec Git.

- Docker : Une Dockerfile configurée pour conteneuriser votre application Django.

- CircleCI : Un fichier .circleci/config.yml configuré pour automatiser les tests et les builds de votre image Docker.

- Render : Un compte Render pour déployer et héberger votre application.



.. raw:: html

    <u>1. Préparation du projet Django</u>


- **Variables d'environnement** : Assurez-vous que toutes les configurations sensibles sont extraites du code et gérées via des variables d'environnement ``SECRET_KEY``, ``SENTRY_DSN``, etc.

- **Fichiers statiques et médias** : Configurez correctement la gestion des fichiers statiques et médias. Pour les fichiers statiques, ``python manage.py collectstatic`` doit être exécuté lors du déploiement.



.. raw:: html

    <u>2. Conteneurisation avec Docker</u>


- **Dockerfile** : Créez un ``Dockerfile`` à la racine de votre projet pour définir l'environnement de votre application. Ce fichier doit inclure l'installation des dépendances, la collecte des fichiers statiques, et la commande pour lancer votre application.

- **Build et Test** : Utilisez CircleCI pour automatiser le build de votre image Docker et exécuter les tests. Ceci est configuré dans ``.circleci/config.yml``.



.. raw:: html

    <u>3. Configuration de CircleCI</u>


- **.circleci/config.yml** : Configurez ce fichier pour automatiser les tests de votre application à chaque push sur votre dépôt Git et pour construire une image Docker si les tests passent.

- **Intégration avec Docker Hub** : Configurez CircleCI pour pousser l'image Docker construite vers Docker Hub ou un autre registre d'images Docker.



.. raw:: html

    <u>4. Déploiement sur Render</u>


- **Service Web** : Créez un service Web sur Render et choisissez Docker comme environnement (déja existant sur le depot GitHub avec le fichier Dockerfile).

- **Configurez les variables d'environnement** nécessaires pour votre application Django dans Render. Cela inclut ``SECRET_KEY``, ``SENTRY_DSN``, et toute autre variable d'environnement que votre application utilise. Ceci est crucial pour la sécurité et le bon fonctionnement de votre application.


.. image:: source/_static/environnement.png
    :align: center

--


.. raw:: html

    <a href="https://raw.githubusercontent.com/waleedos/2023_P13_mettez_a_l-echelle_une_application_Django_en_utilisant-_une_architecture_modulaire/main/docs/source/_static/environnement.png" target="_blank">Agrandir et voir cette Image sur une autre plateforme</a>
 

--

.. raw:: html

    <u>5. Définissez le port</u>

- **Définissez le port sur lequel votre application sera accessible**. Par défaut, Django utilise le port 8000, que vous avez probablement exposé dans votre Dockerfile.



.. raw:: html

    <u>6. Automatisation du déploiement</u>

- **Déclenchez le déploiement de votre service**. Render construira votre image Docker à partir de la Dockerfile et déploiera votre application.

- **Render supporte le déploiement automatique** à chaque push sur une branche spécifique de votre dépôt GitHub. Assurez-vous d'avoir activé cette option pour automatiser le processus de déploiement de votre application.



.. raw:: html

    <u>7. Mettez à jour les URL's dans settings.py</u>


Il est Impératif que vous mettez à jour la ligne suivante pour le cas de ce projet dans le fichier ``settings.py`` comme suit : 


``ALLOWED_HOSTS = ["127.0.0.1", "localhost", "oc-p13-a8c2.onrender.com"]``



.. image:: source/_static/render.png
    :align: center


--

.. raw:: html

    <a href="https://raw.githubusercontent.com/waleedos/2023_P13_mettez_a_l-echelle_une_application_Django_en_utilisant-_une_architecture_modulaire/main/docs/source/_static/render.png" target="_blank">Agrandir et voir cette Image sur une autre plateforme</a>

--    

.. Fin du document