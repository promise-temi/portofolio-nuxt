<template>
  <div id="website-scale-wrapper" ref="wrapper">
    <NuxtRouteAnnouncer />
    <NuxtPage />
  </div>
</template>


<script>
export default {
  data() {
    return {
      BASE_WIDTH: 1250
    }
  },


  mounted() {
    this.scaleSite()
    window.addEventListener('resize', this.scaleSite)
  },


  beforeUnmount() {
    window.removeEventListener('resize', this.scaleSite)
  },


  methods: {
    scaleSite() {
      if (typeof window === 'undefined' || !this.$refs.wrapper) return


      const vw = window.innerWidth
      const wrapper = this.$refs.wrapper


      if (vw > this.BASE_WIDTH) {
        const scale = vw / this.BASE_WIDTH


        // on passe en mode "scaled"
        wrapper.classList.add('scaled')
        wrapper.style.transform = `translateX(-50%) scale(${scale})`
      } else {
        // on revient au mode normal
        wrapper.classList.remove('scaled')
        wrapper.style.transform = 'none'
      }
    }
  }
}

</script>




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
    background-color: black;
    display: flex;

    justify-content: center;
  }

  a{
    color: white;
    text-decoration: none;
  }


@media (min-width:1250px){
  * {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
  font-family: 'Poppins', sans-serif;
}


html, body {
  margin: 0;
  padding: 0;
  overscroll-behavior: none;
  scroll-behavior: smooth;
  background-color: black;
  overflow-x: hidden;
}


body {
  background-color: #10071e;
}


a {
  color: white;
  text-decoration: none;
}


/* LE MONDE DE BASE : 1250px */
#website-scale-wrapper {
  width: 1250px;
  transform-origin: top center;
  position: absolute;
  left: 50%;
  top: 0;
  transform: translateX(-50%) scale(1);
}

}
</style>