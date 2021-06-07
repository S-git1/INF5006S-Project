<template>
    <zingchart :data="chartConfig" :height="'100%'" style="flex:2" ref="chart"/>
</template>
<script>
// The chart currently has no function to choose a range of dates. It displays the data points for the entire date range.
export default {
  props: ['entries'],
  computed: {
    values() {
      return this.entries.map(o => {
        return [parseFloat(o.Date), parseFloat(o.Beta)] // modified; give x-axis values first than y-axis values

      }// ,console.log(this) // line to test what the values() is returning
      )
    },    
    chartConfig() {
      
      return {
        type: 'line',
        title: {
          text: 'Index data over time ("Beta" chosen for now)', // "Beta" chosen from dbo.tbl_BA_Outputs.js file for demonstrative purposes for the time being. 
          adjustLayout: true,
          align: 'left',
          margin: 0,
          fontColor: '#5d7d9a'
        },
        subtitle: {
          text: '',
          align: 'left',
          fontColor: '#5d7d9a'
        },
        plot: {
          aspect: 'spline',
          marker: {
            visible: true, // modified from `false` to `true`
          },

        },
        // crosshairX:{
        //   plotLabel :{
        //     negation: "currency",
        //     text: '$%v',
        //     'thousands-separator': ","
        //   },
        //   marker: {
        //     visible: false,
        //   }
        // },
        tooltip: { 
          visible: false,

        },
        plotarea: {
          margin: '35 35 60 60'

        },
        scaleX: {
          label: {
            text: 'Time'
          },
          // values: "1300:4100:400" // select range of x-axis
          // transform: {
          //   type: 'date',
          //   all: '%M %d',
          // }
        },
        scaleY: {
          label: {
            text: 'Beta',
          },
          // short:true,
          // shortUnit: 'K',
        },
        
        series: [{ // where you input the data
          values: this.values,
        }

        ],
      };
    }
  },
}

</script>
