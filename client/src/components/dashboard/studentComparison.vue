<template>
    <div class="studentLeader">
        <div class="sidebar">
      <div class="sidebar-header">
        <h2 class="sidebar-title">Quiz App</h2>
      </div>
      
      <ul class="sidebar-menu" >
        <li class="sidebar-menu-item">
          <router-link to="/" class="sidebar-menu-link" style>Home</router-link>
        </li>
        <li class="sidebar-menu-item">
          <router-link to="/dashboard" class="sidebar-menu-link">Dashboard</router-link>
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
        <li class="sidebar-menu-item">
          <router-link to="/studentComparison" class="sidebar-menu-link">Student Leaderboard</router-link>
        </li>
      </ul>
      </div>
    <div class="leaderboard-container" style="background-color: #e5dada;;">
      <h2 class="leaderboard-title">Student Leaderboard</h2>
  
      <div class="leaderboard-stats">
        <div class="stat-card">
          <i class="stat-icon fas fa-users"></i>
          <div class="stat-info">
            <div class="stat-label">Total Students</div>
            <div class="stat-value">{{ students.length }}</div>
          </div>
        </div>
        <div class="stat-card">
          <i class="stat-icon fas fa-trophy"></i>
          <div class="stat-info">
            <div class="stat-label">Top Scorer</div>
            <div class="stat-value">{{ getTopScorer().name }}</div>
          </div>
        </div>
        <div class="stat-card">
          <i class="stat-icon fas fa-star"></i>
          <div class="stat-info">
            <div class="stat-label">Highest Avg Score</div>
            <div class="stat-value">{{ getHighestAverageScore().name }}</div>
          </div>
        </div>
      </div>
  
      <table class="leaderboard-table">
        <thead>
          <tr>
            <th>Rank</th>
            <th>Student Name</th>
            <th>Correct Questions</th>
            <th>Quizzes Attempted</th>
            <th>Average Score</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(student, index) in students" :key="student.id" @click="showStudentDetails(student.id)">
            <td>{{ index + 1 }}</td>
            <td>{{ student.name }}</td>
            <td>{{ student.correctQuestions }}</td>
            <td>{{ student.quizzesAttempted }}</td>
            <td>{{ calculateAverageScore(student) }}</td>
          </tr>
        </tbody>
      </table>
  
      <div v-if="selectedStudent" class="student-details">
        <h3 class="details-title">Student Details</h3>
        <div class="details-content">
          <div class="details-row">
            <div class="details-label">Name:</div>
            <div class="details-value">{{ selectedStudent.name }}</div>
          </div>
          <div class="details-row">
            <div class="details-label">Correct Questions:</div>
            <div class="details-value">{{ selectedStudent.correctQuestions }}</div>
          </div>
          <div class="details-row">
            <div class="details-label">Quizzes Attempted:</div>
            <div class="details-value">{{ selectedStudent.quizzesAttempted }}</div>
          </div>
          <div class="details-row">
            <div class="details-label">Average Score:</div>
            <div class="details-value">{{ calculateAverageScore(selectedStudent) }}</div>
          </div>
          <!-- Add more student details here -->
        </div>
      </div>
    </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        students: [
          { id: 1, name: 'John Doe', correctQuestions: 15, quizzesAttempted: 10, scores: [90, 85, 80] },
          { id: 2, name: 'Jane Smith', correctQuestions: 20, quizzesAttempted: 12, scores: [95, 90, 85] },
          { id: 3, name: 'Michael Johnson', correctQuestions: 18, quizzesAttempted: 9, scores: [80, 75, 70] },
          // Add more student data here...
        ],
        selectedStudent: null,
      };
    },
    methods: {
      getTopScorer() {
        return this.students.reduce((prev, current) => (current.correctQuestions > prev.correctQuestions ? current : prev), this.students[0]);
      },
      getHighestAverageScore() {
        return this.students.reduce((prev, current) => (this.calculateAverageScore(current) > this.calculateAverageScore(prev) ? current : prev), this.students[0]);
      },
      calculateAverageScore(student) {
        const sum = student.scores.reduce((acc, score) => acc + score, 0);
        return sum / student.scores.length;
      },
      showStudentDetails(studentId) {
        this.selectedStudent = this.students.find(student => student.id === studentId);
      },
    },
  };
  </script>
  
  <style scoped>
  .sidebar {
  background-color: #2a2b38;
  padding: 20px;
  min-width: 300px;
  color: whitesmoke;
  height: 790px;
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
  color: whitesmoke;
  text-decoration: none;
  display: block;
  padding: 10px;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.sidebar-menu-link:hover {
  background-color: #eaeaea;
}

  .leaderboard-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
    flex-grow: 1;
  }
  .studentLeader{
    display: flex;
  }
  
  .leaderboard-title {
    font-size: 30px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 20px;
    color: #4a4a4a;
  }
  
  .leaderboard-stats {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
  }
  
  .stat-card {
    flex-basis: 30%;
    background-color: #ccc;
    padding: 20px;
    border-radius: 5px;
    display: flex;
    align-items: center;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .stat-icon {
    font-size: 24px;
    margin-right: 10px;
    color: #4a4a4a;
  }
  
  .stat-info {
    flex-grow: 1;
  }
  
  .stat-label {
    font-size: 16px;
    font-weight: bold;
    color: #777;
  }
  
  .stat-value {
    font-size: 24px;
    font-weight: bold;
    color: #4a4a4a;
  }
  
  .leaderboard-table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
  }
  
  .leaderboard-table th,
  .leaderboard-table td {
    padding: 10px;
    border: 1px solid #ccc;
    color: #4a4a4a;
  }
  
  .leaderboard-table th {
    /* background-color: #ccc; */
    font-weight: bold;
    text-align: left;
  }
  
  .leaderboard-table tbody tr:hover {
    background-color: #ccc;
    cursor: pointer;
  }
  
  .student-details {
    background-color: #ccc;
    border-radius: 5px;
    padding: 20px;
    margin-top: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .details-title {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 10px;
    color: #4a4a4a;
  }
  
  .details-content {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 20px;
  }
  
  .details-row {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
    color: #4a4a4a;
  }
  
  .details-label {
    flex-basis: 30%;
    font-weight: bold;
  }
  
  .details-value {
    flex-grow: 1;
  }
  
  @media (max-width: 768px) {
    .leaderboard-stats {
      flex-wrap: wrap;
    }
  
    .stat-card {
      margin-bottom: 10px;
    }
  }
  </style>
  