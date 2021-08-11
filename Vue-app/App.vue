<template>
  <div id="app">
    <section class="dashboard">
      <header>
        <!-- date range placeholder -->
      </header>
      <div class="row"> <!--https://www.w3schools.com/howto/howto_css_two_columns.asp set the drop downs side by side with css-->
        <div class="column">
          <select class="form-control" @change="changeIndexType($event)">
            <option value="" selected disabled>Choose Index Type</option>
            <option v-for="type in IndexTypes" :value="type.id" :key="type.id">{{ type.IT }}</option>
          </select>
          <br><br>
          <p><span>selected Index Type: {{ selectedIndexType  }}</span></p>
        </div>
        <div class="column">
          <select class="form-control" @change="changePeriod($event)">
            <option value="" selected disabled>Choose Period</option>
            <option v-for="p in Periods" :value="p.id" :key="p.id">{{ p.YQ }}</option>
          </select>
          <br><br>
          <p><span>selected Period: {{ selectedPeriod  }}</span></p>
        </div>
      </div>
      <div>
        <h2> Reduced Index table data </h2>
        {{}}
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
      <h2> test site </h2>
      {{Periods}}
    </div>
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
      breakdownByMktandIC : [],
      IndexTypes: [],
      selectedIndexType: null,
      Periods: [],
      selectedPeriod: null
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
    },
    async getIndexTypes(){
      try{
        const response = await DataService.getIndexTypes()
        this.IndexTypes=response.data
      }catch(err){
        this.selectedIndexType=err
    }
    },
    async getPeriods(){
      try{
        const response = await DataService.getPeriods()
        this.Periods=response.data
        console.log("executed")
      }catch(err){
        this.selectedPeriod=err
    }
    },
    
    changeIndexType (event) {
      this.selectedIndexType = event.target.options[event.target.options.selectedIndex].text
    },
    changePeriod (event) {
      this.selectedPeriod = event.target.options[event.target.options.selectedIndex].text
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
    this.getIndexTypes();
    this.getPeriods();
    this.changeIndexType();
    
    this.changePeriod();
    //this.getBABetaOutput();
  }
}
</script>
