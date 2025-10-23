from flask import Flask, jsonify, request, session
from flask_cors import CORS
import random
import os


app = Flask(__name__)



cors = CORS(app,resources={r"/api/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:3000"]}})

cAPTCHA = None

@app.route('/api/captcha')
def make_captcha():
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    sign_list = ['-','+','*']
    sign = random.choice(sign_list)
    global cAPTCHA
    if sign == '+':
        cAPTCHA = x + y
    if sign == '-':
        cAPTCHA = x - y
    if sign == '*':
        cAPTCHA = x * y

    data = {
        'x': x,
        'y': y,
        'sign' : sign
    }

    return jsonify(data), 200

@app.route('/api/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    print(data['captcha'] )
    
    global cAPTCHA

    if int(data['captcha']) == cAPTCHA:
        print(data)
        return jsonify(message="Tout fonctionne parfaitement"), 200
    else:
        return jsonify(message="aie..."), 500


app.run(debug = True)