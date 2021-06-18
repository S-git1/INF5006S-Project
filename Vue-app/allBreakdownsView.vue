<!-- The table does not give the user an option to select a preferred index to display. This needs to be added later. -->
<template>
  <zing-grid
    ref="myGrid"
    caption="All Breakdowns"
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
  >
    <zg-colgroup> <!-- a function to get the names of the columns in the SQL tables needs to be written. Hardcoded for demonstrative purposed for now -->
      <zg-column index='Industry' header='Industry' type='text' ></zg-column>
      <zg-column index='Weight' header='Weight' type='float' ></zg-column>
      <zg-column index='weight' header='weight' type='float' ></zg-column>
      <zg-column index='betas' header='betas' type='float' ></zg-column>
      <zg-column index='sysVol' header='sysVol' type='float' ></zg-column>
      <zg-column index='specVar' header='specVar' type='float' ></zg-column>
      <zg-column index='Year' header='Year' type='float' ></zg-column>
      <zg-column index='Quarter' header='Quarter' type='select' type-select-options="1,2,3,4"></zg-column>
      <zg-column index='IC' header='IC' type='select' type-select-options='ALSI,FLED,LRGC,MIDC,SMLC,TOPI,RESI,FINI,INDI,PCAP,SAPY,ALTI'></zg-column>
      <zg-column index='MktIC' header='MktIC' type='float' ></zg-column>
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
