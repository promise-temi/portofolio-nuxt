<template>
    <NuxtRouteAnnouncer />
    <header>
        <!-- Titre/Logo de mon portofolio -->
        <div class="portofolio__logo">
            <h1>Promise .</h1>
            <DecoLine />
        </div>
        <div class="humberger">
            <svg @click="menuState = !menuState" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-list" viewBox="0 0 16 16">
            <path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5"/>
            </svg>
        </div>
        <!-- Navigation -->
        <nav v-if="menuState">
            <!-- Liste de navigation -->
            <ul class="nav__links">
                <div class="close">
                    <svg @click="menuState = !menuState" xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-x" viewBox="0 0 16 16">
                    <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708"/>
                    </svg>
                </div>
                <li><a href="#acceuil">Acceuil</a></li>
                <li><a href="#motivations">Motivations</a></li>
                <li ><a href="#parcours">Parcours</a></li>
                <!-- <li><a href="#projets">Projets</a></li> -->
                 
                 <!-- Bouton de contact -->
                 <li class="contact"><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
</template>
<script>
export default{
    data(){
        return{
            menuState : false
        }
    }
}
</script>

<style scoped>
/* All the header */

header{
    display: none;
}
@media (max-width: 768px){
header {
    display : flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 30px;
    background-color: #01050D;
    color: #fff;
    position: sticky;
    z-index: 1000;
    width: 100%;
    
}

/* Logo */
.portofolio__logo {
    display: flex;
    flex-direction: column;
    
}
.portofolio__logo h1{
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 10px;
}

/* All the nav entities */
nav {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 50px;
}

/* Navigation list */
.nav__links {
    display: flex;
    flex-direction: column;
    list-style: none;
    
    position: absolute;
    top: 0;
    right: 0;
    background-color: #10071e;
    border: rgba(255, 197, 242, 0.203) solid 0.3px;
    border-right: none;
}
.nav__links li {
    cursor: pointer;
    font-size: 14px;
    padding: 10px;
    padding-right: 70px;
    padding-left: 30px;

}

/* Language choice */
div.language__choice {
    font-size: 13px;
    cursor: pointer;
    display: flex;
    align-items: center;
}

/* Contact button */
li.contact {
    background-image: linear-gradient(to right, #660BDA, 56%, #C014A6);
    
}

div.close{
    position: relative;
    height: 35px;
}

div.close svg{
    position: absolute;
    right: 10px;
    top: 10px;
    cursor: pointer;
}
div.humberger svg{
    position: absolute;
    right: 20px;
    top: 10px;
    cursor: pointer;
}
}
</style>


