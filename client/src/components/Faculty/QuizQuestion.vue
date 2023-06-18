<script>
export default {
}
</script>

<template >
    <div class="form-group">
        <label for="quizDescription">Enter Question:</label>
        <input type="text" id="quiz" name="quizDescription" placeholder="Enter questions">
    </div>
    <div class="form-group">
        <label for="quizDescription">Enter Option 1:</label>
        <input type="text" id="quiz" name="quizDescription" placeholder="Enter option 1">
    </div>
    <div class="form-group">
        <label for="quizDescription">Enter Option 2:</label>
        <input type="text" id="quiz" name="quizDescription" placeholder="Enter option 2">
    </div>
    <div class="form-group">
        <label for="quizDescription">Enter Option 3:</label>
        <input type="text" id="quiz" name="quizDescription" placeholder="Enter option 3">
    </div>
</template>

<style>
.form-group {
  margin-bottom: 20px;
  margin-top: 20px;
}
input[type="text"] {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border-radius: 5px;
  border: 1px solid #ccc;
}
</style>