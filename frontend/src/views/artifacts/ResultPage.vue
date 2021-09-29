<template>
  <div class="result">
    <div class="result-preview">
      <img src="@/assets/images/resultpage-face-left.png" alt="" class="face-left">
      <ResultPreview></ResultPreview>
      <img src="@/assets/images/resultpage-face-right.png" alt="" class="face-right">
    </div>

    <div class="result-box-wrap">
      <span class="material-icons-outlined arrow left" @click="moveBackward">arrow_back_ios</span>
      <transition name="flip" mode="out-in">
        <ResultBox v-if="nowShowing===1" number="1" class="result-box" key="1"></ResultBox>
        <ResultBox v-else-if="nowShowing===2" number="2" class="result-box" key="2"></ResultBox>
        <ResultBox v-else-if="nowShowing===3" number="3" class="result-box" key="3"></ResultBox>
      </transition>
      <span class="material-icons-outlined arrow right" @click="moveForward">arrow_forward_ios</span>
    </div>

    <div class="icon-button-wrap">
      <IconButton value="다시하기" :icon="replay" class="icon-button"></IconButton>
      <IconButton value="공유하기" :icon="share" class="icon-button"></IconButton>
    </div>

  </div>
</template>

<script>
import ResultPreview from "@/components/artifacts/ReseultPreview";
import ResultBox from "@/components/artifacts/ResultBox";
import IconButton from "@/components/artifacts/IconButton";

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
      replay: '<span class="material-icons-outlined md-18">replay</span>',
      share: '<span class="material-icons-outlined md-18">add_to_home_screen</span>'
    }
  },
  methods: {
    // 이전 결과 보기
    moveBackward() {
      if (this.nowShowing === 1) {
        this.nowShowing = 3
      } else this.nowShowing--
    },
    // 다음 결과 보기
    moveForward() {
      if (this.nowShowing === 3) {
        this.nowShowing = 1
      } else this.nowShowing++
    }
  }
}
</script>

<style lang="scss" scoped>
  @import "src/assets/style/artifacts/result";

</style>