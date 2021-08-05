<template>
  <div id="app">
    <section class="dashboard">
      <header>
        <!-- date range placeholder -->
      </header>
      <div class="dashboard__row">
        <latest-transactions-chart ref="latestTransactions" :entries="BABetaOutput"/> <!-- modified 'entries'-->
      </div>
      <div class="dashboard__row">
        <index-table :entries="indexTableView"></index-table> <!-- modified 'entries'-->            
      </div>
      <div class="dashboard__row">
      </div>
      <div class="dashboard__row">
        <share-table :entries="shareTableView"></share-table> <!-- whatever was added in `components` section needs to be here with its name separated by dashes -->
      </div>
      <div class="dashboard__row">
      </div>
      <div class="dashboard__row">
        <all-breakdowns :entries="allBreakdownsView"></all-breakdowns> <!-- whatever was added in `components` section needs to be here with its name separated by dashes -->
      </div>
    </section>
    <div>
      <h2> breakdown by mkt and IC data (Req: buttons to change IC and mkt - currently fixed to mkt J200 and IC ALSI ) </h2>
      {{breakdownByMktandIC}}
    </div>
    <div>
      <h2> BABetaOutput data </h2>
      {{BABetaOutput}}
    </div>
    <div>
      <h2> Testing data </h2>
      {{test}}
    </div>
  </div>

</template>

<script>

import DataService from "./services/DataService";
var test="unchanged";

//Using json files
//import shareTableView from './data/shareTableView.js'; 
//import BABetaOutput from './data/dbo.tbl_BA_Beta_Output.js'; // added row
//import indexTableView from './data/indexTableView.js';
//import allBreakdownsView from './data/allBreakdownsview1.js';

import LatestTransactionsChart from './components/LatestTransactionsChart.vue';
// import TransactionBreakdownChart from './components/TransactionBreakdownChart.vue'; # pie chart commented out
import allBreakdowns from './components/allBreakdownsView.vue';
import shareTable from './components/shareTableView.vue';
import indexTable from './components/indexTableView.vue';

export default {
  name: 'app',
  components: {
    LatestTransactionsChart,
    // TransactionBreakdownChart, // pie chart commented out
    allBreakdowns,
    shareTable, // tag naming format for objects inside <div class="dashboard__row">: SeparatedByCaps = separated-by-caps
    indexTable,
  },
  data() {
    return {
      shareTableView : [], 
      BABetaOutput : [], // added row
      indexTableView : [],
      allBreakdownsView:[],
      test:[],
      breakdownByMktandIC : []
    }
  },
  computed: {
  },
  methods: {
    //this is a test method to look at data in raw form on the dashboard
    async getData(){
      try{
        const response = await DataService.gettest()
        this.test=response.data
      }catch(err){
        this.test=err
      }
    },

    async getbreakdown(){
      try{
        const response = await DataService.getbreakdown()
        this.allBreakdownsView=response.data
      }catch(err){
        this.test=err //console.log() doesn't work so I made atest container for the sake of error checking
      }
    },

    async getSharetable(){
      try{
        const response = await DataService.getSharetable()
        this.shareTableView=response.data
      }catch(err){
        this.test=err
      }
    },

    async getIndextable(){
      try{
        const response = await DataService.getIndextable()
        this.indexTableView=response.data
      }catch(err){
        this.test=err
      }
    },
    async getSpecBreakdown(){
      try{
        const response = await DataService.getSpecBreakdown('ALSI','J200')
        this.breakdownByMktandIC=response.data
      }catch(err){
        this.breakdownByMktandIC=err
      }
    }
/*
    ,
    //commented out for demo
    async getBABetaOutput(){
      try{
        const response = await DataService.getBABetaOutput()
        this.BABetaOutput=response.data
      }catch(err){
        this.test=err
      }
    }
*/
  },
  mounted(){
    this.getData()
    this.getbreakdown();
    this.getSharetable();
    this.getIndextable();
    this.getSpecBreakdown();
    //this.getBABetaOutput();
  }
}
</script>
