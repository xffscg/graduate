<template>  
  <div class="container">
    <div class="Ttitle">
      任务列表
    </div>
    <div class="Ltable">
      <el-table :data="Mlist" style="width: 100%;">
        <el-table-column prop="id" label="任务id" width = "180"> 
        </el-table-column>
        <el-table-column prop="name" label="文件名称" width = "180">
        </el-table-column>
        <el-table-column prop="path" label="保存路径" width = "180">
        </el-table-column>
        <el-table-column prop="time" label="创建时间" width = "180">
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
        }]
      }
    },
    methods:{
      out(){
        console.log(this.Rlist[2].path);
      }
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