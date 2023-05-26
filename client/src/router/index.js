import { createWebHistory, createRouter } from "vue-router"

// import Login from '../components/LoginSingup/views/LoginComponent.vue'
// import login from '../components/LoginSignup/LoginComponent.vue'
//import signup from '../components/LoginSignup/signup.vue'
import Home from "../LandingPageFinal/LandingPage.vue"  
import quiz from "../components/quiz-taking/QuizzesPage.vue"
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
    path: "/quiz",
    name: "quiz",
    component: quiz,
    props: {quizName:'quiz1'}
  },
  {
    path: "/",
    name: "landing",
    component: Home,
  },
  
  
]
// this.$router.push({
//   name: 'user',
//   params: {
//       quizName: 'quiz',
//        quizId: 1
//   }
// }) 


const router = createRouter({
    history: createWebHistory(),
    routes
  })
  
  export default router
