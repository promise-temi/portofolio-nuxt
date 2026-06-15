<template>
<div class="container">
    <article class="card">
        <div class="face face1">
            <div class="content">
                <img :src="image" alt="">
            </div>
        </div>
        <div class="face face2">
            <div class="content">
                <h3>{{ title }}</h3>
            </div>
        </div>
    </article>
</div>
</template>
<script>
export default {
    props: {
        title: String,
        description: String,
        image: String,
        link: String
    }
}
</script>

<style scoped>
article.card {
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8);
    border: 0.3px solid #ffffff17;
    background-color: #34096d41;
}
article.card img {
    width: 100%;
    height: auto;
    object-fit: cover;
}
article.card:hover {
    transform: scale(1.05);
}
div.container .card .face1 {
    width: 300px;
    height: 200px;
}

div.container .card .face2 {
    width: 300px;
    height: 70px;
    

}
h3 {
    font-size: 14px;
    font-weight: 300;
    color: #f5f5f5;
    text-align:justify;
    margin: 20px;
}
</style>