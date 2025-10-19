<template>
    <section id="parcours">
        <div class="title">
            <h2>Parcours </h2>
            <DecoLine/>
        </div>
        <div class="section-all">
            <div class="elements">
                <div class="formations-et-titre">
                    <h4>  <!-- <span>🎓</span> -->Formations </h4> 
                    <div class="formations" v-for="(formation, index) in formations" :key="index" @click="selected == formations[index] ? selected = null : selected = formations[index]">
                        <div class="formation">
                            <p>{{formation.title}} </p>
                            <span>{{formation.institution}} | Tours 37100</span>
                            <h6>{{formation.duration}}</h6>
                            <div class="informations-part" v-show="selected == formations[index]">
                                <DecoLine/>
                                <p>{{formation.description}}</p>
                            </div>
                        </div>
                        
                    </div>
                </div>
                <div class="experiences-et-titre">
                    <h4 >  <!-- <span>💼</span>  -->Experiences   </h4>
                    <div class="experiences" v-for="(experience, index) in experiences" :key="index" @click="selected == experiences[index] ? selected= null : selected = experiences[index]">
                        <div class="experience" >
                            <p>{{experience.title}}</p>
                            <span>{{ experience.institution }}</span>
                            <h6>{{experience.duration}}</h6>
                            <div class="informations-part" v-show="selected == experiences[index]">
                                <DecoLine/>
                                <p>{{experience.description}}</p>
                            </div>
                        </div>
                        
                    </div>
                </div>
            </div>
            
        </div>
    </section>
</template>
<script>
export default{
    data(){
        return {
            showFormations: true,
            showExperiences: false,
            activeIndex: null,
            formations: [
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
                }
            
            ],
            experiences:[
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
            ],
            selected : null,
        }
    },
    methods:{
        
    }

}
</script>
<style scoped>
h4{
    cursor: pointer;
}

h4 span {
    position: relative;
    right: -10px;
}
section{
    /* background-image: linear-gradient(50deg, #10071E, #660BDA); */
    background-color: #34096d;
    position: relative;
    z-index: 5;
    color: white;
    padding: 50px;
    display: none;

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
    width: 100%;
}

div.formations-et-titre{
    width: 100%;
}

div.experiences-et-titre{
    width: 100%;
}

.formations, .experiences{
    display: flex;
    flex-direction: column;
    
    width: 100%;
    min-width: 300px;
    
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
    width: 100%;
    display: flex;
    flex-direction: column;
    padding-right: 20px;
    position: relative;
    bottom: -15px;
    padding-bottom: 20px;
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

.formation, .experience{
    margin-bottom: 15px;
}

@media (max-width:480px){
    section{
        padding-left: 20px;
        padding-right: 20px;
    }
}

@media (max-width:850px){

section{
    display: block;
}
}

</style>