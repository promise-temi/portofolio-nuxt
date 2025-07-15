<template>
<section>
<div class="particles">
    <ParticlesBackgound  class="particles"/>
</div>
<div class="presentation-et-lune">
    <!-- Présentation -->
    <div class="presentation">
        <div class="titles">
            <h2>Promise JOHN</h2>
            <h3>Développeuse Data Intelligence Artificielle</h3>
            <DecoLine/>
        </div>
        <p>Bonjour et bienvenue sur mon portofolio ! <br><br>Passionnée par la data et  l'intelligence artificielle, je mets mes compétences au service de projets innovants et ambitieux. Ici, vous découvrirez ma vision de l'IA, mon parcours et mes projets. <br><br>N'hésitez pas à me contacter pour échanger !</p>
        <!-- Boutons mise en contact -->
        <div class="buttons">
            <button class="curriculum"><a :href="cv" download>Mon CV</a></button>
            <button class="contact"><a href="#contact-section">Contact</a></button>
        </div>
    </div>
    <!-- Lune décoration -->
    <div class="lune">
        <img src="public/drawings/Moon.png" alt="lune">
    </div>
</div>
<!-- Montagnes décoration -->
<img src="public/drawings/landscape2.png" alt="montagne" class="montagnes">
</section>
</template>
<script>
export default {
data(){
        return{
            cv : new URL("@/assets/images/cv.pdf", import.meta.url).href,
            scrollPosition: 0, // Suivre la position de défilement
        }
    },
    mounted() {
    window.addEventListener("scroll", this.moveStars); // Écouteur sur le défilement
    window.addEventListener("scroll", this.moveMoon); // Écouteur sur le défilement
  },
  beforeUnmount() {
    window.removeEventListener("scroll", this.moveStars); // Nettoyer l'écouteur
    window.removeEventListener("scroll", this.moveMoon); // Nettoyer l'écouteur
  },
  methods: {
    moveStars() {
      const scrollTop = window.scrollY || document.documentElement.scrollTop; // Position du défilement
      const stars = document.querySelector(".particles");
      if (stars) {
        stars.style.transform = `translateX(${scrollTop * 0.1}px)`; // Appliquer un effet de défilement
      }
    },
    moveMoon() {
      const scrollTop = window.scrollY || document.documentElement.scrollTop; // Position du défilement
      const moon = document.querySelector(".lune");
      if (moon) {
        moon.style.transform = `translateY(${scrollTop * 0.2}px)`; // Appliquer un effet de défilement
      }
    },
  }

}
</script>
<style scoped>
section{
    display: inline-block;
    position: relative;
    background-image: linear-gradient(to bottom,#01050D,35%,#092C73,69%, #66299F);
    height: 550px;
    width: 100%;
    overflow: hidden;
    }
.particles {
    width: 100%;
    height: 40vw;
    position: absolute;
}
/* links */
a {
    text-decoration: none;
    color: white;
}

/* presentation et lune */

div.presentation-et-lune{
display: flex;
justify-content: space-between;
overflow: hidden;
}

/* Présentation */
div.presentation{
    color: white;
    margin-top: 150px;
    margin-left: 130px;
    position: relative;
    z-index:4;
}

div.titles{
    margin-bottom: 20px;
}

div.presentation h2{
    font-family: "Poppins";
    font-size: 24px;
    font-weight: 700;
}
div.presentation h3{
    font-family: "Poppins";
    font-size: 18px;
    font-weight: 400;
}



div.presentation p{
    margin-bottom: 40px;
    max-width: 600px;
    background-image: linear-gradient(to right, #10071e66,80%, transparent); 
    padding: 10px;
    border-radius: 0px;
    font-size: 14px;
}

/* Boutons */

button{
     width: 100px;
    height: 35px;
    border: none;
    border-radius: 5px;
    color: white;
    font-weight: 600;
    margin-right: 25px;
    font-size: 14px;
    cursor: pointer;
}
button.curriculum{
    background-color: #261B4C;
}

button.contact{
    background-image: linear-gradient(to right,#660BDA,46%,#C014A6);
}

/* image lune */
div.lune img{
    width: 39vw;
    rotate: -175,45;
    margin-top: 8vw;
    opacity: 0.9;
}

img.montagnes{
    position: absolute;
    bottom: 0;
    z-index: 2;
    /* top:160px; */
    width: 100%;
}

</style>