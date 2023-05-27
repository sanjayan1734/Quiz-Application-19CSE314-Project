import { createWebHistory, createRouter } from "vue-router"

import results from "../components/quiz-taking/QuizResults.vue"
import Home from "../LandingPageFinal/LandingPage.vue"  
import quiz from "../components/quiz-taking/QuizzesPage.vue"
 import login from "../components/LoginSignup/LoginComponent.vue"
// import signup from "../components/LoginSignup/Signup.vue"
const routes = [

  {
    path: "/login",
    name: "login",
    component: login,
  },
  
  {
    path: "/quiz",
    name: "quiz",
    component: quiz,
    props: {quizName:'quiz1'}
  },
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path:"/results",
    name: "results",
    component: results,
    props: {
      noOfQuestions:String  ,
      correctAnswers:String}
  }
  
  
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
