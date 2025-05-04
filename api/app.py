from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = 'keys.json'

# JSON dosyasını hazırla
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

@app.route('/')
def home():
    return jsonify({"message": "API is live."})

# Buraya Discord'dan key POST edilecek
@app.route('/store-key', methods=['POST'])
def store_key():
    try:
        data = request.get_json()
        key = data.get('key')
        user_id = data.get('user_id')

        if not key or not user_id:
            return jsonify({'error': 'Key or user_id is missing'}), 400

        # Key'i kaydet
        with open(DATA_FILE, 'r+') as f:
            keys = json.load(f)
            keys.append({'key': key, 'user_id': user_id})
            f.seek(0)
            json.dump(keys, f, indent=2)
        
        return jsonify({'message': 'Key stored successfully'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Key'leri listelemek için:
@app.route('/keys', methods=['GET'])
def get_keys():
    with open(DATA_FILE, 'r') as f:
        keys = json.load(f)
    return jsonify(keys)
