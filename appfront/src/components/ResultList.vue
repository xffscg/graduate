<template>  
  <div class="container">
    <div class="Ttitle">
      任务列表
    </div>
    <div class="Ltable">
      <el-table :data="res_list.slice((currentPage-1)*pagesize,currentPage*pagesize)" style="width: 100% ;table-layout:fixed;" >
        <el-table-column prop="jobId" label="任务id">
        </el-table-column>
        <el-table-column prop="filename" label="文件名称">
        </el-table-column>
        <el-table-column prop="path" label="保存路径">
        </el-table-column>
        <el-table-column prop="createdon" label="创建时间">
        </el-table-column>
        <el-table-column label="操作">
          <template>
            <el-button type = "primary" @click="out">查看</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
  var BASE_URL = "http://localhost:15050/api/";
  export default {
    data(){
      return {
        Rlist:[{
          id: 8,
          name: 'file1',
          path: 'd:2',
          time: '17:30'
        },{
          id: 4,
          name: 'file2',
          path: 'd:2',
          time: '17:30'
        },{
          id: 2,
          name: 'file3',
          path: 'd:3',
          time: '17:30'
        },{
          id: 1,
          name: 'file4',
          path: 'd:4',
          time: '17:30'
        }],
        res_list:[],
        user_id : 4,
        pagesize:6,
        currentPage:1,
      }
    },
    mounted() {
         this.get_res_list();
      },
    methods:{
      out(){
        console.log(this.Rlist[2].path);
      },
      get_res_list(){
        this.$http.get(BASE_URL + 'result_list?userid=' + this.user_id)
          .then((response) => {
            this.res_list = response.body.DATA;
            console.log(this.res_list);
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
    height: 100%;
    background: #FFFAFA;
  }
  .container .Ttitle {
    width: 100%;
    height: 40px;
    padding-top: 10px;
    text-align: center;
    font-size: 18px;
  }
  .container .Ltable {
    width: 100%;
    height: 100%;
    padding-top: 10px;
  }
</style>
