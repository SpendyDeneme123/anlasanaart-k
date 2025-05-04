from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Ortam değişkeninden secret al (Vercel > Settings > Environment Variables kısmına ekle)
API_SECRET = os.environ.get("API_SECRET")

# Key'leri burada tut (isteğe bağlı: veritabanı yerine liste)
stored_keys = []

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API is live."})

@app.route("/store-key", methods=["POST"])
def store_key():
    # Authorization header kontrolü
    auth_header = request.headers.get("Authorization")

    if not auth_header or auth_header != f"Bearer {API_SECRET}":
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    key = data.get("key")
    user_id = data.get("user_id")

    if not key or not user_id:
        return jsonify({"error": "Missing key or user_id"}), 400

    stored_keys.append({"key": key, "user_id": user_id})
    return jsonify({"message": "Key stored successfully.", "total": len(stored_keys)}), 200

@app.route("/keys", methods=["GET"])
def get_keys():
    return jsonify({"keys": stored_keys})
