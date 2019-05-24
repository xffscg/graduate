<template>  
  <div class="container">
  	<el-col :span="6"><div class="grid-content">
      <div class ="file">
        <div class="upload">
          <div class="icon_up">
            <i class="el-icon-folder-add"></i>
          </div>
          <div class="up_load_text">
            <!--<el-button type="primary" plain>上传数据集</el-button>-->
            <el-button type="primary" plain @click="dialogVisible2 = true"><span class="glyphicon glyphicon-upload"></span>上传文件</el-button>
            <el-dialog :visible.sync="dialogVisible2" title="上传文件">
              <el-form :model="fileInfo" label-width="140px">
                <el-form-item label="数据集名称">
                  <el-select
                    v-model="fileInfo.name" filterable  allow-create  default-first-option
                    placeholder="请选择数据集">
                    <el-option
                      v-for="item in set_option"
                      :key="item"
                      :label="item"
                      :value="item">
                    </el-option>
                  </el-select>
                </el-form-item>
                <el-form-item label="第一行有效">
                  <el-switch
										  style="display: inline;"
										  v-model="fileInfo.firstLine"
										  active-color="#13ce66"
										  inactive-color="#ff4949"
										  active-text="有列头（无效）"
										  inactive-text="无列头（有效）">
										</el-switch>
                </el-form-item>
                <el-form-item label="分隔符">
										<el-input v-model="fileInfo.separate"></el-input>
									</el-form-item>
                <el-form-item label="选择文件">
										<input type="file" name="myfiles" id="fileload" multiple>
									</el-form-item >
              </el-form>
              <span slot="footer" class="dialog-footer">
									<el-button @click="dialogVisible2 = false">取 消</el-button>
									<el-button id="submit1" type="primary" @click="submitFileInfor">确 定</el-button>
								</span>
            </el-dialog>
          </div>
        </div>
      </div>
    </div></el-col>
    <el-col :span="18"><div class="grid-content">
      <p>xxxxxx</p>
    </div></el-col>
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
        dialogVisible2:false,
        fileInfo:{
          name:'',
          firstLine:true,
          separate:''
        },
        set_option:['xff','scg'],
        userId: 4,

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
      },
      handleClose(done) {
				this.$confirm('确认关闭？')
				.then(_ => {
					done();
				})
				.catch(_ => {});
			},
      submitFileInfor: function(){
				var obj ={}
				obj.fileAddr = $('#fileload').val();
				obj.filename = $('#fileload').attr('name');
				obj.fileID = $('#fileload').attr('id');
				if(obj.fileAddr == "" || obj.fileAddr == null){
					alert('请选择文件')
				}
				var FL= '';
				if(this.fileInfo.firstLine == true){
					FL = '1';
				}else{
					FL = '0';
				}
				if(this.fileInfo.name == ''  || this.fileInfo.separate == ''){
					alert('文件名称或者分隔符不能为空');
				}else{
					var formData = new FormData();
					formData.append('file',$('#fileload')[0].files[0]);
					formData.append('name',this.fileInfo.name);
					formData.append('firstLine',FL);
					formData.append('separate',this.fileInfo.separate);
					formData.append('userId',this.userId);
					console.log(formData.get('file'));
					var that = this;
					$.ajax({
						url:BASE_URL +'uploadDataFile',
						type:'POST',
						data:formData,
						processData:false,
						contentType:false
					})

					.done(function(data){
						that.dialogVisible2 = false;
					})
					.fail(function(res){console.log(res);});
					this.$nextTick(() => {
						this.dialogVisible2 =false;
					})
				}
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
  .file {
    width: 98%;
    height: 100%;
    padding-top: 10px;
    text-align: center;
    font-size: 18px;
  }
  .upload {
    width: 98%;
    height: 50px;
    margin-top: 10px;
    margin-left: 30px;
  }
  .icon_up {
    float: left;
    font-size: 30px;
    padding-top: 5px;
  }
  .up_load_text {
    float: left;
    margin-left: 20px;
  }
  
</style>
