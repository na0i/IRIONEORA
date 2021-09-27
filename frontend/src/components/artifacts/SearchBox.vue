<template>
  <div>
    <input type="text" class="search-box" :placeholder="placeholder" v-model="indexWord" @keyup.enter="searchKeyWord()"/>
  </div>
</template>

<script>
import axios from 'axios'
  export default {
    name:'SearchBox',
    props: {
      placeholder: {
        type: String,
        default: '검색어를 입력해주세요',
        required: true
      },
    },
  data: function() {
      return {
        //setting values
        serviceKey: "DLuSbLjmCJIDKmhoSB7ELx3eVXXxg9ZBqh9oC8/eFWTcq2gDMqfQA7jrooSkvzWgYv/pd9a6fUJKG40K3VQXHg==",

        // index case
        indexWord: '',
      }
    },
  methods: {
      // index case: search of name
      searchKeyWord: function() {
        console.log(this.indexWord)
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
