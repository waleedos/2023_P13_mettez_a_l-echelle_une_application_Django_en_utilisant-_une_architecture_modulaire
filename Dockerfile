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

# Exposition du port 8000
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
