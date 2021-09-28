<template>
  <div>
    <h1>TodaysArtifact</h1>
  </div>
</template>

<script>
import artifacts from "@/api/artifacts";
import axios from "axios";

export default {
  name: "TodaysArtifact",
  data() {
    return {
      imgUri: '',
      idNumber: ''
    }
  },
  created() {
    // 오늘의 문화재
    const todayPath = artifacts.URL + artifacts.ROUTES.today
    axios.get(todayPath)
      .then(res => {
        this.imgUri = res.data.imgUri
        const serviceKey = 'SrLLfGdZjGbS5OmPmSlewYvcR6tXPmpk11SduYlvFr7r6CA7L9vjF7JRSx7rhrTEvOdAlUDtqkY9HJAg8%2BY6ww%3D%3D'
        const id = res.data.identificationNumber
        const url = `http://www.emuseum.go.kr/openapi/relic/detail?serviceKey=${serviceKey}&id=${id}`
        console.log(url)
        const headers = {'Access-Control-Allow-Origin': "*"}
        axios.get(url, {headers: headers})
        .then((res) => {console.log(res.data)})

      })
  }
}
</script>

<style scoped>

</style>