# Utiliser une image Python officielle
FROM python:3.9

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .


# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 5000 pour l’application Flask
EXPOSE 5000

# Démarrer l'application Flask
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
