<template>

  <div>
    <NuxtRouteAnnouncer />
    <!-- <NuxtWelcome /> -->
    <NuxtPage />
    
  </div>
</template>

<style>

  * {
    box-sizing: border-box;
    padding: 0;
    margin: 0;
    font-family: 'Poppins', sans-serif;
  }
  body {
      background-color: #10071e;
      overflow-x: hidden; /* Empêche le scroll horizontal */
      
  }
  html, body {
  overscroll-behavior: none; /* Empêche le over scroll de la page */
}
html {
    scroll-behavior: smooth; /* Permet le scroll smooth */
  }
</style>