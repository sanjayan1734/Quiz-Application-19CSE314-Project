<template>
    <div class="certification-page">
      <h2 class="certification-title">Quiz Certification</h2>
      <div class="certification-content">
        <div class="certification-details">
          <div class="certification-item">
            <span class="certification-label">Quiz Title:</span>
            <span class="certification-value">{{ quizTitle }}</span>
          </div>
          <div class="certification-item">
            <span class="certification-label">Date Completed:</span>
            <span class="certification-value">{{ completionDate }}</span>
          </div>
          <div class="certification-item">
            <span class="certification-label">Score:</span>
            <span class="certification-value">{{ score }}%</span>
          </div>
        </div>
        <div class="certificate-container">
          <img :src="certificateImage" class="certificate-image" alt="Certificate" />
          <button @click="downloadCertificate" class="download-button">Download Certificate</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        certificateImage: 'quiz1.pdf', // Path to the certificate image for the current quiz
        quizTitle: '', // Title of the quiz
        completionDate: '', // Date when the quiz was completed
        score: 0 // Score achieved in the quiz
      };
    },
    methods: {
      downloadCertificate() {
        const link = document.createElement('a');
        link.href = this.certificateImage;
        link.download = 'certificate.png';
        link.click();
      }
    },
    mounted() {
      // Fetch and set the quiz details and certificate image based on the selected quiz
      this.quizTitle = 'Sample Quiz';
      this.completionDate = 'June 15, 2023';
      this.score = 90;
      this.certificateImage = '/path/to/certificate-image.png';
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
  }
  
  .certification-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    max-width: 800px;
    margin: 0 auto;
  }
  
  .certification-details {
    margin-top: 20px;
    border: 1px solid #ccc;
    padding: 20px;
    border-radius: 4px;
    width: 100%;
  }
  
  .certification-item {
    display: flex;
    justify-content: space-between;
    margin-bottom: 10px;
  }
  
  .certification-label {
    font-weight: bold;
  }
  
  .certificate-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 30px;
  }
  
  .certificate-image {
    max-width: 100%;
    height: auto;
    margin-bottom: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  }
  
  .download-button {
    margin-top: 20px;
    padding: 10px 20px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    cursor: pointer;
  }
  
  @media (max-width: 768px) {
    .certification-details {
      font-size: 14px;
    }
  }
  </style>
  