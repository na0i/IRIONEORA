<template>
  <div class="main">

    <img src="@/assets/images/left-m.png" alt="main page image" class="left-mountain">
    <img src="@/assets/images/right-m.png" alt="" class="right-mountain">
    <img src="@/assets/images/right-mountain2.png" alt="" class="middle-mountain">
    <div class="description">
      <div class="description-1">
        죄송합니다 현재 페이지를 찾을 수 없습니다<br>
      </div>
      <div class="description-2">
        존재하지 않은 주소를 입력하셨거나<br>
      </div>
       <div class="description-3">
        요청하신 페이지의 주소가 변경, 삭제되어 찾을 수 없습니다<br>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'ErrorPage',
}
</script>

<style lang="scss" scoped>
  @import "../../assets/style/common/Error.scss";
</style>