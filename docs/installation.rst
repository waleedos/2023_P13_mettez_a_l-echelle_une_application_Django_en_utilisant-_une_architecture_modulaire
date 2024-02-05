Installation du projet sur votre machine
----------------------------------------

Pour créer un environnement virtuel tout en installant la version de Python 3.11.7 sans affecter la version globale de Python sur votre machine Linux, vous pouvez suivre les étapes ci-dessous. Nous allons détailler chaque étape pour vous aider à comprendre le processus.
Voir la rubrique (Installation de Python 3.11.7 sur votre machine)


**Cloner le Référentiel :**

.. code:: shell

    cd /path/to/put/project/in



**Avec HTTPS**

.. code:: shell

    git clone https://github.com/waleedos/2023_P13_mettez_a_l-echelle_une_application_Django_en_utilisant-_une_architecture_modulaire.git      


**Avec SSH**

.. code:: shell

    git clone git@github.com:waleedos/2023_P13_mettez_a_l-echelle_une_application_Django_en_utilisant-_une_architecture_modulaire.git            




**Dézippé le fichier téléchargé par clone :**

.. code:: shell

    unzip nom_du_fichier.zip


**Allez dans le dossier dézippé :**

.. code:: shell

    cd /path/to/nom_du_dossier_dézippé


.. ATTENTION::

    *Nous recommandons fortement l'utilisation de Python 3.11.7 pour ce projet. Cette version spécifique de Python offre non seulement les dernières fonctionnalités et optimisations du langage, mais elle est également en adéquation avec les dépendances et les exigences du projet.*

    *En alignant l'environnement de développement sur cette version précise, nous assurons la cohérence, la compatibilité des packages et la prévention des problèmes liés aux différences de version.*

    *En outre, l'utilisation de Python 3.11.7 nous permet de tirer pleinement parti des améliorations en termes de performance et de fonctionnalités syntaxiques, optimisant ainsi le développement et l'exécution de l'application.*

    *Pour créer un environnement virtuel tout en installant la version de Python 3.11.7 sans affecter la version globale de Python sur votre machine Linux, vous pouvez suivre les étapes existantes dans la rubrique suivante dans la documentation : "Installation de Python 3.11.7".*

    
Pour plus d'informations, veuillez consulter la section :ref:`guide_installation_version_python`.



**Activez votre environnement virtuel (vide jusqu'à maintenant) :**

.. code:: shell

    source venv/bin/activate


**Installez tous les packets et dépendances de ce projet :**

.. code:: shell

    pip install --requirement requirements.txt


**Démarrez le serveur Django :**

.. code:: shell

    python manage.py runserver


**Aller sur la page du projet dans un navigateur :**

.. code:: shell

    http://localhost:8000

.. Fin du document
