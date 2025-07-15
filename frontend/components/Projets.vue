<template>
    <Section>
            <div class="title">
                <h2>Projets</h2>
                <DecoLine/>
            </div>
        <div class="projects__section">
            <div class="project__cards">
                <Card title="Prédition du nutriscore d'un produit alimentaire" description="Description du projet 1" image="drawings/predict_nutriscore.png" link="#"/>
                <Card title="Prédition de la classification nova d'un produit alimentaire" description="Description du projet 2" image="drawings/predict_nova.png" link="#"/>
                <Card title="Ingrédiants d'un produit alimentaire à partir d'une photo" description="Description du projet 3" image="drawings/ocr_ingrediants.png" link="#"/>
                <Card title="Valeurs nutritonnelles d'un produit alimentaire à partir d'une photo" description="Description du projet 4" image="drawings/ocr_nutri_values.png" link="#"/>
            </div>
        </div>
    </Section>
</template>
<style scoped>
section{
    position: relative;
    z-index: 5;
    padding: 50px;

}
h2{
    position: relative;
    z-index: 5;
    font-family: "Poppins";
    font-size: 20px;
    font-weight: 600;
    color:white;
}
div.projects__section{
   margin: 50px 0;
    display: grid;
  place-items: center;

}
.project__cards {
    display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: flex-start; /* ← aligne à gauche */
  gap: 30px;
  max-width: 1000px;
}
</style>