import { createWebHistory, createRouter } from "vue-router"

// import Login from '../components/LoginSingup/views/LoginComponent.vue'
// import login from '../components/LoginSignup/LoginComponent.vue'
// import signup from '../components/LoginSignup/signup.vue'
import Home from "../LandingPageFinal/LandingPage.vue"  
const routes = [

  // {
  //   path: "/login",
  //   name: "login",
  //   component: login,
  // },
  // {
  //   path:"/signup",
  //   name: "signup",
  //   component: signup
  // },
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  
]


const router = createRouter({
    history: createWebHistory(),
    routes
  })
  
  export default router
