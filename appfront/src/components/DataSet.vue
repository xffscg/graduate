<template>  
  <div class="container">
    <div class="left">
      <div class="upload" @click="showUpload = true">
        <i class="el-icon-folder-add"></i>
        <span>&nbsp;&nbsp;&nbsp;上传文件</span>
      </div>
      <div class="file_list">
          <h3 style="padding-right: 20px;">文件列表</h3>
          <el-menu
            default-active="2"
            class="el-menu-vertical-demo">
            <el-submenu v-for="item in dataList" :index="item.index" :key="item.setname">
              <template slot="title">
                <span>{{item.setname}}</span>
              </template>
              <el-menu-item v-for="file in item.subFile" :key="file.id">
                <template slot="title"><span>{{file.fileName}}</span></template>
              </el-menu-item>
            </el-submenu>
          </el-menu>
        </div>
    </div>
    <div class="right">yyy</div>
    <div class="center">rr</div>
    <el-dialog :visible.sync="showUpload" title="上传文件"
      @close="handleClose"  >
        <el-form :model="fileInfo" label-width="140px">
          <el-form-item label="数据集名称">
            <el-select
              v-model="fileInfo.name" filterable  allow-create  default-first-option
              placeholder="请选择数据集">
              <el-option
                v-for="item in set_option"
                :label="item"
                :value="item" :key="item">
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
              <input type="file" name="myfiles" id="fileload">
            </el-form-item >
          <el-form-item label="文件类型">
              <el-select v-model="fileInfo.fileType" placeholder="请选择">
              <el-option
                v-for="item in fileOptions"
                :key="item"
                :label="item"
                :value="item">
              </el-option>
            </el-select>
            </el-form-item >
        </el-form>
        <span slot="footer" class="dialog-footer">
            <el-button id="submit1" type="primary" @click="submitFileInfor">确 定</el-button>
            <el-button @click="showUpload = false">取 消</el-button>
          </span>
      </el-dialog>
  </div>
</template>

<script>
  var BASE_URL = "http://localhost:15050/api/";
  export default {
    data(){
      return {
        dataList : [],
        showUpload:false,
        fileInfo:{
          name:'',
          firstLine:0,
          separate:'',
          fileType:'',
        },
        set_option:[],
        fileOptions:['csv', 'txt'],
        userId: null,
      }
    },
    mounted() {
        let session = window.sessionStorage;
        this.userId =  session.getItem('userId');
        this.getList();
     },
    methods:{
      getList(){
        this.$http.get(BASE_URL + 'data/get_file_list?userid='+this.userId)
          .then((response) => {
            console.log(response.body);
            this.dataList = response.body.DATA;
            this.set_option = [];
            for(let i in this.dataList){
              this.set_option.push(this.dataList[i].setname);
            }
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
				if(this.fileInfo.name == ''  || this.fileInfo.separate == '' || this.fileInfo.fileType == ''){
					alert('文件名称、分隔符或者文件类型不能为空');
				}else{
					var formData = new FormData();
					formData.append('file',$('#fileload')[0].files[0]);
					console.log($('#fileload')[0]);
					formData.append('name',this.fileInfo.name);
					formData.append('firstLine',FL);
					formData.append('separate',this.fileInfo.separate);
					formData.append('userId',this.userId);
					console.log(formData.get('file'));
					var that = this;
					$.ajax({
						url:BASE_URL +'data/uploadDataFile',
						type:'POST',
						data:formData,
						processData:false,
						contentType:false
					})
					.done(function(data){
						that.showUpload = false;
						that.getList();
					})
					.fail(function(res){console.log(res);});
					this.$nextTick(() => {
						this.dialogVisible2 =false;
					})
				}
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
  .left {
    float: left;
    width: 25%;
    height: 100%;
    border-right: #DBDBDB solid 1px;
  }
  .center {
    margin-left: 22%;
    margin-right: 22%;
    height: 100%;
  }
  .right {
    float: right;
    width: 25%;
    height: 100%;
    border-left: #DBDBDB solid 1px;
  }
  .upload {
    padding: 6px 6px;
    width: 50%;
    height: 50px;
    margin: 50px 15%;
    font-size: 20px;
    border: #c4dce8 1px solid;
    border-radius: 5px;
    vertical-align: middle;
    background: #94D2F2;
    line-height: 50px;
  }
  .upload:hover{
    background: #5897fb;
    font-size: 120%;
  }
  .file_list{
    margin-top: 20px;
    margin-left: 10px;
  }

</style>
