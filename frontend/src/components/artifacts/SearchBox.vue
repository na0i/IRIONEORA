<template>
  <div>
    <input type="text" class="search-box" :placeholder="placeholder" v-model="indexWord" @keyup.enter="searchKeyWord()"/>
    <hr>
    <div class="search-wrap-div">
      <SearchCard 
        v-for="(item,idx) of search_list[1]" 
        :key="idx"
        :artifact="item"
        />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SearchCard from './SearchCard.vue'
  export default {
    name:'SearchBox',
    components: {
      SearchCard,
    },
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
        totalCount: 0,
        search_list : [],
        response_dict : {},
        image_uri : "",
        id_num : "",
        name : "",
      }
    },
  methods: {
      // index case: search of name
      searchKeyWord: function() {
        console.log(this.indexWord)
        axios({
          method: 'get',
          url: `/openapi/relic/list?serviceKey=${this.serviceKey}&indexWord=${this.indexWord}&numOfRows=1&pageNo=1`,
          // headers: 
        })
        .then((res) => {
          this.totalCount = parseInt(res.data.totalCount /100)
          console.log(this.totalCount)
        })
        .then(() => {
          for (var i = 1; i < this.totalCount+2; i++) {
            axios({
              method: 'get',
              url : `/openapi/relic/list?serviceKey=${this.serviceKey}&indexWord=${this.indexWord}&numOfRows=100&pageNo=${i}`, 
            })
            .then((res) => {
              // console.log(res.data.list)
              this.search_list.concat(res.data.list)
              console.log(this.search_list)
              // concat arrayhelpmethod 
              //https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/concat
              
            })
          }
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

