Installation du projet sur votre machine
----------------------------------------

Pour créer un environnement virtuel tout en installant la version de Python 3.11.7 sans affecter la version globale de Python sur votre machine Linux, vous pouvez suivre les étapes ci-dessous. Je vais détailler chaque étape pour vous aider à comprendre le processus.

`Installation de Python 3.11.7 et création de votre environnement virtuel <installation_python_3_11_7_>`_



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


