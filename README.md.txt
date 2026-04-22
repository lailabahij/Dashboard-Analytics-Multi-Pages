# 📊 FinanceCore Dashboard – Data Visualization & Storytelling

## 📌 Contexte du projet

Après avoir :

* Nettoyé les données
* Structuré et stocké les données dans PostgreSQL

L’entreprise **FinanceCore SA** souhaite exploiter ces données via un **dashboard interactif** afin d’aider les décideurs à analyser la performance commerciale.

Ce projet s’inscrit dans une démarche de **Data Visualization & Data Storytelling** pour transformer les données en insights exploitables.

---

## 🎯 Objectifs

* Se connecter à PostgreSQL depuis Python
* Extraire les données via SQLAlchemy
* Calculer des statistiques descriptives
* Construire des KPIs métier
* Créer des visualisations interactives
* Développer un dashboard avec Streamlit
* Implémenter des filtres dynamiques
* Suivre le projet via Jira

---

## 👤 User Story

> En tant qu’équipe Data Analysts, nous devons développer un dashboard interactif permettant aux équipes métiers d’analyser la performance des ventes et la rentabilité.

---

## 🛠️ Technologies utilisées

* Python 3.x
* Streamlit
* PostgreSQL
* SQLAlchemy
* Pandas
* Plotly / Matplotlib / Seaborn
* Dotenv

---

## 🗄️ Base de données

* Base : `financecore_db`

* Tables principales :

  * `transactions`
  * `clients`
  * `comptes`
  * `produits`
  * `agences`
  * `temps`

* Vues utilisées :

  * `vw_transactions_global`
  * `vw_ca_agence`
  * `vw_anomalies`
  * `vw_transactions_temps`

---

## ⚙️ Fonctionnalités du Dashboard

### 📊 Page 1 — Vue Exécutive

* KPIs :

  * 💰 Chiffre d'affaires total
  * 📦 Nombre de transactions
  * 👥 Nombre de clients
  * 📊 Panier moyen
* Graphiques :

  * Évolution mensuelle (ligne)
  * CA par agence (barres)
  * Répartition par segment (camembert)
* Filtres :

  * Agence
  * Segment
  * Produit

---

### ⚠️ Page 2 — Analyse des Risques

* 📊 Scatter : Score crédit vs montant
* 🧠 Heatmap : Corrélation (score, montant, taux rejet)
* 🚨 Tableau : Top clients à risque

---

## 🔄 Pipeline de données

1. Nettoyage des données (Data Cleaning)
2. Transformation (Feature Engineering)
3. Chargement dans PostgreSQL (ETL)
4. Création des vues SQL
5. Consommation via Streamlit

---

## 📂 Structure du projet

```
financecore_dashboard/
│
├── app.py
├── config/
│   └── db.py
│
├── pages/
│   ├── 1_executive.py
│   └── 2_risk.py
│
├── services/
│   ├── queries.py
│   └── metrics.py
│
├── components/
│   ├── filters.py
│   └── charts.py
│   └── kpis.py
│── utils/
│   ├── export.py
│── config/
│   ├── db.py
│  
├── .env
├── requirements.txt
└── README.md
└── docker-compose.yml
```

---

## 🔌 Connexion à la base

Créer un fichier `.env` :

```
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=financecore_db
```

---

## ▶️ Lancer le projet

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📈 KPIs calculés

* Total CA
* Nombre de transactions
* Nombre de clients actifs
* Panier moyen
* Taux de rejet
* Catégorie de risque client

---

## 📊 Visualisations

* Line chart (évolution temporelle)
* Bar chart (CA par agence)
* Pie chart (segments clients)
* Scatter plot (analyse risque)
* Heatmap (corrélation)

---

## 💡 Améliorations possibles

* Ajout Machine Learning (scoring client)
* Alertes automatiques (fraude / risque)
* Déploiement cloud (Streamlit Cloud)
* Dashboard avancé (animations, design pro)

---

## 📌 Conclusion

Ce projet permet de :

* Transformer des données brutes en insights
* Aider à la prise de décision
* Visualiser la performance en temps réel

---
## 🐳 Déploiement avec Docker

Le projet peut être exécuté facilement avec Docker pour garantir un environnement stable.

---

### 📦 Prérequis

* Docker installé
* Docker Compose installé

---

### ⚙️ Configuration

Créer un fichier `.env` à la racine :

```
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
DB_NAME=financecore_db
```

---

### 📄 Dockerfile

```dockerfile
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

### 📄 docker-compose.yml

```yaml
version: '3.8'

services:

  db:
    image: postgres:15
    container_name: financecore_db
    restart: always
    environment:
      POSTGRES_DB: financecore_db
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  app:
    build: .
    container_name: financecore_app
    depends_on:
      - db
    ports:
      - "8501:8501"
    env_file:
      - .env

volumes:
  postgres_data:
```

---

### ▶️ Lancer le projet

```bash
docker-compose up --build
```

---

### 🌐 Accès au dashboard

```
http://localhost:8501
```

---

### 🛑 Arrêter les containers

```bash
docker-compose down
```

---

### 💡 Notes importantes

* La base PostgreSQL est automatiquement créée
* Les données sont persistées dans un volume Docker
* L’application Streamlit est accessible depuis le navigateur

---


## 👨‍💻 Auteur

**Laila Bahij**
Frontend & Data Enthusiast 🚀

---
