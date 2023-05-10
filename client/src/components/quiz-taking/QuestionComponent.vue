<script setup>
    defineProps({
  qno: {
    type: String,
    required: true
  },
  questiontext:{
    type: String,
    required: true
  }
  
})
    

</script>
<template>
    <div class = "qno">
        {{qno}}
        <div class="questions">
            <div class="image">
                image-place-holder
            </div>
            <div class="text">
                {{question-text }}
            </div>
        </div>
    </div>
</template>

