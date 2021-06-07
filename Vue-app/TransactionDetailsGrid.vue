<!-- The table does not give the user an option to select a preferred indice to display. This needs to be added later. -->
<template>
  <zing-grid
    ref="myGrid"
    caption="Indice data"
    layout="row"
    pager
    page-size="20"
    page-size-options="20,50,100"
    control-bar="false"
    style="width: 100%;"
    sort
    filter
    height="580px"
    :data.prop="entries"
  >
    <zg-colgroup> <!-- a function to get the names of the columns in the SQL tables needs to be written. Hardcoded for demonstrative purposed for now -->
      <zg-column index="Date" header="Date" type="date" ></zg-column>
      <zg-column index="Beta" header="Beta" type="float"></zg-column>
      <zg-column index="Instrument" header="Instrument" type="float"></zg-column>
      <zg-column index="Index" header="Index" type="select"
      type-select-options="J200,J203,J250,J257,J258"></zg-column>
      <zg-column index="Start Date" header="Start Date" type="date"></zg-column>
      <zg-column index="End Date" header="End Date" type="date"></zg-column>
      <zg-column index="% Days Traded" header="% Days Traded" type="float"></zg-column>
      <zg-column index="Data Points" header="Data Points" type="float"></zg-column>
    </zg-colgroup>
  </zing-grid>
</template>

<script>
export default {
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
