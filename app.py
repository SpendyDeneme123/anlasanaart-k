from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class KeyRequest(BaseModel):
    discord_id: str
    discord_tag: str
    key: str

@app.post("/save-key")
async def save_key(data: KeyRequest):
    print(f"Key received from {data.discord_tag} ({data.discord_id}): {data.key}")
    # Buraya veritabanı kaydı veya dosyaya yazma gibi işlemler ekleyebilirsin
    return {"status": "success", "message": "Key received successfully"}
