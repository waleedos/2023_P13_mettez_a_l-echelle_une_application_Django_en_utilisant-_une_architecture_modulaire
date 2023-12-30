## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

-------------------------------------------------------------------------------------------------------------------------------
### pylint

pylint --load-plugins pylint_django lettings/

pylint --load-plugins pylint_django .


-------------------------------------------------------------------------------------------------------------------------------
### Couverture des tests

coverage run manage.py test

###  Générer le Rapport de Couverture
```
coverage report
```

Ou pour un rapport en HTML :
```
coverage html
```
-------------------------------------------------------------------------------------------------------------------------------
### Integration de Sentry:
Apres avoir integrer Sentry dans le fichier settins.py, et apres avoir mis et changer sa clé SDN
dans une variable d'environnement (.env), il faut provoquer une erreur pour tester si mon code renvoi bien 
ce que nous attendons vers Sentry : 

#### Étape 1 : Créer une Vue de Test
Créez une vue dans l'un de vos fichiers de vues, par exemple dans views.py de votre application oc_lettings_site :

```
from django.http import HttpResponse

def error_test(request):
    raise Exception("Ceci est une erreur de test pour Sentry.")
    return HttpResponse("Cette réponse ne sera jamais atteinte.")
```

#### Étape 2 : Ajouter l'URL de la Vue de Test
Ajoutez une URL pour cette vue dans votre fichier urls.py. Si vous l'ajoutez dans oc_lettings_site/urls.py, cela ressemblerait à ceci :
```
from django.urls import path
from .views import error_test  # Assurez-vous d'importer la vue

urlpatterns = [
    # Vos autres URL ici...
    path('sentry-test/', error_test, name='sentry-test'),  # Ajoutez cette ligne
]
```

#### Étape 3 : Testez la Vue
Lancez votre serveur de développement Django avec python manage.py runserver.
Ouvrez un navigateur web et accédez à l'URL de la vue de test (par exemple, http://localhost:8000/sentry-test/).
Cette action déclenchera l'exception définie dans votre vue error_test, que Sentry devrait capturer.

-------------------------------------------------------------------------------------------------------------------------------

### CERCLECI
version: 2.1
jobs:
  build:
    docker:
      - image: cimg/python:3.11.7
    working_directory: ~/oc_p13
    environment:
      DJANGO_SETTINGS_MODULE: oc_lettings_site.settings
      # Mettre à jour le PYTHONPATH pour inclure le répertoire du projet
      PYTHONPATH: /home/circleci/oc_p13:/home/oualid/Bureau/oc_p13
    steps:
      - checkout
      - run: pip install -r requirements.txt
      - run:
          name: Initialize Django for Pylint
          command: python -c "import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'oc_lettings_site.settings'; import django; django.setup()"
      - run: pylint --load-plugins pylint_django .
      - run:
          name: Run Tests
          command: coverage run --source='.' manage.py test
      - run:
          name: Check Test Coverage
          command: coverage report --fail-under=80

------------------------------------------------------------------------------------------------------------

### Docker : 

#### Installez Docker avant tout:
Cela depend de votre systeme d'exploitation, mais cela est facile que ce soit sur windows, mac ou linux.

#### Créer votre image du projet docker :
docker build -t orange_county_lettings .

#### (pour la reconstruction de l'image sans utiliser le cache peut résoudre des problèmes inattendus.)
docker build --no-cache -t orange_county_lettings .

#### Créez un compte sur Docker Hub 
oui, sur https://hub.docker.com/

#### Connectez-vous à Docker Hub
depuis votre terminal en utilisant la commande (docker login).

#### Possez votre image ver le repository Docker : 

Taguez votre image Docker avec votre nom d'utilisateur Docker Hub et un tag approprié, par exemple en utilisant le hash de commit ou une version. Utilisez la commande suivante :
```
docker tag orange_county_lettings [votre_nom_utilisateur_docker]/orange_county_lettings:tag
```

Remplacez [votre_nom_utilisateur_docker] par votre nom d'utilisateur Docker Hub et tag par le tag que vous souhaitez utiliser.
Poussez l'image sur Docker Hub en utilisant la commande :
```
docker push [votre_nom_utilisateur_docker]/orange_county_lettings:1.0
```

Dans mons cas, voici la commande complete : 
```
docker push waleedos/orange_county_lettings:1.0
```

#### Téléchargez l'image depuis Docker Hub :
```
sudo docker pull waleedos/orange_county_lettings:1.0

```
#### Pour démarrer le projet sur votre machine : 
```
sudo docker run -p 8000:8000 waleedos/orange_county_lettings:1.0

et

ouvrez votre navigateur, et allez sur la page : 127.0.0.1:8000

```

