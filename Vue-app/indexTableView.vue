<!-- The table does not give the user an option to select a preferred index to display. This needs to be added later. -->
<template>
  <zing-grid
    ref="myGrid"
    caption="Index Table"
    layout="row"
    pager
    page-size="10"
    page-size-options="10,30,50"
    control-bar="false"
    style="width: 100%;"
    sort
    filter
    height="580px"
    width = '1000px' 
    draggable="columns"
    drag-action="reorder"
    :data.prop="entries"
  > <!-- added `width` and `draggable` together to make horizontal scroll possible -->
    <zg-colgroup> <!-- a function to get the names of the columns in the SQL tables needs to be written. Hardcoded for demonstrative purposed for now; date column not needed -->
      <zg-column index='MarketID' header='Market ID' type='select' 
      type-select-options='J203,J200,J250,J257,J258'></zg-column>
      <zg-column index='Code' header='Code' type='text' ></zg-column>
      <zg-column index='Name' header='Name' type='text' ></zg-column>
      <zg-column index='Index Type' header='Index Type' type='text' ></zg-column>
      <zg-column index='Start Date' header='Start Date' type='date' ></zg-column>
      <zg-column index='End Date' header='End Date' type='date' ></zg-column>
      <zg-column index='% Days Traded' header='% Days Traded' type='float' ></zg-column>
      <zg-column index='Data Points' header='Data Points' type='float' ></zg-column>
      <zg-column index='Alpha' header='Alpha' type='float' ></zg-column>
      <zg-column index='Beta' header='Beta' type='float' ></zg-column>
      <zg-column index='SE Alpha' header='SE Alpha' type='float' ></zg-column>
      <zg-column index='SE Beta' header='SE Beta' type='float' ></zg-column>
      <zg-column index='p-Value Alpha' header='p-Value Alpha' type='float' ></zg-column>
      <zg-column index='p-Value Beta' header='p-Value Beta' type='float' ></zg-column>
      <zg-column index='R2' header='R2' type='float' ></zg-column>
      <zg-column index='Total Risk' header='Total Risk' type='float' ></zg-column>
      <zg-column index='Unique Risk' header='Unique Risk' type='float' ></zg-column>
      <zg-column index='Year' header='Year' type='float' ></zg-column>
      <zg-column index='Quarter' header='Quarter' type='select' type-select-options="1,2,3,4"></zg-column>
    </zg-colgroup>
  </zing-grid>
</template>

<script>
export default {
  name: 'index-table',
  props: ['entries'],
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
