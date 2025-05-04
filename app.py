from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class KeyRequest(BaseModel):
    discord_id: str
    discord_tag: str
    key: str

@app.post("/save-key")
async def save_key(data: KeyRequest):
    print(f"[RECEIVED] {data.discord_tag} ({data.discord_id}): {data.key}")
    return {"status": "ok", "key": data.key}
