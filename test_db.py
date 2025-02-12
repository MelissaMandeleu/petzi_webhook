import psycopg2

# Configuration de connexion
db_config = {
    'dbname': 'petzi_db',
    'user': 'petzi',
    'password': 'petzi_password',
    'host': 'localhost',
    'port': '5432'
}

# Test de connexion
try:
    conn = psycopg2.connect(**db_config)
    print("✅ Connexion réussie à PostgreSQL !")
    conn.close()
except Exception as e:
    print(f"❌ Erreur de connexion : {e}")
