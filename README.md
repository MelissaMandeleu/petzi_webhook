# petzi_webhook

# 🎟️ Petzi Webhook Listener

## 📌 Description
Cette application écoute les webhooks envoyés par Petzi lors d'une vente de ticket, vérifie la requête, stocke les données dans PostgreSQL et affiche les tickets sur une interface web.

## 📌 Fonctionnalités
✅ **Réception et vérification des webhooks**  
✅ **Stockage des ventes de tickets dans PostgreSQL**  
✅ **Interface web Flask**  
✅ **Déploiement via Docker et Docker Compose**  

---

## 🚀 Installation

### **1️⃣ Cloner le projet**
git clone https://github.com/ton_pseudo/petzi_webhook.git
cd petzi_webhook

2️⃣ Lancer avec Docker
docker-compose up --build

3️⃣ Simuler une vente de ticket
python app/petzi_simulator.py http://localhost:5000/petzi_webhook
