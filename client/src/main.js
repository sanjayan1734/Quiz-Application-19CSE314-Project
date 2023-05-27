
import router from './router'
    
import 'vue2-perfect-scrollbar/dist/vue2-perfect-scrollbar.css'


import { createApp } from 'vue'
import App from './App.vue'


createApp(App).use(router).mount('#app')
