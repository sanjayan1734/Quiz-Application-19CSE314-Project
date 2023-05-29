<template>
    <div class="faculty-page">
      <header class="header">
        <h1 class="faculty-heading">Welcome, {{ facultyName }}</h1>
      </header>
  
      <div class="main-content">
        <section class="section">
          <h2 class="section-heading">Create Quiz</h2>
          <form @submit.prevent="startQuizCreation">
            <input type="text" v-model="quizTitle" placeholder="Quiz Title" required>
            <button type="submit">Start Quiz Creation</button>
          </form>
          <div v-if="quizCreationStarted">
            <h3>Add Questions</h3>
            <form @submit.prevent="addQuestion">
              <input type="text" v-model="newQuestion" placeholder="Question" required>
              <button type="submit">Add Question</button>
            </form>
            <ul v-if="quizQuestions.length > 0">
              <li v-for="(question, index) in quizQuestions" :key="index">
                {{ question }}
                <button @click="deleteQuestion(index)">Delete</button>
              </li>
            </ul>
            <div v-else>
              <p>No questions added yet.</p>
            </div>
            <button @click="finishQuizCreation">Finish Quiz Creation</button>
          </div>
        </section>
  
        <section class="section">
          <h2 class="section-heading">Student Details</h2>
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
        quizCreationStarted: false
      };
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
  .faculty-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    min-height: 100vh;
    background-color: #f2f2f2;
    font-family: Arial, sans-serif;
  }
  
  .header {
    background-color: #333;
    color: #fff;
    padding: 20px;
    text-align: center;
  }
  
  .faculty-heading {
    font-size: 32px;
    font-weight: bold;
    margin: 0;
  }
  
  .main-content {
    max-width: 800px;
    width: 90%;
    margin-top: 40px;
  }
  
  .section {
    background-color: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
  }
  
  .section-heading {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
  }
  
  form {
    display: flex;
    gap: 10px;
    margin-top: 10px;
  }
  
  input[type='text'] {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    flex: 1;
  }
  
  button {
    padding: 10px 20px;
    background-color: #4CAF50;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #45a049;
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
  