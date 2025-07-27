# Notes App

Application web de prise de notes avec partage, authentification et interface moderne (Next.js + FastAPI + PostgreSQL).
Cette partie est backend:
Vous pouvez consulter le code frontend ici :  
[Fronted]([https://github.com/adnan-khadija/Note_Manager_Frontend)


---

## 📝 Fonctionnalités principales

- **Authentification JWT**  
  Gestion sécurisée des utilisateurs avec des tokens JSON Web Tokens pour l’accès aux ressources.

- **Création, édition, suppression de notes**  
  Interface complète pour gérer vos notes personnelles facilement.

- **Partage de notes avec d'autres utilisateurs**  
  Possibilité de partager des notes spécifiques avec d’autres comptes.

- **Notes publiques via lien unique**  
  Génération de liens publics permettant l’accès aux notes sans authentification.

- **Recherche et filtres dynamiques**  
  Outils puissants pour rechercher et filtrer rapidement vos notes selon différents critères.

- **Interface responsive et moderne**  
  Design adaptatif compatible desktop et mobile pour une expérience utilisateur optimale.
unique_
_Recherche et filtres_

## 🎬 Démonstration
_Connexion_
<img width="1875" height="890" alt="image" src="https://github.com/user-attachments/assets/b4812d2b-53c6-49fe-a037-007ee05c623f" />
_Inscription_
<img width="1875" height="890" alt="image" src="https://github.com/user-attachments/assets/a8dca41a-d453-4966-9767-f2c008d4971a" />
_Aucuiel_
<img width="1875" height="890" alt="image" src="https://github.com/user-attachments/assets/680d4917-fb05-4c94-95a4-50e6c3343dd2" />
_Liste des notes_
<img width="1875" height="890" alt="image" src="https://github.com/user-attachments/assets/89ed0a87-a9e7-44ff-b618-cf41f3873017" />

<img width="1875" height="890" alt="image" src="https://github.com/user-attachments/assets/3e4dd939-46fd-4eac-9533-16d8228603c3" />
_Recherche par tage et titre_
<img width="1875" height="890" alt="image" src="https://github.com/user-attachments/assets/51263d7f-812d-4eca-b7e4-0edeab5afde5" />
_Filtre par status_
<img width="1875" height="890" alt="image" src="https://github.com/user-attachments/assets/604f3903-afeb-4d7d-92f2-4f0cb848e34a" />

## 🛠️ Technologies utilisées

- **Frontend**  
  - [Next.js](https://nextjs.org/) : Framework React pour le rendu côté serveur (SSR) et la création d’interfaces modernes et performantes  
  - [React](https://reactjs.org/) : Bibliothèque JavaScript pour construire l’interface utilisateur  
  - [Tailwind CSS](https://tailwindcss.com/) (optionnel) : Framework CSS utilitaire pour un style rapide et réactif

- **Backend**  
  - [FastAPI](https://fastapi.tiangolo.com/) : Framework Python moderne pour créer des API REST rapides et performantes  
  - [Uvicorn](https://www.uvicorn.org/) : Serveur ASGI ultra-rapide pour exécuter FastAPI  
  - [Pydantic](https://pydantic.dev/) : Validation des données et gestion des modèles  
  - [Tortoise ORM](https://tortoise.github.io/) (selon votre choix) : ORM pour la gestion des bases de données relationnelles

- **Base de données**  
  - [PostgreSQL](https://www.postgresql.org/) : Base de données relationnelle puissante et open source

- **Conteneurisation & Orchestration**  
  - [Docker](https://www.docker.com/) : Conteneurisation des applications backend et frontend  
  - [Docker Compose](https://docs.docker.com/compose/) : Orchestration des services conteneurisés

- **Authentification & Sécurité**  
  - JSON Web Tokens (JWT) : Gestion sécurisée des sessions et authentification utilisateur

---


## Structure du projet 
 ```bash
backend/
  api/
  db/
  main.py
  requirements.txt
frontend/
  app/
  components/
  context/
  lib/
  public/
  next.config.js
  package.json
 docker-compose.yml
```
## 🚀 Lancer le projet

### 1. **Test en local**

#### **Backend**

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000


cd frontend
npm install
npm run dev
# Accède à http://localhost:3000
Backend (API docs) : http://localhost:8000/docs



## Auteur
[Khadija ADNAN](https://github.com/adnan-khadija)

