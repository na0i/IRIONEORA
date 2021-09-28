<template>
  <router-link :to="`/detail/${artifact.identification_number}`" id="card-thumbnail">
    <img :src="`https://${artifact.image_uri}`" alt="artifact_img">
  </router-link>
</template>

<script>
export default {
  name: "CardThumbnail",
  props: ['artifact'],
}
</script>

<style lang="scss">
  @import "src/assets/style/artifacts/_card-thumbnail.scss";
</style>