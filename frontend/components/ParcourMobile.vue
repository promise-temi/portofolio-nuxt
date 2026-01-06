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
                            <span><a :href="formation.link" target="_blank" title="More infos">{{formation.institution}}</a> | {{ formation.localisation }}</span>
                            <h6>{{formation.duration}}</h6>
                            <div class="informations-part" v-show="selected == formations[index]">
                                <DecoLine/>
                                <p style="white-space: pre-line;">{{formation.description}}</p>
                            </div>
                        </div>
                        
                    </div>
                </div>
                <div class="experiences-et-titre">
                    <h4 >  <!-- <span>💼</span>  -->Experiences   </h4>
                    <div class="experiences" v-for="(experience, index) in experiences" :key="index" @click="selected == experiences[index] ? selected= null : selected = experiences[index]">
                        <div class="experience" >
                            <p>{{experience.title}}</p>
                            <span><a :href="experience.link" target="_blank" title="More infos">{{experience.institution}}</a> | {{ experience.localisation }}</span>
                            <h6>{{experience.duration}}</h6>
                            <div class="informations-part" v-show="selected == experiences[index]">
                                <DecoLine/>
                                <p style="white-space: pre-line;">{{experience.description}}</p>
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
                    title: "Artificial Intelligence Developer",
                    institution: "Greta Centre Val de Loire",
                    localisation: "Tours 37100",
                    duration: "nov.2024 - july.2026",
                    description: `A professional training program combining theory and practice, with seven intensive months in class followed by twelve months in a work-study program (apprenticeship). 
                    This course has allowed me to develop strong skills across three complementary areas: 

                    ➜ Data Science
                    ➜ Application Development 
                    ➜ Aplied AI

                    🏆 A comprehensive program that has given me a global understanding of the AI project lifecycle, from raw data to a fully functional tool.`,
                    link: "https://gretaformation.ac-orleans-tours.fr/formation/developpeurse-en-intelligence-artificielle-ia",
                },
                {
                    title: "Full-Stack Web Developer",
                    institution: "Studi",
                    localisation: "Online",
                    duration: "sept.2023 - june.2024",
                    description: `A 100% online training program with Studi, which allowed me to acquire solid foundations in web development, both on the front-end and back-end sides. The program was combined with work-study period (apprenticeship), giving me the opportunity to apply my skills in real professional contexts on a daily basis. 

                    In parallel, I chose to train myself with a more personal and modern stack adapted to my own projects: Vue, Nuxt for the front end, and Python (Flask, FastAPI, Django) for the back end. This personal choice helped me improve my efficiency and, most importantly, enjoy coding. 

                    🏆 The online format, with little direct supervision, was a real challenge. It required motivation, organization, and self-discipline to keep progressing. An intense, rewarding, and deeply formative experience.`,
                    link: "https://www.francecompetences.fr/recherche/rncp/31114/",
                },
                {
                    title: "Engineering program - AI Specialization",
                    institution: "???",
                    localisation: "France",
                    duration: "Seeking admission for September 2026",
                    description: `After building strong foundations in data science, machine learning and applied AI, I am now looking to take my education to the next level.
                    For September 2026, I am seeking admission into an engineering program or a specialized master’s degree in Artificial Intelligence.

                    What I am looking for is a program that will allow me to:
                    ➜ Deepen my theoretical foundations of AI
                    ➜ Explore AI in multiple fields (industry, robotics, cybersecurity, health, embedded systems…)
                    ➜ Develop a truly multidisciplinary engineering mindset, beyond pure data science
                    ➜ Strengthen my ability to design, deploy and validate end-to-end intelligent systems

                    I value engineering schools for their generalist approach and their ability to shape versatile, technically mature and industry-ready profiles.
                    A strong theoretical core followed by an AI specialization is exactly what I am looking for.

                    I am actively exploring programs for 2026, and I am excited to join an environment where I can grow, contribute, and push my expertise in AI even further preferably through a work-study program (apprenticeship), which is my top priority.`,
                }
            
            ],
            experiences:[
                // Experiences
                {
                    title: "Fullstack AI Developer",
                    institution: "Wabtec",
                    localisation: "Saint-Pierre-Des-Corps ",
                    duration: "aug.2025 - sept.2026",
                    description: `Currently working as an AI Developer with Wabtec, a leading American company in the railway industry, on a predictive maintenance project focused on train doors and mobile steps. The project involves time-series analysis to detect patterns and anticipate potential faults, combining data preprocessing, feature engineering, clustering, and model training with the development and deployment of web-based tools.
                    
                    Collaboration with mechanical engineers, R&D engineers and other specialists is key to understanding the operational context and ensuring data quality. 
                    
                    🏆 A challenging and meaningful project that allows me to apply advanced methods, strengthen my technical expertise, and contribute to the use of AI in a high-impact industrial context.
                    
                    🗓️ As part of my work-study program (apprenticeship) with Greta Centre Val de Loire, my schedule alternates three weeks in the company and one week  at school.`,
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
                    
                    🏆 This experience was both challenging and formative. It allowed me to strengthen my autonomy, technical versatility and gain confidence in my ability to learn fast, adapt and deliver concrete results. 
                    
                    🗓️ As part of my work-study program (apprenticeship) with Studi, my schedule alternated three days in the company and two days at school.`,
                    link: "https://www.sinad-emploi.fr/",
                },
                {
                    title: "Fullstack AI Engineer",
                    institution: "???",
                    localisation: "France",
                    duration: "Seeking a work-study program (apprenticeship), starting September 2026",
                    description: `Starting in September 2026, I will be joining an engineering program or a specialized master’s degree in Artificial Intelligence in a work-study format (apprenticeship).
                    I'm therefore looking for a host company for a duration of 1 to 3 years.
                    
                    I'm seeking a company that has a clear vision and strong technological ambition, values innovation, autonomy, and wants to integrate AI deeply into its products, operations or strategy.

                    By 2026, I will already be fully operational as both:
                    - a web developer (full-stack experience, production-ready interfaces),
                    - an applied AI developer (ML pipelines, model integration, real-world deployment).

                    This means you can rely on me from day one.
                    Your teams won’t have to “start from scratch” with me. I will be able to contribute immediately and grow alongside your existing projects.
                    
                    If my vision aligns with yours, I would be excited to contribute, learn, and build long-lasting impact together.`,
                    link: "#",
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
    justify-content:flex-start;
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

.formation span, .experience span, .formation span a, .experience span a{
    font-size: 12px;
    color: #c014a6;
    cursor: pointer;
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