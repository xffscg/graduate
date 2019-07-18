<template>  
  <div>
    <div class="header">
      <span class="mainMenu">
        数据挖掘可视化平台
      </span>
      <div class="logout">
        <span class="logoutS" @click="logout">登出</span>
      </div>
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
  let BASE_URL = "http://localhost:15050/api/";
  export default {
    name : "DataMining.vue",
    data(){
      return {
        userId : null,
      }
    },
    created(){

    },
    mounted() {
      },
    methods:{
      logout(){
        let session = window.sessionStorage;
        session.removeItem('userId');
        // this.$router.push({path:'/'});
      }
    },
    watch: {
		},
  };

</script>

<style>
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
  .logout {
    float: right;
  }
  .logoutS:hover {
    color: #bbccdd;
    font-size: 120%;
    cursor: pointer;
  }
  .logoutS:active {
    color: #00FA9A;
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
