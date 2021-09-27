<template>
  <div>
    <div v-if="likeArtifacts.length === 0" class="no-card">
      마음에 드는 문화재에 좋아요를 눌러주세요
    </div>

    <div class="card-wrap">
      <CardThumbnail
          class="card-thumbnail"
          v-for="(likeArtifact, idx) in likeArtifacts" :key="idx" :artifact="likeArtifact"></CardThumbnail>
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