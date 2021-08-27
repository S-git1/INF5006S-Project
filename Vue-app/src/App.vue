<template>
  <div id="app">
    <div class="sticky-div text.right">
      <section class="card " >
        <div class="card-body row">
          <div class="col-lg-6"  >
            <label class="typo__label text-right" >View Index/Share tables per Quarter</label>
            <VueSlideBar class="addMargin"
              v-model="slider.value"
              :data="slider.data"
              :range="slider.range"
              :labelStyles="{ color: '#4a4a4a', backgroundColor: '#4a4a4a'}"
              :processStyle="{ backgroundColor: '#d8d8d8' }"
              @callbackRange="callbackRange">
              
            </VueSlideBar>
          </div>
          <div class="col-lg-4">
            <br>
            <div class="row">
              <label class="typo__label col-lg-2 text-right" >Select Quarters</label>
              <treeselect class="col-lg-10" v-model="value" :multiple="true" :options="options" />
            </div>
          </div>
          <div class="col-lg-2">
            <select class="btn btn-primary dropdown"  style="margin-top:18px" @change="changeMktIProxy($event)">
              <option value="" selected disabled>Choose Market Proxy</option>
              <option v-for="proxy in mkts" :value="proxy.mkt" :key="proxy.id">{{ proxy.Name }}</option>
            </select>
          </div>
        </div>
      </section>
    </div>

    <div>
      <section class="card">
        <h5 class=card-header>{{indexCaption}}</h5>
        <div class="card-body row">
          <div class="col-lg-2" >
              <select class="btn btn-primary dropdown" @change="changeIndexType($event)">
                <option value="" selected disabled>Choose Index Type</option>
                <option v-for="ind in IndexTypes" :value="ind.id" :key="ind.id">{{ ind.IT }}</option>
              </select>
            </div>
            <div class="col-lg-10 text-right">
              <button
                v-for="tab in indextabs"
                v-bind:key="tab"
                v-bind:class="['tab-button', { active: currentIndexTab === tab }]"
                v-on:click="currentIndexTab = tab"
                class="btn btn-primary"
              >
                {{ tab }}
              </button>
          </div>
        </div>
        <br>
        <div class="card-body row" >
          <div class="col-lg-5">
            <component :is="testvarI" v-bind= "currentIndexTableProperties" class="tab anyClass scrollbar"></component> <!--change to table component-->
          </div>
          <div class="col-lg-7" >
            <component :is="currentIndexTabComponent" v-bind= "currentIndextabProperties" class="tab"></component>
          </div>
        </div>
      </section>

    <!-- {{indexByIndexType}}-->
      

      <!--share charts-->
      
      <section class="card">
        <header class="card-header">
          <h5>{{shareCaption}}</h5>
        </header>    
        <div class="row card-body">
          <div class="col-lg-3" >
              <select class="btn btn-primary dropdown" @change="changeIndustry($event)">
                <option value="" selected disabled>Choose ICB Industry</option>
                <option v-for="ind in ICBtypes" :value="ind.id" :key="ind.id">{{ ind.ICB }}</option>
              </select>
            </div>
        
            <div class="col-lg-9 text-right">
              <button
                v-for="tab in indextabs"
                v-bind:key="tab"
                v-bind:class="['tab-button', { active: currentShareTab === tab }]"
                v-on:click="currentShareTab = tab"
                class="btn btn-primary"
              >
                {{ tab }}
              </button>
              
          </div>

        </div>
        <div class="card-body row" >
          <br>
          <div class="col-lg-5 anyClass">
            <component :is="testvarS" v-bind= "currentShareTableProperties" class="tab  anyClass scrollbar"></component>
          </div>
          <div class="col-lg-7 anyClass" >
            <component :is="currentShareTabComponent" v-bind= "currentSharetabProperties" class="tab"></component>
          </div>
        </div>
      </section>

      <!--breakdown charts-->

      <section class="card">
        <div class="row card-header">
          <div class="col-lg-11">
              <h5>{{breakdownCaption}}</h5>  
          </div>
          <div class="col-lg-1 text-right">
            <span v-bind:title="breakdownInfo">
                <img src="./assets/info_icon.png" alt="more info" width="20" height="20">
            </span>
          </div>
        </div>
        <div class="row card-body"> <!--https://www.w3schools.com/howto/howto_css_two_columns.asp set the drop downs side by side with css-->
          
          <div class="col-lg-6" >
            <select class="btn btn-primary drop-down" @change="changeIndex($event)">
              <option value="LRGC" selected disabled>Choose Index</option>
              <option v-for="ind in indice" :value="ind.id" :key="ind.id">{{ ind.IC }}</option>
            </select>

            <select class="btn btn-primary drop-down" @change="changeStat($event)">
              <option value="" selected disabled>Choose Statistic</option>
              <option v-for="p in stats" :value="p.id" :key="p.id">{{ p.stat }}</option>
            </select>
          </div>
          
          <div class="col-lg-6 text-right" >
            <button
              v-for="tab in tabs"
              v-bind:key="tab"
              v-bind:class="['tab-button', { active: currentTab === tab }]"
              v-on:click="currentTab = tab"
              class="btn btn-primary"
            >
              {{ tab }}
            </button>
          </div>
          <br>
          <br>
        </div>
        <div class="row card-body" >
          <div class="col-lg-6 anyClass " >
            <component :is="tempval" v-bind= "fixedLineChart" class="tab"></component>
          </div>
          <div class="col-lg-6 anyClass scrollbarx" >
            <component :is="currentTabComponent" v-bind= "currentProperties" class="tab"></component>
          </div>
          
        </div>
      </section>      
    </div>
  </div>

</template>

<script>

import DataService from "./services/DataService";
//import Constants from "./services/Constants.js"
var test="unchanged";
//Hardcoded here for now,
//note: stick the constants all in a separate file and make table fields pull directly from api from there so that it is not mounted in liffecycle hook
const stats=[
  {"stat":"betas", "id":1},
  {"stat":"weight2", "id":2},
  {"stat":"specVar", "id":3},
  {"stat":"sysVol", "id":4}
]

const Istats=[
  {"stat":"Start Date", "id":1},
  {"stat":"End Date", "id":2},
  {"stat":"% Days Traded", "id":3},
  {"stat":"Data Points", "id":4},
  {"stat":"Alpha", "id":5},
  {"stat":"Beta", "id":6},
  {"stat":"SE Alpha", "id":7},
  {"stat":"SE Beta", "id":8},
  {"stat":"p Value Alpha", "id":9},
  {"stat":"p Value Beta", "id":10},
  {"stat":"R2", "id":11},
  {"stat":"Total Risk", "id":12},
  {"stat":"Unique Risk", "id":13},
]

const indice=[
  {"IC": "ALSI", "id":1},
  {"IC": "FLED", "id":2},
  {"IC": "LRGC", "id":3},
  {"IC": "MIDC", "id":4},
  {"IC": "SMLC", "id":5},
  {"IC": "TOPI", "id":6},
  {"IC": "RESI", "id":7},
  {"IC": "FINI", "id":8},
  {"IC": "INDI", "id":9},
  {"IC": "PCAP", "id":10},
  {"IC": "SAPY", "id":11},
  {"IC": "ALTI", "id":12}]

const ICBtypes=[
  {"ICB": "Oil & Gas", "id":1},
  {"ICB": "Basic Materials", "id":2},
  {"ICB": "Industrials", "id":3},
  {"ICB": "Consumer Goods", "id":4},
  {"ICB": "Health Care", "id":5},
  {"ICB": "Consumer Services", "id":6},
  {"ICB": "Telecommunications", "id":7},
  {"ICB": "Financials", "id":8},
  {"ICB": "Technology", "id":9},
  {"ICB": "Utilities", "id":10}
  ]

const mkts=[
  {"mkt":"J203","Name":"ALSI Share Index (J203)", "id":1},
  {"mkt":"J200","Name":"Top 40 Index (J200)", "id":2},
  {"mkt":"J250","Name":"Financials & Industrials Index (J250)", "id":3},
  {"mkt":"J257","Name":"Industrials Index (J257)", "id":4},
  {"mkt":"J258","Name":"Resources Index (J258)", "id":5}]

const years=[
  {"year":2017,"id":1},
  {"year":2018,"id":2},
  {"year":2019,"id":3},
  {"year":2020,"id":4},
  {"year":2021,"id":5},
  ]

const quarters=[
  {"quarter":1,"id":1},
  {"quarter":2,"id":2},
  {"quarter":3,"id":3},
  {"quarter":4,"id":4}
  ]


import Vue from 'vue/dist/vue.js';


Vue.component("tab-table", {
  props:['data'],
  //template: `<all-breakdowns :entries="data.Data"></all-breakdowns>`
  template: `<tab-alt2 :entries="data.Data" :columns="data.columns"></tab-alt2>`
});

Vue.component("tab-barchart", {
  props:['data'],
  template: `<latest-transactions-chart :Series="data.mySeries" :tbl="data.tbl" :Heading="data.Heading" :type="data.type" :stacked="data.stacked" :tick="data.tick" :headers="data.headers" :opts="data.opts"></latest-transactions-chart>`
});

Vue.component("tab-linechart", {
  props:['data'],
  template: `<latest-transactions-chart :Series="data.mySeries" :tbl="data.tbl" :Heading="data.Heading" :type="data.type" :stacked="data.stacked" :tick="data.tick" :headers="data.headers" :opts="data.opts"></latest-transactions-chart>`
});

Vue.component("tab-indextable", {
  props:['data'],
  //template: `<index-tab-alt :entries="data.indexData" :Quarter="data.Quarter" ></index-tab-alt>`
  template: `<tab-alt2 :entries="data.Data" :Quarter="data.Quarter" :type="data.type" ></tab-alt2>`
});

Vue.component("tab-sharetable", {
  props:['data'],
  //template: `<share-tab-alt :entries="data.ShareData" :Quarter="data.Quarter" ></share-tab-alt>`
  template: `<tab-alt2 :entries="data.Data" :Quarter="data.Quarter" :type="data.type" ></tab-alt2>`
});


export default {
  name: 'app',
  components: {
  },
  data() {
    return {
      
      rangeValue: {},
      slider: {
        value: "Y2017Q3",
        data: [
          "Y2017Q3",
          "Y2017Q4",
          "Y2018Q1",
          "Y2018Q2",
          "Y2018Q3",
          "Y2018Q4",
          "Y2019Q1",
          "Y2019Q2",
          "Y2019Q3",
          "Y2019Q4",
          "Y2020Q1",
          "Y2020Q2",
          "Y2020Q3",
          "Y2020Q4",
          "Y2020Q1"
        ],
        range: [{label:"Y2017Q3", id: 0},
                {label:"Y2017Q4", isHide:true, id: 1},
                {label:"Y2018Q1", isHide:true, id: 2},
                {label:"Y2018Q2", isHide:true, id: 3},
                {label:"Y2018Q3", id: 4},
                {label:"Y2018Q4", isHide:true, id: 5},
                {label:"Y2019Q1", isHide:true, id: 6},
                {label:"Y2019Q2", isHide:true, id: 7},
                {label:"Y2019Q3", id: 8},
                {label:"Y2019Q4", isHide:true, id: 9},
                {label:"Y2020Q1", isHide:true, id: 10},
                {label:"Y2020Q2", isHide:true, id: 11},
                {label:"Y2020Q3", id: 12},
                {label:"Y2020Q4", isHide:true, id: 13},
                {label:"Y2021Q1", isHide:true, id: 14}]
      },
      // define the default value
      testvarI:"tab-indextable",
      testvarS:"tab-sharetable",
      tempval: 'tab-linechart',
      value: [],
      options: [{label:"Y2017Q3", id: 0},
                {label:"Y2017Q4", id: 1},
                {label:"Y2018Q1", id: 2},
                {label:"Y2018Q2", id: 3},
                {label:"Y2018Q3", id: 4},
                {label:"Y2018Q4", id: 5},
                {label:"Y2019Q1", id: 6},
                {label:"Y2019Q2", id: 7},
                {label:"Y2019Q3", id: 8},
                {label:"Y2019Q4", id: 9},
                {label:"Y2020Q1", id: 10},
                {label:"Y2020Q2", id: 11},
                {label:"Y2020Q3", id: 12},
                {label:"Y2020Q4", id: 13},
                {label:"Y2021Q1", id: 14}],
      breakdownInfo: " Synthetic construction of the most important risk statistics: beta, systematic volatility and specific variance, using the corresponding individual statistics of each index’s constituents and then aggregating these by each constituent’s weight in that index, respectively. ",
      shareTableView : [], 
      BABetaOutput : [], 
      //table constants
      tabs: ["Barchart","Linechart", "Table" ],
      indextabs: [ "Barchart", "Linechart"],

      //BD data
      mySeries: [],
      breakdownByMktandIC : [],
      allBreakdownsView:[],
      //fields selected for BD
      currentTab: "Barchart",
      selectedMktProxy: "",
      selectedIndex : "",
      selectedStat: "",

      //Index tables data
      indexSeries: [],
      indexByIndexType:[],
      indexTableView : [],
      //fields selected for Index tabs
      currentIndexTab: "Linechart",
      selectedIndexType: "",
      selectedPeriod: "",
      selectedIndexMktProxy:"",

      //share table data
      shareSeries: [],
      shareByICB: [],
      currentShareTab: "Linechart",
      selectedIndustry: "",
      selectedSharePeriod: "",

      //Time constants
      quarters: quarters,
      years: years,
      //fixed variables for selection fields
      indice: indice, //all 12 indices
      mkts: mkts, //5 markets
      stats: stats, //breakdown table fields
      Istats: Istats, //index table fields
      Periods: [], //periods used in index and share tables currently pulls from database
      IndexTypes: [], //index types used in index tables
      ICBtypes: ICBtypes, //ICB industries

      //testing variables
      finished: "unchanged",
      test:[],

      //headings
      breakdownCaption: "Breakdown of <Index> using <Proxy> as proxy",
      indexCaption: "Index Betas for <Index Type> in the period <Period>",
      shareCaption: "Share Betas for <ICB Industry> in the period <Period>"
    }
  },
  computed: {
      currentTabComponent() {
          return "tab-" + this.currentTab.toLowerCase();
        },
      fixedLineChart(){
        let temp=this.Periods.map(item => item.YQ).filter((value, index, self) => self.indexOf(value) === index); //setting up periods for graph,
        if((this.breakdownByMktandIC.length!=0)){
        
          
          return{
            data:{
              breakdownCaption: "",
              mySeries: this.mySeries,
              type: 'line',
              stacked: false,
              tick: false,
              headers: temp
            }
          };
        }
        return{
          data:{
              breakdownCaption: "",
              mySeries: [],
              type: 'line',
              stacked: false,
              tick: false,
              headers: temp
          }

        };
      },
      currentProperties(){
        let temp=this.Periods.map(item => item.YQ).filter((value, index, self) => self.indexOf(value) === index); //setting up periods for graph,
        let sorted=this.value.sort(function(a,b){return a-b;})
        let redquarters=sorted.map(i=>temp[i]);
        
        if (this.currentTab==="Linechart"&&this.breakdownByMktandIC.length!=0){
          
          return{
            data:{
              breakdownCaption: this.breakdownCaption,
              mySeries: this.mySeries,
              type: 'line',
              stacked: false,
              tick: false,
              headers: this.value.length==0? temp:redquarters,
              opts: sorted
            }
          };
        }
        else if (this.currentTab==="Barchart"&&this.breakdownByMktandIC.length!=0){
          console.log("breakdowns executing");
          return{
            data:{
              breakdownCaption: "",
              mySeries: this.mySeries,
              type: 'bar',
              stacked: true,
              tick: false,
              headers: this.value.length==0? temp:redquarters,
              opts:sorted
              //headers: ["Y2017Q3","Y2017Q4"],
              
            }
          };
        }
        else if (this.currentTab==="Table"&&this.breakdownByMktandIC.length!=0){
          return{
            data:{
                breakdownCaption: "",
                Data: this.breakdownByMktandIC,
                columns: this.value.length==0? temp:redquarters
            }
          };
        }
        return{
            data:{
                breakdownCaption: "",
                mySeries: [],
                type:'',
                stacked: false,
                headers:temp,
                opts:sorted,
                Data: [],
                columns: this.value.length==0? temp:redquarters
            }
          };
      },
      currentIndexTableProperties(){
        if (this.selectedIndexType!=""&&this.indexByIndexType.length!==0){
          this.indexCaption="Index table of Betas for " +this.selectedIndexType + " Index types in "+ this.slider.value;
          let temp= this.indexByIndexType.filter(iT=> iT["Index Type"]===this.selectedIndexType);
          console.log(temp);
          
          return{
            data:{
                Data: temp,
                Quarter: this.slider.value,
                type: "index",
              }
          };
        }
        this.indexCaption="Index table of Betas for <Index Type> Index types in "+ this.slider.value;
        return{
            data:{
                Data: [],
                MySeries:[],
                Quarter: this.slider.value,
                type: "index",
              }
          };
      },
      currentIndexTabComponent(){
        if(this.currentIndexTab==="Table"){
          return "tab-index" + this.currentIndexTab.toLowerCase();
        }
        return "tab-"+this.currentIndexTab.toLowerCase();
      },
      currentIndextabProperties(){
        if (this.currentIndexTab==="Barchart"&&this.selectedIndexMktProxy!=""){
          console.log("executing"+this.currentIndexTab);
          console.log(this.selectedIndexMktProxy);
          let temp=this.indexSeries.filter(item=>item.IndexType===this.selectedIndexType);
          //var temp=this.indexSeries;
          let mkt=this.selectedIndexMktProxy.slice(-5,-1);
          let temp2=temp.map(item=>({"text":item.Code,"values": Object.entries(item[mkt]).map((e) => e),"Name":item.Name, "IndexType":item.IndexType}));
          console.log("executing currentindex tab ");
          return{
            data:{
              mySeries: temp2,
              type: 'bar',
              stacked: false,
              tick: true,
              headers: this.Periods.map(item => item.YQ).filter((value, index, self) => self.indexOf(value) === index), //setting up periods for graph,
              Heading: this.selectedMktProxy,
              tbl:"I"
            }
          };
        }
        else if(this.currentIndexTab==="Linechart" &&this.selectedIndexMktProxy!=""){
          console.log("executing"+this.currentIndexTab);
          console.log(this.selectedIndexMktProxy);
          let temp=this.indexSeries.filter(item=>item.IndexType===this.selectedIndexType);
          //var temp=this.indexSeries;
          let mkt=this.selectedIndexMktProxy.slice(-5,-1);
          let temp2=temp.map(item=>({"text":item.Code,"values": Object.entries(item[mkt]).map((e) => e),"Name":item.Name, "IndexType":item.IndexType}));
          //this.test=temp;
          console.log("ready for line");
          return{
            data:{
              mySeries: temp2,
              type: 'line',
              stacked: false,
              tick: false,
              headers: this.Periods.map(item => item.YQ).filter((value, index, self) => self.indexOf(value) === index), //setting up periods for graph,
              Heading: this.selectedMktProxy,
              tbl:"I"
            }
          }
        }
        return{
          data:{
              mySeries: [],
              Data: [],
              Quarter: this.slider.value,
              type: "index",
              headers: this.Periods.map(item => item.YQ).filter((value, index, self) => self.indexOf(value) === index),
              tbl:"I"
              
            }
        };
      },
      currentShareTabComponent(){
        if(this.currentShareTab==="Table"){
          return "tab-share" + this.currentShareTab.toLowerCase();
        }
        return "tab-"+this.currentShareTab.toLowerCase();
      },
      currentSharetabProperties(){
        if(this.currentShareTab==="Linechart" &&this.selectedIndexMktProxy!=""){ //change
          console.log("executing"+this.currentShareTab);
          console.log(this.selectedIndexMktProxy); //change
          let temp=this.shareSeries.filter(item=>item.Industry===this.selectedIndustry);
          
          //var temp=this.shareSeries;
          let mkt=this.selectedIndexMktProxy.slice(-5,-1);
          let temp2=temp.map(item=>({"text":item.Code,"values": Object.entries(item[mkt]).map((e) => e), "Industry":item.Industry}));
          //this.test=temp;
          console.log(JSON.stringify(temp2));
          console.log("ready for line");
          return{
            data:{
              mySeries: temp2,
              type: 'line',
              stacked: false,
              tick: false,
              headers: this.Periods.map(item => item.YQ).filter((value, index, self) => self.indexOf(value) === index), //setting up periods for graph,
              Heading: this.selectedMktProxy,
              tbl:"S"
              
            }
          }
        }
        if(this.currentShareTab==="Barchart" &&this.selectedIndexMktProxy!==""){ //change
          console.log("executing"+this.currentShareTab);
          console.log(this.selectedIndexMktProxy); //change
          let temp=this.shareSeries.filter(item=>item.Industry===this.selectedIndustry);
          
          //var temp=this.shareSeries;
          let mkt=this.selectedIndexMktProxy.slice(-5,-1);
          let temp2=temp.map(item=>({"text":item.Code,"values": Object.entries(item[mkt]).map((e) => e), "Industry":item.Industry}));
          //this.test=temp;
          console.log(JSON.stringify(temp2));
          console.log("ready for line");
          return{
            data:{
              mySeries: temp2,
              type: 'bar',
              stacked: false,
              tick: true,
              headers: this.Periods.map(item => item.YQ).filter((value, index, self) => self.indexOf(value) === index), //setting up periods for graph,
              Heading: this.selectedMktProxy,
              tbl:"S"
              
              
            }
          }
        }
        return{
          data:{
            headers: this.Periods.map(item => item.YQ).filter((value, index, self) => self.indexOf(value) === index),
            type: 'line',
            mySeries: [],
            Data: [],
            Quarter: this.slider.value,
            type: "index",
            headers: this.Periods.map(item => item.YQ).filter((value, index, self) => self.indexOf(value) === index),
            Heading: this.selectedMktProxy,
            tbl:"S"
              
          }

        };
      },
      currentShareTableProperties(){
        if (this.selectedIndustry!==""&&this.shareByICB.length!==0){
          this.shareCaption="Share table of Betas for the " +this.selectedIndustry + " Industry in "+ this.slider.value;
          return{
            data:{
                Data: this.shareByICB.filter(item=>item.Industry===this.selectedIndustry),
                Quarter: this.slider.value,
                type: "share"
              }
          };
        }
        
        this.shareCaption="Share table of Betas for the <ICB Industry> Industry in "+ this.slider.value;
        return{
            data:{
                Data: [],
                Quarter: this.slider.value,
                type: "share"
              }
          };
      }  
  },
  methods: {

    async getSpecBreakdown(){
      this.breakdownCaption="Breakdown of " +this.selectedStat + " in the "+ this.selectedIndex +" Index using "+ this.selectedMktProxy+ " as proxy"
      console.log(this.selectedStat)
      console.log(this.selectedIndex)
      console.log(this.selectedMktProxy)
      try{
        
       // if (this.selectedIndexMktProxy!=="" && this.selectedIndex!=="" && this.selectedStat!==""){

          const response = await DataService.getSpecBreakdown(this.selectedIndex,this.selectedIndexMktProxy.slice(-5,-1))
          const FTSE = await DataService.getICB()
          let BDdata=[] //container for table data
          let Ceres=[] //container for chart data
          let industries=FTSE.data.map(item => item.Industry).filter((value, index, self) => self.indexOf(value) === index) //get list of industries
          
          //this for loop loads BDdata with the desired form for the breakdown table and chart
          for (let i = 0; i < industries.length; i++) {
            let hello={"Industry":industries[i]} //create a dummy object which we will populate
            let please=response.data.filter(industry=>industry.Industry===industries[i]) //filter the breakdown data by a particular industry
            //populating data for table
            for (let j=0;j<this.Periods.length;j++){              
                hello[this.Periods[j]["YQ"]]=null
            }
            for (let j=0;j< please.length;j++){
              hello["Y"+parseInt(please[j]["Year"])+"Q"+parseInt(please[j]["Quarter"])]=Math.round((parseFloat(please[j][this.selectedStat])+Number.EPSILON)*1000000)/1000000//extract stat in order of periods
            }
            
            BDdata.push(hello)

            //next 3 lines adjust the data for the line/bar charts
            let alt=JSON.parse(JSON.stringify(hello))
            delete alt["Industry"]
            Ceres.push({"text":industries[i], "values":Object.entries(alt).map((e) => e)})

          }
          this.breakdownByMktandIC=BDdata
          //console.log(JSON.stringify(this.breakdownByMktandIC))
          this.mySeries=Ceres
          //console.log(JSON.stringify(this.mySeries))
          console.log("breakdowns ready")
          
        //}
        //console.log("nope");
      }catch(err){
        this.finished=err
        this.breakdownByMktandIC=[]
        console.log(err)
    }
    },

    async getSpecIndex(){
      
      try{
        //if(this.selectedIndexType!="\{Index Type\}"){
          const response = await DataService.getIndextable()
        
          var temp=response.data
          //this.indexByIndexType=temp
          var Codes=temp.map(item => item.Code).filter((value, index, self) => self.indexOf(value) === index) //get list of codes under the index type
          //this.indexByIndexType=Codes
          var Ceres=[]
          var other=[]

          for (let i = 0; i < Codes.length; i++) {
             //create a dummy object which we will populate
            let please=temp.filter(item=>item.Code===Codes[i]) //filter to get all the data for this code
            const Name=please[0].Name //get name of code, this is a cheat should use filter for robustness
            const IndexType=please[0]["Index Type"]
            //this.finished=Name
            //this.test=please
            let ohello={"Code":Codes[i], "Name":Name,"IndexType":IndexType, J203:[],J200:[],J258:[],J257:[],J250:[]}
            for (let j=0;j<this.Periods.length;j++){
              //console.log(this.Periods[j]["YQ"])
              
                ohello["J203"][this.Periods[j]["YQ"]]=null
                ohello["J200"][this.Periods[j]["YQ"]]=null
                ohello["J258"][this.Periods[j]["YQ"]]=null
                ohello["J257"][this.Periods[j]["YQ"]]=null
                ohello["J250"][this.Periods[j]["YQ"]]=null
            }
            for (let p of this.Periods){
              let hello={"Code":Codes[i], "Name":Name, "YQ":p.YQ, "Index Type":IndexType}
              let filtered=please.filter(item=>item.Year===p.Year && item.Quarter===p.Quarter)              
              if(filtered.length!=0){
                hello["Data Pts"]=parseInt(filtered[0]["Data Points"])
                filtered.map(function(o){
                  let beta=Math.round((parseFloat(o.Beta)+Number.EPSILON)*1000000)/1000000
                  hello[o.MarketID]=beta
                  ohello[o.MarketID][p.YQ]=beta

                })
                //filtered.map(o=>hello["M"+o.MarketID]=[parseFloat(o["p Value Beta"]),parseFloat(o["SE Beta"]),parseFloat(o.Alpha),parseFloat(o["p Value Alpha"]),parseFloat(o["SE Alpha"])])
                filtered.map(o=>hello["M"+o.MarketID]=parseFloat(o["p Value Beta"]))
              }
              Ceres.push(hello)
            }
            other.push(ohello);
            //this.finished="ready"
            
    
          }
          this.indexByIndexType=Ceres
          this.indexSeries=other
          console.log("indexSeries ready")
      }catch(err){
        console.log(this.err)
        console.log("index Series not ready")
        this.finished=err
      }
    },

    async getSpecShareTab(){
      //this.shareCaption=this.selectedIndustry+" "+this.selectedSharePeriod
      try{
        //if(this.selectedIndustry!="\{ICB Industry\}"){
          const response = await DataService.getSharetable()
          
          //let temp=response.data.filter(iT=> iT["Industry"]===this.selectedIndustry) //filter by selected industry
          let temp=response.data
          //this.indexByIndexType=temp
          let Codes=temp.map(item => item.Instrument).filter((value, index, self) => self.indexOf(value) === index) //get list of codes under the index type
          //this.indexByIndexType=Codes
          let Ceres=[]
          let other=[]

          for (let i = 0; i < Codes.length; i++) {
             //create a dummy object which we will populate
            let please=temp.filter(item=>item.Instrument===Codes[i]) //filter to get all the data for this code
            //this.test=please
            const IndexType=please[0]["Industry"]
            //this.finished=Name
            //this.test=please
            let ohello={"Code":Codes[i],"Industry":IndexType, J203:{},J200:{},J258:{},J257:{},J250:{}}
            for (let j=0;j<this.Periods.length;j++){              
                ohello["J203"][this.Periods[j]["YQ"]]=null
                ohello["J200"][this.Periods[j]["YQ"]]=null
                ohello["J258"][this.Periods[j]["YQ"]]=null
                ohello["J257"][this.Periods[j]["YQ"]]=null
                ohello["J250"][this.Periods[j]["YQ"]]=null
            }
            //console.log(JSON.stringify(ohello))
            for (let p of this.Periods){
              //, "Name":Name could pull this using api later
              let hello={"Code":Codes[i], "YQ":p.YQ, "Industry":IndexType}
              let filtered=please.filter(item=>item.Year===p.Year && item.Quarter===p.Quarter)        
              //this.finished=filtered      
              if(filtered.length!=0){
                hello["Data Pts"]=parseInt(filtered[0]["Data Points"]) //fix this in MSServer
                hello["Cap"]=filtered[0]["Cap"]
                hello["Start Date"]=filtered[0]["Start Date"].slice(0,10)
                hello["End Date"]=filtered[0]["End Date"].slice(0,10)
                hello["% Days Traded"]=Math.round(parseFloat(filtered[0]["% Days Traded"])*10000)/100
                
                filtered.map(function(o){
                  let beta=Math.round((parseFloat(o.Beta)+Number.EPSILON)*1000000)/1000000
                  hello[o.MarketID]=beta
                  ohello[o.MarketID][p.YQ]=beta
                  })
                //filtered.map(o=>hello["M"+o.MarketID]=[parseFloat(o["p Value Beta"]),parseFloat(o["SE Beta"]),parseFloat(o.Alpha),parseFloat(o["p Value Alpha"]),parseFloat(o["SE Alpha"])])
                filtered.map(o=>hello["M"+o.MarketID]=parseFloat(o["p Value Beta"]))
              }
              Ceres.push(hello)
            }
            other.push(ohello)
           //this.finished=Ceres
    
          }
          this.shareByICB=Ceres
          this.shareSeries=other
          console.log("shareSeries ready")
        //}
      }catch(err){
        console.log(this.err)
        this.test=err
      }
    },

    async getIndexTypes(){
      try{
        const response = await DataService.getIndexTypes()
        this.IndexTypes=response.data
        console.log("Index types ready")
      }catch(err){
        this.selectedIndexType=err
    }
    },
    async getPeriods(){
      try{
        const response = await DataService.getPeriods()
        this.Periods=response.data
        console.log("Periods ready")
      }catch(err){
        this.selectedPeriod=err
    }
    },
    
    changeIndexType (event) {
      //if (this.selectedIndexType!="\{Index Type\}"){
        this.selectedIndexType = event.target.options[event.target.options.selectedIndex].text
        
        
        //this.getSpecIndex()
      //}
    },
    
    
    changeIndex (event) {
      //if (this.selectedIndex!="\{Index\}"){
        this.selectedIndex = event.target.options[event.target.options.selectedIndex].text
        //this.getSpecBreakdown()
      //}
    },
    changeStat (event) {
      //if (this.selectedStat!="\{statistic\}"){
        this.selectedStat = event.target.options[event.target.options.selectedIndex].text
        this.getSpecBreakdown()
      //}
    },
    changeMktIProxy (event) {
      //if (this.selectedMktProxy!="\{Proxy\}"){
        this.selectedIndexMktProxy = event.target.options[event.target.options.selectedIndex].text
        this.getSpecBreakdown()
        //this.ConfigureIndexchart()
      //}
    },

    changeIndustry(event){
      this.selectedIndustry = event.target.options[event.target.options.selectedIndex].text
      /*this.shareCaption = "Share Betas for " +this.selectedIndustry+" (ICB) in the period "+this.selectedSharePeriod*/
      //this.getSpecShareTab()
    },

    

    callbackRange (val) {
      this.rangeValue = val
    }
  },
  mounted(){
    
    this.getSpecBreakdown();
    this.getIndexTypes();
    this.getPeriods();
    this.getSpecIndex();
    this.getSpecShareTab();
  }
}
</script>
<style scoped>

h5 {
  color: #5d7d9a;
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  font-weight: bold;
  padding-left: 0;
  text-align: left;
            
}
.anyClass{
  height:500px;
  
}

.scrollbary{
  overflow-y:scroll;
  
}
.scrollbarx{
  overflow-x:scroll;
  
}

.scrollbar{
  overflow:scroll;
  
}
.sticky-div {
            position:-webkit-sticky;
            position: sticky;
            top:20px;
            z-index:9999;
        }

.addMargin{
  margin:20px;

}
</style>