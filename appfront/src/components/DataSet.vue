<template>  
  <div class="container">
  	<div class="Ttitle">
	    数据集列表
	  </div>
    <div class="Ltable">
      <el-table :data="tabelData">
        <el-table-column label="id"></el-table-column>
      </el-table>
    </div>
    <div>
      <el-button type="primary">主要按钮bababab</el-button>
      <button @click="demo">try</button>
    </div>
  </div>
</template>

<script>
  var BASE_URL = "http://localhost:15050/api/";
  export default {
    data(){
      return {
        tabelData:[{
          id: 8
        }],
        dataList : [],
        target: 7,
        array:[[1, 2, 8, 9],[2, 4, 9, 12],[4, 7, 10, 13],[6, 8, 11, 15]],

      }
    },
    methods:{
      getList(){
        this.$http.get(BASE_URL + 'get_file_list')
          .then((response) => {
            console.log(response.body);
            this.dataList = response.body.DATA;
          }, (response) => {
		        	console.log('请求失败了');
		        	alert("请求list失败，请刷新重试哦");
		        });
        // var res = get_file_list();
      },

      demo(){
        this.getList();
        var num = this.target;
        var old = this.array;
        var res = this.find(num, old);
        console.log(res);

        
      },

      find(target, array){
          // write code here
          var m = array.length -1;
          var n = array[0].length -1;
          console.log(m);
          console.log(n);
          var res = false;
          while((m >=0) && (n >=0)){
              if(array[m][n] < target){
                  res = false;
                  break;
              }else if(array[m][n] == target){
                  res = true;
                  break;
              }else{
                  if((array[m-1][n] == target) || (array[m][n-1] == target)){
                      res = true;
                      break;
                  }else{
                      if(array[m-1][n] > target){
                          m = m -1;
                      }
                      if(array[m][n-1] > target){
                          n = n -1;
                      }
                  }
              }
          }
          return res;
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
    height: 500px;
    padding-top: 10px;
  }
  
</style>
