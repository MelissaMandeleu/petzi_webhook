from flask import Flask, request, jsonify, render_template
import psycopg2
import hmac
import hashlib
import json
import os

# Initialisation de Flask avec les bons chemins
app = Flask(__name__, template_folder="../templates", static_folder="../static")

print("📂 Chemin des templates :", os.path.abspath(app.template_folder))

# Configuration PostgreSQL
db_config = {
    'dbname': 'petzi_db',
    'user': 'petzi',
    'password': 'petzi_password',
    'host': 'localhost',
    'port': '5432'
}

# Clé secrète utilisée pour la vérification HMAC
SECRET_KEY = "AEeyJhbGciOiJIUzUxMiIsImlzcyI6"

def verifier_signature(signature, payload):
    """ Vérifie si la signature HMAC de la requête est valide. """
    try:
        signature_parts = dict(item.split("=") for item in signature.split(","))
        timestamp = signature_parts.get("t")
        received_signature = signature_parts.get("v1")

        body_to_sign = f"{timestamp}.{payload}".encode()
        computed_signature = hmac.new(SECRET_KEY.encode(), body_to_sign, hashlib.sha256).hexdigest()

        return hmac.compare_digest(computed_signature, received_signature)
    except Exception as e:
        print(f"❌ Erreur lors de la vérification de la signature : {e}")
        return False

@app.route('/petzi_webhook', methods=['POST'])
def recevoir_ticket():
    """ Reçoit et stocke un ticket Petzi dans PostgreSQL """
    try:
        payload = request.get_data(as_text=True)
        signature = request.headers.get("Petzi-Signature")

        if not signature or not verifier_signature(signature, payload):
            print("🚨 Requête non autorisée (signature invalide)")
            return jsonify({"error": "Signature invalide"}), 403

        data = json.loads(payload)
        print("\n--- 🎟️ Nouvelle vente de ticket reçue ---")
        print(json.dumps(data, indent=4))

        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO tickets (json_data) VALUES (%s) RETURNING id;", (json.dumps(data),))
        ticket_id = cursor.fetchone()[0]
        conn.commit()

        print(f"✅ Ticket stocké en base avec l'ID : {ticket_id}")
        return jsonify({"message": "Données de vente reçues avec succès.", "ticket_id": ticket_id}), 200

    except Exception as e:
        print(f"❌ Erreur lors du traitement de la requête : {e}")
        return jsonify({"error": "Erreur interne"}), 500

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

@app.route('/get_tickets', methods=['GET'])
def get_tickets():
    """ Récupère tous les tickets stockés dans PostgreSQL """
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("SELECT id, json_data, received_at FROM tickets ORDER BY received_at DESC")
        tickets = cursor.fetchall()

        result = [{"id": t[0], "json_data": t[1], "received_at": t[2].strftime("%Y-%m-%d %H:%M:%S")} for t in tickets]

        return jsonify(result), 200

    except psycopg2.Error as err:
        print(f"❌ Erreur PostgreSQL : {err}")
        return jsonify({"error": "Erreur lors de la récupération des tickets"}), 500

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

@app.route('/tickets')
def afficher_tickets():
    """ Affiche les tickets en HTML """
    event_filter = request.args.get('event', None)

    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        if event_filter:
            sql_query = """
                SELECT id, json_data, received_at 
                FROM tickets 
                WHERE json_data->'details'->'ticket'->>'event' = %s 
                ORDER BY received_at DESC
            """
            cursor.execute(sql_query, (event_filter,))
        else:
            sql_query = "SELECT id, json_data, received_at FROM tickets ORDER BY received_at DESC"
            cursor.execute(sql_query)

        tickets = cursor.fetchall()

        return render_template("index.html", tickets=tickets, event_filter=event_filter)

    except psycopg2.Error as err:
        return f"❌ Erreur PostgreSQL : {err}"

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

# Lancement de l'application
if __name__ == '__main__':
    # init_db()  # Décommente si la BDD doit être initialisée au démarrage
    app.run(debug=True, port=5000)
