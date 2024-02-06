<h1 align="center">OC Project N°13 - Orange County Letting's</h1>
<h2 align="center">Mettez à l'échelle une application Django en utilisant une architecture modulaire</h1>

![Logo LITReview](https://raw.githubusercontent.com/waleedos/2023_P13_mettez_a_l-echelle_une_application_Django_en_utilisant-_une_architecture_modulaire/main/docs/source/_static/orange_country_lettings.png)

## Compétences acquises et évaluées de ce projet : 
* Documenter une application
* Re-factoriser une application pour réduire la dette technique
* Mettre en place un système de contrôle des codes en utilisant Sentry
* Déployer une application
* Gérer la production de code en utilisant la méthodologie CI/CD
* Appliquer une architecture modulaire dans une application Python

## Technologies Utilisées
- **Langage Principal** : Python (Version 3.11.7)
- **Framework Web** : Django (version 5.0)
- **Base de Données** : sqlite3 (version 3.37.2)
- **Sécurité** : SECRET_KEY chargée depuis un fichier .env + les validateurs de mot de passe de Django.
- **Gestion de Configuration** : python-dotenv pour charger les configurations depuis un fichier .env.
- **Monitoring** : Sentry SDK et Flake8
- **Tests et Assurance Qualité** : Pytest avec pytest-django, Flake8, pylint, Coverage...
- **Conteneurisation** : Docker.
- **Pipeline CI/CD et déploiement** : CircleCI et Render
- **Documentation** : Sphinx, ReadTheDocs.

Pour plus de détails sur les Technologies Utilisées dans ce projet, suivez ce [lien](https://walid-orange-county-lettings.readthedocs.io/fr/latest/technologies_utilisees.html).

## Introduction :
Orange County Lettings est une start-up dans le secteur de la location de biens immobiliers. La start-up est en pleine phase d’expansion aux États-Unis. L'évaluation des technologies utilisées dans le code de l'ancienne application de la société a identifié différents problèmes que nous devons résoudre. 

## Auteurs
L'équipe est composée de EL-WALID EL-KHABOU et de son mentor OpenClassRooms.

## Licence
Logiciel gratuit.

## Mission
- Refonte de l'architecture modulaire de l'application existante;
- Réduction de diverses dettes techniques sur le projet;
- Ajout d'un pipeline CI/CD ainsi que son déploiement; 
- Surveillance de l’application et suivi des erreurs via Sentry; 
- Création de la documentation technique de l’application avec Read The Docs et Sphinx.

L'équipe a dressé une liste de document pour cette mission : 

- **La Mission** : [Mission](https://github.com/waleedos/2023_P13_mettez_a_l-echelle_une_application_Django_en_utilisant-_une_architecture_modulaire/blob/main/oc_lettings_site/Mission/mission-p13.pdf).
- **Le guide** : [Guide d'étapes clés pour l'avancement du projet](https://github.com/waleedos/2023_P13_mettez_a_l-echelle_une_application_Django_en_utilisant-_une_architecture_modulaire/blob/main/oc_lettings_site/Mission/guide-etapes.pdf) 

### Voici La stucture actuelle et finale de ce projet :

- **La structure du projet** : [La structure du projet](https://walid-orange-county-lettings.readthedocs.io/fr/latest/structure_de_ce_projet.html).

### Apres sa refonte, ce projet est composé de 3 applications : 
- oc_lettings_site : Application initiale pour voir la page d'accueil.
- Lettings         : Application pour voir la liste des locations disponibles et adresses.
- Profiles         : Application pour gérer les profils.


## Vous pouvez voir directement la page d'accueil du projet déployé sur Render en suivant ce [lien](https://oc-p13-a8c2.onrender.com).

### Comment cloner ce référentiel GitHub: 
Vous pouvez cloner et forker le repo en totalité via HTTPS:
``` 
git clone https://github.com/waleedos/2023_P13_mettez_a_l-echelle_une_application_Django_en_utilisant-_une_architecture_modulaire.git
```

Vous pouvez aussi cloner et forker le repo en totalité via SSH:
``` 
git@github.com:waleedos/2023_P13_mettez_a_l-echelle_une_application_Django_en_utilisant-_une_architecture_modulaire.git
```

Ou encore, vous pouvez télécharger le dossier entier compressé (.zip) :
- [Téléchargez le dossier complet de ce projet](https://github.com/waleedos/2023_P13_mettez_a_l-echelle_une_application_Django_en_utilisant-_une_architecture_modulaire/archive/refs/heads/main.zip).

### Accédez à la racine du projet:
```
cd [Nom de votre dossier décompressé ou cloné]
```

### Vérification si vous etes au bon dossier : 
```
ls
```
La sortie de cette commande devra vous afficher les dossiers et fichiers suivant : 

| Nom                       | Type     |
|---------------------------|----------|
| docs/                     | dossier  |
| flake-report/             | dossier  |
| htmlcov/                  | dossier  |
| lettings/                 | dossier  |
| logging/                  | dossier  |
| oc_lettings_site/         | dossier  |
| profiles/                 | dossier  |
| static/                   | dossier  |
| staticfiles/              | dossier  |
| templates/                | dossier  |
| __init__.py               | fichier  |
| Dockerfile                | fichier  |
| manage.py                 | fichier  |
| oc-lettings-site.sqlite3  | fichier  |
| pylint_django_setup.py    | fichier  |
| README.md                 | fichier  |
| requirements.txt          | fichier  |
| setup.cfg                 | fichier  |
| start.sh                  | fichier  |


### Créer un environnement virtuel Python (sur une machine linux):
```
python -m venv venv
```
### Activer l'environnement virtuel Python:
```
source env/bin/activate # Sur Linux/Mac
env\Scripts\activate # Sur Windows
```
### Importez et installez tous les modules:
```
pip install -r requirements.txt
```
### Créer un Fichier .env à la racine du projet (dans le dossier crm_events): 
```
mkdir .env
```
### Générer une nouvelle clé secrète, vous pouvez utiliser la console Python:
- Démarrez la console python 
```
python
# ou
python3
```
- Copier/coller le code suivant et validez :
```
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```
Vous allez voir que python a généréré une SECRET_KEY du style :
```
j^$-6tjo-s45j(6)-_=fmb%p4+2enehxlmsuzy8szmozlhc5^6
```

```
### Remplissez le fichier .env créé avec les informations créés suivantes (à titre d'exemple):
```
SECRET_KEY="votre clé que python viens de générer"

et enregistrer le fichier


### Démarrage du serveur :

Assurez vous que vous etes toujours dans le dossier racine du projet
puis
```
python manage.py runserver
```

### Il est temps maintenant de démarrer l'application sur votre navigateur :
Ouvrez votre navigateur et naviguez vers une des deux adresse suivantes :
```
http://127.0.0.1:8000
```
Pour un access Administrateur

```
http://127.0.0.1:8000/admin
# ou bien
http://localhost:8000/admin
```

### Connectez vous en tant que SuperUtilisateur : 
Remplissez les identifiants (E-mail et Password) (admin, mot de passe Abc1234!) et validez.


## Voir toute la documentation de ce projet :

Suivre ce [lien](https://walid-orange-county-lettings.readthedocs.io/fr/latest/index.html).

#### Powered by EL-WALID EL-KHABOU
```
E-mail : ewek.dev@gmail.com
```


