import Vue from 'vue/dist/vue.js'
import App from './App.vue'
//import App from './App_wMultiselect.vue'
import router from './router/index.js' // good case for multipage efforts


Vue.config.productionTip = false;

// import the zingchart-vue component, which in turn, imports the zingchart library itself.
import zingchartVue from 'zingchart-vue';
import Multiselect from 'vue-multiselect';
import allBreakdowns from './components/allBreakdownsView.vue';
import latestTransactionsChart from './components/LatestTransactionsChart.vue';


Vue.component('zingchart', zingchartVue);
Vue.component('multiselect', Multiselect);
Vue.component('all-breakdowns',allBreakdowns);
Vue.component('latest-transactions-chart',latestTransactionsChart);



import { ClientTable } from "vue-tables-2";
let options = {};
let useVuex = false;
let theme = "bootstrap4";
let template = "default";
Vue.use(ClientTable, options, useVuex, theme, template);

import temp from './components/TabAlt2.vue';
Vue.component('tab-alt2',temp);

// import the component
import Treeselect from '@riophae/vue-treeselect';
import '@riophae/vue-treeselect/dist/vue-treeselect.css'
Vue.component('treeselect', Treeselect)

import VueSlideBar from 'vue-slide-bar'
Vue.component('VueSlideBar', VueSlideBar)






new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
/*
new Vue({
  router,
  render:h => h(temp),
}).$mount('#test');*/