<template>
    <section class="contact" id="contact">
        <div class="title">
            <h2>Contact</h2>
            <span class="title-decor"></span>
        </div>

        <div class="contact-form">
            <div>
                <h3>Want to know more ?</h3>
                <p class="contact-sentence">
                    I'm always open to new opportunities, collaborations, or simply a good conversation.
                    <br><br> 👉 Don't hesitate to get in touch or connect with me on 
                    <strong>
                        <a href="https://www.linkedin.com/in/promise-john-93486a2bb/" target="_blank">Linkedin</a>
                    </strong>
                </p>
            </div>
            <form @submit.prevent="sendMessage">
                <div class="fullname">
                    <fieldset>
                        <label for="prenom">Name</label>
                        <input type="text" id="prenom"  required>
                    </fieldset>
                    <fieldset>
                        <label for="nom">Last Name</label>
                        <input type="text" id="nom"  required>
                    </fieldset>
                    
                </div>
                <fieldset>
                        <label for="objet">Subject</label>
                        <input type="text" id="object" maxlength="100" required>
                    </fieldset>
                <!-- <fieldset>
                    <label for="email">Email</label>
                    <input type="email" id="email" required>
                </fieldset> -->
                <fieldset>
                    <label for="message">Message</label>
                    <textarea id="message" maxlength="1000" required></textarea>
                </fieldset>

                <!-- CAPTCHA dynamique -->
                <!-- <fieldset>
                    <label for="captcha">solve this challenge : {{x}} {{ challenge }} {{ y }}</label>
                    <input type="text" id="captcha"  required>
                </fieldset> -->

                <button type="submit" class="submit">Send</button>
            </form>
            <Transition name="fade" mode="out-in">
                <!-- Message de confirmation -->
                <div v-if="messageValidated" class="confirmation-message">
                    <p>Your email app will open with the message pre-filled.</p>
                </div>
            </Transition>
        </div>
    </section>
</template>

<script>
// const api = import.meta.env.VITE_API_BASE_URL
// import axios from 'axios';
export default{
    data(){
        return{
            // challenge : null,
            // x : null,
            // y : null,
            messageValidated: false,
        }
    },
    methods:{
        // escapeHTML(str) {
        //     return String(str).replace(/[&<>"'`]/g, s => ({
        //         '&': '&amp;',
        //         '<': '&lt;',
        //         '>': '&gt;',
        //         '"': '&quot;',
        //         "'": '&#39;',
        //         '`': '&#96;'
        //     }[s]));
        //     },

        // sendMessage(){
            

        //     let data = {
        //         'prenom': this.escapeHTML(document.querySelector('#prenom').value),
        //         'nom': this.escapeHTML(document.querySelector('#nom').value),
        //         'object': this.escapeHTML(document.querySelector('#object').value),
        //         'email': this.escapeHTML(document.querySelector('#email').value),
        //         'message': this.escapeHTML(document.querySelector('#message').value),
        //         // 'captcha': this.escapeHTML(document.querySelector('#captcha').value)
        //     }

            
        //         axios.post(`${api}/send_message`, data)
        //         .then(response => {
        //             console.log(response.data)
        //             document.querySelector('#prenom').value = "";
        //             document.querySelector('#nom').value = "";
        //             document.querySelector('#object').value = "";
        //             document.querySelector('#email').value = "";
        //             document.querySelector('#message').value = "";
        //             document.querySelector('#captcha').value = "";
        //             this.getCaptcha()
        //             this.showMessage()
        //         })
        //         .catch(error => {
        //             alert('something went wrong');
        //             console.log(error)
        //             this.getCaptcha()
        //         })
            
        // },
        sendMessage(){
            const to = "temi.promisejohn@gmail.com"
            const subject = `${document.querySelector('#prenom').value} - ${document.querySelector('#nom').value}  :  ${document.querySelector('#object').value}`
            const body = `${document.querySelector('#message').value}`
            const MailtoLink = `mailto:${to}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`
            window.location.href = MailtoLink;
            this.showMessage()
           
        },

    // getCaptcha(){
    //   axios.get(`${api}/captcha`)
    //   .then(response => {
    //       console.log(response.data)
    //       let result = response.data
    //       this.x = result.x
    //       this.y = result.y
    //       this.challenge = result.sign
    //   })
    //   .catch(error => {
    //     alert('Une erreur s\'est produite')
    //     console.log(error)
    //   })
    // },

    showMessage(){
        this.messageValidated = true
        setTimeout(() => {
            this.messageValidated = false
        }, 5000)
    }
        

    },
    mounted(){
        // this.getCaptcha()
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
    position: relative;
    top: -100px;
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

/* animation */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s ease-in;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
/* end animation */

@media (max-width:480px){
    section{
        padding-left: 20px;
        padding-right: 20px;
    }
}

/* @media (min-width:1300px){
  section{
    padding: 50px 130px;
  }
} */
</style>