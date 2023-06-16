<script>



</script>

<template>
    <h1 style="padding: 2%;"> Quiz Creation</h1>
    <div class="question">
    <h2 class = "createquizheading">Question details</h2>
    <form @submit.prevent = "getFormValues">
        
        <center>
        <label class="createquiztext">Question: </label>
        <input class="createquiz" id= "question" placeholder="what is the question" name="questiondesc"> <br>
        <br>
        <label class="createquiztext">Option 1: </label>
        <input class="createquiz" id = "optionA" placeholder="option A"> <br>
        <br>
        <label class="createquiztext">Option 2: </label>
        <input class="createquiz" id = "optionB" placeholder="option B"> <br>
        <br>
        <label class="createquiztext">Option 3: </label>
        <input class="createquiz" id = "optionC" placeholder="option C"> <br>
        <button>add new question</button>
        <button type="submit" on-submit="console.log(this.question)">Save and close</button>
        </center>
    </form>
</div>
</template>

<style>
   

</style>