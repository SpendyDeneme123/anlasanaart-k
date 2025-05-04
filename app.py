from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List
import json
import os

app = FastAPI()

DATA_FILE = "saved_keys.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

class KeyRequest(BaseModel):
    discord_id: str
    discord_tag: str
    key: str

@app.post("/save-key")
async def save_key(data: KeyRequest):
    with open(DATA_FILE, "r") as f:
        saved = json.load(f)

    saved.append(data.dict())

    with open(DATA_FILE, "w") as f:
        json.dump(saved, f, indent=2)

    return {"status": "saved", "key": data.key}

@app.get("/keys")
async def list_keys():
    with open(DATA_FILE, "r") as f:
        saved = json.load(f)
    return saved
