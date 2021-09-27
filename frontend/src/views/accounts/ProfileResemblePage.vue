<template>
  <div>
    <div v-if="resembleArtifacts.length === 0" class="no-card">
      <a href="/">
        나와 닮은 유물 확인하러 가기
      </a>
    </div>

    <div v-else class="card-wrap">
      <CardThumbnail
          class="card-thumbnail"
          v-for="(resembleArtifact, idx) in resembleArtifacts" :key="idx" :artifact="resembleArtifact">
      </CardThumbnail>
    </div>
  </div>
</template>

<script>
import CardThumbnail from "@/components/artifacts/CardThumbnail";
import {mapState} from "vuex";

export default {
  name: "ProfileResemblePage",
  components: {
    CardThumbnail
  },
  // props
  // data
  // methods
  // computed
  computed: {
    ...mapState({
      resembleArtifacts: state => state.accounts.profileInfo.resemble_artifact
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