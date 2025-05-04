from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Anahtarları tutacak liste
keys = []

@app.route('/endpoint', methods=['POST'])
def handle_key():
    data = request.json  # Gönderilen JSON verisini alıyoruz
    key = data.get('key')
    user_id = data.get('userId')
    username = data.get('username')

    # Anahtarı kaydediyoruz (JSON dosyasına)
    keys.append({
        'key': key,
        'user_id': user_id,
        'username': username
    })
    
    with open('keys.json', 'w') as f:
        json.dump(keys, f, indent=2)

    return jsonify({"message": "Key received successfully!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
