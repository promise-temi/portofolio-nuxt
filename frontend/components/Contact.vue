<template>
    <section class="contact" id="contact">
        <div class="title">
            <h2>Contact</h2>
            <span class="title-decor"></span>
        </div>

        <div class="contact-form">
            <div>
                <h3>Envie d'en savoir plus ?</h3>
                <p class="contact-sentence">
                    Je serais ravie de discuter avec vous ! Que ce soit pour une collaboration ou simplement échanger
                    <br><br> 👉 N'hésitez pas à me contacter ! Retrouvez-moi aussi sur
                    <strong>
                        <a href="https://www.linkedin.com/in/promise-john-93486a2bb/" target="_blank">Linkedin</a>
                    </strong>
                </p>
            </div>
            <form @submit.prevent="sendMessage">
                <div class="fullname">
                    <fieldset>
                        <label for="prenom">Prénom</label>
                        <input type="text" id="prenom"  required>
                    </fieldset>
                    <fieldset>
                        <label for="nom">Nom</label>
                        <input type="text" id="nom"  required>
                    </fieldset>
                </div>
                <fieldset>
                    <label for="email">Email</label>
                    <input type="email" id="email" required>
                </fieldset>
                <fieldset>
                    <label for="message">Message</label>
                    <textarea id="message"  required></textarea>
                </fieldset>

                <!-- CAPTCHA dynamique -->
                <fieldset>
                    <label for="captcha">Résolvez ce CAPTCHA : {{x}} {{ signe }}  {{ y }}</label>
                    <input type="text" id="captcha"  required>
                </fieldset>

                <button type="submit" class="submit">Envoyer</button>
            </form>

            <!-- Message de confirmation -->
            <div  class="confirmation-message">
                <p>Votre message a bien été envoyé. Je vous répondrai dans les plus brefs délais.</p>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios';
export default{
    data(){
        return{
            challenge : null,
            x : null,
            y : null,
        }
    },
    methods:{
        escapeHTML(str) {
            return String(str).replace(/[&<>"'`]/g, s => ({
                '&': '&amp;',
                '<': '&lt;',
                '>': '&gt;',
                '"': '&quot;',
                "'": '&#39;',
                '`': '&#96;'
            }[s]));
            },

        sendMessage(){
            let captcha =  this.escapeHTML(document.querySelector('#captcha').value);

            let data = {
                'prenom': this.escapeHTML(document.querySelector('#prenom').value),
                'nom': this.escapeHTML(document.querySelector('#nom').value),
                'email': this.escapeHTML(document.querySelector('#email').value),
                'message': this.escapeHTML(document.querySelector('#message').value),
            }

            if(captcha == this.challenge){
                axios.post('http://127.0.0.1:5000/api/send_message', data)
                .then(response => {
                    console.log(response.data)
                })
                .catch(error => {
                    alert('something went wrong');
                    console.log(error)
                })
            }
            else{
                alert('wrong captcha')
            }
            this.Capcha()
        },
        Capcha(){
            let signe = Math.floor(1 + Math.random()*2);
            
            this.x = Math.floor(1 + Math.random()*9);
            this.y = Math.floor(1 + Math.random()*9);
            if(signe === 0){
                this.signe = '+'
              this.challenge = this.x + this.y   
            }
            if(signe === 1){
                this.signe = '-'
              this.challenge = this.x - this.y   
            }
            if(signe === 2){
                this.signe = '*'
              this.challenge = this.x * this.y   
            }
            
        }

    },
    mounted(){
        this.Capcha();
    }
}

</script>
<style>
.confirmation-message {
    margin-top: 20px;
    padding: 15px;
    color: white;
    background-image: linear-gradient(to right, #660BDA, #C014A6, 50%, #c014a600);
    border: 1px solid #000000;
    border-radius: 5px;
}
</style>

<style scoped>
h2{
    font-family: "Poppins";
    font-size: 20px;
    margin-bottom: 15px;
    font-weight: 600;
}

div h3{
    font-weight: 700;
    margin-top: 20px;
}
section{
    color: white;
    background-color: #080111;
    padding: 50px;
    width: 100%;
    font-size: 14px;
}
a{
    color: blue;
    text-decoration: underline;
}
.title-decor{
  display: inline-block;
  width: 100px;
  height: 3px;
  background-image: linear-gradient(to right, #660BDA, #C014A6, 50%, #c014a600);
  border-radius: 5px;
  position: relative;
  top:-25px;
}

.contact-sentence{
    max-width: 550px;
    
    margin-bottom: 50px;

}
.contact-sentence strong{
    color: blue;
}

fieldset{
    border: none;
    /* display: flex;
    flex-direction: column; */
    margin-bottom: 10px;
}

fieldset label{
    font-size: 12px;
}

input, textarea{
    border: none;
    border-radius: 5px;
    border-style: solid;
    border-width: 0.1px;
    width: 100%;
    padding: 10px;
    font-size: 12px;
}

textarea{
    height: 100px;
}
input{
    height: 35px;
    
}

div.fullname{
    display: flex;
    gap: 20px;

}

form{
    max-width: 550px;
    display: flex;
    flex-direction: column;
    /* background-color: #10071e71;
    padding: 30px;     
    border-radius: 10px;                                                  */
}

button{
    /* background-color: transparent;
    border: none;
    border-color: white;
    border-width: 0.5px;
    border-style: solid;
    padding: 5px 20px;
    border-radius: 7px;
    margin-left: auto;
    margin-right: auto;
    margin-top: 20px; */
    background-image: linear-gradient(to right,#660BDA,46%,#C014A6);
    width: 100px;
    height: 35px;
    border: none;
    border-radius: 5px;
    color: white;
    font-weight: 600;
    font-size: 14px;
    margin-left: auto;
    margin-right: auto;
    margin-top: 20px;
}

.contact-form{
    
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between; /* Change space-between en center */
    
    gap: 10px;
}

@media (max-width:480px){
    section{
        padding-left: 20px;
        padding-right: 20px;
    }
}
</style>