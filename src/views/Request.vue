<template lang="pug">
.section
  .field(v-for='k in [press, start, setting]')
    .button(@click='request(k)') {{k}}
  .field
    .control.select
      select(v-model='gamemode')
        option(value='timer') timer
        option(value='speed') speed
  .field
    .control
      input.input(v-model.number='gameparam')


</template>

<script lang="ts">
import { Component, Vue, Watch } from "vue-property-decorator";
import ShowTime from "@/components/ShowTime.vue";
import Control from "./Control.vue";
import Display from "./Display.vue";
import io from "socket.io-client";
import axios from "axios";

const api = "http://128.199.216.159:3113";

@Component({
  components: {
    ShowTime,
    Control,
    Display
  }
})
export default class Home extends Vue {
  press: string = api + "/PRESS";
  start: string = api + "/START";
  finish: string = api + "/FINISH";
  setting_raw: string = api + "/SETTING";
  gamemode: string = "timer";
  gameparam: number = 10;
  get setting() {
    console.log(this.setting_raw);
    return (
      this.setting_raw +
      `?gamemode=${this.gamemode}&gameparam=${this.gameparam}`
    );
  }
  request(endpoint: string) {
    axios.get(endpoint).then(res => console.log(res.data));
  }
}
</script>

<style lang="scss" scoped>
* {
  touch-action: none;
}
</style>
