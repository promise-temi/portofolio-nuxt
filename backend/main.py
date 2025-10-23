from flask import Flask, jsonify, request, session
from flask_cors import CORS
from flask_mail import Mail, Message
import os
import random
import os


app = Flask(__name__)

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME=os.getenv('MAIL_USERNAME'),      
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'),      
    MAIL_DEFAULT_SENDER=os.getenv('MAIL_USERNAME')
)
mail = Mail(app)


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
        # Dans /api/send_message, après captcha OK :
        msg = Message(
            subject=data.get('subject','Test'),
            recipients=[os.getenv('MAIL_USERNAME')],       # à toi-même
            body=data.get('message','(vide)')
        )
        mail.send(msg)

        return jsonify(message="Tout fonctionne parfaitement"), 200
    else:
        return jsonify(message="aie..."), 500


app.run(debug = True)