<template>
  <div class="row">
    <div class="col-lg-10">
      <zingchart :data="chartConfig" ref="barchart" />
    </div>
    <div v-if="ShowForLine()" class="col-lg-2 text">
      <label class="typo__label">Customisation</label>
      <multiselect v-model="value" tag-placeholder="Add this as new tag" placeholder="Search or add a tag" label="name" track-by="code" :options="options" :multiple="true" :taggable="true" @tag="addTag"></multiselect>
      <pre class="language-json"><code>{{ value  }}</code></pre>
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
      value: [
        { name: 'Javascript', code: 'js' }
      ],
      options: [
        { name: 'Vue.js', code: 'vu' },
        { name: 'Javascript', code: 'js' },
        { name: 'Open Source', code: 'os' }
      ]
    }
  },
  computed: {
    
    chartConfig(){
      return {
        type: this.type,
          plot: {
            stacked: this.stacked,
            
            barWidth: '50%',
            "animation": {
            "effect": "ANIMATION_SLIDE_BOTTOM",
            "sequence": 0,
            "speed": 600,
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
            alpha: 0,
            text: '%v',
            transform: {
              type: 'date',
              all: '%M %d, %Y<br>%g:%i %a'
            },
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
            text: 'Industry',
            color: '#5D7D9A',
            padding: '10px'
          },
          item: {
            color: '#5D7D9A'
          }
        },
        series: this.Series
      };
    }
  },
  methods: {
    ShowForLine(){
      //return this.type===this.con;
      return false;
    },
    addTag (newTag) {
      const tag = {
        name: newTag,
        code: newTag.substring(0, 2) + Math.floor((Math.random() * 10000000))
      }
      this.options.push(tag)
      this.value.push(tag)
    }
  }
}

</script>
