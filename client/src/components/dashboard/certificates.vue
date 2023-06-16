
<template>
    <div class="certificates">
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
    <div class="certification-page" style="background-color: #e5dada;;">
      <h2 class="certification-title">Quiz Certification</h2>
      <p class="certification-note">Note: The following certificates are sample certificates.</p>
      <div v-for="quiz in quizzes" :key="quiz.id" class="certification-card">
        <div class="certification-details">
          <div class="certification-item">
            <span class="certification-label">Quiz Title:</span>
            <span class="certification-value">{{ quiz.title }}</span>
          </div>
          <div class="certification-item">
            <span class="certification-label">Date Completed:</span>
            <span class="certification-value">{{ quiz.completionDate }}</span>
          </div>
          <div class="certification-item">
            <span class="certification-label">Score:</span>
            <span class="certification-value">{{ quiz.score }}%</span>
          </div>
          <div class="certification-item">
            <span class="certification-label">Issuer:</span>
            <span class="certification-value">{{ quiz.issuer }}</span>
          </div>
          <div class="certificate-image">
  <!--<img :src="photo" alt="Certificate" class="certificate-img">-->
</div>
<div class="certification-item">
    <span class="certification-label">Certificate:</span>
    <button @click="downloadCertificate('{{quiz.certificateUrl}}')" class="download-button">Download Certificate</button>
  </div>
        </div>
      </div>
    </div>
</div>
  </template>
  
  <script>

  function downloadCertificate(certificateUrl) {
    window.open(certificateUrl, '_blank');
  }
  
  export default {
    data() {
      return {
        computed: {
    photo() {
      return '../quiz1.png';
    }
  },
        quizzes: [
          {
            id: 1,
            title: 'Quiz 1',
            completionDate: 'June 15, 2023',
            score: 90,
            issuer: 'Sample Issuer',
            //certificateImageUrl:'https://drive.google.com/file/d/1ObANxb6go-1zBtvebKd1LIKwcJjidTu7/view?usp=sharing',
            certificateUrl: 'https://drive.google.com/file/d/1eCFGBefHzYGfuiBqaxPAjWOtxPyMfSJj/view?usp=sharing'
          },
          {
            id: 2,
            title: 'Quiz 2',
            completionDate: 'June 16, 2023',
            score: 85,
            issuer: 'Sample Issuer',
          //  certificateImageUrl:'quiz2.png',
            certificateUrl: 'https://drive.google.com/file/d/1I910j85WG3z7pEqyh-5_S1IMRnkHcvJ6/view?usp=sharing'
          },
          {
            id: 3,
            title: 'Quiz 3',
            completionDate: 'June 13, 2023',
            score: 95,
            issuer: 'Sample Issuer',
            //certificateImageUrl:'quiz3.png',
            certificateUrl: 'https://drive.google.com/file/d/1ImocrdfmO5NRpcnZN8OwxjVCI7pDsnVX/view?usp=sharing'
          }
        ]
      };
    },
    methods: {
      downloadCertificate(certificateUrl) {
        const link = document.createElement('a');
        link.href = certificateUrl;
        link.download = 'certificate.pdf';
        link.click();
      },
      
    }
  };
  </script>
  
  <style>
  .certificates{
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

  .certification-page {
    flex-grow: 1;
    padding:20px;
    align-items: center;
    
    font-family: Arial, sans-serif;
  }
  
  .certification-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
    align-items: center;
    color: #333;
  }
  
  .certification-note {
    margin-bottom: 20px;
    color: #777;
  }
  
  .certification-card {
    width: 100%;
    max-width: 1000px;
    margin-bottom: 20px;
    align-items: center;
    align-content: center;
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 20px;
  }
  
  .certification-details {
    display: flex;
    flex-direction: column;
  }
  
  .certification-item {
    display: flex;
    justify-content: space-between;
    margin-bottom: 10px;
    color: #333;
  }
  
  .certification-label {
    font-weight: bold;
  }
  
  .certification-value {
    margin-left: 10px;
  }
  
  .certificate-image {
    display: flex;
    justify-content: center;
    margin: 20px 0;
  }
  
  .certificate-img {
    max-width: 100%;
    height: auto;
  }
  
  .download-button {
  padding: 5px 10px;
  background-color: #2a2b38;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  width: 160px;
}
  
  @media (max-width: 768px) {
    .certification-card {
      font-size: 14px;
    }
  }
  </style>
  