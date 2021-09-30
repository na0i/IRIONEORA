<template>
  <div>
    <SearchFilter id="search-filter" theme="시대" :sortlist="nationalityName2" :startnum = "0"  />
    <SearchFilter id="search-filter" theme="유물 종류" :sortlist="purposeName2" :startnum = "8"  />
    <div id="float-clear-div">
      <button @click="searchFilters()" value="search">search</button>
      <hr>
    </div>
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
import SearchFilter from "@/components/artifacts/SearchFilter.vue";
import axios from 'axios'
import SearchCard from '@/components/artifacts/SearchCard.vue'

  export default {
    name: 'SearchFilterPage',
    components : {
      SearchFilter,
      SearchCard
    },
    data () {
      return {
        nationalityName2:[
          {name: '청동기', num:0},
          {name: '고구려', num:1 },
          {name: '백제', num:2 },
          {name: '신라', num:3 },
          {name: '발해', num:4 },
          {name: '고려', num:5 },
          {name: '조선', num:6 },
          {name: '광복이후', num:7 },
         
        ],
        purposeName2:[
          {name: '문헌', num:0 },
          {name: '음악', num:1 },
          {name: '조각', num:2 },
          {name: '공예', num:3 },
          {name: '서화', num:4 },
          {name: '무용/극', num:5 },
        ],

        /// SEARCH BOX
        //setting values
        serviceKey: "DLuSbLjmCJIDKmhoSB7ELx3eVXXxg9ZBqh9oC8/eFWTcq2gDMqfQA7jrooSkvzWgYv/pd9a6fUJKG40K3VQXHg==",

        // FILTER
        nationalityName: "",
        purposeName: "",

        // index case
        totalPage: 0,
        totalNum: 0,
        nowPage: 1,
        search_list : [],
      
        // infinite scroll
        // loading : false,
        reminderFlag: 0,
        nextNumReminder: 0,
        nextNum: 0,
        items: []
      }
    },
    
    methods : {
      getArtifactPageList (pageNum) {
        axios({
              method: 'get',
              url : `/openapi/relic/list?serviceKey=${this.serviceKey}&nationalityName2=${this.nationalityName}&purposeName2=${this.purposeName}&numOfRows=100&pageNo=${pageNum}`, 
            })
            .then((res) => {
              this.search_list.push(...res.data.list)
            })
      },
      searchFilters () {
        console.log(1)
      
        // 필터제한
        if (this.nationalityName === '') {
          // 어떻게 표현하지
          console.log("nn empty")
          return false
        } 

        if (this.purposeName === '') {
          // 어떻게 표현하지
          console.log("pn empty")
          return false
        } 

        // 검색결과 초기화
        this.search_list = []
        this.items = []

        // 응답 요청
        axios({
          method: 'get',
          url : `/openapi/relic/list?serviceKey=${this.serviceKey}&nationalityName2=${this.nationalityName}&purposeName2=${this.purposeName}&numOfRows=1&pageNo=1`, 
        })

        // 응답페이지 수 결정
        .then((res) => {
          console.log(res.data.totalCount)
          this.totalNum = res.data.totalCount
          this.totalPage = parseInt(res.data.totalCount /100) + 2
        })

        // 응답 받아오기
        .then(() => {
          axios({
            method: 'get',
            url : `/openapi/relic/list?serviceKey=${this.serviceKey}&nationalityName2=${this.nationalityName}&purposeName2=${this.purposeName}&numOfRows=100&pageNo=1`, 
          })
          .then((res) => {
            this.search_list.push(...res.data.list)
            this.nowPage = this.nowPage + 1
          })
          .then(() => {
            for (var j = this.nextNum; j < this.nextNum+18; j++) {
              if (this.search_list[j] !== undefined) {
                this.items.push(this.search_list[j]);
              } 
            }
            this.nextNum = j
          })
        })
        .catch((err) => {
          console.log(err)
        })
      },

      // infinite methods
      loadMore () {
        if (this.nextNum > this.totalNum) {
          return false
        }
        // this.loading = true;
        setTimeout(e => {
          console.log(e)
          for (var i = 0; i < 6; i++) {
            this.nextNum++
            this.items.push(this.search_list[this.nextNum]);
            console.log(this.nextNum)
          }
          // this.loading = false;
        }, 200);

        this.nextNumReminder = this.nextNum%100
    
        if (this.reminderFlag === 1 && this.nextNumReminder < 20 ) {
          this.reminderFlag = 0
        }
        
        if ( this.nextNumReminder > 70 && this.reminderFlag === 0 && this.nowPage < this.totalPage ) {
          this.getArtifactPageList(this.nowPage)
          console.log(this.search_list)
          this.nowPage = this.nowPage + 1
          this.reminderFlag = 1
        }

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
      })
    },
  }
</script>

<style lang="scss" scoped>
  @import "src/assets/style/artifacts/_search-filterpage.scss";
</style>