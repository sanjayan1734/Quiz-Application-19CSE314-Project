<script>

export default {
    name:"userCard",

    props:{
    Username : String,
    ratings: String,
    },

    
}


</script>

<template>
    <div class="main-card">
    <div class="flex-container">
        <div class="userName">
            {{Username}}
        </div>
        <div class="ratings">
            {{ratings}}
        </div>
    </div>
</div>
</template>

<style>

.flex-container {
border-radius: 1rem;
padding: 0.5%;
width: 90%;
height: 90px;
display: flex;
justify-content: space-between;
flex-direction: row;

flex-wrap: nowrap;
background-color: lightcoral;
}

.flex-container > div {
    font-size: 20px;
    align-self: center;

}

.main-card {
    padding-left: 5%;
    margin-top: 2%;
}

</style>