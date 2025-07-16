<template>
    <NuxtRouteAnnouncer />
    <header>
        <!-- Titre/Logo de mon portofolio -->
        <div class="portofolio__logo">
            <h1>Promise .</h1>
            <DecoLine />
        </div>
        <!-- Navigation -->
        <nav>
            <!-- Liste de navigation -->
            <ul class="nav__links">
                <li>Acceuil</li>
                <li>Projet Pro</li>
                <li>Parcours</li>
                <li>Projets</li>
            </ul>
            <!-- Choix de la langue -->
            <div v-if="false" class="language__choice" title="Changer la Langue" @click="language = !language">
                <Icon name="flag:bl-4x3" v-if="!language" />
                <Icon name="flag:sh-4x3" v-if="language" />
            </div>
            <!-- Bouton de contact -->
            <button>Contact</button>
        </nav>
    </header>
    
</template>
<script>
export default {
    data(){
        return{
            language: false
        }
    }
}
</script>

<style scoped>
/* All the header */
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
    align-items: center;
    gap: 50px;
}

/* Navigation list */
.nav__links {
    display: flex;
    list-style: none;
    gap: 30px;
}
.nav__links li {
    cursor: pointer;
    font-size: 14px;
}

/* Language choice */
div.language__choice {
    font-size: 13px;
    cursor: pointer;
    display: flex;
    align-items: center;
}

/* Contact button */
button {
    background-image: linear-gradient(to right, #660BDA, 56%, #C014A6);
    width: 100px;
    height: 35px;
    border: none;
    border-radius: 5px;
    color: white;
    font-weight: 600;
    font-size: 14px;
    cursor: pointer;
    position: relative;
    bottom: -5px;
}

@media (max-width: 768px){
nav{
    display: none;
}
}
</style>


