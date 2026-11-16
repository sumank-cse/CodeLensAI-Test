SECRET_KEY = "sk_live_super_secret_key_12345"

def insecure_query(db, user_id):
    return db.execute(f"SELECT * FROM users WHERE id = {user_id}")
