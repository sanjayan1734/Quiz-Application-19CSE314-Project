
import router from './router'
    
import'./components/LandingPageFinal/css/styles.css';
import './components/LandingPageFinal/js/scripts.js';

import { createApp } from 'vue'
import App from './App.vue'


createApp(App).use(router).mount('#app')
