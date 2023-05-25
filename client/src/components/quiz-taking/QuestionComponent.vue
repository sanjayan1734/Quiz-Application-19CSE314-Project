<script>
    export default {
    
      name:"QuestionComponent",
    
      props: {
        noOfQuestions: Number,
        questionId:String,
        questionDescription:String,
        optionA:String,
        optionB:String,
        optionC:String,
      },
      data() {
        return {
          questionOption:String
        }
      },

      methods: {
        updateAnswerValue(ansval) {
          this.questionOption = ansval
          console.log(this.questionOption)
        },

        optionClick(ansval) {
          console.log(ansval)
        },
        passReferenceValue(){
          console.log("ref passed to parent object")
        },
        returnQuestionSelection() {
          return this.questionOption
        }

      }
}

</script>
<template>
    <div class="question">
        <span class="home-text02">
          <span>{{ questionDescription }}</span>
        </span>
        <div class="home-group20">
          <button class="home-group3" id="optionA" @click="updateAnswerValue('A');" >
            <span class="home-text04"  v-bind:style="this.questionOption == 'A'? {color:'Green'} :{color:'Black'} ">
              <span>
                {{optionA}}
                <span ></span>
              </span>
            </span>
            <!-- <span class="home-text06"><span>₹ 17,356,</span></span>
            <span class="home-text08"><span>-0.31%</span></span> -->
            <div class="home-group1">
              <img
                src="https://aheioqhobo.cloudimg.io/v7/_playground-bucket-v2.teleporthq.io_/0b4bec48-8758-4c6c-940b-bc441b647ab9/a27b3738-5a27-42c2-9e43-09d1f3bd5c33?org_if_sml=1914"
                alt="Ellipse11228"
                class="home-ellipse1"
              />
              <span class="home-text10">A</span>
            </div>
          </button>
          <button class="home-group4"  id="optionB" @click="updateAnswerValue('B');" >
            <span class="home-text11" v-bind:style="this.questionOption == 'B'? {color:'Green'} :{color:'Black'} ">
              <span>
                {{optionB}}
                <span ></span>
              </span>
            </span>
            <!-- <span class="home-text13"><span>₹56,226,</span></span>
            <span class="home-text15"><span>-0.31%</span></span> -->
            <div class="home-group11">
              <img
                src="https://aheioqhobo.cloudimg.io/v7/_playground-bucket-v2.teleporthq.io_/0b4bec48-8758-4c6c-940b-bc441b647ab9/f4d9d7e0-e5d5-45a9-9da7-12fcce2693a7?org_if_sml=1914"
                alt="Ellipse11228"
                class="home-ellipse11"
              />
              <span class="home-text17">B</span>
            </div>
        </button>
          <button class="home-group5" id="optionC" @click="updateAnswerValue('C');" >
            <span class="home-text18" v-bind:style="this.questionOption == 'C'? {color:'Green'} :{color:'Black'} ">
              <span>{{ optionC }}</span>
            </span>
            <!-- <span class="home-text20"><span>₹ 17,356,</span></span>
            <span class="home-text22"><span>+2.12%</span></span> -->
            <div class="home-group11">
              <img
                src="https://aheioqhobo.cloudimg.io/v7/_playground-bucket-v2.teleporthq.io_/0b4bec48-8758-4c6c-940b-bc441b647ab9/f4d9d7e0-e5d5-45a9-9da7-12fcce2693a7?org_if_sml=1914"
                alt="Ellipse11228"
                class="home-ellipse11"
              />
              <span class="home-text24">C</span>
            </div>
          </button>
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
    left: 1200px;
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
  }
  .home-text02 {
    top: 181px;
    left: 20%;
    color: rgba(25, 29, 99, 1);
    width: 60%;
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
    left: 20%;
    width: 60%;
    height: 303px;
    display: flex;
    position: absolute;
    /* align-items: flex-start; */
    flex-shrink: 1;
  }
  .home-group3 {
    
    top: 0px;
    left: 0px;
    width: 100%;
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
    /* color: rgba(6, 7, 16, 1); */
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
    width: 100%;
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
    width: 100%;
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
    left: 100px;
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
    left: 60px;
    width: 1320px;
    height: 50px;
    display: flex;
    position: absolute;
    align-items: flex-start;
    flex-shrink: 1;
  }
  .home-group21 {
    top: 0px;
    left: 0px;
    width: 1320px;
    height: 50px;
    display: flex;
    position: absolute;
    align-items: flex-start;
    flex-shrink: 1;
  }
  .home-group13 {
    top: 0px;
    left: 1270px;
    width: 50px;
    height: 50px;
    display: flex;
    position: absolute;
    align-items: flex-start;
    flex-shrink: 1;
  }
  .home-ellipse13 {
    top: 0px;
    left: 0px;
    width: 50px;
    height: 50px;
    position: absolute;
  }
  .home-cancel2-outline {
    top: 8.333333015441895px;
    left: 8.333333015441895px;
    width: 33px;
    height: 33px;
    position: absolute;
  }
  .home-text27 {
    top: 13px;
    left: 575px;
    color: rgba(0, 0, 0, 1);
    height: auto;
    position: absolute;
    font-size: 24px;
    font-style: Semibold;
    text-align: left;
    font-family: General Sans;
    font-weight: 600;
    line-height: 24px;
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

