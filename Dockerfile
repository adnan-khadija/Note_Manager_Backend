# Base Python image
FROM python:3.11-slim

# Empêche Python de générer des fichiers pyc
ENV PYTHONDONTWRITEBYTECODE=1
# Force l'affichage des logs (pas de buffering)
ENV PYTHONUNBUFFERED=1

# Dossier de travail
WORKDIR /app

# Installer les dépendances système nécessaires pour PostgreSQL et compilations
RUN apt-get update \
  && apt-get install -y gcc libpq-dev build-essential python3-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Copier uniquement les dépendances d'abord (optimisation du cache)
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

# Copier tout le code source
COPY . .

# Exposer le port utilisé par uvicorn
EXPOSE 8000

# Commande pour démarrer l'application FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
