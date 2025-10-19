from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

cors = CORS(app,resources={r"/api/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:3000"]}})

@app.route('/api/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    print(data)
    return jsonify(message="Tout fonctionne parfaitement"), 200


app.run(debug = True)