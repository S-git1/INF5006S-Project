<!-- The table does not give the user an option to select a preferred index to display. This needs to be added later. -->
<template>
  <zing-grid
    ref="myGrid"
    layout="row"
    scroll
   
    style="width: 100%;"
    sort
    height="500px"
    width= '1150px' 
    
     
    
  >
  <zg-data :data="QuarterData" >
  </zg-data>
    <zg-colgroup > <!-- a function to get the names of the columns in the SQL tables needs to be written. Hardcoded for demonstrative purposed for now -->
      <zg-column index='Code' header='Code' type='text'  ></zg-column>
      <zg-column index='Cap' header='Cap' type='text' ></zg-column>
      <zg-column index='Start Date' header='First Trade' type='date' ></zg-column>
      <zg-column index='End Date' header='Last Trade' type='date' ></zg-column>
      <zg-column index='% Days Traded' header='% Traded' type='float' ></zg-column>
      <zg-column index='Data Points' header='# Points' type='int'></zg-column>
      <zg-column index='J203' header='J203' type='float' ></zg-column>
      <zg-column index='J200' header='J200' type='float' ></zg-column>
      <zg-column index='J250' header='J250' type='float' ></zg-column>
      <zg-column index='J257' header='J257' type='float' ></zg-column>
      <zg-column index='J258' header='J258' type='float' ></zg-column>
    </zg-colgroup>
  </zing-grid>
</template>

<script>



export default {
  name: 'share-tab-alt',
  props: ['entries','Quarter'],
  computed:{
    QuarterData(){
      //console.log(this.entries);
      try{
        return JSON.stringify(this.entries.filter(o=>o.YQ===this.Quarter).filter(o=>o["% Days Traded"]!=null));
      }catch(err){
        return this.entries;
      }
    },
    
    
    /*
    renderNull(value) {
      console.log("executed");
      if(value == "null") {
	      return ``;
	  } else if(value == "0") {
        console.log("executed 1");
	      return `<span style="color: #b3c1c4; font-style: italic;">${value}</span>`;
	  } else if(value > "0") {
        console.log("executed 2");
        console.log(value);
	      return value;
	  } else {
        console.log("executed 3");
	      return `<span style="color: #ea5374; font-weight: bold; margin-left: -8px;">${value}</span>`;
      
	  }
    
    }*/
    
  },
  methods:{
    renderNull: function(value) {
      console.log("executed");
      if(value == "null") {
	      return `decreased`;
	  } else if(value < 1) {
        console.log("executed 1");
	      return `increased`;
	  } else if(value > 1) {
        console.log("executed 2");
        console.log(value);
	      return `decreased`;
	  } else {
        console.log("executed 3");
        console.log(value);
	      return `increased`;
      
	  }
    }
    
  },
  mounted(){
  }

}
</script>
<style>
.decreased {
      color: #ef5350;
    }
.increased {
      color: #66bb6a;
    }
.none{
  color:black;
}


</style>
