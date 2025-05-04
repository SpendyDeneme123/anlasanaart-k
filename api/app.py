from fastapi import FastAPI, Request
from pydantic import BaseModel
import json
import os

app = FastAPI()

DATA_FILE = "keys.json"

class KeyData(BaseModel):
    user_id: str
    username: str
    key: str

def save_key(data: dict):
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            all_data = json.load(f)
    else:
        all_data = []

    all_data.append(data)

    with open(DATA_FILE, "w") as f:
        json.dump(all_data, f, indent=2)

@app.post("/store-key")
async def store_key(data: KeyData):
    save_key(data.dict())
    return {"status": "success", "message": "Key stored."}

@app.get("/")
def root():
    return {"message": "API is live."}
