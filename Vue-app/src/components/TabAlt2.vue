<template>
  <div >
    
    <v-client-table id="tbl" :data="QuarterData" :columns="TblType" :api-mode="false" :options="options" :filterable="false"></v-client-table>
    <!--<button @click="download" class="btn btn-link">download</button>-->
    
  </div>
</template>

<script>
//import HelloWorld from "./components/HelloWorld";

export default {
  name: "tab-alt2",
  components: {
    //HelloWorld
  },
  props: ["entries", "Quarter","type","columns"],
  data() {
    return {
      //columns: [],
      dateColumns: ['Start Date', 'End Date'],
      dateFormat: 'DD-MM-YYYY',
      tableData:[],
      options: {
        filterable:false,
        perPage:200,
        
        cellClasses:{
          
          J200: [
            {
              class:'blue',
              condition: row => row.MJ200<=0.01
            },
            {
              class:'green',
              condition: row => row.MJ200<=0.05 && row.MJ200>0.01
            },
            {
              class:'red',
              condition: row=> row.J200<0
            }

          ],
          J203: [
            {
              class:'blue',
              condition: row => row.MJ203<=0.01
            },
            {
              class:'green',
              condition: row => row.MJ203<=0.05 && row.MJ203>0.01
            },
            {
              class:'red',
              condition: row=> row.J203<0
            }

          ],
          J250: [
            {
              class:'blue',
              condition: row => row.MJ250<=0.01
            },
            {
              class:'green',
              condition: row => row.MJ250<=0.05 && row.MJ250>0.01
            },
            {
              class:'red',
              condition: row=> row.J250<0
            }

          ],
          J257: [
            {
              class:'blue',
              condition: row => row.MJ257<=0.01
            },
            {
              class:'green',
              condition: row => row.MJ257<=0.05 && row.MJ257>0.01
            },
            {
              class:'red',
              condition: row=> row.J257<0
            }

          ],
          J258: [
            {
              class:'blue',
              condition: row => row.MJ258<=0.01
            },
            {
              class:'green',
              condition: row => row.MJ258<=0.05 && row.MJ258>0.01
            },
            {
              class:'red',
              condition: row=> row.J258<0
            }

          ]
}
        // see the options API
      }
    };
  },
  computed: {
    
    QuarterData: function(){
      
      try{
        if (this.type==="index"||this.type==="share"){
         return this.entries.filter(o=>o.YQ===this.Quarter).filter(o=>o["Data Pts"]!=null);
        }
        //console.log(JSON.stringify(this.entries));
        
        //console.log(temp);
        return this.entries;
      }catch(err){
        return [];
      }
    },
    TblType:function(){
      //console.log(JSON.stringify(this.columns!==undefined))
      if (this.type==="index"){
        return [ "Code", "Name","Data Pts","J203","J200","J250","J257","J258"];
      }
      else if (this.type==="share") {
        return [ "Code", "Cap", "% Days Traded","Data Pts","Start Date", "End Date", "J203","J200","J250","J257","J258"];
      }
      else if (this.columns!==undefined){
        
        this.columns.unshift("Industry");
        //console.log(JSON.stringify(this.columns));
        return this.columns;
      }
      return [];
    }
  },
  methods:{
    download: function(){
      consol.log("file would download");
      

      
    },
  }
  
};
</script>

<style>
.green{
  color: rgb(78, 204, 19);
}
.blue{
  color: #0084ff;
}
.red{
  color: red;
}
.VueTables__limit {
  display: none;
}
</style>