
<script>
import UserCard from './UserCard.vue';
import axios from 'axios';

export default {
    name:"usersPage",
    components: {
        UserCard,
    },
    mounted() {
        axios.get('http://harish2511-001-site1.btempurl.com/api/User/GetAllStudents').then((response) => {
            console.log(response.data[0])
            console.log(response.data)
            this.profileInfo = response.data
            console.log("profileInfo = ")
            console.log(this.profileInfo)
            
        })  
    },
    data() {
        return {
            profileInfo:
        [{
            Email:String,
            Id:Number,
            Name:String,
            quizcount:Number,
            totalcorrectq:Number,
            totalQuizzes:3
        }]
        }
    },
}

</script>

<template>
    <h2 class="heading">Users</h2>
<br><br>
    <div class="user-cards" v-for="item in this.profileInfo" :key="item.Id">
        <p>
            <UserCard :Username = "item.name" :ratings = "item.totalcorrectq" />
        </p>
    </div>
</template>

<style>
.heading {
    margin-left : 2%;
    margin-top: 1%;
}
</style>