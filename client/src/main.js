import './LandingPageFinal/css/styles.css'

import './LandingPageFinal/js/scripts.js'

import router from './router'
 //import "https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/js/bootstrap.min.js"
// import "//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"
//import './Login/login.js'
import './Login/loginstyle.css'
import { createApp } from 'vue'
import App from './App.vue'

createApp(App).use(router).mount('#app')
