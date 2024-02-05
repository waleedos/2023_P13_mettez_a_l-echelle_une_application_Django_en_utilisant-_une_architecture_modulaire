Déploiement Docker
------------------

**Installation de Docker dans notre projet :**

Vous pouvez installer Docker en utilisant le package Python docker. Voici comment procéder :

.. raw:: html

   <u>Installation de Docker via pip :</u>

Pour installer Docker avec pip, ouvrez un terminal et exécutez les commandes suivantes :

Assurez-vous que pip est à jour

.. code:: shell

    pip install --upgrade pip


# Installez le package Docker

.. code:: shell

    pip install docker


.. raw:: html

   <u>Installation de Docker Compose (optionnel) :</u>

Si vous prévoyez d'utiliser Docker Compose, vous pouvez l'installer également :

.. code:: shell

    pip install docker-compose


.. raw:: html

   <u>Vérification de l'installation :</u>

Une fois l'installation terminée, vous pouvez vérifier si Docker est correctement installé en exécutant la commande :

.. code:: shell
    
    docker --version



**Création d'un compte gratuit sur la plateforme Docker_Hub**

Docker Hub est une plateforme qui permet de stocker et partager des images Docker. La création d'un compte Docker Hub est essentielle si vous souhaitez publier vos propres images Docker ou accéder à celles partagées par d'autres.

.. raw:: html

   <u>Accéder au site Docker Hub :</u>

Ouvrez un navigateur web, et accédez au site officiel de Docker Hub à l'adresse https://hub.docker.com/.

.. raw:: html

   <u>Créer un Compte :</u>

Sur la page d'accueil de Docker Hub, recherchez le bouton "Sign Up" ou "Inscription" et cliquez dessus.

.. raw:: html

   <u>Remplir les Informations :</u>

Vous serez redirigé vers la page d'inscription, remplissez les informations requises, y compris notre nom, notre adresse e-mail et un mot de passe sécurisé. Assurez-vous de choisir un mot de passe fort pour protéger notre compte.

.. raw:: html

   <u>Accepter les Conditions d'Utilisation :</u>

Lisez les conditions d'utilisation de Docker Hub; Cochez la case indiquant que vous acceptez les conditions d'utilisation.

.. raw:: html

   <u>Créer le Compte :</u>

Cliquez sur le bouton "Create Account" ou "Créer le Compte" pour finaliser le processus de création de compte.

.. raw:: html

   <u>Vérification de l'E-mail (le cas échéant) :</u>


Docker Hub peut vous demander de vérifier notre adresse e-mail en vous envoyant un e-mail de confirmation. Dans ce cas, vérifiez notre boîte de réception et suivez les instructions pour confirmer notre compte.

.. raw:: html

   <u>Connexion au Compte :</u>

Une fois le compte créé et éventuellement vérifié, revenez sur la page d'accueil de Docker Hub.

Cliquez sur "Log In" ou "Se Connecter" en haut à droite de la page.

Vous avez maintenant un compte Docker Hub prêt à être utilisé pour stocker, partager et gérer des images Docker. Vous pourrez également publier vos propres images Docker sur Docker Hub pour les rendre accessibles à d'autres utilisateurs.    



**Liaison de notre compte Docker_Hub avec ce projet**

Pour intégrer Docker à notre projet, vous devez créer un Dockerfile à la racine de notre projet. Ce fichier contiendra toutes les instructions nécessaires pour construire l'image Docker de notre application. De plus, vous aurez besoin d'un fichier de démarrage (start.sh dans ce cas) pour lancer notre application Django.

.. raw:: html

   <u>Création du Dockerfile : </u>

Tout d'abord, assurez-vous d'avoir un fichier Dockerfile à la racine de notre projet. Vous pouvez créer un nouveau fichier avec l'extension ".Dockerfile" ou simplement "Dockerfile".

.. raw:: html

   <u>Contenu du Dockerfile :</u>

Le Dockerfile que vous avez fourni est un excellent exemple. Voici une explication détaillée des différentes parties de ce Dockerfile :

.. code:: docker

   # Utilisation de l'image de base Python 3.11
   FROM python:3.11

   # Définition du répertoire de travail dans le conteneur
   WORKDIR /oc-p13

   # Copie du fichier requirements.txt dans le conteneur
   COPY requirements.txt .

   # Installation des dépendances
   RUN pip install --no-cache-dir -r requirements.txt

   # Copie du reste du code source de l'application dans le conteneur
   COPY . .

   # Exécution de collectstatic
   RUN python manage.py collectstatic --noinput

   # Rendre le script de démarrage exécutable et le copier dans le conteneur
   COPY start.sh /start.sh
   RUN chmod +x /start.sh

   # Exposition du port 8000
   EXPOSE 8000

   # Commande pour démarrer l'application
   CMD ["/start.sh"]


.. Note::

   - Ce Dockerfile commence par utiliser l'image de base Python 3.11. Il définit également le répertoire de travail dans le conteneur, copie le fichier requirements.txt (qui contient les dépendances de notre application) dans le conteneur, et installe ces dépendances avec la commande RUN pip install.

   - Ensuite, il copie le reste du code source de notre application dans le conteneur, exécute collectstatic pour rassembler les fichiers statiques, rend le script start.sh exécutable, et expose le port 8000.

   - Enfin, la commande CMD spécifie comment démarrer l'application en exécutant le script start.sh.



.. raw:: html

   <u>Création du Fichier start.sh : </u>

Le fichier start.sh est utilisé pour démarrer notre application Django. Voici son contenu :

.. code:: shell

    python manage.py collectstatic --noinput
    python manage.py runserver 0.0.0.0:8000

Ce script effectue les étapes suivantes :

Exécute collectstatic pour rassembler les fichiers statiques de notre application.

Lance le serveur Django en écoutant sur l'adresse 0.0.0.0 et le port 8000.


.. Note::

   Assurez-vous que ce fichier est également à la racine de notre projet.


En suivant ces étapes, vous avez correctement configuré Docker pour notre projet Django, créé un Dockerfile détaillé et un fichier de démarrage start.sh pour lancer notre application dans un conteneur Docker.


**Construction de l'Image Docker**

Cette étape consiste à créer une image Docker de notre application. Le Dockerfile à la racine de notre projet contient les instructions nécessaires pour assembler cette image. Cette image sera utilisée pour exécuter notre application dans n'importe quel environnement Docker.

Pour créer l'image Docker, vous utiliserez la commande suivante dans notre terminal :

.. code:: shell

    docker build -t waleedos/orange_county_lettings:latest .

- docker build : C'est la commande principale pour construire une image Docker.
- -t : Cette option permet de spécifier un nom et une étiquette (tag) pour l'image. Dans cet exemple, l'image est nommée "waleedos/orange_county_lettings" avec l'étiquette "latest".
- . : Le point à la fin de la commande indique que le Dockerfile se trouve dans le répertoire actuel.

Exécution du Dockerfile : Lorsque vous exécutez la commande de construction, Docker lit le Dockerfile et suit les instructions à l'intérieur pour construire l'image. Voici ce que fait chaque instruction dans le Dockerfile :

- FROM python:3.11 : Spécifie l'image de base à utiliser, dans ce cas, Python 3.11.
- WORKDIR /oc-p13 : Définit le répertoire de travail à "/oc-p13" dans le conteneur.
- COPY requirements.txt . : Copie le fichier "requirements.txt" depuis le répertoire local dans le répertoire actuel du conteneur.
- RUN pip install --no-cache-dir -r requirements.txt : Installe les dépendances en utilisant pip.
- COPY . . : Copie tout le code source de l'application dans le conteneur.
- RUN python manage.py collectstatic --noinput : Exécute la commande "collectstatic" pour rassembler les fichiers statiques de l'application.
- COPY start.sh /start.sh : Copie le script de démarrage "start.sh" dans le conteneur.
- RUN chmod +x /start.sh : Rend le script de démarrage exécutable.
- EXPOSE 8000 : Indique que le conteneur écoutera sur le port 8000.
- CMD ["/start.sh"] : Spécifie la commande à exécuter lorsque le conteneur est démarré, ici, il exécute "start.sh".

.. Note::

    *Tager les images Docker avec un label distinct, tel que le "hash" de commit, est une bonne pratique pour identifier de manière unique chaque version de l'image.* *Cela permet de garder une trace de quelle version de votre code source a été utilisée pour construire une image spécifique.* *Voici comment vous pouvez ajouter un label lors de la création de l'image Docker :*

Supposons que vous souhaitez utiliser le "hash" de commit Git comme label. Voici comment vous pouvez le faire :

.. raw:: html

   <u>Obtenir le "hash" du dernier commit :</u>

Avant de créer l'image Docker, obtenez le "hash" du dernier commit Git que vous souhaitez utiliser comme label. Vous pouvez le faire en utilisant la commande Git suivante :

.. code:: shell

    git rev-parse HEAD

Cette commande renverra le "hash" du dernier commit, par exemple : 3b18e51a4b5e80632e35a15a02e62a57f33a891d

Modifier la commande de construction de l'image Docker : Lors de la construction de l'image Docker, ajoutez l'option --build-arg pour transmettre le "hash" de commit en tant qu'argument de construction. Vous pouvez également utiliser l'option -t pour spécifier le nom et l'étiquette de l'image comme vous l'avez fait précédemment.

.. Note::

    Vous n'êtes pas obligé de rentrer toute la longueur du "hash" de commit Git lorsque vous l'utilisez comme label pour votre image Docker. En fait, il est courant de ne saisir que les 7 premiers caractères du "hash" qui sont suffisamment uniques pour identifier de manière distincte un commit. La longueur du "hash" que vous devez spécifier dépend de la longueur du préfixe nécessaire pour qu'il soit unique dans votre référentiel Git.

    Par exemple, un "hash" de commit complet pourrait ressembler à ceci : 3b18e51a4b5e80632e35a15a02e62a57f33a891d. 
    
    Cependant, pour l'utiliser comme label, vous pouvez simplement spécifier les 7 premiers caractères.


Voici comment cela pourrait ressembler :

.. code:: shell

   docker build -t waleedos/orange_county_lettings:latest --build-arg COMMIT_HASH=3b18e51 .


.. Note::

    Vous pouvez tagez la meme image docker existante avec une autre étiquette s'il le faut.


**Publication de l'image sur Docker Hub :**

.. raw:: html

   <u>Connexion à Docker Hub :</u>


Assurez-vous d'être connecté à votre compte Docker Hub en utilisant la commande docker login. Vous devrez saisir vos informations d'identification Docker Hub.

.. code:: shell

    docker login


.. raw:: html

   <u>Publication de l'image sur Docker Hub :</u>


Une fois connecté, vous pouvez publier votre image Docker sur Docker Hub avec la commande suivante, en remplaçant YOUR_COMMIT_HASH par le "hash" du commit correspondant :

.. code:: shell

    docker push waleedos/orange_county_lettings:YOUR_COMMIT_HASH

Cela enverra votre image sur Docker Hub, où d'autres utilisateurs pourront la télécharger.

Une fois cela est fait, votre compte sur ``hub.docker.com`` devrais ressembler à ceci : 

.. image:: source/_static/docker.png
    :align: center


--

.. raw:: html

    <a href="https://raw.githubusercontent.com/waleedos/2023_P13_mettez_a_l-echelle_une_application_Django_en_utilisant-_une_architecture_modulaire/main/docs/source/_static/docker.png" target="_blank">Agrandir et voir cette Image sur une autre plateforme</a>

--    


.. raw:: html

   <u>Vérification de l'image Docker :</u>

Pour tester l'image localement, vous pouvez la télécharger depuis Docker Hub et l'exécuter sur votre machine. Cela vous permettra de vérifier le fonctionnement de l'application dans un environnement similaire à la production.


.. raw:: html

   <u>Téléchargement de l'image depuis Docker Hub :</u>

--

.. Note::

   Vous pouvez télécharger l'image Docker depuis Docker Hub en utilisant la commande docker pull. Assurez-vous de spécifier le bon "hash" du commit que vous avez publié précédemment.

.. code:: shell

    docker pull waleedos/orange_county_lettings:YOUR_COMMIT_HASH



.. raw:: html

   <u>Exécution de l'image localement :</u>

Une fois l'image téléchargée, vous pouvez l'exécuter sur votre machine avec la commande docker run. Assurez-vous de mapper les ports et les volumes appropriés si nécessaire.

.. code:: shell

    docker run -p 8000:8000 -v /chemin/vers/vos/fichiers:/chemin/dans/le/conteneur waleedos/orange_county_lettings:YOUR_COMMIT_HASH

N'oubliez pas de remplacer YOUR_COMMIT_HASH par le "hash" du commit que vous avez réellement utilisé.

Cela lancera l'application dans un conteneur Docker sur votre machine locale, où vous pourrez la tester.

.. raw:: html

   <u>Démarrez le projet sur votre navigateur</u>

.. code:: shell

    http://localhost:8000    
    
    oubien  
    
    http://127.0.0.1:8000
    
     
.. Fin du document