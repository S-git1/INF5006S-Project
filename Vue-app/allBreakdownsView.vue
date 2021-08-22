<!-- The table does not give the user an option to select a preferred index to display. This needs to be added later. -->
<!--:caption.prop="Heading"-->
<template>
  <zing-grid
    ref="myGrid"
    
    layout="row"
    
    style="width: 100%;"
    sort
    
    width = '1150px' 
    
    draggable="columns"
    drag-action="reorder"
    :data.prop="entries"
  > <!--removed filter property-->
    <zg-colgroup> <!-- a function to get the names of the columns in the SQL tables needs to be written. Hardcoded for demonstrative purposed for now -->
      <zg-column index='Industry' header='Industry' type='text' frozen='left'></zg-column>
      <zg-column index='Y2017Q3' header='Y2017Q3' type='number' ></zg-column>
      <zg-column index='Y2017Q4' header='Y2017Q4' type='number' ></zg-column>
      <zg-column index='Y2018Q1' header='Y2018Q1' type='number' ></zg-column>
      <zg-column index='Y2018Q2' header='Y2018Q2' type='number' ></zg-column>
      <zg-column index='Y2018Q3' header='Y2018Q3' type='number' ></zg-column>
      <zg-column index='Y2018Q4' header='Y2018Q4' type='number' ></zg-column>
      <zg-column index='Y2019Q1' header='Y2019Q1' type='number' ></zg-column>
      <zg-column index='Y2019Q2' header='Y2019Q2' type='number' ></zg-column>
      <zg-column index='Y2019Q3' header='Y2019Q3' type='number' ></zg-column>
      <zg-column index='Y2019Q4' header='Y2019Q4' type='number' ></zg-column>
      <zg-column index='Y2020Q1' header='Y2020Q1' type='number' ></zg-column>
      <zg-column index='Y2020Q2' header='Y2020Q2' type='number' ></zg-column>
      <zg-column index='Y2020Q3' header='Y2020Q3' type='number' ></zg-column>
      <zg-column index='Y2020Q4' header='Y2020Q4' type='number' ></zg-column>
      <zg-column index='Y2021Q1' header='Y2021Q1' type='number' ></zg-column>

<!--      <zg-column index='Weight' header='Weight' type='float' ></zg-column>>
      <zg-column index='weight2' header='weight' type='float' ></zg-column>
      <zg-column index='betas' header='betas' type='float' ></zg-column>
      <zg-column index='sysVol' header='sysVol' type='float' ></zg-column>
      <zg-column index='specVar' header='specVar' type='float' ></zg-column>
      <zg-column index='Year' header='Year' type='float' ></zg-column>
      <zg-column index='Quarter' header='Quarter' type='select' type-select-options="1,2,3,4"></zg-column>
      <zg-column index='IC' header='IC' type='select' type-select-options='ALSI,FLED,LRGC,MIDC,SMLC,TOPI,RESI,FINI,INDI,PCAP,SAPY,ALTI'></zg-column>
      <zg-column index='MktIC' header='MktIC' type='float' ></zg-column>-->
    </zg-colgroup>
  </zing-grid>
</template>

<script>

export default {
  name: "all-breakdowns",
  props: ['entries','Heading']
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
