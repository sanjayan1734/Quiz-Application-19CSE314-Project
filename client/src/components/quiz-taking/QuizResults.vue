<script >
// import { defineComponent } from '@vue/composition-api'

export default {
    name: 'results',

    props:{
    noOfQuestions:String,
    correctAnswers:String
    },

}
</script>


<template>
    <h1 class="title">Quiz Results</h1>
    <div class="result">{{ this.correctAnswers }}/{{ this.noOfQuestions }}</div>
    
    <div>Go back</div>

</template>

