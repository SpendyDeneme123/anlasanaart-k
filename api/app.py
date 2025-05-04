from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Bu dosyada keyler saklanacak
keys = {}

@app.route('/store-key', methods=['POST'])
def store_key():
    data = request.json
    key = data.get('key')
    user_id = data.get('user_id')

    if not key or not user_id:
        return jsonify({"error": "Key and user_id are required"}), 400

    # Key'i veritabanına veya dosyaya kaydetme
    keys[user_id] = key  # Örnek olarak user_id ile key saklanıyor

    return jsonify({"message": "Key saved successfully"}), 200

@app.route('/get-key/<user_id>', methods=['GET'])
def get_key(user_id):
    key = keys.get(user_id)
    if not key:
        return jsonify({"error": "Key not found for this user"}), 404
    return jsonify({"key": key}), 200

if __name__ == '__main__':
    app.run(debug=True)
