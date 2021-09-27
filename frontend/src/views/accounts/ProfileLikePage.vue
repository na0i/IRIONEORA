<template>
  <div>
    <div class="card-wrap">
      <CardThumbnail v-for="likeArtifact in likeArtifacts" :key=likeArtifact.id :likeArtifact="likeArtifact"></CardThumbnail>
    </div>
  </div>
</template>

<script>
import CardThumbnail from "@/components/artifacts/CardThumbnail";
import {mapState} from "vuex";

export default {
  name: "ProfileLikePage",
  components: {
    CardThumbnail
  },
  // props
  // data
  // methods
  // computed
  computed: {
    ...mapState({
      likeArtifacts: state => state.accounts.profileInfo.like_artifact
    })
  },
  // watch
  // life cycle hook
  // navigation guard
}
</script>

<style lang="scss">
  @import "src/assets/style/accounts/profile-sub";
</style>