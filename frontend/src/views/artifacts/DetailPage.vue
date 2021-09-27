<template>
  <div class="detail">
    <div style="color: white">
      디테일
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import API from '@/api/artifacts.js'

export default {
  name: 'DetailPage',
  components: {},
  props: {},
  data() {
    return {
      detailInfo: [],
    }
  },
  methods: {
    fetchDetailInfo() {
      axios({
        url: API.URL + API.ROUTES.detail + `${this.$route.params.artifactId}`,
        method: 'get',
      })
      .then((res) => {
        console.log(res.data)
        this.detailInfo = res.data
      })
      .catch((err) => console.log(err))
    },
  },
  computed: {
  },
  created() {
    this.fetchDetailInfo();
  }
}
</script>

<style lang="scss">
  @import "src/assets/style/artifacts/detail.scss";
</style>