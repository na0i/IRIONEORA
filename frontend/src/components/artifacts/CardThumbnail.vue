<template>
  <div id="card-thumbnail">
    {{likeArtifact}}
    <img :src=`https://${likeArtifact.image_uri}` alt="">
  </div>
</template>

<script>
export default {
  name: "CardThumbnail",
  props: ['likeArtifact'],
}
</script>

<style lang="scss">
  @import "src/assets/style/artifacts/_card-thumbnail.scss";
</style>