<template>
  <div>
    <h1>ProfilePage</h1>
    <CardThumbnail>

    </CardThumbnail>
  </div>
</template>

<script>
import accountsApi from "@/api/accounts";
import CardThumbnail from "../../components/artifacts/CardThumbnail";

export default {
  name: "ProfilePage",
  components: {
    CardThumbnail,
  },
  // props
  // data
  // methods
  // computed
  // watch
  // life cycle hook
  created() {
    const result = accountsApi.requestProfile()
    console.log(result)
  }
  // navigation guard
}
</script>

<style lang="scss">
  @import "src/assets/style/accounts/profile.scss";
</style>