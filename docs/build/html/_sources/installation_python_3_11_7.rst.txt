.. _guide_installation_version_python:

Installation de Python 3.11.7
-----------------------------

*Cette documentation détaille le processus d'installation de notre projet sur un système d'exploitation Linux.*

*Il est essentiel de noter que le choix de Linux comme environnement de développement et de déploiement est motivé par sa stabilité, sa sécurité, et sa flexibilité, des qualités appréciées dans le développement de logiciels modernes.*

*De plus, nous recommandons fortement l'utilisation de Python 3.11.7 pour ce projet. Cette version spécifique de Python offre non seulement les dernières fonctionnalités et optimisations du langage, mais elle est également en adéquation avec les dépendances et les exigences du projet.*

*En alignant l'environnement de développement sur cette version précise, nous assurons la cohérence, la compatibilité des packages et la prévention des problèmes liés aux différences de version.*

*En outre, l'utilisation de Python 3.11.7 nous permet de tirer pleinement parti des améliorations en termes de performance et de fonctionnalités syntaxiques, optimisant ainsi le développement et l'exécution de l'application.*

*Suivre ces instructions garantit une installation fluide et un environnement de travail idéal pour contribuer efficacement au projet.*

*Pour créer un environnement virtuel tout en installant la version de Python 3.11.7 sans affecter la version globale de Python sur votre machine Linux, vous pouvez suivre les étapes ci-dessous. Je vais détailler chaque étape pour vous aider à comprendre le processus.*




**Étape 1: Télécharger la dernière version de Python**

    .. code:: shell

        sudo apt-get update
        sudo apt-get install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget


    Allez sur le site officiel de `Python <https://www.python.org/>`_ et trouvez l'URL de la dernière version de Python 3 en format .tar.xz.



    Utilisez wget pour télécharger le fichier :

    .. code:: shell

        wget [URL_du_fichier_python.tar.xz]



    Dézipper le fichier téléchargé pour accéder à son contenu :

    .. code:: shell

        tar -xf [Nom_du_fichier_python.tar.xz]



    Accédez au répertoire extrait :

    .. code:: shell

        cd [Nom_du_répertoire_extrait]



**Étape 2: Configurez les options de compilation**

    .. code:: shell

        ./configure --enable-optimizations --prefix=/opt/python3.11


    Compilez Python :

    .. code:: shell

        make -j 4


    Installez Python dans le répertoire /opt :

    .. code:: shell

        sudo make altinstall



**Étape 3: Créer un environnement virtuel**

    Installez le package virtualenv si ce n'est pas déjà fait :

    .. code:: shell

        sudo apt-get install python3-virtualenv


    Créez un répertoire pour votre environnement virtuel :

    .. code:: shell

        mkdir venv


    Créez un environnement virtuel en utilisant la version de Python que vous venez d'installer :

    .. code:: shell

        virtualenv --python=/opt/python3.11/bin/python3.11 venv/


**Étape 4: Activer l'environnement virtuel**

    .. code:: shell
        
        source venv/bin/activate


Vous devriez maintenant avoir un environnement virtuel fonctionnel qui utilise la version 3.11.7 de Python 3 que vous avez installée, sans affecter la version globale de Python sur votre machine Linux.

.. Fin du document