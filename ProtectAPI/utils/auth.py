import json
from fastapi import Header, HTTPException

API_KEYS_FILE = "data/api_keys.json"

def load_keys():
    with open(API_KEYS_FILE, "r") as f:
        return json.load(f)

def verify_token(x_api_key: str = Header(...)):
    valid_keys = load_keys()
    if x_api_key not in valid_keys:
        raise HTTPException(status_code=401, detail="Invalid API Key")
