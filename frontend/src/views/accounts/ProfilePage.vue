<template>
  <div>
    <ImageBox></ImageBox>

    <div class="nickname">
      {{nickname}}
    </div>

    <div class="router-wrap">
      <router-link to="/profile" class="router-button">
        <Button value="좋아하는 문화재"></Button>
      </router-link>
      <router-link to="/profile/resemble" class="router-button">
        <Button value="나와 닮은 유물"></Button>
      </router-link>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
import accountsApi from "@/api/accounts";
import Button from "@/components/common/Button";
import ImageBox from "@/components/accounts/ImageBox";
import {mapState} from "vuex";

export default {
  name: "ProfilePage",
  components: {
    Button,
    ImageBox,
  },
  // props
  // data
  // methods
  // computed
  computed: {
    ...mapState({
      nickname: state => state.accounts.profileInfo.nickname
    })
  },
  // watch
  // life cycle hook
  created() {
    accountsApi.requestProfile()
      .then(res =>
        this.$store.dispatch('setProfileInfo', res.data)
      )
  }
  // navigation guard
}
</script>

<style lang="scss">
  @import "src/assets/style/accounts/profile.scss";
</style>