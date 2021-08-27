// info.vue

<template>
<div class="col-lg-1 text-right">
  <span v-bind:title="message">
    <img src="../assets/info_icon.png" alt="more info" width="20" height="20">
  </span>
</div>
</template>
<script>
export default {
  name: "info",
  props:["message"]
}
</script>