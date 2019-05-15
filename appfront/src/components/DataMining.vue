<template>  
  <div>
  	<div class="mainMenu">
  	  数据挖掘可视化平台
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

</script>

<style>
  .mainMenu {
  	padding-top: 20px;
    background: #038CB5;
    height: 60px;
    width: 100%;
    text-align:center;
    vertical-align: middle;
    color: #F0F0F0;
    font-size: 25px;
  }
  .menuList {
  	height: 40px;
  	width: 100%;
  	background: #DEF3F9;

  }
  .item {
    font-size: 20px;
  	float: left;
  	height: 35px;
  	width: 25%;
  	padding-top: 10px;
  	text-align: center;
  }
  a{
  	text-decoration: none;
  }
</style>
