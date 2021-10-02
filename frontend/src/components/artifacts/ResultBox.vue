<template>
  <div>
    <div class="result-box-wrap">
      
      <div class="explian-text">
        사진과 닮은 문화재 속 인물입니다.
      </div>

      <img v-if="result.url" :src="imageUri" alt="" class="artifact-image">
      <img v-else src="@/assets/images/mainpage.png" alt="" class="artifact-image">

      <div class="artifact-description">
        <div class="artifact-number">
          {{number}}
        </div>
        <div class="artifact-name">
          {{artifact.artifact_name}}
        </div>
      </div>
      
    </div>
  </div>
</template>

<script>
import ArtifactsApi from "@/api/artifacts";

export default {
  name: "ResultBox",
  props: ['number', 'result'],
  data() {
    return {
      artifact: {
        artifact_name: '',
      }
    }
  },
  computed: {
    imageUri() {
      return `https://${this.result.url}`
    }
  },
  created() {
    console.log(this.result)
    ArtifactsApi.requestDetail(this.result.identification)
    .then(res => this.artifact = res.data)
  }

}
</script>

<style lang="scss" scoped>
  @import "src/assets/style/artifacts/_result-box";
</style>