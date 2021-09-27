<template>
  <div>
    <h1>ProfilePage</h1>
    <CardThumbnail>

    </CardThumbnail>
  </div>
</template>

<script>
import CardThumbnail from "../../components/artifacts/CardThumbnail";

export default {
  name: "ProfilePage",
  components: {
    CardThumbnail,
  }
}
</script>

<style lang="scss">
  @import "src/assets/style/accounts/profile.scss";
</style>