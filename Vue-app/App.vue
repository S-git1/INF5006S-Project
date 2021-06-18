<template>
  <div id="app">
    <section class="dashboard">
      <header>
        <!-- date range placeholder -->
      </header>
      <div class="dashboard__row">
        <latest-transactions-chart ref="latestTransactions" :entries="BABetaOutput"/> <!-- modified 'entries'-->

      </div>
      <div class="dashboard__row">
        <index-table :entries="indexTableView"></index-table> <!-- modified 'entries'-->            
      </div>
      <div class="dashboard__row">
      </div>
      <div class="dashboard__row">
        <share-table :entries="shareTableView"></share-table> <!-- whatever was added in `components` section needs to be here with its name separated by dashes -->
      </div>
      <div class="dashboard__row">
      </div>
      <div class="dashboard__row">
        <all-breakdowns :entries="allBreakdownsView"></all-breakdowns> <!-- whatever was added in `components` section needs to be here with its name separated by dashes -->
      </div>
    </section>
  </div>
</template>

<script>
import shareTableView from './data/shareTableView.js'; 
import BABetaOutput from './data/dbo.tbl_BA_Beta_Output.js'; // added row
import indexTableView from './data/indexTableView.js';
import allBreakdownsView from './data/allBreakdownsview1.js';

import LatestTransactionsChart from './components/LatestTransactionsChart.vue';
// import TransactionBreakdownChart from './components/TransactionBreakdownChart.vue'; # pie chart commented out
import allBreakdowns from './components/allBreakdownsView.vue';
import shareTable from './components/shareTableView.vue';
import indexTable from './components/indexTableView.vue';

export default {
  name: 'app',
  components: {
    LatestTransactionsChart,
    // TransactionBreakdownChart, // pie chart commented out
    allBreakdowns,
    shareTable, // tag naming format for objects inside <div class="dashboard__row">: SeparatedByCaps = separated-by-caps
    indexTable,
  },
  data() {
    return {
      shareTableView, 
      BABetaOutput, // added row
      indexTableView,
      allBreakdownsView,

    }
  },
  computed: {

  },
  methods: {

  }
}
</script>
