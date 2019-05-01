<template lang="pug">
  table 
    tbody
      tr
        td {{array[0]}} 
        td : 
        td {{array[1]}} 
        td : 
        td {{array[2]}} 
    tfoot
      tr
        td min
        td 
        td sec
        td 
        td ms
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  props: {
    value: {
      type: Number,
      default: 0.0
    },
    precition: {
      type: Number,
      default: 2
    }
  },
  computed: {
    array(): Array<any> {
      let val = Math.max(this.value, 0.0);
      let [first, second] = val.toFixed(this.precition).split(".");
      let num = Number(first);
      return [
        // Math.floor(num / 60 / 60) % 60,
        Math.floor(num / 60) % 60,
        num % 60,
        second
      ].map(nm => ("00" + nm).slice(-2));
    }
  }
});
</script>

<style lang="scss" scoped>
td {
  font-family: Courier, monospace;
  text-align: center;
  min-width: 30px;
}
tfoot td {
  font-size: 2rem;
}
tbody td {
  font-size: 5rem;
}
</style>
