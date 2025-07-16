<template>
    <section class="contact" id="contact-section">
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
            <form>
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
                    <label for="captcha">Résolvez ce CAPTCHA : 1+1</label>
                    <input type="text" id="captcha"  required>
                </fieldset>

                <button type="submit" class="submit">Envoyer</button>
            </form>

            <!-- Message de confirmation
            <div v-if="messageEnvoye" class="confirmation-message">
                <p>Votre message a bien été envoyé. Je vous répondrai dans les plus brefs délais.</p>
            </div> -->
        </div>
    </section>
</template>
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
    max-width: 450px;
    
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
</style>