<template>
    <div class="certification-page">
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
  <img src="quiz.certificateImageUrl" alt="Certificate" class="certificate-img">
</div>
          <div class="certification-item">
            <span class="certification-label">Certificate:</span>
            <button @click="downloadCertificate(quiz.certificateUrl)" class="download-button">Download Certificate</button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        quizzes: [
          {
            id: 1,
            title: 'Quiz 1',
            completionDate: 'June 15, 2023',
            score: 90,
            issuer: 'Sample Issuer',
            certificateImageUrl:'https://drive.google.com/file/d/1ObANxb6go-1zBtvebKd1LIKwcJjidTu7/view?usp=sharing',
            certificateUrl: 'https://drive.google.com/file/d/1eCFGBefHzYGfuiBqaxPAjWOtxPyMfSJj/view?usp=sharing'
          },
          {
            id: 2,
            title: 'Quiz 2',
            completionDate: 'June 16, 2023',
            score: 85,
            issuer: 'Sample Issuer',
            certificateImageUrl:'quiz2.png',
            certificateUrl: 'https://drive.google.com/file/d/1I910j85WG3z7pEqyh-5_S1IMRnkHcvJ6/view?usp=sharing'
          },
          {
            id: 3,
            title: 'Quiz 3',
            completionDate: 'June 13, 2023',
            score: 95,
            issuer: 'Sample Issuer',
            certificateImageUrl:'quiz3.png',
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
      }
    }
  };
  </script>
  
  <style>
  .certification-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 50px;
    font-family: Arial, sans-serif;
  }
  
  .certification-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
    color: #333;
  }
  
  .certification-note {
    margin-bottom: 20px;
    color: #777;
  }
  
  .certification-card {
    width: 100%;
    max-width: 800px;
    margin-bottom: 20px;
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
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 14px;
  }
  
  @media (max-width: 768px) {
    .certification-card {
      font-size: 14px;
    }
  }
  </style>
  