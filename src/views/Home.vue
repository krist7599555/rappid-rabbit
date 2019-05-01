<template lang="pug">
.section
  //- .title PRESSING GAME
  //- Control
  div(style='position: absolute;')
    figure.image(style='max-width: 200px;')
      img.logo(src='../assets/compengesslogo.png')
  .columns
    //- Display(:isstart='isstart' :penalty='penalty' :currentLignt='currentLignt')
    .column(align='center')
      div
        div(style='margin: 20px; font-size: 13rem;')
          template(v-if='gamemode == "speed"' align='center')
            div {{score}}/{{expectscore}}
          template(v-if='gamemode == "timer"' align='center')
            div {{score}}
        div
          ShowTime(:value='time')

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
  socket = io(api);
  gamemode: string = "timer";
  gameparam: number = 10;

  isstart: boolean = false;
  isfinish: boolean = false;

  time: number = 10;
  score: number = 0;
  expectscore: number = 0;

  idx: number = 0;
  arr: string = "_";
  penalty: boolean = false;

  timeloop: any = null;

  cleartimeloop() {
    if (this.timeloop) {
      clearInterval(this.timeloop);
      this.timeloop = null;
    }
  }
  setting() {
    this.cleartimeloop();
    if (this.gamemode == "timer") {
      this.time = this.gameparam;
      this.score = 0;
    }
    if (this.gamemode == "speed") {
      this.time = 0;
      this.score = 0;
      this.expectscore = this.gameparam;
    }
  }
  async start() {
    this.cleartimeloop();
    if (this.isstart) {
      this.isstart = false;
      this.isfinish = true;
      return;
    }
    this.isstart = true;
    this.isfinish = false;
    if (this.gamemode == "timer") {
      this.time = this.gameparam;
      this.score = 0;
      this.timeloop = setInterval(async () => {
        if (this.time <= 0) {
          this.cleartimeloop();
          this.isstart = false;
          this.socket.emit("FINISH");
        } else {
          this.time -= 0.01;
        }
      }, 10);
    }
    if (this.gamemode == "speed") {
      this.time = 0;
      this.score = 0;
      this.expectscore = this.gameparam;
      this.timeloop = setInterval(() => {
        if (this.score >= this.expectscore) {
          clearInterval(this.timeloop);
          this.timeloop = null;
          this.isstart = false;
          this.socket.emit("FINISH");
        } else {
          this.time += 0.01;
        }
      }, 10);
    }
  }

  async press(btn: number) {
    if (this.penalty || !this.isstart || this.isfinish) return;
    if (String(btn) == this.currentLignt) {
      let url = api + "/PRESS";
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
    this.socket.on("SETTING", ({ gamemode, gameparam }: any) => {
      console.log("GAME SETTING");
      this.gamemode = gamemode;
      this.gameparam = gameparam;
      this.expectscore = gameparam;
      this.isstart = false;
      this.isfinish = false;
      this.setting();
    });
    this.socket.on("FINISH", () => {
      console.log("GAME FINISH");
      this.cleartimeloop();
      this.isstart = false;
      this.isfinish = true;
      if (this.gamemode == "timer") {
        this.time = 0;
      }
    });
    this.socket.on("START", () => {
      console.log("GAME START");
      this.start();
    });
    this.socket.on("PRESS", (btn: number) => {
      console.log("GAME PRESS");
      this.press(btn);
    });
    this.socket.on("SCORE", ({ score }: any) => {
      this.score = score;
    });
  }
  get currentLignt(): string {
    return this.penalty || this.idx == -1 ? "X" : this.arr[this.idx];
  }
  btnClass(num: number) {
    if (!this.isstart) return "is-info";
    if (this.penalty) return "is-danger";
    return String(num) == this.currentLignt ? "is-success" : "";
  }
}
</script>

<style lang="scss" scoped>
img.logo {
  opacity: 0.7;
  transition: transform 3s, background-color 3s, opacity 3s;
  // transition: background-color 3s;
  &:hover {
    transform: scale(4) translate(10vw, 8vh);
    opacity: 1;
    background-color: white;
  }
}
</style>
