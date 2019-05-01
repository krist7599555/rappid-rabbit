<template lang="pug">
  div.is-size-7(align='center')
    button
    //- .field.is-grouped
    //-   .control
    //-     button.button(@click='start') EXEC
    //-   .control
    //-     input.input.is-static(value='http://128.199.216.159:PORT/SETTING?gamemode=' style='width: 380px')
    //-   .control.select
    //-     select(v-model='gamemode')
    //-       option(value="timer") timer
    //-       option(value="speed") speed
    //-   .control
    //-     input.input.is-static(value='&gameparam=' style='width: 100px')
    //-   .control
    //-     input.input(v-model.number='gameparam' style='width: 40px') 
</template>

<script lang="ts">
import { Component, Vue, Watch } from "vue-property-decorator";
import ShowTime from "@/components/ShowTime.vue";
import io from "socket.io-client";
import axios from "axios";

const api = "http://localhost:3001";

@Component({
  components: {
    ShowTime
  }
})
export default class Home extends Vue {
  //   socket = io(api);
  //   gamemode: string = "timer";
  //   gameparam: number = 10;
  //   starting: boolean = false;
  //   time: number = 0;
  //   score: number = 0;
  //   expectscore: number = 0;
  //   idx: number = 0;
  //   arr: string = "_";
  //   penalty: boolean = false;
  //   timeloop: any = null;
  //   async start() {
  //     if (this.starting) {
  //       this.starting = false;
  //       if (this.timeloop) {
  //         clearInterval(this.timeloop);
  //         this.timeloop = null;
  //       }
  //       return;
  //     }
  //     let url = api + "/START?mode=" + this.gamemode + "&param=" + this.gameparam;
  //     this.starting = true;
  //     if (this.gamemode == "timer") {
  //       this.time = this.gameparam;
  //       this.score = 0;
  //       this.timeloop = setInterval(() => {
  //         if (this.time <= 0) {
  //           clearInterval(this.timeloop);
  //           this.timeloop = null;
  //           this.starting = false;
  //         } else {
  //           this.time -= 0.01;
  //         }
  //       }, 10);
  //     }
  //     if (this.gamemode == "speed") {
  //       this.time = 0;
  //       this.score = 0;
  //       this.expectscore = this.gameparam;
  //       this.timeloop = setInterval(() => {
  //         if (this.score >= this.expectscore) {
  //           clearInterval(this.timeloop);
  //           this.timeloop = null;
  //           this.starting = false;
  //         } else {
  //           this.time += 0.02;
  //         }
  //       }, 10);
  //     }
  //     await axios.get(url);
  //   }
  //   @Watch("gamemode")
  //   @Watch("gameparam")
  //   async setinitscore() {
  //     let url =
  //       api + "/SETTING?mode=" + this.gamemode + "&param=" + this.gameparam;
  //     if (!this.starting) {
  //       let res = await axios.get(url);
  //       console.log(res.data);
  //       this.arr = String(res.data);
  //     }
  //   }
  //   async press(btn: number) {
  //     if (this.penalty || !this.starting) return;
  //     if (String(btn) == this.currentLignt) {
  //       let url = api + "/PRESS";
  //       this.idx += 1;
  //       await axios.get(url);
  //     } else {
  //       this.penalty = true;
  //       this.idx += 1;
  //       setTimeout(() => {
  //         this.penalty = false;
  //       }, 1000);
  //     }
  //   }
  //   mounted() {
  //     this.setinitscore();
  //     this.socket.on("SETTING", (data: any) => {
  //       console.log("SETTING", data);
  //       let { gamemode, gameparam } = data;
  //       this.gamemode = gamemode;
  //       this.gameparam = gameparam;
  //       this.expectscore = gameparam; // speed
  //     });
  //     this.socket.on("SCORE", (data: any) => {
  //       let { score } = data;
  //       this.score = score;
  //     });
  //     this.socket.on("FINISH", (data: any) => {
  //       this.starting = false;
  //     });
  //   }
  //   get currentLignt(): string {
  //     return this.penalty || this.idx == -1 ? "X" : this.arr[this.idx];
  //   }
  //   btnClass(num: number) {
  //     if (!this.starting) return "is-info";
  //     if (this.penalty) return "is-danger";
  //     return String(num) == this.currentLignt ? "is-success" : "";
  //   }
}
</script>

<style lang="scss" scoped>
.winner {
  // border: solid 10px yellow;
  border-radius: 10px;
  background-color: rgb(224, 241, 125);
}
</style>
