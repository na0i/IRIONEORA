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
      console.log(this.$route.params.artifactId)
      axios({
        url: API.URL + API.ROUTES.detail + `${this.$route.params.artifactId}`,
        method: 'get',
      })
      .then((res) => {
        console.log(res.data)
        this.detailInfo = res.data
        console.log(this.detailInfo[0][1])
      })
      .catch((err) => console.log(err))
    },
  },
  computed: {

  },
  created() {
    console.log('생성')
    this.fetchDetailInfo();
  }
}
</script>

<style lang="scss">
  @import "src/assets/style/artifacts/detail.scss";
</style>