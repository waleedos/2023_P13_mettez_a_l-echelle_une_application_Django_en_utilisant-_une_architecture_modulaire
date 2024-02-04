Demarrage avec Docker
---------------------

Vous pouvez démarrer l'application sur votre ordinateur directement et tres facilement avec docker, sans avoir à configurer un environnement virtuel ou quoi que ce soit :

**Démarrez Docker (s’il ne fonctionne pas déjà en arrière-plan).**

**1- Vérifiez le status de docker :**

.. code:: shell
    
    sudo systemctl status docker


**2- Si docker ne fonctionne pas déjà en arrière-plan, démarrez le:**

.. code:: shell
    
    sudo systemctl restart docker


**3- Télécharger le tout dernier (Tag) avec la commande suivante:**

.. code:: shell
    
    docker pull waleedos/orange_county_lettings:latest


.. Note::

    *Vous ne verrez PAS de nouveau fichier dans votre dossier, mais l’image est automatiquement téléchargée dans un conteneur correspondant à un Docker et apparaîtra directement dans le logiciel Docker-Desktop (si vous l'avez installer).*



**4- Démarrer et executer cette dernière image téléchargée:**

.. code:: shell

    docker run -p 8000:8000 waleedos/orange_county_lettings:latest

L’image est en cours d’exécution. Vous devriez voir des lignes similaires à celles ci-dessous :



**5- Ouvrez votre navigateur et connectez-vous à l’application via:** 

.. code:: shell

    http://127.0.0.1:8000/ 
    
    ou 
    
    http://localhost:8000/


*Une fois que vous avez terminé, et si vous utilisez l'application Docker-desktop, vous pouvez soit appuyer sur le bouton d’arrêt (le carré), soit appuyer directement sur la poubelle, ce qui arrêtera la course et supprimera le conteneur actuel.*

--    
.. Fin du document