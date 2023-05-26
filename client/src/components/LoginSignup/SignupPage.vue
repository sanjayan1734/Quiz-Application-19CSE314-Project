<template>
    <div class="vue-tempalte">
        <form>
            <h3>Sign Up</h3>
            <div class="form-group">
                <label>Full Name</label>
                <input type="text" class="form-control form-control-lg"/>
            </div>
            <div class="form-group">
                <label>Email address</label>
                <input type="email" class="form-control form-control-lg" />
            </div>
            <div class="form-group">
                <label>Password</label>
                <input type="password" class="form-control form-control-lg" />
            </div>

            <button type="submit" class="btn btn-dark btn-lg btn-block">Sign Up</button>
            <p class="forgot-password text-right">
                Already registered 
                <router-link :to="{name: 'login'}">sign in?</router-link>
            </p>
        </form>

            <label for="name">Confirm Password</label>
            <div>
                <v-text-field type="password">
                    <input v-model="password" type="password" placeholder="Enter the confirmed password ..." required /><img
                        v-if="!password_confirmation" style="display: none;" src="../assets/ok.svg" alt=""><img
                        v-else-if="password === password_confirmation" src="../assets/ok.svg" alt="">
                </v-text-field>
            </div>

        </div>



        <div class="check_bar">
            <div> <input type="checkbox" name="" id="">
                <label for="">Remember Me</label>
            </div>

            <a href="">Forgot your password? </a>

        </div>


        <button class="log">
            Signup
        </button>


        <!-- <span>Have an existing account? <a href="/Login">Login</a> </span> -->

    </div>
</template>
<script>
    export default {
        data() {
            return {
                questionobj:{
                questionDescription: "",//this.individualQuestion.question,
                questionid: "",//this.individualQuestion.questionid,
                optionA:"",//this.individualQuestion.opt1,
                optionB: "",//this.individualQuestion.opt2,
                optionC: "",//this.individualQuestion.opt3
    },
            }
        }
    }
</script>