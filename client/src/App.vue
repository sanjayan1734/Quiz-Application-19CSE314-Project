<!-- <script>
  // import login from './Login/Login.vue'
  import QuizzesPage from './components/quiz-taking/QuizzesPage.vue'  // import landing from './LandingPageFinal/Landingpage.vue'
  import Landingpage from './LandingPageFinal/Landingpage.vue';
  export default {
    name: 'app',
    components: {
      // login,
      QuizzesPage,
      Landingpage
    },
    data() {
      return {
      quizparameters:{
      quizName : "sample quiz",
      quizId : "quiz1.1",
      noOfQuestions: "10"
      }
    }
  }
  };
</script> -->

<template>
<router-view />

  <Landingpage />
  <!-- <QuizzesPage v-bind="quizparameters" /> -->

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