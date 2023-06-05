
<script>
import UserCard from './UserCard.vue';
import axios from 'axios';

export default {
    name:"usersPage",
    components: {
        UserCard,
    },
    mounted() {
        axios.get('https://localhost:7282/api/User/GetAllStudents').then((response) => {
            console.log(response[0])
            console.log(response)
        })  
    },
    data() {
        return {
            ParticipantDetails:[{
                name:String
            }]
        }
    },
}

</script>

<template>
    <h2 class="heading">Users</h2>
<br><br>
    <UserCard />
    <UserCard />
</template>

<style>
.heading {
    margin-left : 2%;
    margin-top: 1%;
}
</style>