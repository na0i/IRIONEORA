<template>
  <div>
    <SearchBox />
  </div>
</template>

<script>
import SearchBox from "@/components/artifacts/SearchBox.vue";
import axios from'axios'
global.jQuery = require('jquery');
var $ = global.jQuery;
window.$ = $;
  export default {
    name: 'SearchIndexPage',
    components: {
      SearchBox
    },
    data: function() {
      return {
        //setting const
        serviceKey: "DLuSbLjmCJIDKmhoSB7ELx3eVXXxg9ZBqh9oC8/eFWTcq2gDMqfQA7jrooSkvzWgYv/pd9a6fUJKG40K3VQXHg==",

        // data
        indexWord: '',
      }
    },
    methods: {
      // index case: search of name
      searchKeyWord: function() {
        axios({
        method: 'get',
        url: `http://www.emuseum.go.kr/openapi/relic/list?serviceKey=${this.serviceKey}&indexWord=${this.indexWord}&numOfRows=1&pageNo=1`,
        // headers: 
      })
        .then((res) => {
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
      },
    }
  }
</script>

<style lang="scss" scoped>
  @import "src/assets/style/artifacts/_search-box.scss";
</style>

