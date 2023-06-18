<template>
     <div class="sidebar">
      <div class="logo-details">
        <span class="logo_name">Quiz App</span>
      </div>
      <ul class="nav-links">
        <li>
          <a href="#" class="active">
            <i class="bx bx-grid-alt"></i>
            <span class="links_name">Dashboard</span>
          </a>
        </li>
        <li>
          <a href="/event">
            <i class="bx bx-box"></i>
            <span class="links_name">Event Management</span>
          </a>
        </li>

        <li class="log_out">
          <a href="/">
            <i class="bx bx-log-out"></i>
            <span class="links_name">Log out</span>
          </a>
        </li>
      </ul>
    </div>
    <section class="home-section">
      <nav>
        <div class="sidebar-button">
          <span class="dashboard">Faculty Dashboard</span>
        </div>
        <!--<div class="search-box">
          <input type="text" placeholder="Search..." />
          <i class="bx bx-search"></i>-->
        
        <div class="profile-details">
          <img src="../Faculty/user.png" alt="" />
          <span class="admin_name">Radhika N</span>
        </div>
      </nav>
      
      <div class="home-content">

        <div class="sales-boxes">
          <div class="recent-sales box">
            <div class="title">CREATE QUIZ</div>  
            
              <div class="form-group">
                <label for="quizName">Quiz Name:</label>
                <input type="text" id="quizName" name="quizName" placeholder="Enter quiz name">
              </div>
              
              <div class="form-group">
                <label for="quizDescription">Quiz Description:</label>
                <input type="text" id="quizDescription" name="quizDescription" placeholder="Enter quiz description">
              </div>
              <div class="form-group">
                <label for="Numberofquestions">Number of questions:</label>
                <input type="text" id="Numberofquestions" name="quizDescription" placeholder="Enter number of questions">
              </div>
              <div class="form-group">
                <label for="Number of options">Number of options:</label>
                <select id="Numberofoptions" name="quizName">
                  <option value="option2">3</option>
                  <!-- Add more options as needed -->
                </select>
                </div>

              <button @click="myFunction()">Proceed</button>

                <div id="opts" v-if="pressedButton == 1">
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
                    <button @click="submitdata()">Create</button>
                    <div class="thank-you" v-if="dataSubmitted">Your quiz data has been successfully added! Please wait for 10-20 minutes to receive the change</div>
                </div>
            <!--<div class="button">
              <a href="#">See All</a>
            </div>-->
        </div>

          <div class="top-sales box">
            <div class="title1">MAKE CHANGES</div>
            <ul class="top-sales-details">
                
                    <ul>
                        <li>Quiz-1<button2 class="close" @click="closebutton()">x</button2></li>
                        <li>Quiz-2<button2 class="close" @click="closebutton()">x</button2></li>
                        <li>Quiz-3<button2 class="close" @click="closebutton()">x</button2></li>           
                        
                    </ul>
                

              
            </ul>
          </div>
        </div>
      </div>
    </section>
  </template>
  <script>
  //var on = document.getElementById("on");
//var off = document.getElementById("off");

 export default {
  data() {
    return {
      pressedButton: 0,
      dataSubmitted: false,
    }

  },
  methods: {
    closebutton()
    {
      var closebtns = document.getElementsByClassName("close");
var i;

for (i = 0; i < closebtns.length; i++) {
  closebtns[i].addEventListener("click", function() {
    this.parentElement.style.display = 'none';
  });
}
  alert('Quiz has been successfully deleted !')
    },
    myFunction() {
    console.log("pressed button")
    this.pressedButton = 1
},
submitdata()
{
  this.dataSubmitted= true;
}
  }
 } 


</script>

  
  <style scoped>
  /* Add your CSS styles here */
  

@import url('https://unpkg.com/boxicons@2.0.7/css/boxicons.min.css');
/* Googlefont Poppins CDN Link */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap');

#opts{
    visibility: visible;
}
.thank-you {
    font-size: 18px;
    color: green;
    margin-top: 20px;
  }
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Poppins', sans-serif;
}
.sidebar{
  position: fixed;
  height: 100%;
  width: 240px;
  background: #0A2558;
  transition: all 0.5s ease;
}
.sidebar.active{
  width: 60px;
}
.sidebar .logo-details{
  height: 80px;
  display: flex;
  align-items: center;
}
.sidebar .logo-details i{
  font-size: 28px;
  font-weight: 500;
  color: #fff;
  min-width: 60px;
  text-align: center
}
.sidebar .logo-details .logo_name{
  color: #fff;
  font-size: 24px;
  font-weight: 500;
  margin-left: 15px;
}
.sidebar .nav-links{
  margin-top: 10px;
}
.sidebar .nav-links li{
  position: relative;
  list-style: none;
  height: 50px;
}
.sidebar .nav-links li a{
  height: 100%;
  width: 100%;
  display: flex;
  align-items: center;
  text-decoration: none;
  transition: all 0.4s ease;
}
.sidebar .nav-links li a.active{
  background: #081D45;
}
.sidebar .nav-links li a:hover{
  background: #081D45;
}
.sidebar .nav-links li i{
  min-width: 60px;
  text-align: center;
  font-size: 18px;
  color: #fff;
}
.sidebar .nav-links li a .links_name{
  color: #fff;
  font-size: 15px;
  font-weight: 400;
  white-space: nowrap;
}
.sidebar .nav-links .log_out{
  position: absolute;
  bottom: 0;
  width: 100%;
}
.home-section{
  position: relative;
  background: #f5f5f5;
  min-height: 100vh;
  width: calc(100% - 240px);
  left: 240px;
  transition: all 0.5s ease;
}
.sidebar.active ~ .home-section{
  width: calc(100% - 60px);
  left: 60px;
}
.home-section nav{
  display: flex;
  justify-content: space-between;
  height: 80px;
  background: #fff;
  display: flex;
  align-items: center;
  position: fixed;
  width: calc(100% - 240px);
  left: 240px;
  z-index: 100;
  padding: 0 20px;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.1);
  transition: all 0.5s ease;
}
.sidebar.active ~ .home-section nav{
  left: 60px;
  width: calc(100% - 60px);
}
.home-section nav .sidebar-button{
  display: flex;
  align-items: center;
  font-size: 24px;
  font-weight: 500;
}
nav .sidebar-button i{
  font-size: 35px;
  margin-right: 10px;
}
.home-section nav .search-box{
  position: relative;
  height: 50px;
  max-width: 550px;
  width: 100%;
  margin: 0 20px;
}
nav .search-box input{
  height: 100%;
  width: 100%;
  outline: none;
  background: #F5F6FA;
  border: 2px solid #EFEEF1;
  border-radius: 6px;
  font-size: 18px;
  padding: 0 15px;
}
nav .search-box .bx-search{
  position: absolute;
  height: 40px;
  width: 40px;
  background: #2697FF;
  right: 5px;
  top: 50%;
  transform: translateY(-50%);
  border-radius: 4px;
  line-height: 40px;
  text-align: center;
  color: #fff;
  font-size: 22px;
  transition: all 0.4 ease;
}
.home-section nav .profile-details{
  display: flex;
  align-items: center;
  background: #F5F6FA;
  border: 2px solid #EFEEF1;
  border-radius: 6px;
  height: 50px;
  min-width: 190px;
  padding: 0 2px 0 2px;
}
nav .profile-details img{
  height: 40px;
  width: 40px;
  border-radius: 6px;
  object-fit: cover;
}
nav .profile-details .admin_name{
  font-size: 15px;
  font-weight: 500;
  color: #333;
  margin: 0 10px;
  white-space: nowrap;
}
nav .profile-details i{
  font-size: 25px;
  color: #333;
}
.home-section .home-content{
  position: relative;
  padding-top: 104px;
}
.home-content .overview-boxes{
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  padding: 0 20px;
  margin-bottom: 26px;
}
.overview-boxes .box{
  display: flex;
  align-items: center;
  justify-content: center;
  width: calc(100% / 4 - 15px);
  background: #fff;
  padding: 15px 14px;
  border-radius: 12px;
  box-shadow: 0 5px 10px rgba(0,0,0,0.1);
}
.overview-boxes .box-topic{
  font-size: 20px;
  font-weight: 500;
}
.home-content .box .number{
  display: inline-block;
  font-size: 35px;
  margin-top: -6px;
  font-weight: 500;
}
.home-content .box .indicator{
  display: flex;
  align-items: center;
}
.home-content .box .indicator i{
  height: 20px;
  width: 20px;
  background: #8FDACB;
  line-height: 20px;
  text-align: center;
  border-radius: 50%;
  color: #fff;
  font-size: 20px;
  margin-right: 5px;
}
.box .indicator i.down{
  background: #e87d88;
}
.home-content .box .indicator .text{
  font-size: 12px;
}

.home-content .box .number{
  font-size: 24px;
}

.home-content .box .cart{
  display: inline-block;
  font-size: 32px;
  height: 50px;
  width: 50px;
  background: #cce5ff;
  line-height: 50px;
  text-align: center;
  color: #66b0ff;
  border-radius: 12px;
  margin: -15px 0 0 6px;
}
.home-content .box .cart.two{
   color: #2BD47D;
   background: #C0F2D8;
 }
.home-content .box .cart.three{
   color: #ffc233;
   background: #ffe8b3;
 }
.home-content .box .cart.four{
   color: #e05260;
   background: #f7d4d7;
 }
.home-content .total-order{
  font-size: 120px;
  font-weight: 500;
}
.home-content .sales-boxes{
  display: flex;
  justify-content: space-between;
  /* padding: 0 20px; */
}

/* left box */
.home-content .sales-boxes .recent-sales{
  width: 65%;
  background: #fff;
  padding: 20px 30px;
  margin: 0 20px;
  border-radius: 12px;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
}
.home-content .sales-boxes .sales-details{
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.sales-boxes .box .title{
  margin-left: 280px ;
  font-size: 24px;
  font-weight: 500;
  /* margin-bottom: 10px; */
}

.sales-boxes .box .title1{
  margin-left: 100px ;
  font-size: 24px;
  font-weight: 500;
  /* margin-bottom: 10px; */
}
.sales-boxes .sales-details li.topic{
  font-size: 20px;
  font-weight: 500;
}
.sales-boxes .sales-details li{
  list-style: none;
  margin: 8px 0;
}
.sales-boxes .sales-details li a{
  font-size: 18px;
  color: #333;
  font-size: 400;
  text-decoration: none;
}
.sales-boxes .box .button{
  width: 100%;
  display: flex;
  justify-content: flex-end;
}
.sales-boxes .box .button a{
  color: #fff;
  background: #0A2558;
  padding: 4px 12px;
  font-size: 15px;
  font-weight: 400;
  border-radius: 4px;
  text-decoration: none;
  transition: all 0.3s ease;
}
.sales-boxes .box .button a:hover{
  background:  #0d3073;
}

/* Right box */
.home-content .sales-boxes .top-sales{
  width: 35%;
  background: #fff;
  padding: 20px 30px;
  margin: 0 20px 0 0;
  border-radius: 12px;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
}
.sales-boxes .top-sales li{
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 10px 0;
}
.sales-boxes .top-sales li a img{
  height: 40px;
  width: 40px;
  object-fit: cover;
  border-radius: 12px;
  margin-right: 10px;
  background: #333;
}
.sales-boxes .top-sales li a{
  display: flex;
  align-items: center;
  text-decoration: none;
}
.sales-boxes .top-sales li .product,
.price{
  font-size: 17px;
  font-weight: 400;
  color: #333;
}


/* Responsive Media Query */
@media (max-width: 1240px) {
  .sidebar{
    width: 60px;
  }
  .sidebar.active{
    width: 220px;
  }
  .home-section{
    width: calc(100% - 60px);
    left: 60px;
  }
  .sidebar.active ~ .home-section{
    left: 220px;
    width: calc(100% - 220px);
    overflow: hidden;
  }
  .home-section nav{
    width: calc(100% - 60px);
    left: 60px;
  }
  .sidebar.active ~ .home-section nav{
    width: calc(100% - 220px);
    left: 220px;
  }
}
@media (max-width: 1150px) {
  .home-content .sales-boxes{
    flex-direction: column;
  }
  .home-content .sales-boxes .box{
    width: 100%;
    overflow-x: scroll;
    margin-bottom: 30px;
  }
  .home-content .sales-boxes .top-sales{
    margin: 0;
  }

}
@media (max-width: 1000px) {
  .overview-boxes .box{
    width: calc(100% / 2 - 15px);
    margin-bottom: 15px;
  }
}
@media (max-width: 700px) {
  nav .sidebar-button .dashboard,
  nav .profile-details .admin_name,
  nav .profile-details i{
    display: none;
  }
  .home-section nav .profile-details{
    height: 50px;
    min-width: 40px;
  }
  .home-content .sales-boxes .sales-details{
    width: 560px;
  }
  
  .home-content .overview-boxes .title {
    font-size: 224px;
    font-weight: 500;
  }
}
@media (max-width: 550px) {
  .overview-boxes .box{
    width: 100%;
    margin-bottom: 15px;
  }
  .sidebar.active ~ .home-section nav .profile-details{
    display: none;
  }
}
@media (max-width: 400px) {
  .sidebar{
    width: 0;
  }
  .sidebar.active{
    width: 60px;
  }
  .home-section{
    width: 100%;
    left: 0;
  }
  .sidebar.active ~ .home-section{
    left: 60px;
    width: calc(100% - 60px);
  }
  .home-section nav{
    width: 100%;
    left: 0;
  }
  .sidebar.active ~ .home-section nav{
    left: 60px;
    width: calc(100% - 60px);
  }
}

.form-group {
  margin-bottom: 20px;
  margin-top: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input[type="text"] {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

button {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #0d3073;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 0px;
  margin-left: 300px;
}

button:hover {
  background-color: #2862cc;
}

button2 {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #0d3073;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 0px;
  margin-left: 100px;
}

button2:hover {
  background-color: #2862cc;
}
label {
display: block;
margin-bottom: 5px;
}

select {
width: 100%;
padding: 10px;
font-size: 16px;
border-radius: 5px;
border: 1px solid #ccc;
}

button1 {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #0d3073;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 10px;
  margin-left: 150px;
}

button1:hover {
  background-color: #2862cc;
}
  </style>
  
