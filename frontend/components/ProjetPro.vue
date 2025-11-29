<template>
    <section id="motivations">
        <!-- Titre section -->
        <div class="title">
            <h2>Motivations</h2>
            <DecoLine />
        </div>
        <!-- Partie 1 AI -->
        <div class="partie partie-1">
            <div class="image">
                <img src="/drawings/ai_.png" alt="image IA" class="ai">
            </div>
            <div class="texte">
                <h3>AI : more than an advancement, a true revolution</h3>
                <p>Beyond a simple technological achievement, Artificial Intelligence is a true revolution that redefines our capabilities. It makes it possible to :</p>
                <ul>
                    <li>Automate and optimize complex processes,</li>
                    <li>Analyze vast amounts of data in order to anticipate trends,</li>
                    <li>Develop intelligent tools that transform current challenges into lasting opportunities.</li>
                </ul>
            </div>
            <!-- Partie 2 Ma formation -->
        </div>
        <div class="partie partie-2">
            <div class="texte">
                <h3>My training serving innovation</h3>
                <p>It is precisely in this field that I am currently specializing. I am building a profile at the crossroads of complementary skills that combine :</p>
                <ul>
                    <li><strong>Data Science</strong> : collecting, cleaning, and exploiting large datasets.</li>
                    <li><strong>Artificial Intelligence</strong> : training machine learning and deep learning models to solve complex problems.</li>
                    <li><strong>Application Development</strong> : integrating these solutions into concrete tools deployed in real-world environments.</li>
                </ul>  
            </div>
            <div class="image">
                <img src="/drawings/computer_.png" alt="image computer" class="computer">
            </div>
        </div>
        <!-- Partie 3 Ensemble -->
        <div class="partie partie-3">
            <div class="image">
            <img src="/drawings/winning_.png" alt="image winning" class="winning">
            </div>
            <div class="texte">
            <h3>Let’s bring your AI projects to life</h3>
            <p>What am I looking for ? A work-study opportunity (alternance) where I can contribute to ambitious projects and help your company fully harness the potential of its data. I’m ready to relocate, wherever you are, to join your team and put my skills at the service of your goals. With AI, opportunities are endless ✨, and I’m eager to be part of your success.</p>
        </div>
        </div>
    </section>
</template>

<style scoped>
/* Section */

section{
    background-color: #10071E;
    position: relative;
    z-index: 5;
    color: white;
    padding: 50px;
}
/* Titre section */
h2{
    font-family: "Poppins";
    font-size: 20px;
    font-weight: 600;
}


/* Titre partie */

h3{
  font-size: 22px;
  font-weight: 400;
  margin-bottom: 20px;
}

/* Partie */

div.partie{
  display: flex;
  justify-content: space-between;
  gap: 100px;
  font-size: 16px;
}

div.partie a{
  color: rgb(69, 69, 254);
}

ul{
  list-style: disc;
  margin-left: 25px;
}

div.image{
  background-repeat: no-repeat;
  background-size: contain;
  
}

div.partie-1, div.partie-3 .texte{
  margin-right: 60px;
}
div.partie-2 .texte{
  margin-left: 30px;
}

div.texte{
 margin-top: 80px;
 text-align: justify;
 font-size: 14px;
 font-weight: 300;
 color: #FFFAFA;
}

.computer{
  max-width: 300px;
}
.ai{
  max-width: 300px;
}
.winning{

  max-width: 300px;
}

@media(max-width: 992px){
  section{
    padding-bottom: 0px;
  }
  .computer{
  min-width: 250px;
  position: relative;
}
.ai{
  min-width: 250px;
  position: relative;
}
.winning{
  min-width: 250px;
  position: relative;
}

h3{
  font-size: 18px;
}

div.texte{
  font-size: 14px;
 margin-top: 0px;
 margin-bottom: 100px;


}

div.partie{
  gap: 50px;

  
}
}

@media(max-width: 768px){
  div.partie{
  flex-direction: column;
}
.computer{
  display: none;
}
.ai{
  display: none;
}
.winning{
  display: none;
}
div.texte{
 margin-top: 0px;
 margin-bottom: 100px;
 text-align: start;
}
div.partie{
  gap: 0px;
}
section{
  padding-bottom: 0px;
}

div.partie-1, div.partie-3 .texte{
  margin-right: 0px;
}
div.partie-2 .texte{
  margin-left: 0px;
}
}

@media (max-width:450px){
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