<!-- <script>
  // import login from './Login/Login.vue'
  import QuizzesPage from './components/quiz-taking/QuizzesPage.vue'  // import landing from './LandingPageFinal/Landingpage.vue'

  export default {
    name: 'app',
    components: {
      // login,
      QuizzesPage
    },
    data() {
      return {
      quizparameters:{
      quizName : "Quiz1",
      quizId : "quiz1.1",
      }
    }
  }
  };
</script> -->

<template>
  <!-- <QuizzesPage v-bind="quizparameters" /> -->
  <router-view/>
  <!-- <div id="app">
  <login/>
    <router-view />
  </div> -->
  
  <!-- <landing /> -->
</template>

<!-- <style lang="scss">
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
  }
</style> -->