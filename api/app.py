from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/upload', methods=['POST'])
def upload():
    data = request.get_json()

    # Verileri al
    user_id = data.get('user_id')
    key = data.get('key')
    timestamp = data.get('timestamp')

    # Hata kontrolü
    if not user_id or not key or not timestamp:
        return jsonify({"error": "Missing data"}), 400

    # Veriyi logla (örnek olarak data.txt'ye yazılıyor)
    try:
        with open("data.txt", "a") as f:
            f.write(f"{timestamp} - {user_id} - {key}\n")
    except Exception as e:
        return jsonify({"error": f"Error writing data: {str(e)}"}), 500

    # Başarılı yanıt
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(debug=True)
