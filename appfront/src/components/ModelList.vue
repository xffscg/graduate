<template>  
  <div class="container">
    <div class="Ttitle">
      任务列表
    </div>
    <div class="Ltable">
      <el-table :data="model_list.slice((currentPage-1)*pagesize,currentPage*pagesize)" ref="multipleTable" style="width: 100%;table-layout:fixed;"  @selection-change="handleSelectionChange">

        <el-table-column
          type="selection" :reserve-selection="true">
        </el-table-column>
        <el-table-column
          prop="jobId"
          label="模型ID"
          width="80">
        </el-table-column>
        <el-table-column
                prop="modelname"
                label="模型名称">
        </el-table-column>
        <el-table-column
                prop="algoname"
                label="算法名称">
        </el-table-column>
        <el-table-column
                prop="datasetname"
                label="数据集名称">
        </el-table-column>
        <el-table-column
            prop="modelpath"
            label="模型路径"
        >
        </el-table-column>
        <el-table-column
            prop="createdon"
            label="构建时间"
        >
        </el-table-column>
        <el-table-column
            prop="time"
            label="运行时间"
        >
        </el-table-column>
        <el-table-column
            prop="status"
            label="保存状态"
        >
        </el-table-column>
        <el-table-colum
            label="模型结果"
        >
        </el-table-colum>
        <!-- <el-table-column label="操作" >
            <template scope="scope">
                <el-button type="primary"
                    plain
                    @click="open3">
                    下载
                </el-button>
            </template>
        </el-table-column> -->
  </el-table>
    </div>
  </div>
</template>

<script>
  var BASE_URL = "http://localhost:15050/api/";
  export default {
    data(){
      return {
        Mlist:[{
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
        model_list:[],
        user_id : 4,
        pagesize:6,
        currentPage:1,
      }
    },
    mounted() {
         this.get_model_list();
      },
    methods:{
      out(){
        console.log(this.Rlist[2].path);
      },
      get_model_list(){
        this.$http.get(BASE_URL + 'model_list?userid=' + this.user_id)
          .then((response) => {
            this.model_list = response.body.DATA;
            console.log(this.model_list);
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
