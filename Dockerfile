FROM python:3.12.2-alpine3.18

# Créer le répertoire de l'application
WORKDIR /app

# Copier le fichier des dépendances depuis le dossier racine
COPY requirements.txt .

# Installer les dépendances
RUN pip install -r requirements.txt

# Copier le code source depuis le dossier src
COPY src/ .

EXPOSE 8080

# Commande par défaut à exécuter lorsque le conteneur démarre
CMD ["python", "main.py"]
