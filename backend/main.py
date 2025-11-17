from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv
load_dotenv()
# MY MODULES
from modules.api_tools import make_captcha
import html


app = Flask(__name__)



MAIL_USERNAME = os.getenv('MAIL_USERNAME')          
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')          
MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER') or MAIL_USERNAME

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME=MAIL_USERNAME,
    MAIL_PASSWORD=MAIL_PASSWORD,
    MAIL_DEFAULT_SENDER=MAIL_DEFAULT_SENDER,
)

mail = Mail(app)

cors = CORS(app,resources={r"/api/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:3000","https://portfolio-promise-john.onrender.com/"]}})

cAPTCHA = None

@app.route('/api/captcha')
def get_captcha():
    try:
        global cAPTCHA
        data, cAPTCHA = make_captcha()
        return jsonify(data), 200
    except Exception as e:
        print('Une erreur est survenue')
        print(e)
        return jsonify({'message':'Une erreur interne est survenue'}), 500

@app.route('/api/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    global cAPTCHA
    # Verifie si le captcha est bon 
    if int(data['captcha']) == cAPTCHA:
        
        # Dans /api/send_message, après captcha OK :
        msg = Message(
            subject=f"Portofolio : {data['object']}",
            sender=MAIL_DEFAULT_SENDER,                  # <— important
            recipients=[MAIL_USERNAME],
            # body=f"{data['email']}\n\n{data['message']}"
            html= f"""
            <body style="margin: 0; padding: 0; box-sizing: border-box; font-family: Verdana, Geneva, Tahoma, sans-serif; font-size: 11px;">
    <ul class="infos" style="list-style-type: none; margin: 0; padding: 15px; color:white; box-sizing: border-box; background-image: linear-gradient(to right, #C014A6, #660BDA);">
        <li>Nom : <strong>{data['nom']}</strong></li>
        <li>Prenom : <strong>{data['prenom']}</strong></li>
        <li>Mail : <strong>{data['email']}</strong></li>
    </ul>
    <div class="message">
        <p style="padding: 15px; line-height: 22px;">
            {html.unescape(data['message'])}
        </p>
    </div>
</body>
"""
        )
        mail.send(msg)
        return jsonify({"message":"Tout fonctionne parfaitement"}), 200
        

    else:
        return jsonify({"message":"Une erreur est survenue"}), 500

