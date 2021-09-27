<template>
  <div class="button">
    <input type="button" :value="value">
  </div>
</template>

<script>
export default {
  name: "Button",
  props: {
    value: {
      type: String,
      required: true
    }
  }
}
</script>

<style lang="scss">
  @import "src/assets/style/common/button.scss";

</style>