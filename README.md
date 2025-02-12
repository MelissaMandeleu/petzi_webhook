# 🎟️ Petzi Webhook Listener

## 📌 Description
Cette application reçoit et stocke les webhooks envoyés par **Petzi** lorsqu'un ticket est vendu.  
Elle **vérifie la validité** de la requête via **HMAC**, **extrait les données** et les stocke dans une base **PostgreSQL**.

---

## 📌 🔥 Fonctionnalités  

✅ **Réception et vérification des webhooks** (signature HMAC)  
✅ **Stockage des ventes de tickets dans PostgreSQL**  
✅ **Interface web pour visualiser les ventes en direct**  
✅ **Déploiement avec Docker et Docker Compose**  

---

## 📌 🛠 Installation  

### 🔹 1️⃣ **Prérequis**
Avant de commencer, assurez-vous d'avoir installé :
- **Docker** 🐳 → [Guide d’installation](https://docs.docker.com/get-docker/)
- **Git** 🖥️ → [Télécharger Git](https://git-scm.com/downloads)
- **Python 3** 🐍 (si vous souhaitez tester avec le simulateur) → [Télécharger Python](https://www.python.org/downloads/)

---

### 🔹 2️⃣ **Cloner le projet**
- **git** clone https://github.com/ton-utilisateur/petzi_webhook_app.git
- **cd** petzi_webhook_app
---

### 🔹3️⃣ **Tester les Webhooks**
Vous pouvez envoyer une vente test avec le simulateur :
python petzi_simulator.py http://localhost:5000/petzi_webhook

✅ Si tout fonctionne, vous verrez un message confirmant la réception des données.

---

### 🔹4️⃣ Voir les tickets vendus
- 🔹 Version API (JSON)
Ouvrez cette URL dans un navigateur ou utilisez un client API :
http://localhost:5000/get_tickets

➡️ Cela retourne une liste JSON avec tous les tickets enregistrés.

- 🔹 Version Interface Web (Jolie avec Bootstrap)
Ouvrez l’interface visuelle :
http://localhost:5000/

➡️ Vous pourrez voir tous les tickets affichés sous forme de tableau.

---

### 🔹 5️⃣ Gestion et dépannage

#### ⏹️ Arrêter l’application

**docker-compose down**


#### 🔄 Relancer après modification du code

**docker-compose up --build -d**

💡 Cette commande reconstruit l’image Docker et applique les changements.

🔍 Vérifier l’état des conteneurs

**docker ps -a**


📌 Voir les logs en cas d’erreur

**docker logs petzi_webhook_app**

🛠 Réinitialiser complètement

Si vous souhaitez repartir de zéro :

**docker-compose down -v**

**docker-compose up --build -d**

---

## 📌 Déploiement distant (optionnel)
Si vous souhaitez déployer cette application sur un serveur distant, vous pouvez suivre les étapes suivantes :

git add .

git commit -m "Ajout du README et Docker Compose"

git push origin main

Et configurez un serveur avec Docker pour exécuter docker-compose up -d.
