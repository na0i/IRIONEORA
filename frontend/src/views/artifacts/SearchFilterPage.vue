<template>
  <div>
    <SearchFilter/>
  </div>
</template>

<script>
import SearchFilter from "@/components/artifacts/SearchFilter.vue";
  export default {
    name: 'SearchFilterPage',
    components : {
      SearchFilter
    }
  }
</script>

<style lang="scss" scoped>
  @import "src/assets/style/artifacts/_search-box.scss";
</style>