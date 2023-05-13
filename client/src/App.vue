<template>
  <div id="app">
  <landing/>
    <router-view />
  </div>
</template>
<script>
  import Nav from './components/Nav.vue';
  import Home from './views/Home.vue';
  import About from './views/About.vue';
  import landing from './LandingPageFinal/Landingpage.vue'
  export default {
    name: 'app',
    components: {
      landing,
    },
  };
</script>
<!-- <style lang="scss">
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
  }
</style> -->