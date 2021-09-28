<template>
  <div>

    <div class="search-card">

      <div class="search-card-img">
        <img :src="`https://${artifact.imgThumUriS}`"  alt="11"/> 
      </div>

      <div class="search-card-p">
        <p>{{artifact.name}}</p>
        <!-- {{artifact}} -->
      </div>

    </div>

  </div>
</template>

<script>
  export default {
    name: 'SearchCard',
    props: ['artifact'],
  }
</script>

<style lang="scss" scoped>
  @import "src/assets/style/artifacts/_search-card.scss";
</style>