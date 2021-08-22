<!-- The table does not give the user an option to select a preferred index to display. This needs to be added later. -->
<template>
  <div>
    <zing-grid
      ref="myGrid"

      layout="row"
      
      style="width: 100%;"
      sort
      
  
      
      :data.prop="QuarterData"
    > <!-- added `width` and `draggable` together to make horizontal scroll possible -->
      <zg-colgroup> <!-- a function to get the names of the columns in the SQL tables needs to be written. Hardcoded for demonstrative purposed for now; date column not needed -->
      <!--  <zg-column index='MarketID' header='Market ID' type='select' 
        type-select-options='J203,J200,J250,J257,J258'></zg-column>-->
        <zg-column index='Code' header='Code' type='text' ></zg-column>
        <zg-column index='Name' header='Name' type='text' ></zg-column>
        <!--<zg-column index='Index Type' header='Index Type' type='text' ></zg-column>-->
        <!--<zg-column index='Start Date' header='Start Date' type='date' ></zg-column>-->
        <!--<zg-column index='End Date' header='End Date' type='date' ></zg-column>-->
        <!--<zg-column index='% Days Traded' header='% Days Traded' type='float' ></zg-column>-->
        <zg-column index='Data Points' header='Data Points' type='int' ></zg-column>
        <!--<zg-column index='Alpha' header='Alpha' type='float' ></zg-column>-->
        <zg-column index='J203' header='J203' type='float' ></zg-column>
        <zg-column index='J200' header='J200' type='float' ></zg-column>
        <zg-column index='J250' header='J250' type='float' ></zg-column>
        <zg-column index='J257' header='J257' type='float' ></zg-column>
        <zg-column index='J258' header='J258' type='float' ></zg-column>
        <!--<zg-column index='YQ' header='YQ' type='text' ></zg-column>-->
        <!--<zg-column index='SE Alpha' header='SE Alpha' type='float' ></zg-column>-->
        <!--<zg-column index='SE Beta' header='SE Beta' type='float' ></zg-column>-->
        <!--<zg-column index='p-Value Alpha' header='p-Value Alpha' type='float' ></zg-column>-->
        <!--<zg-column index='p-Value Beta' header='p-Value Beta' type='float' ></zg-column>-->
        <!--<zg-column index='R2' header='R2' type='float' ></zg-column>-->
        <!--<zg-column index='Total Risk' header='Total Risk' type='float' ></zg-column>-->
        <!--<zg-column index='Unique Risk' header='Unique Risk' type='float' ></zg-column>-->
      <!--  <zg-column index='Year' header='Year' type='float' ></zg-column>-->
      <!--  <zg-column index='Quarter' header='Quarter' type='select' type-select-options="1,2,3,4"></zg-column>-->
      </zg-colgroup>
    </zing-grid>
  </div>
</template>

<script>
export default {
  name: "index-tab-alt",
  props: ['entries','Quarter'],
  computed:{
    QuarterData(){
      try{
        return this.entries.filter(o=>o.YQ===this.Quarter).filter(o=>o["Data Points"]!=null);
      }catch(err){
        return this.entries;
      }
    }
  }
}
</script>

<style>

zg-head-cell {
  background: white;
  color: #5d7d9a;
  font-size: 1rem;
}
zg-row:nth-child(odd) {
  background: rgb(250, 250, 250);
}
zg-control-bar {
  display: none;
}
zg-caption {
color: #5d7d9a;
font-family: "Avenir", Helvetica, Arial, sans-serif;
font-weight: bold;
background: white;
padding-left: 0;
font-size: 1.4rem;
height: 54px;
text-align: left;

}
zing-grid {
  border: 0px;
}

zing-grid input[type="text"], zing-grid input[type="number"]{
  border-radius: 5px;
}

</style>
