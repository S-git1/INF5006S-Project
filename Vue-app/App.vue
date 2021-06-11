<template>
  <div id="app">
    <section class="dashboard">
      <header>
        <!-- date range placeholder -->
      </header>
      <div class="dashboard__row">
        <latest-transactions-chart ref="latestTransactions" :entries="BABetaOutput"/> <!-- modified 'entries'-->
        <transaction-breakdown-chart ref="transactionBreakdown"  />
      </div>
      <div class="dashboard__row">
        <transaction-details-grid :entries="BABetaOutput"></transaction-details-grid> <!-- modified 'entries'-->
      </div>
    </section>
  </div>
</template>

<script>
import transactions from './data/transactions.js'; // this row was left in so that it does not cause errors with some other charts from the default template of ZingChart. Will be removed later.
import BABetaOutput from './data/dbo.tbl_BA_Beta_Output.js'; // added row

import LatestTransactionsChart from './components/LatestTransactionsChart.vue';
import TransactionBreakdownChart from './components/TransactionBreakdownChart.vue';
import TransactionDetailsGrid from './components/TransactionDetailsGrid.vue';

export default {
  name: 'app',
  components: {
    LatestTransactionsChart,
    TransactionBreakdownChart,
    TransactionDetailsGrid,
  },
  data() {
    return {
      transactions, // this row was left in so that it does not cause errors with some other charts from the default template of ZingChart. Will be removed later.
      BABetaOutput, // added row
    }
  },
  computed: {

  },
  methods: {

  }
}
</script>
