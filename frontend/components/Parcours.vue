<template>
    <section id="parcours">
        <div class="title">
            <h2>Parcours </h2>
            <DecoLine/>
        </div>
        <div class="section-all">
            <div class="elements">
                <div class="formations-et-titre">
                  <h4>  <!-- <span>🎓</span> -->Formations</h4> 
                    <div class="formations">
                        <div class="formation" @click="number = 0 ">
                            <p>Développeur en intélligence artificielle <span v-if="number === 0">✨</span></p>
                            <span>Greta centre val de loire ( 2024 - 2026 )</span>
                        </div>
                        <div class="formation" @click="number = 1">
                            <p>Développeur web et web mobile <span v-if="number === 1">✨</span></p>
                            <span>Studi</span>
                        </div>
                    </div>
                </div>
                <div class="experiences-et-titre">
                  <h4>  <!-- <span>💼</span>  -->Experiences</h4>
                    <div class="experiences">
                        <div class="experience" @click="number = 2">
                            <p>Apprenti Développeur IA <span v-if="number === 2">✨</span></p>
                            <span>Wabtec corporation</span>
                        </div>
                        <div class="experience" @click="number = 3">
                            <p>Développeur web fullstack <span v-if="number === 3">✨</span></p>
                            <span>Sinad emploi</span>
                        </div>
                    </div>
                </div>
            </div>
            <Transition name="fade" mode="out-in">
            <div class="informations-part" :key="number">
                <div class="title">
                    <h4>{{parcours[number].title}}</h4>  
                    <h6><a :href="parcours[number].link" target="_blank" title="En savoir plus">{{parcours[number].institution}}</a>  |  Tours 37100</h6>
                    <h6>{{parcours[number].duration}}</h6>
                    <DecoLine/>
                </div>
                <p>{{parcours[number].description}}</p>
            </div>
            </Transition>
        </div>
    </section>
</template>
<script>
export default{
    data(){
        return {
            number: 0,
            parcours: [
                // Formations
                {
                    title: "Développeur en intélligence artificielle",
                    institution: "Greta Centre Val de Loire",
                    duration: "nov.2024 - juil.2026",
                    description: "Une formation professionnalisante qui mêle théorie et pratique, avec 7 mois intensifs en centre suivis de 12 mois en alternance. Ce parcours m’a permis de développer des compétences solides autour de trois axes complémentaires :     La science des données : collecte, nettoyage et exploitation de vastes bases de données.     L’intelligence artificielle : conception de modèles de Machine Learning et Deep Learning pour résoudre des problématiques complexes.     Le développement d’applications : intégration de ces solutions dans des outils concrets, déployés en environnement réel. Une formation complète, qui m’a donné une vision globale du cycle de vie d’un projet IA — de la donnée brute à l’outil fonctionnel.",
                    link: "https://gretaformation.ac-orleans-tours.fr/formation/developpeurse-en-intelligence-artificielle-ia",
                },
                {
                    title: "Développeur web et web mobile",
                    institution: "Studi",
                    duration: "sept.2023 - juin.2024",
                    description: "Une formation 100 % en ligne avec Studi, qui m’a permis d’acquérir des bases solides en développement web, aussi bien côté front-end que back-end. Le tout en alternance, ce qui m’a permis de mettre en pratique mes compétences au quotidien, dans un vrai contexte professionnel.En parallèle, j’ai choisi de me former sur ma propre stack, plus moderne et mieux adaptée à mes projets : Vue.js pour le front-end, et Python (Flask/FastAPI) pour le back-end.Un choix personnel qui m’a permis de gagner en autonomie, en efficacité, et en plaisir de coder.Le format à distance, avec peu d’encadrement direct, représentait un vrai défi. Il fallait être motivé, organisé et suffisamment autodidacte pour progresser.Une expérience intense, enrichissante, et profondément structurante.",
                    link: "https://www.francecompetences.fr/recherche/rncp/31114/",
                },
            // Experiences
                {
                    title: "Développeur IA en alternance",
                    institution: "Wabtec Corporation",
                    duration: "aout.2025 - sept.2026",
                    description: "Travail en tant qu'apprenti développeur IA, impliqué dans des projets de machine learning et d'analyse de données.",
                    link: "https://www.wabteccorp.com/",
                },
                {
                    title: "Développeur web fullstack en alternance",
                    institution: "Sinad Emploi",
                    duration: "sept.2023 - aout.2024",
                    description: "Expérience en développement web fullstack, travaillant sur divers projets pour améliorer les compétences techniques.",
                    link: "https://www.sinad-emploi.fr/",
                }
            ]
        }
    },

}
</script>
<style scoped>
section{
    /* background-image: linear-gradient(50deg, #10071E, #660BDA); */
    background-color: #34096d;
    position: relative;
    z-index: 5;
    color: white;
    padding: 50px;

}
.title{
    
    margin-bottom: 30px;
}
h2{
    position: relative;
    z-index: 5;
    font-family: "Poppins";
    font-size: 20px;
    font-weight: 600;
}


.section-all{
    display: flex;
    justify-content: space-between;
    gap: 50px;
}
.elements{
    display: flex;
    flex-direction: column;
    gap: 30px;
}

.formations, .experiences{
    display: flex;
    flex-direction: column;
    gap: 10px;
    width: 500px;
    min-width: 450px;
    
    cursor: pointer;
}
.formation, .experience{
    background-color: #10071e71;
    padding: 10px;
    font-size: 14px;
    border-radius: 10px;
    padding-left: 30px;
}

.formations-et-titre h4, .experiences-et-titre h4{
    font-size: 14px;
    margin-bottom: 10px;
    font-weight: 500;
}



.formations-et-titre h4 span{
    font-size: 20px;
}
.experiences-et-titre h4 span{
    font-size: 16px;
}

.formation p, .experience p{
    font-size: 14px;
    font-weight: 400;
    
}

.formation span, .experience span{
    font-size: 12px;
    color: #c014a6;
    
}

.informations-part{
    width: 650px;
    display: flex;
    flex-direction: column;
}

.informations-part .title h4{
    font-size: 22px;
    font-weight: 600;
}
.informations-part .title h6{
    font-size: 12px;
    font-weight: 600;
}
.informations-part p{
    font-size: 14px;
    font-weight: 300;
    text-align: justify;
}

.informations-part a{
     font-size: 13px;
    
     color: #c014a6;

}
.informations-part a:hover{
    text-decoration: underline;
     color: #c014a6;

}

/* animation */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.1s ease-in;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
/* end animation */
</style>