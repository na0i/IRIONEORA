<template>
  <div>

    <div class="search-card">

      <div class="search-card-img">
        <img :src="`${changed_url}`" alt=""/> 
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
      image_url : this.artifact.imgThumUriM,
      changed_url : ""
      }
    },
    methods: {
      // URL 주소 체인지
      change_url (url) {
        const splitResult = url.split('/',3)
        const sumUrl = 'http://www.emuseum.go.kr' + '/' + splitResult[1] + '/' + splitResult[2]
        this.changed_url = sumUrl
      }
    },
    mounted () {
      this.change_url(this.image_url)
    }
  }
</script>

<style lang="scss" scoped>
  @import "src/assets/style/artifacts/_search-card.scss";
</style>