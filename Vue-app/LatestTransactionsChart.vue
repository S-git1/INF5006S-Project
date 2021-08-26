<template>


  <div class="row">
    <div class="col-lg-10">
      <zingchart :data="chartConfig" ref="barchart" :caption="noData" />
      
    </div>

    <div v-if="ShowForLine()" class="col-lg-2 text">      
      <treeselect v-model="value" :multiple="true" :options="options" :limit='5' placeholder="Select Index"  @input="IndexSelect(value)"/>
      <treeselect-value :value="value" />
      <br>{{value}}
    </div>
  </div>
</template>


<script>
import 'zingchart/es6';
//import zingchartVue from 'zingchart-vue';
// The chart currently has no function to choose a range of dates. It displays the data points for the entire date range.

export default {
  name: 'latest-transactions-chart',
  props: ['Heading','Series','type','stacked', 'headers','tick'],
  
  data () {
    return {
      con: 'line',
      //con: '',         


      // define the default value
        value: null,
        // define options
        options: [],

        // [{
        //   id: this.Series.map(value => value.IndexType)[0],
        //   label: this.Series.map(value => value.IndexType)[0],
        //   children: [ {
        //     id: this.Series.map(value => value.text)[0],
        //     label: this.Series.map(value => value.text)[0],
        //   }, {
        //     id: this.Series.map(value => value.text)[1],
        //     label: this.Series.map(value => value.text)[1],
        //   },
        //   {
        //     id: this.Series.map(value => value.text)[3],
        //     label: this.Series.map(value => value.text)[3],
        //   }],
        // }]       

        selections: [],
    }
  },
  computed: {
    noData(){
      if(this.Series===null){
          return "No Data Available" ;
      }
      return "";
    },
    chartConfig(){
      return {
        type: this.type,
          plot: {
            stacked: this.stacked,
            
            barWidth: '50%',
            "animation": {
            "effect": "ANIMATION_SLIDE_LEFT",
            "sequence": 0,
            "speed": 800,
            "delay": 200
            }
          },
          /*title: {
            text:  this.Heading,
            color: '#5D7D9A',
            align: 'left',
            padding: '30 0 0 35'
          },*/
          scaleX: {
            text: "Quarters",
            
            values: this.headers,
            
            tick:{
              visible: this.tick,
              _lineColor: '#D8D8D8',
              size:20,
              placement:"cross"
            },
            "itemsOverlap": true,
            item: {
              color: '#6C6C6C',
              angle: '-80',
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
            fontFamily: 'Georgia'
          }
        },
        plotarea: {
          margin: '130 10 90 60'
        },
        
        legend: {
          layout: '3x4',
          align: 'right',
          verticalAlign: 'top',
          margin: '5 0 0 0',
          padding: '5px',
          borderRadius: '5px',
          header: {
            text: 'Industry (PS:you can select me)',
            color: '#5D7D9A',
            padding: '10px'
          },
          item: {
            color: '#5D7D9A'
          }
        },
        series: this.Series.filter(ind => this.selections.includes(ind.IndexType) || this.selections.includes(ind.text)) // this line applies the filter from the treeselect
        // series: this.Series.filter(ind => ["J200", "J202", "J203"].includes(ind.text))
      };
    }
  },
  methods: { 
    getTreeList: function(){ // function to generate treelike list for tree-select
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

    onChange () {
      console.log(this.months)
    },
    ShowForLine(){
      // console.log(JSON.stringify(this.Series))
      return this.type===this.con;
      // this.Series...some loop
      //return false;
    },
    addTag (newTag) {
      const tag = {
        name: newTag,
        code: newTag.substring(0, 2) + Math.floor((Math.random() * 10000000))
      }
      this.options.push(tag)
      this.value.push(tag)
    }
  },
  beforeMount(){ // change to created? need to check again; supposed to call function getTreeList() when page is first loaded
      this.getTreeList()
    },
}

</script>
