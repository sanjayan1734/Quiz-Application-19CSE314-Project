<template>
    <div class="faculty-pages">
      <header class="headers">
        <h1 class="faculty-headings">Welcome, Dr.Radhika N</h1>
      </header>
  
      <div class="main-contents">
        <section class="sectionss">
          <h2 class="section-headings">Create Quiz</h2>
          <form @submit.prevent="startQuizCreation">
            <input type="text" v-model="quizTitle" placeholder="Quiz Title" class ="inputs" required>
            <button type="submit" class="buttons">Start Quiz Creation</button>
          </form>
          <div v-if="quizCreationStarted">
            <h3>Add Questions</h3>
            <form @submit.prevent="addQuestion" class="forms">
              <input type="text" v-model="newQuestion" placeholder="Question" class="inputs" required>
              <button type="submit" class="buttons">Add Question</button>
            </form>
            <ul v-if="quizQuestions.length > 0">
              <li v-for="(question, index) in quizQuestions" :key="index">
                {{ question }}
                <button @click="deleteQuestion(index)" class="buttons">Delete</button>
              </li>
            </ul>
            <div v-else>
              <p>No questions added yet.</p>
            </div>
            <button @click="finishQuizCreation" class="buttons">Finish Quiz Creation</button>
          </div>
        </section>
  
        <section class="sectionss">
          <h2 class="section-headings">Student Details</h2>
          <ul v-if="studentDetails.length > 0">
            <li v-for="(student, index) in studentDetails" :key="index">
              <span>{{ student.name }}</span> - <span>{{ student.grade }}</span>
            </li>
          </ul>
          <div v-else>
            <p>No student details available.</p>
          </div>
        </section>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'FacultyPage',
    data() {
      return {
        facultyName: 'John Doe',
        quizTitle: '',
        quizQuestions: [],
        newQuestion: '',
        studentDetails: [
          { name: 'Alice', grade: 'A' },
          { name: 'Bob', grade: 'B' },
          { name: 'Charlie', grade: 'A+' }
        ],
        quizCreationStarted: false,

        profileInfo:
        {
            Email:String,
            Id:Number,
            Name:String,
            quizcount:Number,
            totalcorrectq:Number,
            totalQuizzes:3
        },
      };
    },
    mounted() {
    console.log(this.$route.params.mail)
    axios.get('https://localhost:7282/api/User/GetStudentsbyEmail?mail=' + this.$route.params.mail).then((response) => {
      this.profileInfo = response.data
      console.log(response.data)
    });

    },
    methods: {
      startQuizCreation() {
        this.quizCreationStarted = true;
      },
      addQuestion() {
        if (this.newQuestion.trim() !== '') {
          this.quizQuestions.push(this.newQuestion);
          this.newQuestion = '';
        }
      },
      deleteQuestion(index) {
        this.quizQuestions.splice(index, 1);
      },
      finishQuizCreation() {
        // Perform final quiz creation logic, e.g., send API request
        console.log('Quiz Created:', this.quizTitle, this.quizQuestions);
        this.quizTitle = '';
        this.quizQuestions = [];
        this.quizCreationStarted = false;
      }
    }
  };
  </script>
  
  <style>
  .faculty-pages {
    display: flex;
    flex-direction: column;
    align-items: center;
    min-height: 100vh;
    background-color: #f2f2f2;
    font-family: Arial, sans-serif;
  }
  
  .headers {
    background-color: #333;
    color: #fff;
    padding: 20px;
    text-align: center;
  }
  
  .faculty-headings {
    font-size: 32px;
    font-weight: bold;
    margin: 0;
  }
  
  .main-contents {
    max-width: 800px;
    width: 90%;
    margin-top: 40px;
  }
  
  .sectionss {
    background-color: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
  } */
  
  .section-headings {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
  }
  
  .forms {
    display: flex;
    gap: 10px;
    margin-top: 10px;
  }
  
  .inputs {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    flex: 1;
  }
  
  .buttons {
    padding: 10px 20px;
    background-color: #4CAF50;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
 
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
  }
  
  @media screen and (max-width: 768px) {
    .main-content {
      width: 100%;
    }
  }
  </style>
  