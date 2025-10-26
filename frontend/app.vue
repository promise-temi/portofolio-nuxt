<template>

  <div>
    <NuxtRouteAnnouncer />
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
      max-width: 1440px
  }
  html, body {
  overscroll-behavior: none; /* Empêche le over scroll de la page */
}
html {
    scroll-behavior: smooth; /* Permet le scroll smooth */
    background-color: black;
    display: flex;

    justify-content: center;
  }

  a{
    color: white;
    text-decoration: none;
  }
</style>