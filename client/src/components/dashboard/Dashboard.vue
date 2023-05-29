<template>
    <div class="dashboard" style="background-color:#e5dada ;">
      <div class="dashboard-header">
        <h1 class="dashboard-title">Welcome, {{this.profileInfo.name}}!</h1>
        <div class="dashboard-stats">
          <div class="dashboard-stat-item">
            <p class="dashboard-stat-label">Total Quizzes</p>
            <p class="dashboard-stat-value">{{ this.profileInfo.totalQuizzes }}</p>
          </div>
          <div class="dashboard-stat-item">
            <p class="dashboard-stat-label">Quizzes Completed</p>
            <p class="dashboard-stat-value">{{ this.profileInfo.quizcount }}</p>
          </div>
          <div class="dashboard-stat-item">
            <p class="dashboard-stat-label">Correct Answers</p>
            <p class="dashboard-stat-value">{{ this.profileInfo.totalcorrectq }}</p>
          </div>
        </div>
      </div>
      <div class="dashboard-content">
        <div class="dashboard-section">
          <h2 class="dashboard-section-title">Statistics</h2>
          <div class="dashboard-chart">
            <PieChart :chart-data="statisticsChartData"></PieChart>
          </div>
        </div>
        <div class="dashboard-section">
          <h2 class="dashboard-section-title">Available Quizzes</h2>
          <ul class="quiz-list">
            <li class="quiz-item" v-for="quiz in quizzes" :key="quiz.id">
              <router-link :to="'/quiz/' + quiz.id" class="quiz-link">{{ quiz.title }}</router-link>
            </li>
          </ul>
        </div>
        <div class="dashboard-section">
          <h2 class="dashboard-section-title">Notifications</h2>
          <ul class="notification-list">
            <li class="notification-item" v-for="notification in notifications" :key="notification.id">
              <p>{{ notification.message }}</p>
              <span class="notification-date">{{ notification.date }}</span>
            </li>
          </ul>
        </div>
        <div class="dashboard-section">
          <h2 class="dashboard-section-title">Upcoming Events</h2>
          <ul class="event-list">
            <li class="event-item" v-for="event in events" :key="event.id">
              <div class="event-info">
                <h3 class="event-title">{{ event.title }}</h3>
                <p class="event-description">{{ event.description }}</p>
                <span class="event-date">{{ event.date }}</span>
              </div>
              <div class="event-actions">
                <button class="event-register-button">Register</button>
                <button class="event-details-button">Details</button>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { Pie } from 'vue-chartjs';
  import axios from 'axios';
  import { toRaw } from 'vue';
  
  export default {
    // components: {
    //   PieChart: {
    //     extends: Pie,
    //     props: ['chartData', 'options'],
    //     mounted() {
    //       this.renderChart(this.chartData, this.options);
    //     }
    //   }
    // },
    mounted() {
        console.log(this.$route.params.mail)
        axios.get('https://localhost:7282/api/User/GetStudentsbyEmail?mail='+ this.$route.params.mail).then((response) => {
            this.tempprofileInfo = response.data
            this.profileInfo = toRaw(this.tempprofileInfo)
            console.log(response.data)
            console.log(this.profileInfo)
            console.log(this.profileInfo.totalcorrectq)
            console.log(this.profileInfo.quizcount)
        });

    },
    data(){
      return {
        profileInfo:
        {
            Email:String,
            Id:Number,
            Name:String,
            quizcount:Number,
            totalcorrectq:Number,
            totalQuizzes:3
        },
        tempprofileInfo:{
            Email:String,
            Id:Number,
            Name:String,
            quizcount:Number,
            totalcorrectq:Number
        },
        totalQuizzes: 5,
        quizzesCompleted: 3,
        correctAnswers: 12,
        quizzes: [
          { id: 1, title: "Quiz 1" },
          { id: 2, title: "Quiz 2" },
          { id: 3, title: "Quiz 3" },
          // Add more quizzes as needed
        ],
        notifications: [
          { id: 1, message: "New quiz available!", date: "2023-05-28" },
          { id: 2, message: "Quiz result published", date: "2023-05-27" },
          // Add more notifications as needed
        ],
        events: [
          {
            id: 1,
            title: "Webinar: Introduction to Software Engineering",
            description: "Join our webinar to learn the basics of software engineering.",
            date: "2023-06-02"
          },
          {
            id: 2,
            title: "Workshop: Building IoT Applications",
            description: "Get hands-on experience in building IoT applications.",
            date: "2023-06-05"
          },
          // Add more events as needed
        ],
        statisticsChartData: {
          labels: ["Correct", "Incorrect"],
          datasets: [
            {
              backgroundColor: ["#55a630", "#d41f1f"],
              data: [this.correctAnswers, this.totalQuizzes - this.correctAnswers]
            }
          ]
        }
      };
    },
  };
  </script>
  
  <style>
  /* Your existing styles */
  
  .dashboard {
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: #f5f5f5;
    padding: 20px;
  }
  
  .dashboard-header {
    text-align: center;
    margin-bottom: 40px;
  }
  
  .dashboard-title {
    font-size: 36px;
    font-weight: bold;
    margin-bottom: 20px;
    color: #30336b;
  }
  
  .dashboard-stats {
    display: flex;
    justify-content: center;
    margin-bottom: 40px;
  }
  
  .dashboard-stat-item {
    text-align: center;
    margin: 0 20px;
  }
  
  .dashboard-stat-label {
    font-size: 16px;
    color: #888;
    margin-bottom: 8px;
  }
  
  .dashboard-stat-value {
    font-size: 24px;
    font-weight: bold;
  }
  
  .dashboard-content {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
  }
  
  .dashboard-section {
    flex: 1 1 400px;
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .dashboard-section-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
    color: #30336b;
  }
  
  .dashboard-chart {
    width: 100%;
    height: 300px;
  }
  
  .quiz-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .quiz-item {
    margin-bottom: 10px;
  }
  
  .quiz-link {
    display: inline-block;
    padding: 10px 20px;
    background-color: #30336b;
    color: #fff;
    text-decoration: none;
    border-radius: 4px;
  }
  
  .notification-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .notification-item {
    margin-bottom: 10px;
    padding-bottom: 10px;
    border-bottom: 1px solid #ccc;
  }
  
  .notification-date {
    font-size: 12px;
    color: #888;
  }
  
  .event-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .event-item {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
    padding-bottom: 10px;
    border-bottom: 1px solid #ccc;
  }
  
  .event-info {
    flex: 1;
  }
  
  .event-title {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 5px;
    color: #30336b;
  }
  
  .event-description {
    margin-bottom: 5px;
  }
  
  .event-date {
    font-size: 12px;
    color: #888;
  }
  
  .event-actions {
    display: flex;
    gap: 10px;
  }
  
  .event-register-button,
  .event-details-button {
    padding: 8px 12px;
    background-color: #30336b;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  /* Additional styles for the pie chart */
  .chartjs-render-monitor {
    width: 100% !important;
    height: 100% !important;
  }
  
  /* Add more custom styles as needed */
  </style>
  