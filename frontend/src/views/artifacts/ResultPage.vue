<template>
  <div class="result">
    <div class="result-preview">
      <img src="@/assets/images/resultpage-face-left.png" alt="" class="face-left">
      <ResultPreview></ResultPreview>
      <img src="@/assets/images/resultpage-face-right.png" alt="" class="face-right">
    </div>

    <ResultBox v-if="nowShowing===1" number="1"></ResultBox>
    <ResultBox v-if="nowShowing===2" number="2"></ResultBox>
    <ResultBox v-if="nowShowing===3" number="3"></ResultBox>

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
  }
}
</script>

<style lang="scss" scoped>
  @import "src/assets/style/artifacts/result";

</style>