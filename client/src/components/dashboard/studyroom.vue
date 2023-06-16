<template>
    <div class="group-study-room">
      <h2 class="group-study-title">Group Study Room</h2>
      <div class="study-room-container">
        <div class="study-room-left">
          <h3 class="study-room-heading">Participants</h3>
          <ul class="participant-list">
            <li v-for="participant in participants" :key="participant.id" class="participant-item">
              <div class="participant-avatar">
                <img :src="participant.avatar" :alt="participant.name" class="avatar-image" />
              </div>
              <div class="participant-details">
                <span class="participant-name">{{ participant.name }}</span>
                <span class="participant-status" :class="participant.status.toLowerCase()">{{ participant.status }}</span>
              </div>
            </li>
          </ul>
          <div class="invite-section">
            <input v-model="newParticipant" placeholder="Enter participant name" class="participant-input" />
            <button @click="addParticipant" class="invite-button">Invite</button>
          </div>
        </div>
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
          <div class="add-material-section">
            <input v-model="newMaterialName" placeholder="Enter material name" class="material-input" />
            <select v-model="newMaterialType" class="material-select">
              <option value="Book">Book</option>
              <option value="Article">Article</option>
              <option value="Presentation">Presentation</option>
            </select>
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
          { id: 1, name: 'John Doe', status: 'Online', avatar: 'https://placeimg.com/50/50/people' },
          { id: 2, name: 'Jane Smith', status: 'Online', avatar: 'https://placeimg.com/50/50/people' },
          { id: 3, name: 'Alex Johnson', status: 'Offline', avatar: 'https://placeimg.com/50/50/people' }
        ],
        newParticipant: '',
        materials: [
          { id: 1, name: 'Mathematics Textbook', type: 'Book', icon: 'fas fa-book' },
          { id: 2, name: 'Physics Lecture Notes', type: 'Presentation', icon: 'fas fa-file-powerpoint' },
          { id: 3, name: 'Chemistry Article', type: 'Article', icon: 'fas fa-newspaper' }
        ],
        newMaterialName: '',
        newMaterialType: 'Book'
      };
    },
    methods: {
      addParticipant() {
        if (this.newParticipant.trim() !== '') {
          const newParticipant = {
            id: this.participants.length + 1,
            name: this.newParticipant.trim(),
            status: 'Online',
            avatar: 'https://placeimg.com/50/50/people'
          };
          this.participants.push(newParticipant);
          this.newParticipant = '';
        }
      },
      addMaterial() {
        if (this.newMaterialName.trim() !== '') {
          const newMaterial = {
            id: this.materials.length + 1,
            name: this.newMaterialName.trim(),
            type: this.newMaterialType,
            icon: this.getMaterialIcon(this.newMaterialType)
          };
          this.materials.push(newMaterial);
          this.newMaterialName = '';
          this.newMaterialType = 'Book';
        }
      },
      getMaterialIcon(type) {
        switch (type) {
          case 'Book':
            return 'fas fa-book';
          case 'Article':
            return 'fas fa-newspaper';
          case 'Presentation':
            return 'fas fa-file-powerpoint';
          default:
            return '';
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .group-study-room {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 50px;
    font-family: Arial, sans-serif;
  }
  
  .group-study-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
  }
  
  .study-room-container {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    max-width: 800px;
  }
  
  .study-room-left,
  .study-room-right {
    flex: 1;
  }
  
  .study-room-heading {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 10px;
  }
  
  .participant-list,
  .material-list {
    list-style: none;
    padding: 0;
  }
  
  .participant-item,
  .material-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
  }
  
  .participant-avatar,
  .material-icon {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    overflow: hidden;
  }
  
  .avatar-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  
  .participant-details,
  .material-details {
    flex: 1;
    margin-left: 10px;
  }
  
  .participant-name,
  .material-name {
    font-weight: bold;
  }
  
  .participant-status,
  .material-type {
    color: #888;
  }
  
  .participant-input,
  .material-input {
    padding: 10px;
    margin-bottom: 10px;
    width: 100%;
    border: 1px solid #ccc;
    border-radius: 4px;
    outline: none;
  }
  
  .participant-input:focus,
  .material-input:focus {
    border-color: #007bff;
  }
  
  .invite-button,
  .add-material-button {
    padding: 10px 20px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 14px;
    transition: background-color 0.3s ease;
  }
  
  .invite-button:hover,
  .add-material-button:hover {
    background-color: #0056b3;
  }
  
  .material-select {
    padding: 10px;
    margin-right: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  @media (max-width: 768px) {
    .study-room-container {
      flex-direction: column;
    }
  }
  </style>
  