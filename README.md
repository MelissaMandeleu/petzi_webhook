🎟️ Petzi Webhook App
📌 Description
Ce projet permet de recevoir et enregistrer automatiquement les ventes de billets via les webhooks de Petzi et de les stocker dans une base de données PostgreSQL.

💡 Fonctionnalités :

✅ Réception et stockage des webhooks Petzi 🎫 
✅ Vérification de l’authenticité des requêtes 🔐 
✅ Sauvegarde dans une base PostgreSQL 💾 
✅ Interface Web Flask pour voir les tickets vendus 🖥️ 
✅ Déploiement automatisé via Docker 🐳


📌 1️⃣ Prérequis
Avant de commencer, vous devez installer :

Docker → Guide d’installation
Git → Télécharger Git
Python 3 (si vous souhaitez tester avec le simulateur) → Télécharger Python
📌 2️⃣ Cloner le projet
Téléchargez le code source en local :

bash
Copier
Modifier
git clone https://github.com/ton-utilisateur/petzi_webhook_app.git
cd petzi_webhook_app
📌 3️⃣ Construire et Lancer l'application
Tout se fait en deux commandes :

bash
Copier
Modifier
docker-compose build    # Recrée l’image Docker
docker-compose up -d    # Lance l’application en arrière-plan
💡 Explication :
🛠 docker-compose build : Construit l’image Flask à partir du Dockerfile
🚀 docker-compose up -d : Lance l’application et PostgreSQL
📡 Expose l’API sur http://localhost:5000
📂 Les données sont sauvegardées même après l’arrêt du conteneur
📌 4️⃣ Tester les Webhooks
🚀 Envoyer une vente test avec le simulateur :
bash
Copier
Modifier
python petzi_simulator.py http://localhost:5000/petzi_webhook
✅ Vous verrez un message confirmant la réception des données.

📌 5️⃣ Voir les tickets vendus
🔹 Version API (JSON)
📌 Ouvrir dans le navigateur ou avec un client API :

bash
Copier
Modifier
http://localhost:5000/get_tickets
➡️ Cela retourne une liste JSON avec tous les tickets enregistrés.

🔹 Version Interface Web (avec Bootstrap)
📌 Interface visuelle :

arduino
Copier
Modifier
http://localhost:5000/
➡️ Vous pourrez voir tous les tickets affichés en tableau.

📌 6️⃣ Arrêter et Relancer
📌 Pour arrêter l’application :

bash
Copier
Modifier
docker-compose down
📌 Pour relancer après modification du code :

bash
Copier
Modifier
docker-compose up --build -d
💡 Cela reconstruit l’image et applique les changements.

📌 7️⃣ Dépannage
Si l’application ne fonctionne pas, voici quelques commandes utiles :

🔍 Vérifier l’état des conteneurs :
bash
Copier
Modifier
docker ps -a
📌 Si petzi_webhook_app n’est pas démarré, essayez :

bash
Copier
Modifier
docker logs petzi_webhook_app
Cela affiche les logs et peut aider à identifier le problème.

🔄 Supprimer tous les conteneurs et repartir de zéro :
bash
Copier
Modifier
docker-compose down -v   # Supprime aussi les volumes (données stockées)
docker-compose up --build -d   # Reconstruit tout proprement
📌 8️⃣ Structure du Projet
📂 Fichiers importants :

graphql
Copier
Modifier
📁 petzi_webhook_app
 ├── 📂 templates        # Interface Web Flask
 │   ├── index.html      # Page HTML affichant les tickets
 │   ├── layout.html     # Layout global
 ├── app.py             # API Flask pour recevoir et afficher les tickets
 ├── requirements.txt    # Dépendances Python
 ├── docker-compose.yml  # Configuration pour Docker
 ├── Dockerfile          # Image du serveur Flask
 ├── petzi_simulator.py  # Simulateur pour tester les webhooks
📌 9️⃣ Contribution
🙌 Toute aide est la bienvenue !
📌 Ouvrez une issue ou proposez une pull request sur GitHub si vous souhaitez améliorer l’application.

🚀 🎟️ Merci d’utiliser Petzi Webhook App !
Si vous avez des questions, n’hésitez pas à nous contacter. 😊

✅ Résumé rapide (TL;DR)
Cloner le projet → git clone ...
Construire et lancer → docker-compose up --build -d
Tester un webhook → python petzi_simulator.py http://localhost:5000/petzi_webhook
Voir les tickets vendus → http://localhost:5000/
