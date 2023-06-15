<template>
    <div class="discussions">
    <div class="sidebar">
      <div class="sidebar-header">
        <h2 class="sidebar-title">Quiz App</h2>
      </div>
      
      <ul class="sidebar-menu" >
        <li class="sidebar-menu-item">
          <router-link to="/" class="sidebar-menu-link" style>Home</router-link>
        </li>
        <li class="sidebar-menu-item">
          <router-link to="/dashboard/dash" class="sidebar-menu-link">Dashboard</router-link>
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
    <div class="main-content" style="background-color: #e5dada;;">
    <div class="container">
      <div class="navbar">
        <h1 class="navbar-title">Discussion Forum</h1>
        <ul class="quiz-list">
          <li
            v-for="quiz in quizzes"
            :key="quiz.id"
            @click="selectQuiz(quiz.id)"
            :class="{ active: selectedQuiz === quiz.id }"
          >
            {{ quiz.name }}
          </li>
        </ul>
      </div>
  
      <div class="discussion-container">
        <div class="discussion-header">
          <h2 class="discussion-title">Discussion: {{ selectedQuiz }}</h2>
        </div>
  
        <div class="discussion-messages">
          <div
            v-for="post in paginatedPosts"
            :key="post.id"
            class="discussion-message"
          >
            <div class="message-header">
              <div class="user-info">
                <span class="username">{{ post.author }}</span>
                <span class="timestamp">{{ formatTimestamp(post.timestamp) }}</span>
              </div>
              <div class="post-actions">
                <button @click="deletePost(post.id)" class="delete-button">Delete</button>
              </div>
            </div>
            <div class="message-body">{{ post.content }}</div>
          </div>
        </div>
  
        <div class="pagination">
          <button
            v-for="pageNumber in totalPages"
            :key="pageNumber"
            @click="changePage(pageNumber)"
            :class="{ active: currentPage === pageNumber }"
          >
            {{ pageNumber }}
          </button>
        </div>
  
        <div class="reply-form">
          <h3 class="form-title">Add Reply</h3>
          <div class="form-group">
            <label for="author">Author:</label>
            <input v-model="newReply.author" type="text" id="author" required>
          </div>
          <div class="form-group">
            <label for="content">Content:</label>
            <textarea v-model="newReply.content" id="content" required></textarea>
          </div>
          <button @click="addReply" class="submit-button">Submit</button>
        </div>
      </div>
    </div>
    </div>
    </div>
  </template>
  
  <script>
  import moment from 'moment';
  
  export default {
    data() {
      return {
        quizzes: [
          { id: 1, name: 'Quiz 1' },
          { id: 2, name: 'Quiz 2' },
          { id: 3, name: 'Quiz 3' },
        ],
        selectedQuiz: 1,
        posts: [
          { id: 1, author: 'John Doe', content: 'This is the first post.', timestamp: 1634325600000 },
          { id: 2, author: 'Jane Smith', content: 'This is the second post.', timestamp: 1634326800000 },
          { id: 3, author: 'Michael Johnson', content: 'This is the third post.', timestamp: 1634328000000 },
          // Add more sample posts here...
        ],
        currentPage: 1,
        postsPerPage: 5,
        newReply: {},
      };
    },
    computed: {
      paginatedPosts() {
        const startIndex = (this.currentPage - 1) * this.postsPerPage;
        const endIndex = startIndex + this.postsPerPage;
        return this.posts.slice(startIndex, endIndex);
      },
      totalPages() {
        return Math.ceil(this.posts.length / this.postsPerPage);
      },
    },
    methods: {
      selectQuiz(quizId) {
        this.selectedQuiz = quizId;
        this.currentPage = 1;
      },
      formatTimestamp(timestamp) {
        return moment(timestamp).format('MMMM Do YYYY, h:mm:ss a');
      },
      changePage(pageNumber) {
        this.currentPage = pageNumber;
      },
      addReply() {
        const { author, content } = this.newReply;
        if (author && content) {
          const newPost = {
            id: this.posts.length + 1,
            author,
            content,
            timestamp: Date.now(),
          };
          this.posts.push(newPost);
          this.newReply = {};
        }
      },
      deletePost(postId) {
        const index = this.posts.findIndex(post => post.id === postId);
        if (index !== -1) {
          this.posts.splice(index, 1);
        }
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
}
.discussions {
  display: flex;
}
.main-content {
  flex-grow: 1;
  padding: 20px;
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
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
  }
  
  .navbar-title {
    font-size: 30px;
    font-weight: bold;
  }
  
  .quiz-list {
    list-style-type: none;
    display: flex;
    align-items: center;
    padding: 0;
    margin: 0;
  }
  
  .quiz-list li {
    cursor: pointer;
    padding: 10px;
    margin-left: 10px;
    background-color: #f5f5f5;
    border-radius: 5px;
  }
  
  .quiz-list li.active {
    background-color: #ccc;
  }
  
  .discussion-container {
    margin-top: 20px;
  }
  
  .discussion-header {
    margin-bottom: 20px;
  }
  
  .discussion-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
  }
  
  .discussion-messages {
    margin-bottom: 20px;
  }
  
  .discussion-message {
    margin-bottom: 20px;
    border: 1px solid #ccc;
    padding: 10px;
    border-radius: 5px;
  }
  
  .message-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
  }
  
  .user-info {
    display: flex;
    align-items: center;
  }
  
  .username {
    font-weight: bold;
    margin-right: 10px;
  }
  
  .timestamp {
    color: #777;
    font-size: 14px;
  }
  
  .post-actions {
    display: flex;
    align-items: center;
  }
  
  .delete-button {
    background-color: #f44336;
    color: #fff;
    border: none;
    padding: 5px 10px;
    font-size: 14px;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .message-body {
    font-size: 16px;
  }
  
  .pagination {
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
  }
  
  .pagination button {
    background-color: #f5f5f5;
    border: none;
    padding: 5px 10px;
    margin-right: 5px;
    cursor: pointer;
  }
  
  .pagination button.active {
    background-color: #ccc;
  }
  
  .reply-form {
    background-color: #f5f5f5;
    padding: 20px;
    border-radius: 5px;
  }
  
  .form-title {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 10px;
  }
  
  .form-group {
    margin-bottom: 10px;
  }
  
  .form-group label {
    display: block;
    font-weight: bold;
  }
  
  .form-group input,
  .form-group textarea {
    width: 100%;
    padding: 5px;
    font-size: 16px;
    border-radius: 5px;
    border: 1px solid #ccc;
  }
  
  .submit-button {
    background-color: #4caf50;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    border-radius: 5px;
    cursor: pointer;
  }
  </style>
  