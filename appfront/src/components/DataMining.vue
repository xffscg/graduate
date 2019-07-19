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
  		<router-link :class="$route.path == '/DataMining/DataSet'?'active':'item'" to="/DataMining/DataSet">Data Set</router-link>
  		<router-link :class="$route.path == '/DataMining/Mining'?'active':'item'" to="/DataMining/Mining">Data Mining</router-link>
  		<router-link :class="$route.path == '/DataMining/ModelList'?'active':'item'" to="/DataMining/ModelList">Model List</router-link>
  		<router-link :class="$route.path == '/DataMining/ResultList'?'active':'item'" to="/DataMining/ResultList">Result List</router-link>
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
      let session = window.sessionStorage;
      if(!session.getItem("userId")){
        alert("请先登陆！");
        this.$router.push({path:'/'});
      }else{
        this.userId = session.getItem("userId");
      }

    },
    mounted() {
      },
    methods:{
      logout(){
        let session = window.sessionStorage;
        session.removeItem('userId');
        this.$router.push({path:'/'});
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
    margin: 15px;
    font-size: 20px;
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
    display: flex;
    justify-content: flex-start;
  	height: 40px;
  	width: 100%;
  	background: #DEF3F9;
    overflow: hidden;

  }
  .item {
    font-size: 20px;
  	height: 40px;
  	width: 25%;
  	padding-top: 10px;
  	text-align: center;
    vertical-align: middle;
  }
  .active {
    font-size: 20px;
  	height: 40px;
  	width: 25%;
  	padding-top: 10px;
  	text-align: center;
    vertical-align: middle;
    background: #9FF0E2;
  }
  a{
  	text-decoration: none;
  }
</style>
