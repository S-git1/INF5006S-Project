<template>
  <div>
    <v-client-table id="tbl" :data="QuarterData" :columns="TblType" :api-mode="false" :options="options" :filterable="false"></v-client-table>
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
        filterable: false,
        perPage:200,
        
        cellClasses:{
          
          J200: [
            {
              class:'blue',
              condition: row => row.MJ200[0]<=0.01
            },
            {
              class:'green',
              condition: row => row.MJ200[0]<=0.05 && row.MJ200[0]>0.01
            },
            {
              class:'red',
              condition: row=> row.J200<0
            }

          ],
          J203: [
            {
              class:'blue',
              condition: row => row.MJ203[0]<=0.01
            },
            {
              class:'green',
              condition: row => row.MJ203[0]<=0.05 && row.MJ203[0]>0.01
            },
            {
              class:'red',
              condition: row=> row.J203<0
            }

          ],
          J250: [
            {
              class:'blue',
              condition: row => row.MJ250[0]<=0.01
            },
            {
              class:'green',
              condition: row => row.MJ250[0]<=0.05 && row.MJ250[0]>0.01
            },
            {
              class:'red',
              condition: row=> row.J250<0
            }

          ],
          J257: [
            {
              class:'blue',
              condition: row => row.MJ257[0]<=0.01
            },
            {
              class:'green',
              condition: row => row.MJ257[0]<=0.05 && row.MJ257[0]>0.01
            },
            {
              class:'red',
              condition: row=> row.J257<0
            }

          ],
          J258: [
            {
              class:'blue',
              condition: row => row.MJ258[0]<=0.01
            },
            {
              class:'green',
              condition: row => row.MJ258[0]<=0.05 && row.MJ258[0]>0.01
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
        if (this.columns!=null){
         return this.entries;  
        }
        console.log(this.entries);
        var temp=this.entries.filter(o=>o.YQ===this.Quarter).filter(o=>o["Data Points"]!=null);
        //console.log(temp);
        return temp;
      }catch(err){
        return [];
      }
    },
    TblType:function(){
      if (this.type==="index"){
        return [ "Code", "Name","Data Points","J203","J200","J250","J257","J258"];
      }
      else if (this.type==="share") {
        return [ "Code", "Cap", "% Days Traded","Data Points","Start Date", "End Date", "J203","J200","J250","J257","J258"];
      }
      else if (this.columns!=null){
        console.log(this.entries);
        this.columns.unshift("Industry");
        return this.columns;
      }
      return [];
    }
  }
};
</script>

<style>
.green{
  color: green;
}
.blue{
  color: blue;
}
.red{
  color: red;
}
.VueTables__limit {
  display: none;
}
</style>