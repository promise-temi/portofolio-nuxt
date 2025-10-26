<template>
    <section id="parcours">
        <div class="title">
            <h2>Background </h2>
            <DecoLine/>
        </div>
        <div class="section-all">
            <div class="elements">
                <div class="formations-et-titre">
                    <h4>  <!-- <span>🎓</span> -->Education </h4> 
                    <div class="formations" v-for="(formation, index) in formations" :key="index" @click="selected=formations[index]" >
                        <div class="formation">
                            <p>{{formation.title}} <span v-if="selected === formations[index]">✨</span></p>
                            <span>{{formation.institution}} | {{ formation.localisation }}</span>
                            <h6>{{formation.duration}}</h6>
                        </div>
                        
                    </div>
                </div>
                <div class="experiences-et-titre">
                    <h4 >  <!-- <span>💼</span>  -->Experiences   </h4>
                    <div class="experiences" v-for="(experience, index) in experiences" :key="index" @click="selected=experiences[index]" >
                        <div class="experience" >
                            <p>{{experience.title}} <span v-if="selected === experiences[index]">✨</span></p>
                            <span>{{ experience.institution }} | {{ experience.localisation }}</span>
                            <h6>{{experience.duration}}</h6>
                        </div>
                        
                    </div>
                </div>
            </div>
            <Transition name="fade" mode="out-in">
            <div class="informations-part" :key="number">
                <div class="title">
                    <h4>{{selected.title}}</h4>  
                    <h6><a :href="selected.link" target="_blank" title="More infos">{{selected.institution}}</a>  |  {{ selected.localisation }}</h6>
                    <h6>{{selected.duration}}</h6>
                    <DecoLine/>
                </div>
                <p style="white-space: pre-line;">{{selected.description}}</p>
            </div>
            </Transition>
        </div>
    </section>
</template>
<script>
export default{
    data(){
        return {
            showFormations: true,
            showExperiences: false,
            
            formations: [
                // Formations
                {
                    title: "Artificial Intelligence Developer",
                    institution: "Greta Centre Val de Loire",
                    localisation: "Tours 37100",
                    duration: "nov.2024 - july.2026",
                    description: `A professional training program combining theory and practice, with seven intensive months in class followed by twelve months in a work-study program (alternance). 
                    This course has allowed me to develop strong skills across three complementary areas: 

                    ➜ Data Science : Collecting, cleaning and exploring large datasets,
                    ➜ Artificial Intelligence : Training machine learning and deep learning models to solve complex problems,
                    ➜ Application Development : Integrating these solutions into concrete tools deployed in real-world environments. 

                    A comprehensive program that has given me a global understanding of the AI project lifecycle, from raw data to a fully functional tool.`,
                    link: "https://gretaformation.ac-orleans-tours.fr/formation/developpeurse-en-intelligence-artificielle-ia",
                },
                {
                    title: "Full-Stack Web Developer",
                    institution: "Studi",
                    localisation: "Online",
                    duration: "sept.2023 - june.2024",
                    description: `A 100% online training program with Studi, which allowed me to acquire solid foundations in web development, both on the front-end and back-end sides. The program was combined with work-study period (alternance), giving me the opportunity to apply my skills in real professional contexts on a daily basis. 

                    In parallel, I chose to train myself with a more personal and modern stack adapted to my own projects: Vue, Nuxt for the front end, and Python (Flask, FastAPI, Django) for the back end. This personal choice helped me improve my efficiency and, most importantly, enjoy coding. 

                    The online format, with little direct supervision, was a real challenge. It required motivation, organization, and self-discipline to keep progressing. An intense, rewarding, and deeply formative experience.`,
                    link: "https://www.francecompetences.fr/recherche/rncp/31114/",
                },
            
            ],
            experiences:[
                // Experiences
                {
                    title: "AI & Data Developer",
                    institution: "Wabtec",
                    localisation: "Saint-Pierre-Des-Corps ",
                    duration: "aug.2025 - sept.2026",
                    description: `Currently working as an AI Developer with Wabtec, a leading American company in the railway industry, on a predictive maintenance project focused on train doors and mobile steps. The project involves time-series analysis to detect patterns and anticipate potential faults, combining data preprocessing, feature engineering, clustering, and model training with the development and deployment of web-based tools.
                    
                    Collaboration with mechanical engineers, R&D engineers and other specialists is key to understanding the operational context and ensuring data quality. 
                    
                    A challenging and meaningful project that allows me to apply advanced methods, strengthen my technical expertise, and contribute to the use of AI in a high-impact industrial context.
                    
                    As part of my work-study program (alternance) with Greta Centre Val de Loire, my schedule alternates three weeks in the company and one week  at school.`,
                    link: "https://www.wabteccorp.com/",
                },
                {
                    title: "Fullstack Web Developer",
                    institution: "Interaction",
                    localisation: "Rennes (Head Office)",
                    duration: "sept.2023 - aug.2024",
                    description: `Joined Interaction Group, one of France’s leading employment agencies, as a web developer for my first professional experience in tech. I took part in projects that went beyond traditional web development, working on data-related and automation tools.
                    
                    One of the most notable projects was an auto-scraping tool designed to collect and display job offers in real time.

                    I was fully responsible for the projects progress, from design to delivery.
                    
                    This experience was both challenging and formative. It allowed me to strengthen my autonomy, technical versatility and gain confidence in my ability to learn fast, adapt and deliver concrete results. 
                    
                    As part of my work-study program (alternance) with Studi, my schedule alternates three days in the company and two days at school.`,
                    link: "https://www.sinad-emploi.fr/",
                }
            ],
            selected: null
        }
        
        
    },
    created(){
        
            this.selected = this.formations[0]
        },
    methods:{
        sshowFormation(){
            if(window.innerWidth > 850){ 
                this.showFormations = !this.showFormations;
                this.showExperiences = false

            }
        },

        sshowExperience(){
            if(window.innerWidth > 850){ 
                this.showExperiences = !this.showExperiences;
                this.showFormations = false
            }
        }
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

div.formations-et-titre{
    width: 500px;
}

div.experiences-et-titre{
    width: 500px;
}

.formations, .experiences{
    display: flex;
    flex-direction: column;
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

.formation, .experience{
    margin-bottom: 10px;
}
@media (max-width:1000px) {
    /* section#parcours{
        display: none;
    } */

    div.formations-et-titre{
    width: 400px;
}

div.experiences-et-titre{
    width: 400px;
}

.formations, .experiences{
    width: 400px;
    min-width: 350px;
}
}

@media (max-width:850px){
div.informations-part{
    display: none;
}

section{
    display: none;
}
/* 
div.formations-et-titre{
    width: 100%;
}

div.experiences-et-titre{
    width: 100%;
}

.formations, .experiences{
    width: 100%;
    min-width: auto;
}
div.elements{
    width: 100%;
}

h4 svg {
    display: none;
} */



}

@media (min-width:1300px){
  section{
    padding: 50px 130px;
  }
}
</style>