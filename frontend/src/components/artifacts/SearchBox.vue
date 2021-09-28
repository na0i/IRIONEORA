<template>
  <div>
    <button @click="scrollmove()">scroll move</button>
    <input type="text" class="search-box" :placeholder="placeholder" v-model="indexWord" @keyup.enter="searchKeyWord()"/>
    <hr>
    <div class="search-wrap-div">
      <SearchCard 
        v-for="(item,idx) of items" 
        :key="idx"
        :artifact="item"
        />
    </div>
    <!-- <infinite-loading @infinite="infiniteHandler" spinner="waveDots"></infinite-loading> -->
    <!-- <button>scroll move<button/> -->
  </div>
</template>

<script>
// import InfiniteLoading from 'vue-infinite-loading'
import axios from 'axios'
import SearchCard from './SearchCard.vue'

  export default {
    name:'SearchBox',
    components: {
      SearchCard,
  
      // InfiniteLoading
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

        // infinite scroll
        // limit: 0,
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

      // // infinite methods
      loadMore () {
        /** This is only for this demo, you could 
          * replace the following with code to hit 
          * an endpoint to pull in more data. **/
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
        /**************************************/
      
    },
      scrollmove () {
        console.log(1)
        const myurl =`/openapi/relic/list?serviceKey=${this.serviceKey}&indexWord=${this.indexWord}&numOfRows=100&pageNo=1`
        axios.get(myurl)
        .then((res)=> console.log(res))
      }
  
      // infiniteHandler($state) { 
      //   axios.get(api, { 
      //     params: { 
      //       page: this.page, 
      //     }, 
      //   }).then(({ data }) => { 
      //     if (data.hits.length) { 
      //       this.page += 1; 
      //       this.list.push(...data.hits); 
      //       $state.loaded()
      //     } else { 
      //       $state.complete();
      //       } 
      //     })
      //   },


    },
    mounted () {

    // Detect when scrolled to bottom.
    const listElm = document.querySelector('.search-wrap-div');
    listElm.addEventListener('scroll', e => {
      console.log(e)
      console.log(listElm.scrollTop)
      console.log(listElm.clientHeight)
      console.log(listElm.scrollHeight)
      if(listElm.scrollTop + listElm.clientHeight >= listElm.scrollHeight-10) {
        this.loadMore();
      }
    });
  },
  watch: {
      // question 이 변경될 때마다, 이 함수가 실행될 것 입니다.
      search_list() {
        for (var i = 0; i < 5; i++) {
            this.nextNum++
            this.items.push(this.search_list[this.nextNum]);
          }
      }
    },

}

</script>

<style lang="scss" scoped>
  @import "src/assets/style/artifacts/_search-box.scss";
</style>

