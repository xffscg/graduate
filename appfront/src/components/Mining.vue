<template>  
  <div class="container">
    <div class="left1">
      <h3>列表区</h3>
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
            <draggable  v-model="item.subFile" v-bind="{group:{name:'data', pull:'clone', put:false }}" @start="isDragging=true" @end="isDragging=false">
              <li v-for="file in item.subFile" :key="item.id">
                <div class="eachlist data">
                  <span>{{file.fileName}}</span>
                </div>
              </li>
            </draggable>
          </el-submenu>
        </el-submenu>
        <el-submenu index="2">
          <template slot="title">
            <span>算法</span>
          </template>
          <el-submenu v-for="item in allList.alglist" :index="item.index">
            <template slot="title"><span>{{item.Name}}</span></template>
            <draggable  v-model="item.subFile" v-bind="{group:{name:'alg', pull:'clone', put:false }}" @start="isDragging=true" @end="isDragging=false">
              <li class="list-group-item" v-for="file in item.subFile" :key="item.id">
                <div class="eachlist alg">
                  <span>{{file.fileName}}</span>
                </div>
              </li>
            </draggable>
          </el-submenu>
        </el-submenu>
        <el-submenu index="3">
          <template slot="title">
            <span>模型</span>
          </template>
          <draggable  v-model="allList.modellist" v-bind="{group:{name:'model', pull:'clone', put:false }}" @start="isDragging=true" @end="isDragging=false">
            <li v-for="item in allList.modellist" :key="item.jobId">
              <div class="eachlist model">
                <span>{{item.modelname}}</span>
              </div>
            </li>
          </draggable>
        </el-submenu>
      </el-menu>
    </div>
    <div class="right1">
      <h3>配置区</h3>
    </div>
    <div class="center1">
      <div class="newJob" @click="showCreate = true">
        <i class="el-icon-plus"></i>
        <span>&nbsp;&nbsp;&nbsp;新建任务</span>
      </div>
      <h3>工作区</h3>
      <div class="work">
        <div style="height: 100px; width: 90%; margin: 5% 5%">
          <div class="tagEach data">数据</div>
          <draggable v-model="jobList.data" v-bind="{group:{name:'data'}}" class="listBox">
            <transition-group>
              <li class="list-group" v-for="ele in jobList.data" :key="ele.id">
                <div class="groupEach data" id="dataBox" @click="getDetail">{{ele.fileName}}
                </div>
              </li>
            </transition-group>
          </draggable>
          <div class="deleteSpace"><i class="el-icon-delete" style="font-size: 30px; color: #5897fb" id="delData" @click="deleteList"></i></div>
        </div>
        <div style="height: 100px; width: 90%; margin: 5% 5%">
          <div class="tagEach alg">算法</div>
          <draggable v-model="jobList.alg" v-bind="{group:{name:'alg'}}" class="listBox">
            <transition-group>
              <li class="list-group" v-for="ele in jobList.alg" :key="ele.id" :id="ele.type+ele.id">
                <div class="groupEach alg" id="algBox" @click="getDetail">
                  <span>{{ele.fileName}}</span>
                </div>
              </li>
            </transition-group>
          </draggable>
          <div class="deleteSpace"><i class="el-icon-delete" style="font-size: 30px; color: #5897fb" id="delAlg" @click="deleteList"></i></div>
        </div>
        <div style="height: 100px; width: 90%; margin: 5% 5%">
          <div class="tagEach model">模型</div>
          <draggable v-model="jobList.model" v-bind="{group:{name:'model'}}" class="listBox">
            <transition-group>
              <li class="list-group" v-for="ele in jobList.model" :key="ele.id" :id="ele.type+ele.id">
                <div class="groupEach model" id="modelBox" @click="getDetail">
                  <span>{{ele.fileName}}</span>
                </div>
              </li>
            </transition-group>
          </draggable>
          <div class="deleteSpace"><i class="el-icon-delete" style="font-size: 30px; color: #5897fb" id="delModel" @click="deleteList"></i></div>
        </div>
        <button class="submitButton" type="button" @click="goRun">运行</button>
      </div>
    </div>
    <el-dialog :visible.sync="showCreate" title="新建任务">
      <el-form :model="jobInfo" label-width="140px">
        <el-form-item label="任务名称">
          <el-input v-model="jobInfo.jobName"></el-input>
        </el-form-item>
        <el-form-item label="任务类型">
            <el-switch
                style="display: inline;"
                v-model="jobInfo.jobType"
                active-color="#13ce66"
                inactive-color="#ff4949"
                active-text="训练"
                inactive-text="预测">
              </el-switch>
          </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
          <el-button type="primary" @click="newJob">确 定</el-button>
          <el-button @click="showCreate = false">取 消</el-button>
        </span>
    </el-dialog>
  </div>
</template>

<script>
  import draggable from "vuedraggable";
  var BASE_URL = "http://localhost:15050/api/";
  export default {
    components: {
			draggable,
		},
    data(){
      return {
        allList : [],
        userId: null,
        jobInfo: {
          jobId : null,
          jobName : "",
          jobType : 0,
        },
        showCreate : false,
        isDragging: false,
        delayedDragging: false,
        jobList :{
          data:[],
          model:[],
          alg:[]
        }
      }
    },
    mounted() {
      let session = window.sessionStorage;
      this.userId =  session.getItem('userId');
      this.getList();
      },
    methods:{
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      },
      end(evt){
        console.log(evt.to);
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
      getDetail(ev, type){
        if(type === undefined){
          if($(event.target)[0].id == "dataBox"){
            console.log("data");
          }else if($(event.target)[0].id == "algBox"){
            console.log("alg");
          }else if($(event.target)[0].id == "modelBox"){
            console.log("model");
          }
        }else{
          console.log(type + "lll");
        }
      },
      newJob(){
        if(this.jobInfo.jobName == ""){
          alert("任务名不能为空")
        }else{
          if(this.jobInfo.jobType == true){
            //1是训练
            this.jobInfo.jobType = 1;
          }else{
            this.jobInfo.jobType = 0;
          }
          this.$http.get(BASE_URL + 'new_job?userid='+this.userId + "&jobname=" + this.jobInfo.jobName
          + "&jobtype=" + this.jobInfo.jobType)
            .then((response) => {
              console.log(response.body);
              this.jobInfo.jobId = response.body.jobId
              let session = window.sessionStorage;
              session.setItem('jobId',response.body.jobId);
              this.showCreate = false;
            }, (response) => {
                console.log('请求失败了');
                alert("新建任务失败，请刷新重试哦");
              });
        }
      },
      deleteList(){
        var targetId = $(event.target)[0].id;
        console.log(targetId);
        if(targetId == 'delData'){
          this.jobList.data = [];
        }else if(targetId == 'delAlg'){
          this.jobList.alg = [];
        }else if(targetId == 'delModel'){
          this.jobList.model = [];
        }
      },
      goRun(){}
    },
    watch: {
			isDragging(newValue) {
				if (newValue) {
					console.log(this.isDragging);
					console.log(this.jobList);
					this.delayedDragging = true;
					return;
				}
				this.$nextTick(() => {
					this.delayedDragging = false;
				});
			},
      "jobList.data":{
			  handler(curVal, oldVal){
			    if(curVal.length == 0 && oldVal.length == 1){
			      console.log("iii")
          }else if(curVal.length == 1 && oldVal.length == 0){
			      this.getDetail(null, curVal[0].type);
          }
        }
      },
      "jobList.alg":{
			  handler(curVal, oldVal){
			    if(curVal.length == 0 && oldVal.length == 1){
			      console.log("iii")
          }else if(curVal.length == 1 && oldVal.length == 0){
			      this.getDetail(null, curVal[0].type);
          }
        }
      },
		}
  };

</script>

<style>
  .submitButton {
    background: #409EFF;
    width: 150px;
    height: 50px;
    border: #AEEEEE 1px solid;
    border-radius: 20px;
    margin: 10px;
    font-size: 15px;
  }
  .submitButton:hover{
    background: #3875d7;
    font-size: 120%;
  }
  .container {
    margin-top: 10px;
    margin-left: 1%;
    margin-right: 1%;
    width: 97%;
    height: 700px;
    background: #FFFAFA;
  }
  .left1 {
    float: left;
    height: 100%;
    width: 25%;
    border-right: #DBDBDB solid 1px;
  }
  .right1 {
    float: right;
    height: 100%;
    width: 30%;
    border-left: #DBDBDB solid 1px;
  }
  .center1 {
    height: 100%;
    overflow: hidden;
  }
  .newJob {
    float: right;
    width: 30%;
    height: 30px;
    margin: 15px 15px 15px;
    font-size: 15px;
    border: #c4dce8 1px solid;
    border-radius: 5px;
    vertical-align: middle;
    background: #94D2F2;
    line-height: 30px;
  }
  .newJob:hover{
    background: #5897fb;
    font-size: 120%;
  }
  .work {
    border:1px solid#ddd;
    width: 90%;
    margin: 5% 5%;
    height: 500px;
    background-color: #F0FFF0;
  }
  .list-group {
    height: 90px;
    width: 100%;
    list-style-type:none;
  }
  .list-group-item {
    cursor: move;
  }
  .eachlist{
    height:30px;
    margin: 5px 10px;
    border:1px solid#ddd;
    text-align: center;
    color:black;
    border-radius: 5%;
  }
  .eachlist.data {
    background-color:#5ac594;
  }
  .eachlist.alg {
    background-color:#81b5d4;
  }
  .eachlist.model {
    background-color:#ED9EB1;
  }
  .itemfont {
    height: 50px;
    width: 90%;
  }
  .listBox {
    width: 58%;
    height: 89px;
    float: left;
    border: #5b80b2 1px solid;
  }
  .deleteSpace {
    height: 90px;
    width: 8%;
    margin-left: 10px;
    text-align: center;
    line-height: 90px;
    float: left;
  }
  .tagEach {
    height: 90px;
    width: 30%;
    border-radius: 3px;
    float: left;
    line-height: 90px;
    font-size: 25px;
  }
  .tagEach.data {
    background:#5ac594;
  }
  .tagEach.alg {
    background-color:#81b5d4;
  }
  .tagEach.model {
    background-color:#ED9EB1;
  }
  .groupEach {
    height: 85px;
    width: 98%;
    margin: 2px 2px;
    border-bottom: #4f4f4f 2px solid;
    text-align: center;
    line-height: 85px;
    font-size: 20px;
  }
  .groupEach.data {
    background-color:#5ac594;
  }
  .groupEach.alg {
    background-color:#81b5d4;
  }
  .groupEach.model {
    background-color:#ED9EB1;
  }
</style>
