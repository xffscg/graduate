import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/home'
import DataMining from '@/components/DataMining'
import DataSet from '@/components/DataSet'
import Mining from '@/components/Mining'
import ResultList from '@/components/ResultList'
import ModelList from '@/components/ModelList'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name : 'home',
      component: home
    },
    {
      path: '/DataMining',
      name: 'DataMining',
      component: DataMining,
      children:[
        {
        	path:'/',
        	redirect: 'DataSet',
        },
        {
        	path: 'DataSet',
        	name: 'DataSet',
        	component: DataSet,
        },
        {
        	path: 'Mining',
        	name: 'Mining',
        	component: Mining,
        },
        {
        	path: 'ResultList',
        	name: 'ResultList',
        	component: ResultList,
        },
        {
        	path: 'ModelList',
        	name: 'ModelList',
        	component: ModelList,
        },
      ]
    }
  ]
})
