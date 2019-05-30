<template>  
  <div class="container">
    <el-col :span="6"><div class="grid-content">
      <div>
        <el-menu
            default-active="2"
            class="el-menu-vertical-demo"
            @open="handleOpen">
          <el-submenu index="1">
            <template slot="title">
              <span>数据</span>
            </template>
            <el-submenu v-for="item in allList.datalist" :index="item.index">
              <template slot="title"><span>{{item.setname}}</span></template>
              <el-menu-item v-for="file in item.file_list">
                <template slot="title"><span>{{file.filename}}</span></template>
              </el-menu-item>
            </el-submenu>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title">
              <span>模型</span>
            </template>
            <el-menu-item-group v-for="item in allList.modellist" :index="item.index">
              <template slot="title"><span>{{item.modelname}}</span></template>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>
      </div>
    </div></el-col>
    <el-col :span="12"><div class="grid-content">
      <span>xxyy</span>
    </div></el-col>
    <el-col :span="6"><div class="grid-content">
      <span>yyx</span>
    </div></el-col>
  </div>
</template>

<script>
  import draggable from "vuedraggable";
  var BASE_URL = "http://localhost:15050/api/";
  export default {
    data(){
      return {
        allList : [],
        userId: 4,

      }
    },
    mounted() {
      this.getList();
      },
    methods:{
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      },
      getList(){
        this.$http.get(BASE_URL + 'get_all?userid='+this.userId)
          .then((response) => {
            console.log(response.body);
            this.allList = response.body.DATA;
            console.log(this.allList.datalist);
          }, (response) => {
		        	console.log('请求失败了');
		        	alert("请求list失败，请刷新重试哦");
		        });
      },
    },
  };

</script>

<style>
  .container {
    margin-top: 10px;
    margin-left: 1%;
    margin-right: 1%;
    width: 97%;
    height: 700px;
    background: #FFFAFA;
  }
</style>
