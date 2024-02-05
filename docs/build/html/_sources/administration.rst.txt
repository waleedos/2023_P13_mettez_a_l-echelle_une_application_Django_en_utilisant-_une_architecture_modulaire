Administration pour notre projet Orange County Lettings
-------------------------------------------------------

**Panel d’administration**

Aller sur l’url suivante (dans le cas d’un test en local): 

.. code:: shell

   http://localhost:8000/admin



Connectez-vous en tant qu'administrateur avec les identifiants suivants :

.. code:: shell
   
   user     :  admin
   password :  Abc1234!

L'administration Django est une interface puissante qui permet une gestion aisée des modèles et des données du site.



**Accès à l'Administration :**

   - URL     : /admin/
   - Méthode : GET pour l'accès, POST pour les interactions (ajout, modification, suppression des données).



**Modèle Letting :**

   - Fichier         : lettings/admin.py
   - Classe          : LettingAdmin
   - Configuration   : Les champs address et title du modèle Letting sont affichés dans l'interface d'administration.



**Modèle Profile :**

   - Fichier         : profiles/admin.py
   - Classe          : ProfileAdmin
   - Configuration   : Les champs user et favorite_city du modèle Profile sont affichés dans l'interface d'administration.



**Gestion des Données :**

Les administrateurs peuvent effectuer les actions suivantes dans l'interface d'administration :

   - Ajouter de nouvelles instances pour les modèles Letting et Profile.
   - Modifier les données existantes des instances de ces modèles.
   - Supprimer des instances si nécessaire.



**Sécurité et Accès :**

L'accès à l'interface d'administration est restreint aux utilisateurs ayant des droits d'administrateur. Il est recommandé de gérer attentivement les comptes administrateurs pour maintenir la sécurité du site.

Personnalisation et Extensions :
L'interface d'administration Django est hautement personnalisable. Si des fonctionnalités supplémentaires sont nécessaires (par exemple, des filtres avancés, des champs personnalisés, etc.), elles peuvent être ajoutées en étendant les classes ModelAdmin.

--
.. Fin du document