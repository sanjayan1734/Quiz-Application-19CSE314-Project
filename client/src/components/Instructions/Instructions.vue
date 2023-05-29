<template>
    <div class="quiz-instructions">
        <div class="content">
            <h1>Welcome to the Quiz</h1>
            <p class="quiz-description">Prepare yourself by going through the instructions below:</p>
            <button class="start-button" @click="startQuiz">Start Quiz</button>
        </div>

        <div class="sidebar">
            <h3>Quiz Instructions</h3>
            <p class="subtitle">Read the instructions carefully before starting the quiz:</p>
            <ol class="instruction-list">
                <li>There are a total of 6 questions in this quiz.</li>
                <li>You will have 2 minutes to complete the entire test</li>
                <li>You can change your answer even after selecting one</li>
                <li>Make sure to click the "Next" button to submit your answer and proceed to the next question.</li>
                <li>Click submit and the end of the test to view your scores.</li>
            </ol>
        </div>
    </div>
</template>

<script>
export default {
    methods: {
        startQuiz() {
            // Implement the logic to start the quiz here
        },
    },
};
</script>

<style scoped>
.quiz-instructions {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    padding: 20px;
}

.content {
    text-align: center;
    margin-right: 40px;
}

h1 {
    font-size: 40px;
    margin-bottom: 20px;
    color: #30336b;
}

.quiz-description {
    font-size: 20px;
    margin-bottom: 30px;
    color: #555;
}

.start-button {
    padding: 14px 28px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    font-size: 20px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.start-button:hover {
    background-color: #0069d9;
}

.sidebar {
    width: 400px;
    text-align: left;
}

.sidebar h3 {
    font-size: 24px;
    margin-bottom: 10px;
    color: #30336b;
}

.subtitle {
    font-size: 18px;
    margin-bottom: 20px;
    color: #555;
}

.instruction-list {
    margin-left: 0;
    padding-left: 20px;
}

.instruction-list li {
    font-size: 16px;
    margin-bottom: 10px;
    color: #555;
}
</style>