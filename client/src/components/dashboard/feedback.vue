<template>
    <div class="feedbacks">
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
    <div class="feedback-page" style="background-color: #e5dada;;">
        
      <h2 class="feedback-title">Share your thoughts on us!</h2>
      <div class="feedback-container">
        <form class="feedback-form" @submit.prevent="submitFeedback">
          <div class="form-group">
            <label for="name">Name:</label>
            <input type="text" id="name" v-model="feedback.name" required>
          </div>
          <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" v-model="feedback.email" required>
          </div>
          <div class="form-group">
            <label for="message">Message:</label>
            <textarea id="message" v-model="feedback.message" required></textarea>
          </div>
          <div class="form-group">
            <label for="rating">Rating:</label>
            <div class="rating">
              <span class="star" v-for="index in 5" :key="index" :class="{ 'filled': index <= feedback.rating }" @click="setRating(index)">
                &#9733;
              </span>
            </div>
          </div>
          <div class="button-group">
            <button type="submit" class="submit-button">Submit Feedback</button>
            <button type="button" class="clear-button" @click="clearForm">Clear Form</button>
          </div>
        </form>
      </div>
      <div class="thank-you" v-if="feedbackSubmitted">Thank you for your feedback!</div>
      <div class="recent-feedback-container">
        <h3 class="recent-feedback-title">Recent Feedback</h3>
        <div v-if="recentFeedback.length === 0" class="no-feedback">No feedback available</div>
        <div v-else class="feedback-item" v-for="feedbackItem in recentFeedback" :key="feedbackItem.id">
          <div class="feedback-header">
            <span class="feedback-name">{{ feedbackItem.name }}</span>
            <span class="feedback-date">{{ formatDate(feedbackItem.date) }}</span>
          </div>
          <div class="feedback-content">
            <div class="feedback-email">{{ feedbackItem.email }}</div>
            <div class="feedback-message">{{ feedbackItem.message }}</div>
            <div class="feedback-rating">
              <span class="rating-label">Rating:</span>
              <div class="stars">
                <span class="star" v-for="index in 5" :key="index" :class="{ 'filled': index <= feedbackItem.rating }">
                  &#9733;
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        feedback: {
          name: '',
          email: '',
          message: '',
          rating: 0
        },
        recentFeedback: [
          {
            id: 1,
            name: 'John Doe',
            email: 'johndoe@example.com',
            message: 'Great quiz! I learned a lot.',
            rating: 5,
            date: new Date()
          },
          {
            id: 2,
            name: 'Jane Smith',
            email: 'janesmith@example.com',
            message: 'The quiz was challenging but informative.',
            rating: 4,
            date: new Date()
          }
        ],
        feedbackSubmitted: false
      };
    },
    methods: {
      submitFeedback() {
        const newFeedback = {
          id: Date.now(),
          name: this
  
  .feedback.name,
          email: this.feedback.email,
          message: this.feedback.message,
          rating: this.feedback.rating,
          date: new Date()
        };
        this.recentFeedback.unshift(newFeedback);
        this.clearForm();
        this.feedbackSubmitted = true;
      },
      clearForm() {
        this.feedback.name = '';
        this.feedback.email = '';
        this.feedback.message = '';
        this.feedback.rating = 0;
        this.feedbackSubmitted = false;
      },
      setRating(rating) {
        this.feedback.rating = rating;
      },
      formatDate(date) {
        return new Intl.DateTimeFormat('en-US', { dateStyle: 'long', timeStyle: 'short' }).format(date);
      }
    }
  };
  </script>
  
  <style scoped>
  .feedbacks{
    display: flex;
  }
  .sidebar {
  background-color: #2a2b38;
  padding: 20px;
  min-width: 300px;
  color: whitesmoke;
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
  .feedback-page {
    flex-grow: 1;
  padding: 30px;
    flex-direction: column;
    align-items: center;
    
    font-family: Arial, sans-serif;
  }
  
  .feedback-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
  }
  
  .feedback-container {
    width: 100%;
    max-width: 900px;
    padding: 30px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .feedback-form {
    display: flex;
    flex-direction: column;
  }
  
  .form-group {
    margin-bottom: 20px;
  }
  
  .form-group label {
    font-weight: bold;
  }
  
  .form-group input,
  .form-group textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .rating {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  
  .star {
    font-size: 24px;
    cursor: pointer;
  }
  
  .star.filled {
    color: gold;
  }
  
  .button-group {
    display: flex;
    justify-content: flex-end;
  }
  
  .submit-button,
  .clear-button {
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    font-weight: bold;
  }
  
  .submit-button {
    background-color: #2a2b38;
    color: #fff;
    margin-right: 10px;
  }
  
  .clear-button {
    background-color: #ccc;
    color: #000;
  }
  
  .thank-you {
    font-size: 18px;
    color: green;
    margin-top: 20px;
  }
  
  .recent-feedback-container {
    width: 100%;
    max-width: 800px;
    margin-top: 50px;
  }
  
  .recent-feedback-title {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 20px;
  }
  
  .no-feedback {
    font-style: italic;
    color: #888;
  }
  
  .feedback-item {
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 20px;
    margin-bottom: 20px;
  }
  
  .feedback-header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 10px;
  }
  
  .feedback-name {
    font-weight: bold;
  }
  
  .feedback-date {
    color: #888;
  }
  
  .feedback-content {
    font-size: 16px;
  }
  
  .feedback-email {
    margin-bottom: 10px;
  }
  
  .feedback-rating {
    display: flex;
    align-items: center;
  }
  
  .rating-label {
    font-weight: bold;
    margin-right: 10px;
  }
  
  .stars {
    color: gold;
    font-size: 20px;
  }
  
  .star.filled {
    color: gold;
  }
  
  @media (max-width: 768px) {
   
  
   .feedback-form {
      font-size: 14px;
    }
  }
  </style>