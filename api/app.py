from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

API_SECRET = "5Xr98LmBt!secretKey"
KEY_FILE = "stored_keys.json"

if not os.path.exists(KEY_FILE):
    with open(KEY_FILE, 'w') as f:
        json.dump([], f)

@app.route("/store-key", methods=["POST"])
def store_key():
    auth_header = request.headers.get("Authorization", "")
    if auth_header != f"Bearer {API_SECRET}":
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    if not data or "key" not in data or "user_id" not in data:
        return jsonify({"error": "Missing fields"}), 400

    new_entry = {
        "key": data["key"],
        "user_id": data["user_id"]
    }

    try:
        with open(KEY_FILE, 'r+') as f:
            stored = json.load(f)
            stored.append(new_entry)
            f.seek(0)
            json.dump(stored, f, indent=2)
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
