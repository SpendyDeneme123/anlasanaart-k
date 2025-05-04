from flask import Flask, jsonify
import random
import string

app = Flask(__name__)

# Anahtarları rastgele oluşturma fonksiyonu
def generate_key():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the API!"})

@app.route('/generate_key', methods=['GET'])
def generate_api_key():
    api_key = generate_key()
    return jsonify({"api_key": api_key})

if __name__ == '__main__':
    app.run(debug=True)
