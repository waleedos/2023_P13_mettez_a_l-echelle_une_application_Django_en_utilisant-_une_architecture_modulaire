Structure de la base de données
-------------------------------

S'assurer que vous etes dans le repertoire du projet :
   .. code:: shell

       cd [Nom_du_répertoire_du projet]


Ouvrez une session Shell pour sqlite :
   .. code:: shell

       sqlite3


Connecter vous à la base de données :
   .. code:: shell

       .open oc-lettings-site.sqlite3


Afficher les tables dans la base de données :
   .. code:: shell

       .tables


Afficher par exemple les colonnes dans le tableau des profils :
   .. code:: shell

       PRAGMA table_info("profiles_profile");


Lancer une requête sur la table des profils pour filtrer uniquement les enregistrements où la valeur de la colonne favorite_city commence par la lettre 'B' :
   .. code:: shell

       select user_id, favorite_city from profiles_profile where favorite_city like 'B%';



**Voici le diagramme de notre base de données**

.. image:: docs/source/images/diagramme.png
   :align: center

