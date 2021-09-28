<template>
  <div>
    <input type="text" class="search-box" :placeholder="placeholder" v-model="indexWord" @keyup.enter="searchKeyWord()"/>
    <hr>
    <div class="search-wrap-div">
      <SearchCard 
        v-for="(item,idx) of items" 
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
    data: function() {
        return {
          //setting values
          serviceKey: "DLuSbLjmCJIDKmhoSB7ELx3eVXXxg9ZBqh9oC8/eFWTcq2gDMqfQA7jrooSkvzWgYv/pd9a6fUJKG40K3VQXHg==",
          placeholder: '검색어를 입력해주세요',

          // index case
          indexWord: '',
          totalCount: 0,
          search_list : [],
          response_dict : {},
          image_uri : "",
          id_num : "",
          name : "",

          // infinite scroll
          loading : false,
          nextNum: 0,
          items: []
        }
      },
    methods: {
        // search of name
        searchKeyWord: function() {
          console.log(this.indexWord)
          axios({
            method: 'get',
            url: `/openapi/relic/list?serviceKey=${this.serviceKey}&indexWord=${this.indexWord}&numOfRows=1&pageNo=1`,
            // headers: 
          })
          .then((res) => {
            console.log(res)
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
                this.search_list.push(...res.data.list)
                console.log(this.search_list)     
              })
            }
          })
          .catch((err) => {
            console.log(err)
          })
        },

        // infinite methods
        loadMore () {
          this.loading = true;
          setTimeout(e => {
            console.log(e)
            for (var i = 0; i < 6; i++) {
              this.nextNum++
              this.items.push(this.search_list[this.nextNum]);
              console.log(this.nextNum)
            }
            this.loading = false;
          }, 200);
        },
      },

    mounted () {
      // Detect when scrolled to bottom.
      const listElm = document.querySelector('.search-wrap-div');
      listElm.addEventListener('scroll',e => {
        console.log(e)
        // console.log(listElm.scrollTop)
        // console.log(listElm.clientHeight)
        // console.log(listElm.scrollHeight)
        if(listElm.scrollTop + listElm.clientHeight >= listElm.scrollHeight-10) {
          this.loadMore();
        }
      });
    },
    watch: {
      search_list() {
        for (var j = this.nextNum; j < this.nextNum+9; j++) {
            this.items.push(this.search_list[j]);
          }
        this.nextNum = j
      }
    },
  }

</script>

<style lang="scss" scoped>
  @import "src/assets/style/artifacts/_search-box.scss";
</style>

