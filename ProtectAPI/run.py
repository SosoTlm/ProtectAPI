import os
import json
import uuid

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")

def create_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)

def create_file_if_not_exists(file_path, default_data):
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump(default_data, f, indent=4)
        print(f"[🆕] {file_path} créé.")

def load_users():
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def install_user():
    name = input("👤 Entrez le nom du premier utilisateur : ").strip()
    if not name:
        print("❌ Le nom ne peut pas être vide.")
        return

    users = load_users()
    user_id = str(uuid.uuid4())
    role = "admin" if len(users) == 0 else "user"
    
    user_data = {
        "id": user_id,
        "name": name,
        "role": role,
        "punishments": []
    }
    
    users.append(user_data)
    save_users(users)

    print(f"\n[✅] Utilisateur '{name}' ajouté avec :")
    print(f"   🆔 ID     : {user_id}")
    print(f"   🔐 Rôle  : {role}")
    print(f"   🚫 Sanctions : Aucune\n")

def main():
    print("🔧 Installation de ProtectAPI...\n")
    create_data_dir()
    create_file_if_not_exists(USERS_FILE, [])

    install_user()
    print("🎉 Setup terminé. Tu peux maintenant lancer ton serveur ProtectAPI 🚀")

if __name__ == "__main__":
    main()
