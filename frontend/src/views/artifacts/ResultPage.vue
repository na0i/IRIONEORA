<template>
  <div class="result">
    <div class="result-preview">
      <img src="@/assets/images/resultpage-face-left.png" alt="" class="face-left">
      <ResultPreview></ResultPreview>
      <img src="@/assets/images/resultpage-face-right.png" alt="" class="face-right">
    </div>

    <div class="result-box-wrap">
      <span class="material-icons-outlined arrow left" @click="moveBackward">arrow_back_ios</span>
      <transition :name="slideTransition" mode="out-in">
        <ResultBox v-if="nowShowing===1" :result="results[0]" number="1" class="result-box" key="1"></ResultBox>
        <ResultBox v-else-if="nowShowing===2" :result="results[1]" number="2" class="result-box" key="2"></ResultBox>
        <ResultBox v-else-if="nowShowing===3" :result="results[2]" number="3" class="result-box" key="3"></ResultBox>
      </transition>
      <span class="material-icons-outlined arrow right" @click="moveForward">arrow_forward_ios</span>
    </div>

    <div class="icon-button-wrap">
      <IconButton value="다시하기" icon="https://irioneora.s3.ap-northeast-2.amazonaws.com/result-replay.png" class="icon-button"></IconButton>
      <IconButton value="공유하기" icon="https://irioneora.s3.ap-northeast-2.amazonaws.com/result-share.png" class="icon-button"></IconButton>
    </div>

  </div>
</template>

<script>
import ResultPreview from "@/components/artifacts/ReseultPreview";
import ResultBox from "@/components/artifacts/ResultBox";
import IconButton from "@/components/artifacts/IconButton";
import {mapState} from "vuex";

export default {
  name: "ResultPage",
  components: {
    ResultPreview,
    ResultBox,
    IconButton
  },
  data() {
    return {
      nowShowing: 1,
      slideTransition: 'slide-right',
    }
  },
  methods: {
    // 이전 결과 보기
    moveBackward() {
      this.slideTransition = 'slide-left'

      if (this.nowShowing === 1) {
        this.nowShowing = 3
      } else this.nowShowing--

      const transition = document.getElementById('transition')
      console.log(transition)
    },
    // 다음 결과 보기
    moveForward() {
      this.slideTransition = 'slide-right'

      if (this.nowShowing === 3) {
        this.nowShowing = 1
      } else this.nowShowing++
    },
  },
  computed: {
    ...mapState({
      results: state => state.artifacts.results
    })
  }
}
</script>

<style lang="scss" scoped>
  @import "src/assets/style/artifacts/result";

</style>