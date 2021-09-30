<template>
  <div style="color: #DEC8A4">
    <div class="result-box-wrap">
      
      <div class="explian-text">
        사진과 닮은 문화재 속 인물입니다.
      </div>

      <img src="@/assets/images/mainpage.png" alt="" class="artifact-image">

      <div class="artifact-description">
        <div class="artifact-number">
          {{number}}
        </div>
        <div class="artifact-name">
          사직단 국왕 친향도 병풍
          <!--{{name}}-->
        </div>
      </div>
      
    </div>
  </div>
</template>

<script>
export default {
  name: "ResultBox",
  props: ['number', 'name']
}
</script>

<style lang="scss" scoped>
  @import "src/assets/style/artifacts/_result-box";
</style>