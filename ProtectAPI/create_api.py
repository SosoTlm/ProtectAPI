import json
import os
import secrets
import string

API_KEYS_FILE = "data/api_keys.json"
KEY_LENGTH = 32  # 256 bits

def generate_key(length=KEY_LENGTH):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def load_keys():
    if not os.path.exists(API_KEYS_FILE):
        return []

    with open(API_KEYS_FILE, "r") as f:
        return json.load(f)

def save_keys(keys):
    with open(API_KEYS_FILE, "w") as f:
        json.dump(keys, f, indent=4)

def create_api_key():
    keys = load_keys()
    while True:
        new_key = generate_key()
        if new_key not in keys:
            keys.append(new_key)
            save_keys(keys)
            print(f"[✅] Nouvelle API Key générée : {new_key}")
            break
        else:
            print("[⚠️] API avec même schéma détectée, génération d’une nouvelle clé...")

if __name__ == "__main__":
    create_api_key()
