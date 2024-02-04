Le Linting
----------

**Vérification du code avec le Linting**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Le linting est une étape essentielle dans le maintien et le développement moderne de la qualité du code dans tout projet de développement logiciel garantissant la cohérence du code et le respect des bonnes pratiques. 

Dans le cadre du projet Orange County Lettings, nous utilisons pylint avec des plugins spécifiques à Django et flake8, un outil de linting pour Python qui combine les fonctionnalités de pyflakes, mccabe, et pep8 pour assurer la conformité de notre code aux standards de codage.


**Configuration de l'Environnement Python :**

La commande 

.. code:: shell

	export PYTHONPATH=$PYTHONPATH:[chemin_exact_du_projet_/oc_p13

est utilisée pour ajouter le répertoire de notre projet au PYTHONPATH. Cela permet aux outils comme pylint de reconnaître correctement les modules de notre projet lors de l'exécution de l'analyse.



**Exécution de Pylint avec des Plugins Django :**

La commande 

.. code:: shell

	pylint --load-plugins pylint_django . 

est la commande pour exécuter pylint tout en chargeant les plugins spécifiques à Django. Cela permet à pylint d'analyser plus efficacement le code Django en tenant compte de ses particularités.

- L'option --load-plugins pylint_django active des fonctionnalités spécifiques à Django, comme la reconnaissance des modèles Django et des configurations spéciales.

- Le (.) à la fin de la commande indique à pylint de vérifier tous les fichiers Python dans le répertoire actuel (et ses sous-répertoires).

Cela nous permet une meilleure reconnaissance des modèles Django, des champs de base de données, et des spécificités de Django qui ne sont pas présents dans les projets Python standards.


L'exécution de cette commande dans le répertoire racine du projet (indiqué par .) permet à pylint de parcourir l'ensemble du projet, y compris les applications Django, et d'identifier les problèmes potentiels tels que les erreurs de syntaxe, les problèmes de style, les erreurs de codage, et autres non-conformités aux bonnes pratiques.

En intégrant ces étapes de linting dans notre flux de travail, nous nous assurons que le code de notre projet est non seulement fonctionnel mais aussi propre, bien organisé et conforme aux standards de codage Python et Django. Cela facilite la maintenance du code, améliore sa lisibilité et contribue à une base de code de haute qualité.

Voici l'assurance que nous donne l'éxecution de cette commande : 

--

.. image:: source/_static/linting.png
   :align: center

--


**Flake8 & la qualité du code**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Flake8, en 2024, demeure un outil essentiel pour la programmation Python, combinant les fonctionnalités de pyflakes, mccabe, et pep8.*

*Il est utilisé pour vérifier le style de codage et la qualité logique du code Python.* 

*Flake8 aide les développeurs à identifier les erreurs potentielles, les styles de codage non conformes aux normes PEP 8, et les problèmes de complexité.* 

*Il facilite la maintenance du code en assurant une cohérence stylistique et en améliorant sa lisibilité.* 

*Il est largement intégré dans les environnements de développement intégrés (IDE) et les pipelines CI/CD, renforçant les pratiques de codage propre et efficace.*


**Configuration de flake8**

*Avant de penser à la configuration de flake8, il faut d'abord l'installer dans l'environnement virtuel du projet ainsi que ses composantes.*
*Pour cela utilisez les commandes suivantes :*

.. code:: shell

   pip install flake8

   et

   pip install flake8-html


Afin d'élaborer un rapport de toutes les erreurs exisatntes et pouvoir les corriger, il faut d'abord configurer flake8.

Pour cela, il faut créer un fichier nommé ".flake8" à la racine du projet, et dans l'exemple de ce projet, voici le contenu de ce fichier : 

.. code:: shell

    [flake8]
    max-line-length = 99
    exclude = venv, .git, .gitignore, __pycache__, env, vmigrations, migrations


Maintenant que tout les reglages sont faits, nous pouvons utiliser la commande suivante, qui garce à la quelle, un dossier nommé *flake-report* va etre créé à la racine du projet, et nous trouverons dedans un fichier *index.html* consultable dans un navigateur, pour voir toutes les erreurs détéctées en détails : 

.. code:: shell
    
    flake8 --format=html --htmldir=flake-report


--

.. image:: source/_static/flake8.png
   :align: center

--

.. raw:: html

    <a href="https://raw.githubusercontent.com/waleedos/2023_P13_mettez_a_l-echelle_une_application_Django_en_utilisant-_une_architecture_modulaire/main/docs/source/_static/flake8.png" target="_blank">Agrandir et voir cette Image sur une autre plateforme</a>

--    
.. Fin du document