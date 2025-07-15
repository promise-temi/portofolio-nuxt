<template>
    <section id="projet__pro__section">
        <!-- Titre section -->
        <div class="title">
            <h2>Projet pro</h2>
            <DecoLine />
        </div>
        <!-- Partie 1 AI -->
        <div class="partie partie-1">
            <div class="image">
                <img src="public/drawings/ai_.png" alt="image IA" class="ai">
            </div>
            <div class="texte">
                <h3>L’IA : plus qu’une avancée, une véritable révolution</h3>
                <p>Au-delà d’une simple prouesse technologique, l’intelligence artificielle (IA) constitue une révolution qui propulse les entreprises vers de nouveaux sommets. Elle permet notamment de :</p>
                <ul>
                    <li>Automatiser et optimiser des processus complexes,</li>
                    <li>Analyser d’immenses volumes de données pour anticiper les tendances,</li>
                    <li>Concevoir des outils intelligents qui transforment les défis actuels en opportunités durables.</li>
                </ul>
            </div>
            <!-- Partie 2 Ma formation -->
        </div>
        <div class="partie partie-2">
            <div class="texte">
                <h3>Ma formation au service de l’innovation</h3>
                <p>C’est précisément dans cet univers que je me spécialise actuellement, grâce à ma formation de <a href="https://gretaformation.ac-orleans-tours.fr/formation/developpeurse-en-intelligence-artificielle-ia" target="_blank">Développeur en Intelligence Artificielle</a> au GRETA. Un métier à la croisée des compétences, qui combine :</p>
                <ul>
                    <li><strong>La science des données</strong> : collecte, nettoyage et exploitation de vastes bases de données.</li>
                    <li><strong>L’intelligence artificielle</strong> : conception de modèles de Machine Learning et Deep Learning pour résoudre des problématiques complexes.</li>
                    <li><strong>Le développement d’applications</strong> : intégration de ces solutions dans des outils concrets, déployés en environnement réel.</li>
                </ul>  
            </div>
            <div class="image">
                <img src="public/drawings/computer_.png" alt="image computer" class="computer">
            </div>
        </div>
        <!-- Partie 3 Ensemble -->
        <div class="partie partie-3">
            <div class="image">
            <img src="public/drawings/winning_.png" alt="image winning" class="winning">
            </div>
            <div class="texte">
            <h3>Ensemble, concrétisons vos projets IA</h3>
            <p>Ce que je recherche ? Une alternance pour contribuer à des projets ambitieux et aider votre entreprise à exploiter pleinement le potentiel de ses données. Je suis prête à me déplacer où que vous soyez, afin de rejoindre votre équipe et mettre mes compétences au service de vos objectifs. Avec l’IA, les opportunités sont infinies ✨, et j’ai hâte de participer à votre réussite.</p>
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
  font-size: 23px;
  font-weight: 700;
  margin-bottom: 20px;
}

/* Partie */

div.partie{
  display: flex;
  justify-content: space-between;
  gap: 100px;
  font-size: 16px;
  margin-bottom: 30px;
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
 color: #FFFAFA;
}

.computer{
  max-width: 350px;
}
.ai{
  max-width: 350px;
}
.winning{

  max-width: 350px;
}

</style>