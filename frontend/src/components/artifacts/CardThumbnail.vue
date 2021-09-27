<template>
  <div id="card-thumbnail">
    <img :src="`https://${artifact.image_uri}`" alt="artifact_img">
  </div>
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