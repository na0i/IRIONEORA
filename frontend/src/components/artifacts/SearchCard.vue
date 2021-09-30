<template>
  <div>

    <div @click="moveDetail(idNum)" class="search-card">

      <div class="search-card-img">
        <img :src="`${changedUrl}`" alt=""/> 
      </div>

      <div class="search-card-p">
        <p>{{artifact.name}}</p>
      </div>

    </div>

  </div>
</template>

<script>
  export default {
    name: 'SearchCard',
    props: ['artifact'],

    data () {
    return {
      imageUrl : this.artifact.imgThumUriM,
      changedUrl : "",
      idNum : this.artifact.id
      }
    },

    methods: {
      // URL 주소 체인지
      changeUrl (url) {
        const splitResult = url.split('/',3)
        const sumUrl = 'http://www.emuseum.go.kr' + '/' + splitResult[1] + '/' + splitResult[2]
        this.changedUrl = sumUrl
      },

      // 디테일 페이지로 보내기
      moveDetail (id_num) {
        const target = '/detail/' + String(id_num)
        this.$router.push(target);
      }
    },

    mounted () {
      this.changeUrl(this.imageUrl)
    }
  }
</script>

<style lang="scss" scoped>
  @import "src/assets/style/artifacts/_search-card.scss";
</style>