<template>
  <div>
    <div class="img-wrap">
      <img v-if="preview" :src="preview" :style="previewImgClip" alt="profile image">
      <img v-else src="@/assets/images/logo-main.png" alt="profile image">
    </div>
  </div>
</template>

<script>
import {mapState} from "vuex";

export default {
  name: "ResultPreview",
  computed: {
    ...mapState({
      preview: state => state.artifacts.preview,
      kakaoResult: state => state.accounts.kakaoResult
    }),
    previewImgClip() {
      return {
        '--face-start-x': this.kakaoResult.faces[0].x,
        '--face-start-y': this.kakaoResult.faces[0].y,
        '--face-width': this.kakaoResult.faces[0].w,
        '--face-height': this.kakaoResult.faces[0].h,
        '--image-width': this.kakaoResult.width,
        '--image-height': this.kakaoResult.height
      }
    }
  },
}
</script>

<style lang="scss" scoped>
  @import "src/assets/style/accounts/_image-box";
</style>