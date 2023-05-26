import { createWebHistory, createRouter } from "vue-router"

// import Login frommport login from '. '../components/LoginSingup/views/LoginComponent.vue'
// i./components/LoginSignup/LoginComponent.vue'

import Home from "../LandingPageFinal/LandingPage.vue"  
import login from "../components/LoginSignup/LoginComponent.vue"
const routes = [

  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "login",
    component: login,
  },
]


const router = createRouter({
    history: createWebHistory(),
    routes
  })
  
  export default router
