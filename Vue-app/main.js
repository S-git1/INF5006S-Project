import Vue from 'vue/dist/vue.js'
import App from './App.vue'
import router from './router/index.js' // good case for multipage efforts


Vue.config.productionTip = false;

// import the zingchart-vue component, which in turn, imports the zingchart library itself.
import zingchartVue from 'zingchart-vue';
import Multiselect from 'vue-multiselect';
import allBreakdowns from './components/allBreakdownsView.vue';
import latestTransactionsChart from './components/LatestTransactionsChart.vue';
import indexTableView from './components/indexTableView.vue';
import shareTableView from './components/shareTableView.vue';
import altIndexTableView from './components/IndexTabAlt.vue';
import altShareTableView from './components/shareTabAlt.vue';
Vue.component('zingchart', zingchartVue);
Vue.component('multiselect', Multiselect);
Vue.component('all-breakdowns',allBreakdowns);
Vue.component('latest-transactions-chart',latestTransactionsChart);
Vue.component('index-table',indexTableView);
Vue.component('share-table',shareTableView);
Vue.component('index-tab-alt',altIndexTableView);
Vue.component('share-tab-alt',altShareTableView);


// Import the ZingGrid library, By default, the ZingGrid library registers itself as a web component.
import ZingGrid from "zinggrid";




new Vue({
  router,
  render: h => h(App),
}).$mount('#app');

