<template>
  <div>
    <h1>TodaysArtifact</h1>
  </div>
</template>

<script>
import ArtifactsApi from "@/api/artifacts";
// import axios from "axios";

export default {
  name: "TodaysArtifact",
  data() {
    return {
      imgUri: '',
      idNumber: ''
    }
  },
  methods: {
    // async gettodayArtifact() {
    //   const res = await ArtifactsApi.requestToday()
    //   return res.data.identificationNumber
    // }
  },
  created() {
    // 오늘의 문화재
    // this.gettodayArtifact()
    // .then(id => {
    //   const museumApiPath = `/openapi/relic/detail?serviceKey=${ArtifactsApi.SERVICE_KEY}&id=${id}`
    //   axios({
    //     methods: 'get',
    //     url: museumApiPath
    //   })
    //   .then(res => console.log(res))
    //
    // })
    ArtifactsApi.requestToday()
      .then(res =>
          console.log(typeof res.data)
      )
  }
}
</script>

<style scoped>

</style>