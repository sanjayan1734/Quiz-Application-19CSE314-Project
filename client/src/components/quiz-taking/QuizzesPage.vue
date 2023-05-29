<!-- <QuestionComponent v-bind="questionobj" /> -->

<script >
import { RouterLink } from "vue-router"

import QuestionComponent from "./questionComponent.vue"
// import { Ref } from "vue"
import axios from 'axios'
import { toRaw } from 'vue'
//import VueAxios from 'vue-axios'
 //Vue.use(VueAxios,axios)
export default {
  name: 'QuizzesPage',
  
  mounted()
  {
    this.getQuizURL()
    this.getvalidateURL()
    axios.get(this.quizURL).then((response) => {
      this.questionData = response.data
      console.log(response.data);
      this.individualQuestion=response.data[this.currentQuestion]
      console.log(this.individualQuestion)
      console.log(this.individualQuestion.question)
      this.questionobj.questionid=this.individualQuestion.questionid
      this.questionobj.questionDescription=this.individualQuestion.question
      this.questionobj.optionA=this.individualQuestion.opt1
      this.questionobj.optionB=this.individualQuestion.opt2
      this.questionobj.optionC=this.individualQuestion.opt3
      this.noOfQuestions = response.data.length
      });
  },
  
  components:{
    QuestionComponent,
  },
  props:{
    quizName:String,
    quizId: String,
    
  },
  data() {
    return {
      validateURL:'https://localhost:7282/api/Quiz/ValidateAnswersfor',
      quizURL:'https://localhost:7282/api/Quiz/GetQuestionsbyquiz?qid=',
      chosenOption:String,
      userChoices:[],
      rawUserChoices:[],
      quizId:String,
      questionData:[
      {
        question:String,
        questionid:String,
        opt1:String,
        opt2:String,
        opt3:String
      }
      ],
      individualQuestion:{
        question:String,
        questionid:String,
        opt1:String,
        opt2:String,
        opt3:String
      },
      noOfQuestions: String,
    questionobj:{
      questionDescription: "",//this.individualQuestion.question,
      questionid: "",//this.individualQuestion.questionid,
      optionA:"",//this.individualQuestion.opt1,
      optionB: "",//this.individualQuestion.opt2,
      optionC: "",//this.individualQuestion.opt3
    },
      currentQuestion: 0,
      
    }
  },
  methods: {
    pressedContinue() {
        this.getChosenOption()
        this.currentQuestion += 1
        this.renderquestion();
        
    },
    pressedSubmit() {
      this.getChosenOption()
      this.rawUserChoices = toRaw(this.userChoices)
      console.log(this.rawUserChoices)
      axios.post(this.validateURL,this.rawUserChoices).then((response) => {
        console.log(response.data)
        alert('Your score is ' + response.data)
        // this.$router.push({name:'results', params:{noOfQuestions:this.noOfQuestions, correctAnswers:response.data}})
        this.$router.push({path:'/'})
      })
      
      
      
    },
    renderquestion() {
      
      this.individualQuestion=this.questionData[this.currentQuestion]
      console.log(this.individualQuestion)
      console.log(this.individualQuestion.question)
      this.questionobj.questionid=this.individualQuestion.questionid
      this.questionobj.questionDescription=this.individualQuestion.question
      this.questionobj.optionA=this.individualQuestion.opt1
      this.questionobj.optionB=this.individualQuestion.opt2
      this.questionobj.optionC=this.individualQuestion.opt3
      
      this.$forceUpdate()
    },
    getQuizURL() {
      this.quizId = this.$route.params.quizId
      this.quizURL += this.quizId
      console.log(this.quizURL)
      console.log()
      this.quizURL += this.quizid
  
    },
    getvalidateURL() {
      this.validateURL +=this.quizName
    },
    getChosenOption() {
      this.chosenOption = String(this.$refs.questioncomponent.questionOption)
      this.userChoices.push(JSON.parse(JSON.stringify(this.chosenOption)))

    }
    
  }
}
</script>

<template>
    <div class="home-container">
      <div class="home-web">

        <button class="home-group7" v-if="currentQuestion+1 != noOfQuestions" @click="pressedContinue();">
          <span class="home-text" >
          <span>CONTINUE</span></span>
        </button>

        <button class="home-group7" v-if="currentQuestion+1 == noOfQuestions" @click="pressedSubmit();">
          <span class="home-text"><span>SUBMIT</span></span>
        </button>
        
        <div class="home-group6" >
          <span class="home-text25"><span>{{currentQuestion + 1}}/{{ noOfQuestions }}</span></span>
        </div>
        
        <div class="home-group14">
          <div class="home-group21">
  
            <span class="home-text27"><span>{{quizName}}</span></span>
            
          </div>
        </div>
        <div class="question">
            <QuestionComponent  v-bind="questionobj" ref="questioncomponent"/>
            <!--  props - :questionDescription= 'questionDesc'  questionid = 'questionId'  optionA = 'optionA' optionB = optionB optionC = optionC -->
        </div>
        </div>
    </div>
  </template>
  
 
  
  <style scoped>
  .home-container {
    width: 100%;
    height:100%;
    display: flex;
    overflow:hidden;
    /* min-height: 100vh; */
    align-items: center;
    flex-direction: column;
  }
  .home-web {
    width: 100%;
    height: 755px;
    display: flex;
    overflow:visible;
    position: relative;
    align-items:center;
    flex-shrink: 29;
    background-color: rgba(237, 232, 227, 1);
  }

  .home-group7 {
    top: 670px;
    left: 60%;
    width: 240px;
    height: 60px;
    display: flex;
    position: absolute;
    align-items: flex-start;
    flex-shrink: 1;
    background-color: rgba(208, 35, 35, 1);
  }
  .home-text {
    top: 20px;
    left: 76.9999771118164px;
    color: rgba(237, 232, 226, 1);
    height: auto;
    position: absolute;
    font-size: 16px;
    font-style: Semibold;
    text-align: left;
    font-family: General Sans;
    font-weight: 600;
    line-height: 20px;
    font-stretch: normal;
    text-decoration: none;
    font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  }
  .home-text02 {
    top: 181px;
    left: 375px;
    color: rgba(25, 29, 99, 1);
    width: 690px;
    height: auto;
    position: absolute;
    font-size: 28px;
    font-style: Semibold;
    text-align: center;
    font-family: General Sans;
    font-weight: 600;
    line-height: 38px;
    font-stretch: normal;
    text-decoration: none;
  }
  .home-group20 {
    top: 310px;
    left: 465px;
    width: 510px;
    height: 303px;
    display: flex;
    position: absolute;
    align-items: flex-start;
    flex-shrink: 1;
  }
  .home-group3 {
    top: 0px;
    left: 0px;
    width: 510px;
    height: 81px;
    display: flex;
    position: absolute;
    align-items: flex-start;
    flex-shrink: 1;
    background-color: rgba(244, 243, 246, 1);
  }
  .home-text04 {
    top: 27px;
    left: 103px;
    color: rgba(6, 7, 16, 1);
    height: auto;
    position: absolute;
    font-size: 20px;
    font-style: Semibold;
    text-align: left;
    font-family: General Sans;
    font-weight: 600;
    line-height: 27.044775009155273px;
    font-stretch: normal;
    text-decoration: none;
  }
  .home-text06 {
    top: 27px;
    left: 206.791015625px;
    color: rgba(6, 7, 16, 1);
    height: auto;
    position: absolute;
    font-size: 20px;
    font-style: Medium;
    text-align: left;
    font-family: General Sans;
    font-weight: 500;
    line-height: 27.044775009155273px;
    font-stretch: normal;
    text-decoration: none;
  }
  .home-text08 {
    top: 27px;
    left: 286.791015625px;
    color: rgba(164, 0, 33, 1);
    height: auto;
    position: absolute;
    font-size: 20px;
    font-style: Medium;
    text-align: left;
    font-family: General Sans;
    font-weight: 500;
    line-height: 27.044775009155273px;
    font-stretch: normal;
    text-decoration: none;
  }
  .home-group1 {
    top: 16px;
    left: 24px;
    width: 49px;
    height: 49px;
    display: flex;
    position: absolute;
    align-items: flex-start;
    flex-shrink: 1;
  }
  .home-ellipse1 {
    top: 0px;
    left: 0px;
    width: 49px;
    height: 49px;
    position: absolute;
  }
  .home-text10 {
    top: 10px;
    left: 16.999998092651367px;
    color: rgba(6, 7, 16, 1);
    height: auto;
    position: absolute;
    font-size: 21.635820388793945px;
    font-style: Semibold;
    text-align: left;
    font-family: General Sans;
    font-weight: 600;
    line-height: normal;
    font-stretch: normal;
    text-decoration: none;
  }
  .home-group4 {
    top: 111px;
    left: 0px;
    width: 510px;
    height: 81px;
    display: flex;
    position: absolute;
    align-items: flex-start;
    flex-shrink: 1;
    background-color: rgba(244, 243, 246, 1);
  }
  .home-text11 {
    top: 26px;
    left: 103px;
    color: rgba(6, 7, 16, 1);
    height: auto;
    position: absolute;
    font-size: 20px;
    font-style: Semibold;
    text-align: left;
    font-family: General Sans;
    font-weight: 600;
    line-height: 27.044775009155273px;
    font-stretch: normal;
    text-decoration: none;
  }
  .home-text13 {
    top: 26px;
    left: 261.2537841796875px;
    color: rgba(6, 7, 16, 1);
    height: auto;
    position: absolute;
    font-size: 20px;
    font-style: Medium;
    text-align: left;
    font-family: General Sans;
    font-weight: 500;
    line-height: 27.044775009155273px;
    font-stretch: normal;
    text-decoration: none;
  }
  .home-text15 {
    top: 26px;
    left: 342.2537841796875px;
    color: rgba(164, 0, 33, 1);
    height: auto;
    position: absolute;
    font-size: 20px;
    font-style: Medium;
    text-align: left;
    font-family: General Sans;
    font-weight: 500;
    line-height: 27.044775009155273px;
    font-stretch: normal;
    text-decoration: none;
  }
  .home-group11 {
    top: 16px;
    left: 24px;
    width: 49px;
    height: 49px;
    display: flex;
    position: absolute;
    align-items: flex-start;
    flex-shrink: 1;
  }
  .home-ellipse11 {
    top: 0px;
    left: 0px;
    width: 49px;
    height: 49px;
    position: absolute;
  }
  .home-text17 {
    top: 10px;
    left: 16.999998092651367px;
    color: rgba(6, 7, 16, 1);
    height: auto;
    position: absolute;
    font-size: 21.635820388793945px;
    font-style: Semibold;
    text-align: left;
    font-family: General Sans;
    font-weight: 600;
    line-height: normal;
    font-stretch: normal;
    text-decoration: none;
  }
  .home-group5 {
    top: 222px;
    left: 0px;
    width: 510px;
    height: 81px;
    display: flex;
    position: absolute;
    align-items: flex-start;
    flex-shrink: 1;
    background-color: rgba(244, 243, 246, 1);


  }
  .home-text18 {
    top: 27px;
    left: 103px;
    color: rgba(6, 7, 16, 1);
    height: auto;
    position: absolute;
    font-size: 20px;
    font-style: Semibold;
    text-align: left;
    font-family: General Sans;
    font-weight: 600;
    line-height: 27.044775009155273px;
    font-stretch: normal;
    text-decoration: none;
  }
  .home-text20 {
    top: 27px;
    left: 238.850830078125px;
    color: rgba(6, 7, 16, 1);
    height: auto;
    position: absolute;
    font-size: 20px;
    font-style: Medium;
    text-align: left;
    font-family: General Sans;
    font-weight: 500;
    line-height: 27.044775009155273px;
    font-stretch: normal;
    text-decoration: none;
  }
  .home-text22 {
    top: 27px;
    left: 318.850830078125px;
    color: rgba(31, 185, 110, 1);
    height: auto;
    position: absolute;
    font-size: 20px;
    font-style: Medium;
    text-align: left;
    font-family: General Sans;
    font-weight: 500;
    line-height: 27.044775009155273px;
    font-stretch: normal;
    text-decoration: none;
  }
  .home-group12 {
    top: 17px;
    left: 24px;
    width: 49px;
    height: 49px;
    display: flex;
    position: absolute;
    align-items: flex-start;
    flex-shrink: 1;
  }
  .home-ellipse12 {
    top: 0px;
    left: 0px;
    width: 49px;
    height: 49px;
    position:fixed;
    
  }
  .home-text24 {
    top: 10px;
    left: 15.999998092651367px;
    color: rgba(6, 7, 16, 1);
    height: auto;
    position: absolute;
    font-size: 21.635820388793945px;
    font-style: Semibold;
    text-align: left;
    font-family: General Sans;
    font-weight: 600;
    line-height: normal;
    font-stretch: normal;
    text-decoration: none;
  }
  .home-group6 {
    top: 700px;
    left: 20%;
    width: 240px;
    height: 20px;
    display: flex;
    position: absolute;
    align-items: flex-start;
    flex-shrink: 1;
  }
  .home-text25 {
    left: 150px;
    color: rgba(117, 117, 117, 1);
    height: auto;
    position: absolute;
    font-size: 40px;
    font-style: Semibold;
    text-align: left;
    font-family: General Sans;
    font-weight: 600;
    line-height: 20px;
    font-stretch: normal;
    text-decoration: none;
  }
  .home-group9 {
    top: 1.9999966621398926px;
    left: 0px;
    width: 200px;
    height: 16px;
    display: flex;
    position: absolute;
    align-items: flex-start;
    flex-shrink: 1;
    background-color: rgba(237, 232, 227, 1);
  }
  .home-rectangle3 {
    top: 0px;
    left: 0px;
    width: 40px;
    height: 16px;
    position: absolute;
    border-radius: 16px;
  }
  .home-group14 {
    top: 40px;
    left: 10%;
    width: 80%;
    height: 50px;
    display: flex;
    position: absolute;
    align-items: flex-start;
    flex-shrink: 1;
  }
  .home-group21 {
    top: 0px;
    left: 0px;
    width: 100%;
    height: 50px;
    display: flex;
    position: absolute;
    align-items: flex-start;
    flex-shrink: 1;
  }


  .home-cancel2-outline {
    top: 8.333333015441895px;
    left: 8.333333015441895px;
    width: 33px;
    height: 33px;
    position: absolute;
  }
  .home-text27 {
    /* top: 40px;
    left: 50%; */
    color: rgba(0, 0, 0, 1);
    height: auto;
    position: absolute;
    font-size: 30px;
    font-style: Semibold;
    text-align: left;
    font-family: General Sans;
    font-weight: 600;
    line-height: 50px;
    font-stretch: normal;
    text-decoration: none;
  }
  .home-group13 {
    top: 7px;
    left: 0px;
    width: 95.45454406738281px;
    height: 35px;
    display: flex;
    position: absolute;
    align-items: flex-start;
    flex-shrink: 1;
    background-color: rgba(244, 243, 246, 1);
  }
  .home-group12 {
    top: 6.363636493682861px;
    left: 12.727272987365723px;
    width: 68.63633728027344px;
    height: 23px;
    display: flex;
    position: absolute;
    align-items: flex-start;
    flex-shrink: 1;
  }
  .home-text29 {
    top: -0.000011097301467088982px;
    left: 28.636341094970703px;
    color: rgba(25, 29, 99, 1);
    height: auto;
    position: absolute;
    font-size: 22.272727966308594px;
    font-style: Semibold;
    text-align: left;
    font-family: General Sans;
    font-weight: 600;
    line-height: 22.272727966308594px;
    font-stretch: normal;
    text-decoration: none;
  }
  .home-image3 {
    top: 0px;
    left: 0px;
    width: 22px;
    height: 22px;
    position: absolute;
  }
  </style>
  