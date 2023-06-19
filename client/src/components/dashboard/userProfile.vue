<template>
    <div class="userprofile" style="background-color: #e5dada;;">
    <div class="sidebar">
      <div class="sidebar-header">
        <h2 class="sidebar-title">Quiz App</h2>
      </div>
      
      <ul class="sidebar-menu" >
        
        <li class="sidebar-menu-item">
          <router-link to="/" class="sidebar-menu-link" style>Home</router-link>
        </li>
        <li class="sidebar-menu-item">
          <router-link to="/userprofile" class="sidebar-menu-link">User Profile</router-link>
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
        <li class="sidebar-menu-item">
          <router-link to="/studyroom" class="sidebar-menu-link">Study Room</router-link>
        </li>
        
        <br>
        <br>
        <br>
        <li class="log_out">
          <a href="/">
            <i class="bx bx-log-out"></i>
            <span class="links_name">Log out</span>
          </a>
        </li>
      </ul>
      </div>
    <div class="user-profile" :class="{ 'dark-mode': darkMode }">
      <h2 class="profile-title">User Profile</h2>
      <div class="profile-details">
        <div class="avatar-container">
        <img :src="avatar" alt="Profile Avatar" class="avatar" />
        <input type="file" @change="handleAvatarChange" accept="image/*" class="avatar-upload" />
      </div>
      <br>
        <form @submit.prevent="updateProfile">
          <div class="form-field">
            <label for="name" class="form-label">Name</label>
            <input type="text" id="name" v-model="user.name" class="form-input" />
          </div>
          <div class="form-field">
            <label for="email" class="form-label">Email</label>
            <input type="email" id="email" v-model="user.email" class="form-input" />
          </div>
          <div class="form-field">
            <label for="password" class="form-label">Password</label>
            <input type="password" id="password" v-model="user.password" class="form-input" />
          </div>
          
          <div class="form-field form-actions">
            <button type="submit" class="update-btn">Update Profile</button>
            <button type="button" class="password-btn" @click="redirectToReset">Change Password</button>
          </div>
          <div v-if="isUpdated" class="success-message">User profile updated successfully!</div>
        </form>
      </div>
      <div class="additional-features">
        <!-- Other form fields -->
      </div>
      <div class="advanced-section">
        <button class="advanced-btn" @click="toggleAdvanced">
          {{ showAdvanced ? 'Hide Advanced' : 'Show Advanced' }}
        </button>
        <div v-show="showAdvanced" class="advanced-content">
          <h3 class="advanced-title">Advanced Features</h3>
          <div class="advanced-options">
            <div class="option">
              <span class="option-label">Dark Mode</span>
              <label class="switch">
                <input type="checkbox" v-model="darkMode" @change="toggleDarkMode" />
                <span class="slider"></span>
              </label>
            </div>
            
            <div class="option">
              <span class="option-label">Data Privacy</span>
              <div class="data-privacy">
                <label>
                  <input type="radio" v-model="dataPrivacy" value="public" />
                  Public
                </label>
                <label>
                  <input type="radio" v-model="dataPrivacy" value="private" />
                  Private
                </label>
                <label>
                  <input type="radio" v-model="dataPrivacy" value="custom" />
                  Custom
                </label>
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
        avatar: 'https://dummyimage.com/150x150/6a6a6a/ffffff&text=Profile',
        user: {
          name: 'Harish',
          email: 'harish251102@gmail.com',
          password: 'harish02',
          // Other user properties
        },
        newPassword: '',
        confirmPassword: '',
        isUpdated: false,
        showAdvanced: false,
        darkMode: false,
        notificationPrefs: {
          email: false,
          sms: false,
          push: false,
        },
        dataPrivacy: 'public',
      };
    },
    methods: {
        handleAvatarChange(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
          this.avatar = e.target.result;
        };
        reader.readAsDataURL(file);
      }
    },
    // Other methods


      updateProfile() {
        // Logic to update the user profile with the provided information
        // Assuming the profile update is successful, show the success message
        this.isUpdated = true;
      },
      toggleAdvanced() {
        this.showAdvanced = !this.showAdvanced;
      },
      redirectToReset() {
        // Logic to redirect to the password reset page
        // Replace this with your actual route navigation code
        this.$router.push('/reset');
      },
      toggleDarkMode() {
        // Update the dark mode preference here
        // You can modify this method to apply dark mode styles to the entire page
        // For simplicity, we'll just update the class on the root element
        const rootElement = document.documentElement;
        if (this.darkMode) {
          rootElement.classList.add('dark-mode');
        } else {
          rootElement.classList.remove('dark-mode');
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .user-profile {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f7f7f7;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  .userprofile{
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
  .profile-title {
    text-align: center;
    margin-bottom: 20px;
  }
  
  .profile-details {
    margin-bottom: 20px;
  }
  
  .form-field {
    margin-bottom: 15px;
  }
  
  .form-label {
    display: block;
    font-weight: bold;
    margin-bottom: 5px;
  }
  
  .form-input {
    width: 100%;
    padding: 8px;
    font-size: 14px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .form-actions {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .update-btn,
  .password-btn {
    padding: 8px 16px;
    font-size: 14px;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .update-btn {
    background-color: grey;
    color: #fff;
    border: none;
  }
  
  .password-btn {
    background-color: grey;
    color: #fff;
    border: none;
  }
  
  .success-message {
    margin-top: 10px;
    text-align: center;
    color: #008000;
    font-weight: bold;
  }
  
  .advanced-section {
    margin-top: 20px;
    text-align: center;
  }
  
  .advanced-btn {
    padding: 8px 16px;
    font-size: 14px;
    border-radius: 4px;
    cursor: pointer;
    background-color: grey;
    color: #fff;
    border: none;
  }
  
  .advanced-content {
    margin-top: 20px;
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .advanced-title {
    margin-top: 0;
  }
  
  .advanced-options {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
  }
  
  .option {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  
  .option-label {
    font-weight: bold;
  }
  
  .switch {
    position: relative;
    display: inline-block;
    width: 40px;
    height: 20px;
  }
  
  .switch input {
    opacity: 0;
    width: 0;
    height: 0;
  }
  
  .slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #ccc;
    transition: .4s;
    border-radius: 34px;
  }
  
  .slider:before {
    position: absolute;
    content: "";
    height: 16px;
    width: 16px;
    left: 2px;
    bottom: 2px;
    background-color: white;
    transition: .4s;
    border-radius: 50%;
  }
  
  input:checked + .slider {
    background-color: #2196F3;
  }
  
  input:focus + .slider {
    box-shadow: 0 0 1px #2196F3;
  }
  
  input:checked + .slider:before {
    transform: translateX(20px);
  }
  
  .notification-preferences label {
    margin-right: 10px;
  }
  
  .data-privacy label {
    display: block;
    margin-bottom: 5px;
  }
  
  .dark-mode {
    background-color: #222;
    color: #fff;
  }
  
  .dark-mode .profile-title {
    color: #fff;
  }
  
  .dark-mode .form-input {
    background-color: #444;
    color: #fff;
    border-color: #444;
  }
  
  .dark-mode .update-btn,
  .dark-mode .password-btn {
    background-color: #009688;
  }
  
  .dark-mode .success-message {
    color: #00FF00;
  }
  
  .dark-mode .advanced-btn {
    background-color: #9C27B0;
  }
  
  .dark-mode .advanced-content {
    background-color: #333;
    color: #fff;
  }
  
  .dark-mode .option-label {
    color: #fff;
  }
  </style>
  