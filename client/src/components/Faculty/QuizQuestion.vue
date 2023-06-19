<script>
export default {
    props: {
        questionid:Number
    }
}
</script>

<template >
    <div class="form-groups">
        <label for="quizDescription">Enter Question{{ questionid }}:</label>
        <input type="text" id="quiz" name="quizDescription" placeholder="Enter questions" class="inputs">
    </div>
    <div class="form-groups">
        <label for="quizDescription">Enter Option 1:</label>
        <input type="text" id="quiz" name="quizDescription" placeholder="Enter option 1" class="inputs">
    </div>
    <div class="form-groups">
        <label for="quizDescription">Enter Option 2:</label>
        <input type="text" id="quiz" name="quizDescription" placeholder="Enter option 2" class="inputs">
    </div>
    <div class="form-groups">
        <label for="quizDescription">Enter Option 3:</label>
        <input type="text" id="quiz" name="quizDescription" placeholder="Enter option 3" class="inputs">
    </div>
</template>

<style>
.form-groups {
  margin-bottom: 20px;
  margin-top: 20px;
}
.inputs {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border-radius: 5px;
  border: 1px solid #ccc;
} 
</style>