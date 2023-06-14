import { createWebHistory, createRouter } from "vue-router"

import results from "../components/quiz-taking/QuizResults.vue"
 import Home from "../components/LandingPageFinal/LandingPage.vue"  
import quiz from "../components/quiz-taking/QuizzesPage.vue"
 import login from "../components/LoginSignup/LoginComponent.vue"
import dashboard from "../components/dashboard/Dashboard.vue"
import Instructions from "../components/Instructions/Instructions.vue"
import faculty from "../components/Faculty/FacultyPage.vue"
import forgotpassword from "../components/LoginSignup/ForgotPassword.vue"
import resetpwd from "../components/LoginSignup/ResetPassword.vue"
import UsersPage from "../components/ReportAndAnalytics/UsersPage.vue"
import createQuiz from "../components/quiz-taking/createQuiz.vue"

const routes = [

  {
    path: "/login",
    name: "login",
    component: login,
  },
  {
    path: "/reset",
    name: "reset",
    component: resetpwd,
  },
  {
    path: "/forgotpwd",
    name: "forgotpwd",
    component: forgotpassword,
  },
  {
    path: "/faculty",
    name: "faculty",
    component: faculty,
  },
  {
    path: "/dashboard/:mail",
    name: "dashboard",
    component: dashboard,
    props: true,
  },
  
  {
    path: "/quiz/:quizId",
    name: "quiz",
    component: quiz,
    props: true
  },
  {
    path: "/users",
    name: "usersPage",
    component: UsersPage,
    
  },
  {
    path:"/results",
    name: "results",
    component: results,
    props: {
      noOfQuestions:String  ,
      correctAnswers:String}
  },
    {
    path: "/Instructions",
    name: "Instructions",
    component: Instructions,
  },
  {
    path: "/",
    name: "home",
    component: Home,
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
