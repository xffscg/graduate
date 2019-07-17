<template>  
  <div>
    <div class="header">
      <span class="mainMenu">
        数据挖掘可视化平台
      </span>
      <div class="login">
        <span class="loginS" @click="showR">注册</span>
        <span> | </span>
        <span class="loginS"> 登陆</span>
      </div>
      <div v-if="showLogin" class="loginPart"></div>
    </div>
    <div id="forPop"></div>
    <div v-if="showRegister" class="registerPart">
      <h1>注册</h1>
      <form v-model="registerInfo">
        <label for="userN">用户名:&nbsp&nbsp&nbsp&nbsp&nbsp</label>
        <input id="userN" type="text" placeholder="请输入10位字符以内的用户名"></input><br>
        <label for="pw">密码:&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</label>
        <input id="pw" type="text" placeholder="请输入由数字大写字母和小写字母组成的密码"></input><br>
        <label for="pw">确认密码：</label>
        <input id="pwa" type="text" placeholder="请确认密码"></input><br>
        <p id="registerError"></p>
        <input type="submit"></input>
      </form>
    </div>
  	<div class="menuList">
  		<div class="item"><router-link to="/DataSet">Data Set</router-link></div>
  		<div class="item"><router-link to="/Mining">Data Mining</router-link></div>
  		<div class="item"><router-link to="/ModelList">Model List</router-link></div>
  		<div class="item"><router-link to="/ResultList">Result List</router-link></div>
  	</div>
    <div class="app-content">
      <keep-alive>
        <router-view></router-view>
      </keep-alive>
    </div>
  </div>
</template>

<script>
  export default {
    data(){
      return {
        showRegister : false,
        showLogin : false,
        registerInfo : [],
      }
    },
    mounted() {
      },
    methods:{
      showR(){
        //document.getElementById("forPop).style.display = "block"
        $('#forPop').css("display", "block");
        this.showRegister = true;
      }
      // registerUser(){
      //
      // };
    },
    watch: {
		}
  };

</script>

<style>
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
  input[type="text"]:focus{
    border: #87CEFF 2px solid;
  }
  input[type="submit"]:hover{
    background: #3875d7;
    font-size: 120%;
  }
  .header {
    background: #038CB5;
  	padding-top: 20px;
    height: 60px;
    width: 100%;
    position :sticky;
    vertical-align: middle;
    color: #F0F0F0;
  }
  .mainMenu {
    float: left;
    width: 60%;
    text-align:right;
    font-size: 25px;
  }
  .login {
    float: right;
    width: 15%;
    text-align:center;
    font-size: 18px;
  }
  .loginS:hover {
    color: #bbccdd;
    font-size: 120%;
    cursor: pointer;
  }
  .loginS:active {
    color: #00FA9A;
  }
  #forPop {
    width: 100%;
    height: 100%;
    top:0px;
    left:0px;
    position:absolute;
    /*因为IE不支持opacity 所以用filter 为了兼容两个都写*/
    filter: Alpha(opacity=60);
    opacity:0.6;
    background:#000000;
    display:none;
  }
  .registerPart {
    background-color: #d6d6d6;
    width: 500px;
    height: 400px;
    border: #888888 2px solid;
    position: fixed;
    left: 50%;
    top: 50%;
    margin-top: -200px;
    margin-left: -250px;
  }
  .menuList {
  	height: 40px;
  	width: 100%;
  	background: #DEF3F9;
    overflow: hidden;

  }
  .item {
    font-size: 20px;
  	float: left;
  	height: 35px;
  	width: 25%;
  	padding-top: 10px;
  	text-align: center;
    vertical-align: middle;
  }
  a{
  	text-decoration: none;
  }
</style>
