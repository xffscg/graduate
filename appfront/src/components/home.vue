<template>
  <div><div class="home">
    <div id="forPop"></div>
    <div class="login">
      <span class="loginS" @click="showR">注册</span>
      <span> | </span>
      <span class="loginS" @click="showL"> 登陆</span>
    </div>
    <div v-if="showRegister" class="registerPart">
      <div id="closeR" class="close" @click="close">x</div>
      <h1>注册</h1>
      <form v-model="registerInfo">
        <label for="userN">用户名:&nbsp&nbsp&nbsp&nbsp&nbsp</label>
        <input id="userN" type="text" v-model="registerInfo.userName" placeholder="请输入20位字符以内的用户名" required></input><br>
        <label for="pw">密码:&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</label>
        <input id="pw" type="text" v-model="registerInfo.password" placeholder="请输入小于20为由数字、大写字母和小写字母组成的密码" required></input><br>
        <label for="pw">确认密码：</label>
        <input id="pwa" type="text" v-model="registerInfo.passwordAgain" placeholder="请确认密码" required></input><br>
        <p style="color: red" id="registerError"></p>
        <div style="display: inline; margin-left: 20px;">
          <input type="submit" @click="goRegister"></input>
          <input id="cancelR" type="button" value="取消" @click="close"></input>
        </div>
      </form>
    </div>
    <div v-if="showLogin" class="registerPart">
      <div id="closeL" class="close" @click="close">x</div>
      <h1>登陆</h1>
      <form v-model="loginInfo">
        <label for="userLoginN">用户名:&nbsp&nbsp&nbsp&nbsp&nbsp</label>
        <input id="userLoginN" type="text" v-model="loginInfo.userName" placeholder="请输入20位字符以内的用户名"></input><br>
        <label for="pwLogin">密码:&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</label>
        <input id="pwLogin" type="text" v-model="loginInfo.password" placeholder="请输入小于20为由数字、大写字母和小写字母组成的密码"></input><br>
        <p style="color: red" id="loginError"></p>
        <div style="display: inline; margin-left: 20px;">
          <input type="submit" @click="goLogin"></input>
          <input id="cancelL" type="button" value="取消" @click="close"></input>
        </div>
      </form>
    </div>
  </div></div>
    
</template>

<script>
    let BASE_URL = "http://localhost:15050/api/";
    export default {
        name: "home.vue",
         data(){
          return {
            showRegister : false,
            showLogin : false,
            userId : null,
            registerInfo : {
              userName: '',
              password: '',
              passwordAgain: ''
            },
            loginInfo : {
              userName: '',
              password: ''
            },
          }
        },
      methods:{
        showR(){
          //document.getElementById("forPop).style.display = "block"
          $('#forPop').css("display", "block");
          this.showRegister = true;
        },
        showL(){
          //document.getElementById("forPop).style.display = "block"
          $('#forPop').css("display", "block");
          this.showLogin = true;
        },
        close(){
          if($(event.target)[0].id == "closeR" || $(event.target)[0].id == "cancelR"){
            this.showRegister = false;
          }else{
            this.showLogin = false;
          }
        },
        goRegister(){
          let errorInfo = document.getElementById("registerError");
          errorInfo.innerText = "";
          if(this.registerInfo.userName == null || this.registerInfo.userName == "" || this.registerInfo.password == null || this.registerInfo.password == ""){
            errorInfo.innerText = "用户名或密码不能为空";
          }else if(this.registerInfo.userName.length > 20 || this.registerInfo.password.length > 20){
            errorInfo.innerText = "用户名或密码不能超过20个字符";
          }else if(!((/[a-z]/g).test(this.registerInfo.password) && (/[A-Z]/g).test(this.registerInfo.password) && (/[1-9]/g).test(this.registerInfo.password))){
            errorInfo.innerText = "密码需要包含数字、大写字母和小写字母";
          }else if(this.registerInfo.password != this.registerInfo.passwordAgain){
            errorInfo.innerText = "两次输入密码不一致";
          }else{
            let that = this;
            this.$http.get(BASE_URL + 'user_register?username='+this.registerInfo.userName+'&password='+this.registerInfo.password)
            .then((response) => {
              console.log(response);
              if(response.body.status == "success"){
                that.showRegister = false;
                $('#forPop').css("display", "none");
                alert("注册成功");
              }else{
                errorInfo.innerText = response.body.error;
              }
            }, (response) => {
                console.log('请求失败了');
                alert("注册失败，请刷新重试哦");
              });
          }
        },
        goLogin(){
          let errorInfo = document.getElementById("loginError");
          errorInfo.innerText = "";
          if(this.loginInfo.userName == null || this.loginInfo.userName == "" || this.loginInfo.password == null || this.loginInfo.password == ""){
            errorInfo.innerText = "用户名或密码不能为空";
          }else if(this.loginInfo.userName.length > 20 || this.loginInfo.password.length > 20){
            errorInfo.innerText = "用户名或密码不能超过20个字符";
          }else{
            let that = this;
            this.$http.get(BASE_URL + 'user_login?username='+this.loginInfo.userName+'&password='+this.loginInfo.password)
            .then((response) => {
              console.log(response);
              if(response.body.status == "success"){
                that.userId = response.body.userId;
                that.showLogin = false;
                $('#forPop').css("display", "none");
                let session = window.sessionStorage;
                session.setItem('userId',response.body.userId);
                alert("登陆成功");
                this.$router.push({path:'/DataMining'});
              }else{
                errorInfo.innerText = response.body.error;
              }
            }, (response) => {
                console.log('请求失败了');
                alert("登陆失败，请刷新重试哦");
              });
          }
        },
      },
    }
</script>

<style scoped>
  input[type="text"]{
    width: 280px;
    height: 50px;
    border: #888888 1px solid;
    border-radius: 7px;
    margin: 10px;
  }
  input[type="submit"]{
    background: #409EFF;
    width: 150px;
    height: 50px;
    border: #AEEEEE 1px solid;
    border-radius: 20px;
    margin: 10px;
    font-size: 15px;
  }
  input[type="button"]{
    background: none;
    width: 150px;
    height: 50px;
    margin: 10px;
    border: none;
    font-size: 15px;
  }
  input[type="text"]:focus{
    border: #87CEFF 2px solid;
  }
  input[type="submit"]:hover{
    background: #3875d7;
    font-size: 120%;
  }
  input[type="button"]:hover{
    font-size: 120%;
  }
  .home {
    width: 100%;
    height: 700px;
    background-image: url("../assets/18.jpg");
    background-repeat: no-repeat;
    background-position:center;
  }
  .login {
    width: 200px;
    height: 100px;
    border: ridge #D1EEEE 5px;
    position: absolute;
    left: 45%;
    top: 60%;
    color: #bbccdd;
    font-size: 35px;
    padding-top: 40px;
    animation-name: breath;
    animation-duration: 2s;
    animation-delay: 1s;
    animation-iteration-count: 10;
    -webkit-animation-name: breath;
    -webkit-animation-duration: 3s;
    -webkit-animation-delay: 1s;
    -webkit-animation-iteration-count: 10;
  }
  .loginS:hover {
    color: #FFF5EE;
    font-size: 120%;
    cursor: pointer;
  }
  .loginS:active {
    color: #00FA9A;
  }
   #forPop {
    width: 100%;
    height: 100%;
    top:0;
    left:0;
    position:absolute;
    /*因为IE不支持opacity 所以用filter 为了兼容两个都写*/
    filter: Alpha(opacity=60);
    opacity:0.6;
    background:#000000;
    display:none;
  }
  .registerPart {
    background-color: #D4EAF3;
    width: 500px;
    height: 500px;
    border: #888888 2px solid;
    position: fixed;
    left: 50%;
    top: 50%;
    margin-top: -200px;
    margin-left: -250px;
  }
  .close {
    width: 30px;
    height: 30px;
    background: #D0D6D9;
    color: black;
    position: absolute;
    top: 0;
    right: 0;
    padding: 5px;
    font-size: 25px;
  }
  .close:hover {
    background: #BDC3C5;
    width: 35px;
    height: 35px;
  }

  .close:active {
    background: #BDC3C5;
    width: 30px;
    height: 30px;
  }
  @keyframes breath {
    from {border: ridge #052DB3 7px;}
    to {border: ridge #D1EEEE 5px;}
  }
  @-webkit-keyframes breath {
    from {border: ridge #052DB3 7px;}
    to {border: ridge #D1EEEE 5px;}
  }

</style>
