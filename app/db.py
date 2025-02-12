import psycopg2
from psycopg2 import sql

# Configuration PostgreSQL
db_config = {
    'dbname': 'petzi_db',
    'user': 'petzi',
    'password': 'petzi_password',
    'host': 'localhost',
    'port': '5432'
}

def init_db():
    """ Crée la base de données et la table si elles n'existent pas encore """
    try:
        # Connexion à PostgreSQL
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # Création de la table si elle n'existe pas
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                id SERIAL PRIMARY KEY,
                json_data JSONB NOT NULL,
                received_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        conn.commit()
        print("✅ Base de données et table vérifiées/créées avec succès.")

    except psycopg2.Error as err:
        print(f"❌ Erreur PostgreSQL : {err}")

    finally:
        cursor.close()
        conn.close()

# Exécuter la fonction si ce fichier est lancé directement
if __name__ == "__main__":
    init_db()
