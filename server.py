from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/login', methods=['POST'])
def login():
    data = request.json  # Get the JSON payload from the request
    email = data.get('email')
    password = data.get('password')
    print(f"Received email: {email}, password: {password}")
    return jsonify({"message": "Login data received successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
