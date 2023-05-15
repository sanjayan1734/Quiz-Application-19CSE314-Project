<template>
  <div id="app">
  <login/>
    <router-view />
  </div>
</template>
<script>
  import login from './Login/Login.vue'
  import landing from './LandingPageFinal/Landingpage.vue'

  export default {
    name: 'app',
    components: {
      login,
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