<template>
  <div id="app">
    <section class="dashboard">
      <header>
        <h3>{{breakdownCaption}}</h3>
      </header>    

      <div class="row"> <!--https://www.w3schools.com/howto/howto_css_two_columns.asp set the drop downs side by side with css-->
        <br>
        <div class="col-lg-3" style="margin:0px">
          <select class="form-control" @change="changeMktProxy($event)">
            <option value="" selected disabled>Choose Market Proxy</option>
            <option v-for="proxy in mkts" :value="proxy.mkt" :key="proxy.id">{{ proxy.Name }}</option>
          </select>

        </div>
        <div class="col-lg-2" style="margin:0px">
          <select class="form-control" @change="changeIndex($event)">
            <option value="" selected disabled>Choose Index</option>
            <option v-for="ind in indice" :value="ind.id" :key="ind.id">{{ ind.IC }}</option>
          </select>

        </div>
        <div class="col-lg-2" style="margin:0px">
          <select class="form-control" @change="changeStat($event)">
            <option value="" selected disabled>Choose Statistic</option>
            <option v-for="p in stats" :value="p.id" :key="p.id">{{ p.stat }}</option>
          </select>
        </div>  
        <div class="col-lg-5 text-right" >
          <button
            v-for="tab in tabs"
            v-bind:key="tab"
            v-bind:class="['tab-button', { active: currentTab === tab }]"
            v-on:click="currentTab = tab"
            class="btn btn-default"
          >
            {{ tab }}
          </button>
        </div>

        <!-- <div v-if="ShowForLine()" class="col-lg-2 text"> -->
        <!-- <div class="col-lg-2 text">
          <label class="typo__label">Customisation</label>
          <select v-model="value" :custom-label="nameWithLang" :close-on-select="false" placeholder="Select one" label="name" track-by="name" :multiple="true">
            <option value="" selected disabled>Choose a industry</option>
            <option v-for="i in industryList" :value="i.code" :key="i.name">{{ i.name }}</option>
          <pre class="language-json"><code>{{ value  }}</code></pre>
          </select>
        </div> -->
         <div class="col-lg-2 text">
          <label class="typo__label">Customisation</label>
          <multiselect v-model="value" :options="options" :close-on-select="false" return='code' selectLabel='' deselectLabel='' placeholder="Select industry" label="name" track-by="name" :multiple="true" 
          @input="genIndexList(value)"></multiselect>
          <!-- <pre class="language-json"><code>{{ value  }}</code></pre> -->
        </div>


        <br>
        <br>
      </div>
      <div class="row" >
<!--        <keep-alive>-->
        <div class="col-lg-12" >
          <component :is="currentTabComponent" v-bind= "currentProperties" class="tab"></component>
<!--        </keep-alive>-->
        </div>
      </div>
    </section>

    <br><br><br><br>
    
    <section>
      <header>
        <h3>{{indexCaption}}</h3>
      </header>    
      <div class="row">
        <div class="col-lg-3" >
            <select class="form-control" @change="changeIndexType($event)">
              <option value="" selected disabled>Choose Index Type</option>
              <option v-for="ind in IndexTypes" :value="ind.id" :key="ind.id">{{ ind.IT }}</option>
            </select>

          </div>
          <div class="col-lg-2" >
            <select class="form-control" @change="changePeriod($event)">
              <option value="" selected disabled>Choose Period</option>
              <option v-for="p in Periods" :value="p.id" :key="p.id">{{ p.YQ }}</option>
            </select>
          </div> 
          <div class="col-lg-7 text-right">
            <button
              v-for="tab in indextabs"
              v-bind:key="tab"
              v-bind:class="['tab-button', { active: currentIndexTab === tab }]"
              v-on:click="currentIndexTab = tab"
              class="btn btn-default"
            >
              {{ tab }}
            </button>
            
        </div>

      </div>
      <div class="row" >
        
        <component :is="currentIndexTabComponent" v-bind= "currentIndextabProperties" class="tab"></component>
        
      </div>
    </section>
    
    <br><br><br><br>

    <section>
      <header>
        <h3>{{shareCaption}}</h3>
      </header>    
      <div class="row">
        <div class="col-lg-3" >
            <select class="form-control" @change="changeIndustry($event)">
              <option value="" selected disabled>Choose ICB Industry</option>
              <option v-for="ind in ICBtypes" :value="ind.id" :key="ind.id">{{ ind.ICB }}</option>
            </select>

          </div>
          <div class="col-lg-2" >
            <select class="form-control" @change="changeSharePeriod($event)">
              <option value="" selected disabled>Choose Period</option>
              <option v-for="p in Periods" :value="p.id" :key="p.id">{{ p.YQ }}</option>
            </select>
          </div> 
          <div class="col-lg-2" >
            <select class="form-control" @change="changeSharePeriod($event)">
              <option value="" selected disabled>Choose Period</option>
              <option v-for="p in Periods" :value="p.id" :key="p.id">{{ p.YQ }}</option>
            </select>
          </div>
          <div class="col-lg-7 text-right">
            <button
              v-for="tab in tabs"
              v-bind:key="tab"
              v-bind:class="['tab-button', { active: currentShareTab === tab }]"
              v-on:click="currentShareTab = tab"
              class="btn btn-default"
            >
              {{ tab }}
            </button>
            
        </div>

      </div>
      <div class="row vh-100" >
        <div class="col-lg-12" >
          <component :is="currentShareTabComponent" v-bind= "currentSharetabProperties" class="tab"></component>
        </div>
      </div>
    </section>


    <div>
    <!--  {{test}}-->
      <br><br>
      {{finished}}
      <br><br>
    <!--  {{myData}}-->
     {{indexByIndexType}}-->
     <!--  {{breakdownByMktandIC}}-->
    <!--  {{mySeries}}-->
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
  {"mkt":"J203","Name":"FTSE/JSE ALSI Share Index (J203)", "id":1},
  {"mkt":"J200","Name":"FTSE/JSE Top 40 Index (J200)", "id":2},
  {"mkt":"J250","Name":"FTSE/JSE Financials & Industrials Index (J250)", "id":3},
  {"mkt":"J257","Name":"FTSE/JSE Industrials Index (J257)", "id":4},
  {"mkt":"J258","Name":"FTSE/JSE Resources Index (J258)", "id":5}]

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

// new const added
const industryList=[
  { "name": 'Oil & Gas', "code": 0 },
  { "name": 'Basic Materials', "code": 1 },
  { "name": 'Industrials', "code": 2 },
  { "name": 'Consumer Goods', "code": 3 },
  { "name": 'Health Care', "code": 4 },        
  { "name": 'Consumer Services', "code": 5 },
  { "name": 'Telecommunications', "code": 6 },
  { "name": 'Utilities', "code": 7 },
  { "name": 'Financials', "code": 8 },
  { "name": 'Technology', "code": 9 }, 
]

// new var added
var IndCodeArr = []



import Vue from 'vue/dist/vue.js';


Vue.component("tab-table", {
  props:['data'],
  template: `<all-breakdowns :entries="data.breakdownByMktandIC" v-bind:Heading="data.breakdownCaption"></all-breakdowns>`
});

Vue.component("tab-barchart", {
  props:['data'],
  template: `<latest-transactions-chart :Heading="data.breakdownCaption" :Series="data.mySeries" :type="data.type" :stacked="data.stacked"></latest-transactions-chart>`
});

Vue.component("tab-linechart", {
  props:['data'],
  template: `<latest-transactions-chart :Series="data.mySeries" :type="data.type" :stacked="data.stacked"></latest-transactions-chart>`
});

Vue.component("tab-indextable", {
  props:['data'],
  template: `<index-tab-alt :entries="data.indexData" :Quarter="data.Quarter" ></index-tab-alt>`
});

Vue.component("tab-sharetable", {
  props:['data'],
  template: `<share-tab-alt :entries="data.ShareData" :Quarter="data.Quarter" ></share-tab-alt>`
});

export default {
  name: 'app',
  components: { 
  },
  data() {
    return {
      // new data added
      value: [ // default value(s) of multiselect
        { name: 'Oil & Gas', code: 0 },
        //{ name: 'Javascript', code: 'js' }
      ],
      options: [ // array to use inside multiselect
        { "name": 'Oil & Gas', "code": 0 },
        { "name": 'Basic Materials', "code": 1 },
        { "name": 'Industrials', "code": 2 },
        { "name": 'Consumer Goods', "code": 3 },
        { "name": 'Health Care', "code": 4 },        
        { "name": 'Consumer Services', "code": 5 },
        { "name": 'Telecommunications', "code": 6 },
        { "name": 'Utilities', "code": 7 },
        { "name": 'Financials', "code": 8 },
        { "name": 'Technology', "code": 9 },  
        // name: 'Vue.js', code: 'vu' },
        //{ name: 'Javascript', code: 'js' },
        //{ name: 'Open Source', code: 'os' }
      ],

      shareTableView : [], 
      BABetaOutput : [], 
      //table constants
      tabs: ["Table", "Barchart", "Linechart"],
      indextabs: ["Table", "Barchart", "Linechart"],

      //BD data
      mySeries: [],
      breakdownByMktandIC : [],
      allBreakdownsView:[],
      //fields selected for BD
      currentTab: "Table",
      selectedMktProxy: "\{Proxy\}",
      selectedIndex : "\{Index\}",
      selectedStat: "\{statistic\}",

      //Index tables data
      indexSeries: [],
      indexByIndexType:[],
      indexTableView : [],
      //fields selected for Index tabs
      currentIndexTab: "Table",
      selectedIndexType: "\{Index Type\}",
      selectedPeriod: "\{Period\}",

      //share table data
      shareSeries: [],
      shareByICB: [],
      currentShareTab: "Table",
      selectedIndustry: "\{Industry\}",
      selectedSharePeriod: "\{Period\}",

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
      indexCaption: "Index table of Betas for <Index Type> in the period <Period>",
      shareCaption: "Share table of Betas for <ICB Industry> in the period <Period>"
    }
  },
  computed: {
      currentTabComponent() {
          return "tab-" + this.currentTab.toLowerCase();
        },
      
      currentProperties(){
        if (this.currentTab==="Linechart"){
          return{
            data:{
              //breakdownCaption: this.breakdownCaption,
              mySeries: this.mySeries,
              type: 'line',
              stacked: false
            }
          };
        }
        if (this.currentTab==="Barchart"){
          return{
            data:{
              breakdownCaption: this.breakdownCaption,
              mySeries: this.mySeries,
              type: 'bar',
              stacked: true
            }
          };
        }
        return{
          data:{
              breakdownCaption: this.breakdownCaption,
              breakdownByMktandIC: this.breakdownByMktandIC
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
        return{
          data:{
              indexData: this.indexByIndexType,
              Quarter: this.selectedPeriod
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
        return{
          data:{
              ShareData: this.shareByICB,
              Quarter: this.selectedSharePeriod
            }
        };
      }  
  },
  methods: {
    /*
    async getbreakdown(){
      try{
        const response = await DataService.getbreakdown()
        this.allBreakdownsView=response.data
      }catch(err){
        this.test=err //console.log() doesn't work so I made atest container for the sake of error checking
      }
    },*/
    /*
    async getSharetable(){
      try{
        const response = await DataService.getSharetable()
        this.shareTableView=response.data
      }catch(err){
        this.test=err
      }
    },
    */
  /*
    async getIndextable(){
      try{
        const response = await DataService.getIndextable()
        this.indexTableView=response.data
      }catch(err){
        this.test=err
      }
    },*/

    // new function added
    

    async getSpecBreakdown(){
      this.breakdownCaption="Breakdown of " +this.selectedStat + " in the "+ this.selectedIndex +" Index using "+ this.selectedMktProxy+ " as proxy"
      try{
        
        if (this.selectedMktProxy!="\{Proxy\}" && this.selectedIndex!="\{Index\}" && this.selectedStat!="\{statistic\}"){

          const response = await DataService.getSpecBreakdown(this.selectedIndex,this.selectedMktProxy.slice(-5,-1))
          const FTSE = await DataService.getICB()
          var BDdata=[] //container
          var Ceres=[]
          // new section added
          // console.log(IndCodeArr)
          var allIndustries = FTSE.data.map(item => item.Industry).filter((value, index, self) => self.indexOf(value) === index)
          var industries = [];
          IndCodeArr.forEach(i => industries.push(allIndustries[i]))
          ////
          // var industries=FTSE.data.map(item => item.Industry).filter((value, index, self) => self.indexOf(value) === index)
          
          //this for loop loads BDdata with the desired form for the breakdown table
          for (let i = 0; i < industries.length; i++) {
            var hello={"Industry":industries[i]} //create a dummy object which we will populate
            var please=response.data.filter(industry=>industry.Industry===industries[i]) //filter the breakdown data by a particular industry
            for (let j=0;j< please.length;j++){
              hello["Y"+parseInt(please[j]["Year"])+"Q"+parseInt(please[j]["Quarter"])]=parseFloat(please[j][this.selectedStat]) //extract stat in order of periods
            }
            for (let j=0;j<this.Periods.length;j++){
              if (!(this.Periods[j]["YQ"] in hello)){
                hello[this.Periods[j]["YQ"]]=0
              }
            }
            BDdata.push(hello)

          }
          this.breakdownByMktandIC=BDdata
          
          //restructuring data for the chart of breakdowns
          for (let i=0; i<industries.length;i++){
            const temp=BDdata.filter(industry=>industry.Industry===industries[i])[0]
            var hello={"text":industries[i], "values":[]}
            //this.finished=temp
            //this.Periods[0]["YQ"]
            for (let j=0;j<this.Periods.length;j++){
              hello["values"].push(temp[this.Periods[j]["YQ"]])
              
            }
            Ceres.push(hello)
          }
          this.mySeries=Ceres
          //this.myData["scaleX"]["labels"]= this.Periods.map(item => item.YQ).filter((value, index, self) => self.indexOf(value) === index) //setting up periods for graph,
          //this.finished=this.Periods.map(item => item.YQ).filter((value, index, self) => self.indexOf(value) === index) //setting up periods for graph,
        }
      }catch(err){
        this.finished=err
        this.breakdownByMktandIC=[]
    }
    },

    async getSpecIndex(){
      
      try{
        if(this.selectedIndexType!="\{Index Type\}"){
          const response = await DataService.getIndextable()
        
          var temp=response.data.filter(iT=> iT["Index Type"]===this.selectedIndexType) //filter by selected index type
          //this.indexByIndexType=temp
          var Codes=temp.map(item => item.Code).filter((value, index, self) => self.indexOf(value) === index) //get list of codes under the index type
          //this.indexByIndexType=Codes
          var Ceres=[]
          

          for (let i = 0; i < Codes.length; i++) {
             //create a dummy object which we will populate
            var please=temp.filter(item=>item.Code===Codes[i]) //filter to get all the data for this code
            var Name=please[0].Name //get name of code, this is a cheat should use filter for robustness
            //this.finished=Name
            //this.test=please
            
            for (let p of this.Periods){
              var hello={"Code":Codes[i], "Name":Name, "YQ":p.YQ}
              var filtered=please.filter(item=>item.Year===p.Year && item.Quarter===p.Quarter)              
              if(filtered.length!=0){
                hello["Data Points"]=parseInt(filtered[0]["Data Points"])
                filtered.map(o=>hello[o.MarketID]=parseFloat(o.Beta))
                filtered.map(o=>hello["M"+o.MarketID]=[parseFloat(o["p Value Beta"]),parseFloat(o["SE Beta"]),parseFloat(o.Alpha),parseFloat(o["p Value Alpha"]),parseFloat(o["SE Alpha"])])
                
              }
              Ceres.push(hello)
            }
            //this.finished=Ceres
    
          }
          this.indexByIndexType=Ceres
          
        }
      }catch(err){
        console.log(this.err)
        this.finished=err
      }
    },

    async getSpecShareTab(){
      //this.shareCaption=this.selectedIndustry+" "+this.selectedSharePeriod
      try{
        if(this.selectedIndustry!="\{ICB Industry\}"){
          const response = await DataService.getSharetable()
        
          var temp=response.data.filter(iT=> iT["Industry"]===this.selectedIndustry) //filter by selected index type
          //this.indexByIndexType=temp
          var Codes=temp.map(item => item.Instrument).filter((value, index, self) => self.indexOf(value) === index) //get list of codes under the index type
          //this.indexByIndexType=Codes
          var Ceres=[]
          

          for (let i = 0; i < Codes.length; i++) {
             //create a dummy object which we will populate
            var please=temp.filter(item=>item.Instrument===Codes[i]) //filter to get all the data for this code
            var Name=please[0].Name //get name of code, this is a cheat should use filter for robustness
            //this.finished=Name
            //this.test=please
            
            for (let p of this.Periods){
              //, "Name":Name could pull this using api later
              var hello={"Code":Codes[i], "YQ":p.YQ}
              var filtered=please.filter(item=>item.Year===p.Year && item.Quarter===p.Quarter)        
              //this.finished=filtered      
              if(filtered.length!=0){
                hello["Data Points"]=parseInt(filtered[0]["Data Points"]) //fix this in MSServer
                hello["Cap"]=filtered[0]["Cap"]
                hello["Start Date"]=filtered[0]["Start Date"]
                hello["End Date"]=filtered[0]["End Date"]
                hello["% Days Traded"]=Math.round(parseFloat(filtered[0]["% Days Traded"])*10000)/100
                //hello["p Value Beta"]=
                filtered.map(o=>hello[o.MarketID]=parseFloat(o.Beta))
                filtered.map(o=>hello["M"+o.MarketID]=[parseFloat(o["p Value Beta"]),parseFloat(o["SE Beta"]),parseFloat(o.Alpha),parseFloat(o["p Value Alpha"]),parseFloat(o["SE Alpha"])])
              }
              Ceres.push(hello)
            }
           //this.finished=Ceres
    
          }
          this.shareByICB=Ceres
          
        }
      }catch(err){
        console.log(this.err)
        this.test=err
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
    
    async genIndexList(mutiselectInd){
      try{
        var multiIndArr = JSON.parse(JSON.stringify(mutiselectInd));
        IndCodeArr.length = 0
        multiIndArr.forEach(function(item) {
        IndCodeArr.push(item.code)
        this.getSpecBreakdown()
        });
        console.log(IndCodeArr)             
      }
      catch(err){
        console.log("not working");
      }
    },

    changePeriod (event) {
      //if (this.selectedPeriod!="\{period\}"){
        this.selectedPeriod = event.target.options[event.target.options.selectedIndex].text
        this.indexCaption="Index table of Betas for " +this.selectedIndexType + " in the period "+ this.selectedPeriod 
        //this.getSpecIndex()
      //}
    },
    changeIndexType (event) {
      //if (this.selectedIndexType!="\{Index Type\}"){
        this.selectedIndexType = event.target.options[event.target.options.selectedIndex].text
        this.indexCaption="Index table of Betas for " +this.selectedIndexType + " in the period "+ this.selectedPeriod 
        this.getSpecIndex()
      //}
    },
    changeMktProxy (event) {
      //if (this.selectedMktProxy!="\{Proxy\}"){
        this.selectedMktProxy = event.target.options[event.target.options.selectedIndex].text
        this.getSpecBreakdown()
      //}
    },
    changeIndex (event) {
      //if (this.selectedIndex!="\{Index\}"){
        this.selectedIndex = event.target.options[event.target.options.selectedIndex].text
        this.getSpecBreakdown()
      //}
    },
    changeStat (event) {
      //if (this.selectedStat!="\{statistic\}"){
        this.selectedStat = event.target.options[event.target.options.selectedIndex].text
        this.getSpecBreakdown()
      //}
    },

    changeIndustry(event){
      this.selectedIndustry = event.target.options[event.target.options.selectedIndex].text
      this.shareCaption = "Share table of Betas for " +this.selectedIndustry+" (ICB) in the period "+this.selectedSharePeriod
      this.getSpecShareTab()
    },

    changeSharePeriod(event){
      this.selectedSharePeriod = event.target.options[event.target.options.selectedIndex].text
      this.shareCaption = "Share table of Betas for " +this.selectedIndustry+" (ICB) in the period "+this.selectedSharePeriod
    },


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
    
    
    //this.getbreakdown();
    //this.getSharetable();
    //this.getIndextable();
    this.getSpecBreakdown();
    this.getIndexTypes();
    this.getPeriods();
    this.getSpecIndex();
    this.getSpecShareTab();
    this.genIndexList();

    
    
    this.changePeriod();
    this.changeIndexType();
    this.changeMktProxy();
    this.changeIndex();
    this.changeStat();
    this.changeIndustry();
    this.changeSharePeriod();
       
    //this.getBABetaOutput();
  }
}
</script>
<style scoped>

h3 {
  color: #5d7d9a;
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  font-weight: bold;
  background: white;
  padding-left: 0;
  text-align: left;
            
}
</style>