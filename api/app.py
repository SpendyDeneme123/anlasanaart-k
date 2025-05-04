from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/api/upload', methods=['POST'])
def upload():
    data = request.get_json()
    user_id = data.get('user_id')
    key = data.get('key')
    timestamp = data.get('timestamp')

    if not user_id or not key:
        return jsonify({"error": "Missing data"}), 400

    with open("data.txt", "a") as f:
        f.write(f"{timestamp} - {user_id} - {key}\n")

    return jsonify({"status": "ok"})
