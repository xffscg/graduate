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
              <draggable  v-model="item.subFile" v-bind="{group:{name:'people', pull:'clone', put:false }}" @start="isDragging=true" @end="isDragging=false">
                <li class="list-group-item" v-for="file in item.subFile" :key="item.id">
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
              <draggable  v-model="item.subFile" v-bind="{group:{name:'people', pull:'clone', put:false }}" @start="isDragging=true" @end="isDragging=false">
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
            <draggable  v-model="allList.modellist" v-bind="{group:{name:'people', pull:'clone', put:false }}" @start="isDragging=true" @end="isDragging=false">
              <li v-for="item in allList.modellist" :key="item.jobId">
                <div>
                  <span>{{item.modelname}}</span>
                </div>
              </li>
            </draggable>
          </el-submenu>
        </el-menu>
      </div>
    </div></el-col>
    <el-col :span="12"><div class="grid-content">
      <span>WorkSpace</span>
      <div class="work">
        <draggable v-model="delList" v-bind="{group:{name:'people'}}" class="deleteSpace">
          <i class="el-icon-delete" style="font-size: 30px; vertical-align: middle;"></i>
        </draggable>
        <draggable v-model="lists" v-bind="{group:{name:'people'}}" class="list-group" @end="end">
          <transition-group name="no" tag="ul">
            <item v-for="ele in lists" :key="ele.id" :childMsg="ele.type" :id="ele.type+ele.id" >
              {{ele.fileName}}
            </item>
          </transition-group>
        </draggable>
      </div>
    </div></el-col>
    <el-col :span="6"><div class="grid-content">
      <span>yyx</span>

    </div></el-col>
  </div>
</template>

<script>
  import draggable from "vuedraggable";
  import item from "../components/item";
  var BASE_URL = "http://localhost:15050/api/";
  export default {
    components: {
			draggable,
      item,
		},
    data(){
      return {
        allList : [],
        userId: 4,
        lists:[],
        listpro:[],
        isDragging: false,
        delayedDragging: false,
        delList : []
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
      addClick(){
        var idName = $("#" + this.listpro[this.listpro.length-1].type + this.listpro[this.listpro.length-1].id);
        idName.click(function () {
          getConfig();
        });
        console.log(idName);
      }
    },
    watch: {
			isDragging(newValue) {
				if (newValue) {
					console.log(this.isDragging);
					console.log(this.lists);
					this.delayedDragging = true;
					return;
				}
				this.$nextTick(() => {
					this.delayedDragging = false;
				});
			},
      lists: {
				handler(curVal, oldVal) {
					console.log(this.lists);
					if(this.lists.length == 1){
					  this.listpro[0] = this.lists[0];
					  this.$nextTick(() => {
							this.addClick();
							// this.showdetail=true;
						});
          }
				}
			},
		}
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
  .work {
    border:1px solid#ddd;
    width: 90%;
    margin-left: 3%;
    margin-right: 3%;
    height: 700px;
    background-color: #F0FFF0;
  }
  .list-group {
    min-height: 60px;
    width: 90%;
  }
  .list-group-item {
    cursor: move;
  }
  .eachlist{
    height:30px;
    border:1px solid#ddd;
    margin-top:10px;
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
  .itemfont {
    height: 50px;
    width: 90%;
  }
  .deleteSpace {
    height: 80px;
    width: 100%;
    border-bottom: #4f4f4f 2px solid;
    text-align: center;
  }
</style>
