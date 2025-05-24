import os
from flask import Flask, request, jsonify, send_from_directory
import random
import string

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
print("Serving static files from:", BASE_DIR)


app = Flask(__name__, static_folder=BASE_DIR)

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    long_url = data.get("url", "")
    
    if not long_url:
        return jsonify({"error": "No URL provided"}), 400

    short_code = generate_short_code()
    return jsonify({"short": short_code}), 200

if __name__ == '__main__':
    app.run(port=5000)
