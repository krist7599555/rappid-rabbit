<template lang="pug">
.container(align='center')
  .title.is-size-1 {{currentLignt || "none"}}
  .subtitle
    .field.is-grouped(style='max-width: 100px')
      button.button(@click='press(1)' :class='btnClass(1)') 1
      button.button(@click='press(2)' :class='btnClass(2)') 2
      button.button(@click='press(3)' :class='btnClass(3)') 3
</template>

<script lang="ts">
import { Component, Vue, Watch, Prop, Emit } from "vue-property-decorator";
import io from "socket.io-client";
import axios from "axios";

const api = "http://localhost:3001";

@Component({})
export default class Home extends Vue {
  socket = io(api);
  @Prop()
  currentLignt!: String;
  @Prop()
  starting!: boolean;
  @Prop()
  penalty!: boolean;

  @Emit("press")
  press(btn: number) {
    return btn;
  }

  btnClass(num: number) {
    if (!this.starting) return "is-info";
    if (this.penalty) return "is-danger";
    return String(num) == this.currentLignt ? "is-success" : "";
  }
}
</script>

<style lang="scss" scoped></style>
