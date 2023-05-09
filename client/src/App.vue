<script setup>
import Questioncomponent from './components/quiz-taking/QuizComponent.vue'
import Navbar from './components/Navbar/NavBar.vue';
import QuizzesPage from './components/quiz-taking/QuizzesPage.vue'
let gprops 

</script>

<template class = "main">
    <Navbar></Navbar>
    <Questioncomponent v-bind="gprops"></Questioncomponent>
    <QuizzesPage></QuizzesPage>
    
</template>

<style scoped>

</style>
