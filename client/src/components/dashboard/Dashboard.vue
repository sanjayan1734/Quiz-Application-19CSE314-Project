<template>
  <div class="dashboard">
    <div class="sidebar">
      <div class="sidebar-header">
        <h2 class="sidebar-title">Quiz App</h2>
      </div>
      <ul class="sidebar-menu">
        <li class="sidebar-menu-item">
          <router-link to="/" class="sidebar-menu-link">Home</router-link>
        </li>
        <li class="sidebar-menu-item">
          <router-link to="/quizzes" class="sidebar-menu-link">Quizzes</router-link>
        </li>
        <li class="sidebar-menu-item">
          <router-link to="/certificates" class="sidebar-menu-link">Certificates</router-link>
        </li>
        <li class="sidebar-menu-item">
          <router-link to="/discussions" class="sidebar-menu-link">Discussions</router-link>
        </li>
        <li class="sidebar-menu-item">
          <router-link to="/feedback" class="sidebar-menu-link">Feedback</router-link>
        </li>
      </ul>
    </div>
    <div class="main-content">
      <div class="dashboard-header">
        <h1 class="dashboard-title">Welcome, {{ profileInfo.name }}!</h1>
        <div class="dashboard-stats">
          <div class="dashboard-stat-item">
            <p class="dashboard-stat-label">Total Quizzes</p>
            <p class="dashboard-stat-value">{{ profileInfo.quizcount }}</p>
          </div>
          <div class="dashboard-stat-item">
            <p class="dashboard-stat-label">Quizzes Completed</p>
            <p class="dashboard-stat-value">{{ profileInfo.quizzesCompleted }}</p>
          </div>
          <div class="dashboard-stat-item">
            <p class="dashboard-stat-label">Correct Answers</p>
            <p class="dashboard-stat-value">{{ profileInfo.totalcorrectq }}</p>
          </div>
        </div>
      </div>
      <div class="dashboard-content">
        <div class="dashboard-section">
          <h2 class="dashboard-section-title">Statistics</h2>
          <div class="dashboard-chart">
            <GChart type="PieChart" :options="options" :data="data" />
          </div>
          <div class="progress-container">
            <div class="progress-label">Level Progress</div>
            <div class="progress-bar">
              <div class="progress-value" :style="{ width: levelProgress + '%' }"></div>
            </div>
          </div>
        </div>
        <div class="dashboard-section">
          <h2 class="dashboard-section-title">Available Quizzes</h2>
          <div class="quiz-grid">
            <div v-for="quiz in quizzes" :key="quiz.id" class="quiz-item">
              <router-link :to="'/quiz/' + quiz.id" class="quiz-link">{{ quiz.title }}</router-link>
              <div class="quiz-meta">
                <div class="quiz-meta-item">
                  <span class="quiz-meta-label">Questions:</span>
                  <span class="quiz-meta-value">{{ quiz.questions }}</span>
                </div>
                <div class="quiz-meta-item">
                  <span class="quiz-meta-label">Duration:</span>
                  <span class="quiz-meta-value">{{ quiz.duration }} mins</span>
                </div>
              </div>
            </div>
          </div>
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
          <div class="event-grid">
            <div v-for="event in events" :key="event.id" class="event-item">
              <div class="event-info">
                <h3 class="event-title">{{ event.title }}</h3>
                <p class="event-description">{{ event.description }}</p>
                <span class="event-date">{{ event.date }}</span>
              </div>
              <div class="event-actions">
                <button class="event-register-button">Register</button>
                <button class="event-details-button">Details</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { GChart } from "vue-google-charts";

export default {
  components: {
    GChart
  },
  data() {
    return {
      profileInfo: {
        email: '',
        id: 0,
        name: '',
        quizcount: 0,
        quizzesCompleted: 0,
        totalcorrectq: 0
      },
      totalQuizzes: 5,
      quizzes: [
        { id: 'quiz1', title: "Quiz 1", questions: 10, duration: 20 },
        { id: 'quiz2', title: "Quiz 2", questions: 15, duration: 30 },
        { id: 'quiz3', title: "Quiz 3", questions: 12, duration: 25 },
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
      data: [
        ['Daily Routine', 'Hours per Day'],
        ['Correct Answers', 10],
        ['Wrong Answers', 2],
      ],
      options: {
        width: 350,
        height: 250
      }
    };
  },
  created() {
    this.fetchProfileInfo();
  },
  methods: {
    fetchProfileInfo() {
      const email = this.$route.params.mail;
      axios.get(`http://harish2511-001-site1.btempurl.com/api/User/GetStudentsbyEmail?mail=${email}`)
        .then(response => {
          this.profileInfo = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    levelProgress() {
      const totalQuizzes = this.profileInfo.quizcount || 0;
      const correctAnswers = this.profileInfo.totalcorrectq || 0;
      return Math.floor((correctAnswers / totalQuizzes) * 100);
    },
    shareCertificate() {
      // Implement certificate sharing functionality
      // You can use external libraries or APIs for social media sharing
    },
    joinDiscussion() {
      // Implement join discussion functionality
      // You can navigate to a discussion forum page or open a modal for joining the discussion
    },
    provideFeedback() {
      // Implement feedback functionality
      // You can open a feedback form or display a modal for providing feedback
    },
    shareQuestion() {
      // Implement question sharing functionality
      // You can use external libraries or APIs for sharing the question
    }
  }
};
</script>

<style>
/* Add your custom styling here */

.dashboard {
  display: flex;
}

.sidebar {
  background-color: #f2f2f2;
  padding: 20px;
  min-width: 300px;
}

.sidebar-header {
  margin-bottom: 20px;
}

.sidebar-title {
  font-size: 24px;
  font-weight: bold;
}

.sidebar-menu {
  list-style-type: none;
  padding: 0;
}

.sidebar-menu-item {
  margin-bottom: 10px;
}

.sidebar-menu-link {
  color: #333;
  text-decoration: none;
  display: block;
  padding: 10px;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.sidebar-menu-link:hover {
  background-color: #eaeaea;
}

.main-content {
  flex-grow: 1;
  padding: 20px;
}

.dashboard-header {
  margin-bottom: 30px;
}

.dashboard-title {
  font-size: 32px;
  font-weight: bold;
  margin-bottom: 10px;
}

.dashboard-stats {
  display: flex;
  justify-content: space-between;
}

.dashboard-stat-item {
  text-align: center;
}

.dashboard-stat-label {
  font-size: 14px;
  color: #888;
}

.dashboard-stat-value {
  font-size: 24px;
  font-weight: bold;
}

.dashboard-content {
  display: grid;
  grid-gap: 30px;
}

.dashboard-section-title {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 20px;
}

.dashboard-chart {
  height: 300px;
}

.progress-container {
  margin-top: 20px;
}

.progress-label {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 10px;
}

.progress-bar {
  height: 20px;
  background-color: #eaeaea;
  border-radius: 10px;
  overflow: hidden;
}

.progress-value {
  height: 100%;
  background-color: #3498db;
  transition: width 0.3s;
}

.quiz-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  grid-gap: 20px;
}

.quiz-item {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.quiz-link {
  font-size: 18px;
  font-weight: bold;
  color: #333;
  text-decoration: none;
  transition: color 0.3s;
}

.quiz-link:hover {
  color: #3498db;
}

.quiz-meta {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}

.quiz-meta-item {
  display: flex;
}

.quiz-meta-label {
  font-size: 14px;
  color: #888;
  margin-right: 5px;
}

.quiz-meta-value {
  font-size: 14px;
}

.notification-list {
  list-style-type: none;
  padding: 0;
}

.notification-item {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 10px;
}

.notification-date {
  font-size: 12px;
  color: #888;
}

.event-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  grid-gap: 20px;
}

.event-item {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.event-info {
  flex-grow: 1;
  margin-right: 20px;
}

.event-title {
  font-size: 18px;
  font-weight: bold;
  color: #333;
  margin-bottom: 10px;
}

.event-description {
  font-size: 14px;
  color: #888;
  margin-bottom: 10px;
}

.event-date {
  font-size: 14px;
  color: #888;
}

.event-actions {
  display: flex;
}

.event-register-button,
.event-details-button {
  background-color: #3498db;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px 15px;
  margin-left: 10px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.event-register-button:hover,
.event-details-button:hover {
  background-color: #2980b9;
}

</style>