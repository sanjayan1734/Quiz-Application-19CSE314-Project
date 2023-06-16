<template>
    <div class="studyroom">
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
        <li class="sidebar-menu-item">
          <router-link to="/studyroom" class="sidebar-menu-link">Study Room</router-link>
        </li>
      </ul>
      </div>
    <div class="group-study-room"  style="background-color: #e5dada;;">
      <h2 class="group-study-title">Group Study Room</h2>
      <br>
      <br>
      <div class="study-room-container">
        
          <h3 class="study-room-heading">Participants</h3>
          <ul class="participant-list">
            <li v-for="participant in participants" :key="participant.id" class="participant-item">
              <div class="participant-avatar">
                <i class="fas fa-user"></i>
              </div>
              <div class="participant-details">
                <span class="participant-name">{{ participant.name }}</span>
                <span class="participant-status">{{ participant.status }}</span>
              </div>
            </li>
          </ul>
          <div class="invite-form">
            <input v-model="newParticipant" class="participant-input" type="text" placeholder="Enter participant name" />
            <button @click="addParticipant" class="invite-button">Invite</button>
          </div>
        </div>
        <br>
        <br>
        <div class="study-room-right">
          <h3 class="study-room-heading">Study Materials</h3>
          <ul class="material-list">
            <li v-for="material in materials" :key="material.id" class="material-item">
              <div class="material-icon">
                <i :class="material.icon"></i>
              </div>
              <div class="material-details">
                <span class="material-name">{{ material.name }}</span>
                <span class="material-type">{{ material.type }}</span>
              </div>
            </li>
          </ul>
          <div class="material-form">
            <div class="material-input-container">
              <input v-model="newMaterialName" class="material-input" type="text" placeholder="Enter material name" />
              <select v-model="newMaterialType" class="material-select">
                <option value="Book">Book</option>
                <option value="Article">Article</option>
                <option value="Presentation">Presentation</option>
              </select>
            </div>
            <button @click="addMaterial" class="add-material-button">Add Material</button>
          </div>
        </div>
      </div>
    </div>
    
  </template>
  
  <script>
  export default {
    data() {
      return {
        participants: [
          { id: 1, name: "John Doe", status: "Online" },
          { id: 2, name: "Jane Smith", status: "Offline" },
          { id: 3, name: "Mike Johnson", status: "Online" }
        ],
        newParticipant: "",
        materials: [
          { id: 1, name: "Book 1", type: "Book", icon: "fas fa-book" },
          { id: 2, name: "Article 1", type: "Article", icon: "fas fa-newspaper" },
          { id: 3, name: "Presentation 1", type: "Presentation", icon: "fas fa-file-powerpoint" }
        ],
        newMaterialName: "",
        newMaterialType: "Book"
      };
    },
    methods: {
      addParticipant() {
        if (this.newParticipant.trim() !== "") {
          const newParticipant = {
            id: this.participants.length + 1,
            name: this.newParticipant.trim(),
            status: "Online"
          };
          this.participants.push(newParticipant);
          this.newParticipant = "";
        }
      },
      addMaterial() {
        if (this.newMaterialName.trim() !== "") {
          const newMaterial = {
            id
  
  : this.materials.length + 1,
            name: this.newMaterialName.trim(),
            type: this.newMaterialType,
            icon: this.MaterialIcon(this.newMaterialType)
          };
          this.materials.push(newMaterial);
          this.newMaterialName = "";
          this.newMaterialType = "Book";
        }
      },
      MaterialIcon(type) {
        switch (type) {
          case "Book":
            return "fas fa-book";
          case "Article":
            return "fas fa-newspaper";
          case "Presentation":
            return "fas fa-file-powerpoint";
          default:
            return "fas fa-book";
        }
      }
    }
  };
  </script>
  
  <style>
  .sidebar {
  background-color: #2a2b38;
  padding: 20px;
  min-width: 300px;
  color: whitesmoke;
  height: 900px;
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
  .studyroom{
    display: flex;
  }
  .group-study-room {
    flex-grow: 1;
    padding: 20px;
    
    align-items: center;
    
    font-family: Arial, sans-serif;
  }
  
  .group-study-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
  }
  
  .study-room-container {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    width:800px;
    gap: 40px;
  }
  
  
  .study-room-right {
    width:800px;
  }
  
  .study-room-heading {
    font-size: 26px;
    font-weight: bold;
    margin-bottom: 10px;
  }
  
  .participant-list,
  .material-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .participant-item,
  .material-item {
    display: flex;
    align-items: center;
    padding: 10px 0;
    border-bottom: 1px solid #ccc;
  }
  
  .participant-details,
  .material-details {
    margin-left: 10px;
  }
  
  .participant-name,
  .material-name {
    font-weight: bold;
  }
  
  .participant-input,
  .material-input,
  .material-select {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .invite-button,
  .add-material-button {
    padding: 10px;
    background-color: #2a2b38;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 14px;
    width: 100%;
    text-align: center;
  }
  
  .material-icon {
    font-size: 18px;
    color: #888;
  }
  
  .material-input-container {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  
  @media (max-width: 768px) {
    .study-room-container {
      flex-direction: column;
    }
    .study-room-left,
    .study-room-right {
      width: 100%;
    }
  }
  </style>