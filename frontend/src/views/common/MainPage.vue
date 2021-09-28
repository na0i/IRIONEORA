<template>
  <div class="main">
    <img src="@/assets/images/mainpage.png" alt="main page image" class="background">
    <div class="description">
      <div class="description-kr">
        이리오너라에서<br>
        조금 더 쉽고, 조금 더 재미있게<br>
        다양한 문화재를 만나보세요!
      </div>
      <div class="description-eng">
        WELCOME <br>
        TO
      </div>
    </div>

    <!-- 이미지 입력/ 안내 -->
    <div class="image-upload">
      <Button value="나와 닮은 문화재 찾기 →" class="button" @click.native="onImage"></Button>
      <ImageInput class="image-input" ref="image" ></ImageInput>

      <div class="info">
        사진은 저장되지 않습니다.<br>
        얼굴이 흐릿하게 나오거나, 판별하기 어려운 사진은 결과가 도출되지 않을 수 있습니다.
      </div>
    </div>

    <!-- 오늘의 문화재 -->
    <div class="todays-artifact">
      오늘의 문화재
      <TodaysArtifact></TodaysArtifact>
    </div>



  </div>
</template>

<script>
import Button from "@/components/common/Button";
import ImageInput from "@/components/artifacts/ImageInput";
import TodaysArtifact from "@/components/artifacts/TodaysArtifact";

export default {
  name: "MainPage",
  components: {
    Button,
    ImageInput,
    TodaysArtifact,
  },
  methods: {
    // input 호출
    onImage() {
      this.$refs.image.onOpen()
    }
  }
}
</script>

<style lang="scss">
 @import "src/assets/style/common/main";

</style>