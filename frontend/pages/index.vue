<template>
<NuxtRouteAnnouncer />
<Header></Header>
<HeaderMobile/>
<Main></Main>
<ProjetPro></ProjetPro>
<Parcours></Parcours>
<ParcourMobile/>

<Projets></Projets>
<Contact></Contact>
<Footer></Footer>
</template>
<style>
body{
    min-width: 350px;
}

input:focus{
    outline: none;
  box-shadow: none;
  border-color: inherit; 
}

textarea:focus{
    outline: none;
  box-shadow: none;
  border-color: inherit; 
}
</style>