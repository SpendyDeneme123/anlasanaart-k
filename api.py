
from flask import Flask, request, jsonify
import json
import os
import settings

app = Flask(__name__)

# Load settings
DATA_FILE = settings.DATA_FILE

# Eğer dosya yoksa oluştur
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump({'keys': []}, f, indent=2)

# JSON dosyasını yükle
def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# JSON dosyasını kaydet
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

# Key ekleme endpoint'i
@app.route('/add_key', methods=['POST'])
def add_key():
    data = request.get_json()
    key = data.get('key')

    if not key:
        return jsonify({'error': 'No key provided'}), 400

    db = load_data()
    if key in db['keys']:
        return jsonify({'error': 'Key already exists'}), 409

    db['keys'].append(key)
    save_data(db)
    return jsonify({'message': 'Key added successfully'}), 200

# Tüm key'leri listeleme (test amaçlı)
@app.route('/keys', methods=['GET'])
def get_keys():
    db = load_data()
    return jsonify(db['keys'])

if __name__ == '__main__':
    app.run(debug=settings.DEBUG, host=settings.HOST, port=settings.PORT)
