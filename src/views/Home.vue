<template lang="pug">
.section
  .title PRESSING GAME
  div(align='center')
    .field.is-grouped(style='max-width: 200px')
      button.button(@click='start') START
      input.input(v-model.number='gameparam' style='width: 200px') 
      .control.select.is-fullwidth
        select(v-model='gamemode')
          //- option(value="versus") versus
          option(value="timer") timer
          option(value="speed") speed
    br
    .title {{currentLignt}}
    .field.is-grouped(style='max-width: 100px')
      button.button(@click='press(1)' :class='btnClass(1)') 1
      button.button(@click='press(2)' :class='btnClass(2)') 2
      button.button(@click='press(3)' :class='btnClass(3)') 3
  hr
  br

  div(v-if='gamemode == "speed"' align='center')
    .columns(style='max-width: 500px')
      .column
        .title BUTTON
        .is-size-1

  div(v-if='gamemode == "timer"' align='center')
    .columns(style='max-width: 500px')
      .column
        .title TIME {{Math.floor(gameparam/60)}}:{{gameparam%60}}
        .is-size-1 your score = {{score}}

</template>

<script lang="ts">
import { Component, Vue, Watch } from "vue-property-decorator";
import HelloWorld from "@/components/HelloWorld.vue"; // @ is an alias to /src
import io from "socket.io-client";
import axios from "axios";

const api = "http://localhost:3001";

@Component({
  components: {
    HelloWorld
  }
})
export default class Home extends Vue {
  socket = io(api);
  score: number = 0;
  gamemode: string = "timer";
  gameparam: number = 10;
  starting: boolean = false;

  idx: number = 0;
  arr: string = "_";
  penalty: boolean = false;

  async start() {
    let url = api + "/START?mode=" + this.gamemode + "&param=" + this.gameparam;
    this.starting = true;
    if (this.gamemode == "timer") {
      const timeloop = setInterval(() => {
        if (this.gameparam <= 0) {
          clearInterval(timeloop);
          this.starting = false;
        } else {
          this.gameparam -= 1;
        }
      }, 1000);
    }
    await axios.get(url);
  }

  @Watch("gamemode")
  @Watch("gameparam")
  async setinitscore() {
    let url =
      api + "/SETTING?mode=" + this.gamemode + "&param=" + this.gameparam;
    if (this.gamemode == "timer") {
      this.score = 0;
    }
    let res = await axios.get(url);
    if (!this.starting) {
      this.arr = String(res.data);
    }
  }
  async press(btn: number) {
    if (this.penalty || !this.starting) return;
    console.log(String(btn), this.currentLignt);
    if (String(btn) == this.currentLignt) {
      let url = api + "/PRESS?player=" + btn;
      this.idx += 1;
      await axios.get(url);
    } else {
      this.penalty = true;
      this.idx += 1;
      setTimeout(() => {
        this.penalty = false;
      }, 1000);
    }
  }
  mounted() {
    this.setinitscore();
    this.socket.on("SETTING", (data: any) => {
      let { mode, param } = data;
      this.gamemode = mode;
      this.gameparam = param;
    });
    this.socket.on("SCORE", (data: any) => {
      let { score } = data;
      this.score = score;
    });
    this.socket.on("FINISH", (data: any) => {
      this.starting = false;
    });
  }
  get currentLignt(): string {
    return this.penalty || this.idx == -1 ? "X" : this.arr[this.idx];
  }
  btnClass(num: number) {
    return "is-danger";
  }
}
</script>

<style lang="scss" scoped>
.winner {
  // border: solid 10px yellow;
  border-radius: 10px;
  background-color: rgb(224, 241, 125);
}
</style>
