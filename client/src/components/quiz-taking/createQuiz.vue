<template>
    pass
    
</template>

<!-- <script>
<template>
    pass
</template>


 <script>
export default {
    data (){
        return{
            question : {
                noOfQuestions: Number,
                questionId:String,
                questionDescription:String,
                optionA:String,
                optionB:String,
                optionC:String,
            }
        }
    },
    methods: {
    getFormValues (submitEvent) {
      this.question["questionDescription"] = submitEvent.target.elements.questiondesc.value
    }
  }
}

</script>
<

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
    .question {
        top: 15%;
        position: absolute;
        width: 70%;
        height: 60%;
        color: lightblue;
        background-color: lightblue;
        left: 15%;
        display: block;
    }
    .createquiz {
        position: relative;
        width: 80%;
        height: 40px;
        border-radius: 10px;
    }
    .createquizheading {
        color: black;
        left: 5%;
        display: black;
        padding: 2%;
    }
    .createquiztext {
        color: black;
        padding: 1%;
    }

</style> -->