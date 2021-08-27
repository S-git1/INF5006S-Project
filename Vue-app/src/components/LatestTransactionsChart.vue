<template>

<div>
  <div v-if="ShowForLine()" class=" text">  
    <treeselect v-model="value" :multiple="true" :options="options" :limit='5' placeholder="Select Index"  @input="IndexSelect(value)"/>
      <treeselect-value :value="value" />
  </div>
  <zingchart :data="chartConfig" ref="chart" :caption="noData" />

</div>
</template>
<script>
import 'zingchart/es6';
import Treeselect from '@riophae/vue-treeselect';
import '@riophae/vue-treeselect/dist/vue-treeselect.css'
//Vue.component('treeselect', Treeselect)
//import zingchartVue from 'zingchart-vue';
// The chart currently has no function to choose a range of dates. It displays the data points for the entire date range.
export default {
  name: 'latest-transactions-chart',
  components:{
    Treeselect
  },
  props: ['Heading','Series','type','stacked', 'headers','tick','opts', 'statistic',"tbl"],
  data () {
    return {
      con: 'line',

      // define the default value
      value: null,
      // define options
      options: [],

      selections: [],
    }
  },
  computed: {
    
    chartConfig(){
      return {
        type: this.type,
          plot: {
            stacked: this.stacked,            
            barWidth: '40%',
            padding: '20 20 20 20'
            /*"animation": {
            "effect": this.type==="line"? "ANIMATION_SLIDE_LEFT":"ANIMATION_SLIDE_BOTTOM",
            "sequence": 0,
            "speed": 800,
            "delay": 200
            }*/
          },
          title: {
            text:  this.noData(),
            color: '#5D7D9A',
            align: 'left',
            padding: '0 0 0 40'
          },
          "scale-y": {
            label: {
              text:this.ShowForLine()? "beta":this.statistic,
             
          
            
              
             
              fontSize: 16,
           
             
              padding: '5px 20px'
            },
            markers: [
              {
                type: "area",
                range: [1, 10],
                backgroundColor: "#5D7D9A",
                alpha: 0.1
              },
              {
                type: "area",
                range: [0, -10],
                backgroundColor: "#5D7D9A",
                alpha: 0.1
              }
            ]
          },
          scaleX: {
            label: {
              text:"Quarters",
              offsetY:25,
              'font-size':20
            },
            values: this.headers,
            //values: this.value.sort(function(a,b){return a.id-b.id;}).map(item => item.YQ).filter((value, index, self) => self.indexOf(value) === index),
            
            tick:{
              visible: this.tick,
              _lineColor: '#D8D8D8',
              size:20,
              placement:"cross"
            },
            
            item: {
              color: '#6C6C6C',
              angle: '-30',
              "itemsOverlap": true,
              }
          },
        tooltip: {
          visible: false
        },
        crosshairX: {
          plotLabel: {
            fontColor: '#333',
            backgroundColor: '#fff',
            borderRadius: 5,
            borderColor: '#EEE',
            padding: 10
          },
          scaleLabel: {
            alpha: 1,
            text: '%v',
            fontFamily: 'Georgia',
            
          }
        },
        plotarea: {
          margin: '100 25 90 50',
         
        },
        
        legend: {
          layout: '2x5',
          align: 'right',
          verticalAlign: 'top',
          "max-items": 10,
          "overflow": "scroll",
          "scroll": {
            "bar": {
              "background-color": "#c9c8cc",
            },
            "handle": {
              "background-color": "#5D7D9A",
              "border-left": "2px #5D7D9A",
              "border-right": "2px #5D7D9A",
              "border-top": "2px #5D7D9A",
              "border-bottom": "2px #5D7D9A",
              "border-radius": "15px"
            }
          },
          "x": "75%",
          "y": "25%",
          header: {
            text: 'Industry (PS:you can select me)',
            color: '#5D7D9A',
            
          },
          item: {
            color: '#5D7D9A'
          }
        },
        series: (this.opts!="null")? this.DataProcess(): this.series
      };
    }
  },
  methods: {
    ShowForLine(){
      // console.log(JSON.stringify(this.Series))
      return this.tbl==="I"||this.tbl==="S";
      // this.Series...some loop
      //return false;
    },
    getTreeList: function(){ // function to generate treelike list for tree-select
      if (this.Series!==undefined){
        if(this.Series.length!=0){
          
            var indTypes = this.Series.map(value => value.IndexType);
            var distinctIndTypes = [...new Set(indTypes)]; // discard duplicate index types and keep unique only
            // console.log(distinctIndTypes);
            // var shareType = this.Series.map(value => value.text);
            var shareByInd = [];
            for (let j = 0; j < distinctIndTypes.length; j++) {
              var tempArr = []
              var tempGroup = this.Series.filter(ind=> ind.IndexType == distinctIndTypes[j]).map(val => val.text)
              for (let k = 0; k < tempGroup.length; k++) {
                tempArr.push({
                  id: tempGroup[k],
                  label: tempGroup[k]
                })
              }
              shareByInd.push(tempArr)	
            };
            // parent array merged with child array
            var dict = [];
            for (let i = 0; i < distinctIndTypes.length; i++){        
              dict.push({
                id: distinctIndTypes[i],
                label: distinctIndTypes[i],
                children: shareByInd[i]
              })
            };
            this.options = dict // set options variable to have array of tree options
            // console.log(JSON.stringify(dict[0]));
            // console.log(JSON.stringify(dict[1]));
            // console.log(JSON.stringify(dict[2]));
            // console.log(JSON.stringify(dict[3])); 
          
          
        }
      }
    },    
    IndexSelect(x){ // function to receive output from 
      // console.log(JSON.stringify(x));
      var selectionsArr = JSON.parse(JSON.stringify(x));
      var selectionsF = [];
      selectionsArr.forEach(function(item) {
        selectionsF.push(item);
      }); 
      // console.log(selectionsF);
      this.selections = selectionsF;
      // thischartConfig();
    },
    
    noData(){
      //console.log(JSON.stringify(this.Series));
      if(this.ShowForLine()){
        if(this.Series===undefined){
            return "No Data Available ";
        }
        else if(this.Series.length===0){
            return "No Data Available ";
        }
        this.getTreeList();
        return "Betas w/ "+this.Heading+" as Mkt Proxy";
      }
      return "";
    },
    DataProcess(){
      console.log(this.ShowForLine())
      console.log(JSON.stringify(this.Series))
      if(this.ShowForLine()==true){
        return this.DataProcess2();
      }
      return this.DataProcess1();
    },
    DataProcess1(){
      
      if (this.headers==null){
        return [];
      }
      else if(this.headers.length===0){
        return [];
      }
      else if(this.headers.length<15){
        let temp=JSON.parse(JSON.stringify(this.Series)); // this line applies the filter from the treeselect));
        for (let item of temp){
          item.values=this.opts.map(i=>item.values[i]);
        }
        return temp;
      }
      return this.Series // this line applies the filter from the treeselect;
    },
    DataProcess2(){
      if (this.headers==null||this.headers.length===0){
        return [];
      }
      else if(this.headers.length<15){
        let temp=JSON.parse(JSON.stringify(this.Series.filter(ind => this.selections.includes(ind.IndexType) || this.selections.includes(ind.text)))); // this line applies the filter from the treeselect));
        for (let item of temp){
          item.values=this.opts.map(i=>item.values[i]);
        }
        console.log(JSON.stringify(temp));
        return temp;
      }
      return this.Series.filter(ind => this.selections.includes(ind.IndexType) || this.selections.includes(ind.text)) // this line applies the filter from the treeselect;
    }
  },
  beforemounted(){
     // change to created? need to check again; supposed to call function getTreeList() when page is first loaded
      this.getTreeList();
    
  }
}
</script>