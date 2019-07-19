<template>  
  <div class="container">
    <div class="left">
      <div class="upload">
        <i class="el-icon-folder-add"></i>
        <span>&nbsp;&nbsp;&nbsp;上传文件</span>
      </div>
      <div class="file_list"></div>
    </div>
    <div class="right">yyy</div>
    <div class="center">rr</div>
  </div>
</template>

<script>
  var BASE_URL = "http://localhost:15050/api/";
  export default {
    data(){
      return {
        dataList : [],
        dialogVisible2:false,
        fileInfo:{
          name:'',
          firstLine:true,
          separate:'',
          fileType:'',
        },
        set_option:[],
        fileOptions:['csv', 'txt'],
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
        this.$http.get(BASE_URL + 'get_file_list?userid='+this.userId)
          .then((response) => {
            console.log(response.body);
            this.dataList = response.body.DATA;
            var i;
            for(i in this.dataList){
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
						url:BASE_URL +'uploadDataFile',
						type:'POST',
						data:formData,
						processData:false,
						contentType:false
					})
					.done(function(data){
						that.dialogVisible2 = false;
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
