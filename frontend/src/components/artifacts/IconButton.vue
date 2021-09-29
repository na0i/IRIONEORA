<template>
  <div>
    <button>
      {{value}}&nbsp;
      <span v-html="icon"></span>
    </button>
  </div>
</template>

<script>
export default {
  name: "IconButton",
  props: ['value', 'icon']
}
</script>

<style lang="scss" scoped>
  @import "src/assets/style/artifacts/_icon-button";
</style>