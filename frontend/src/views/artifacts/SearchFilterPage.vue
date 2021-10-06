<template>
  <div>
    <hr>
    <SearchFilter @change="getNation" id="search-filter" theme="시대 구분" :sortlist="nationalityName2" :startnum = "0"  />
    <SearchFilter @change="getPurpose" id="search-filter" theme="유물 종류" :sortlist="purposeName2" :startnum = "8"  />
    <div id="float-clear-div">
      <div class="search-button-div">
        <button class="search-button" @click="searchFilters()" value="search">search</button>
      </div>
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
          {name: '청동기', num:0, code: 'PS06001004'},
          {name: '고구려', num:1, code: 'PS06001008'},
          {name: '백제', num:2, code: 'PS06001009' },
          {name: '신라', num:3, code: 'PS06001010' },
          {name: '통일신라', num:4, code: 'PS06001013' },
          {name: '고려', num:5, code: 'PS06001016' },
          {name: '조선', num:6, code: 'PS06001018' },
          {name: '광복이후', num:7, code: 'PS06001021' },
         
        ],
        purposeName2:[
          {name: '전통과학', num:3, code:'PS09006' },
          {name: '사회생활', num:2, code:'PS09007' },
          {name: '종교신앙', num:0, code:'PS09008' },
          {name: '문화예술', num:1, code:'PS09009' },
        ],

        /// SEARCH BOX
        //setting values
        serviceKey: "DLuSbLjmCJIDKmhoSB7ELx3eVXXxg9ZBqh9oC8/eFWTcq2gDMqfQA7jrooSkvzWgYv/pd9a6fUJKG40K3VQXHg==",

        // FILTER
        nationalityCode: "",
        purposeCode: "",

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
      getNation (value) {
        this.nationalityCode = value
      },
      getPurpose (value) {
        this.purposeCode = value
      },
      getArtifactPageList (pageNum) {
        axios({
              method: 'get',
              url : `/openapi/relic/list?serviceKey=${this.serviceKey}&nationalityCode=${this.nationalityCode}&purposeCode=${this.purposeCode}&numOfRows=100&pageNo=${pageNum}`, 
            })
            .then((res) => {
              this.search_list.push(...res.data.list)
            })
      },
      searchFilters () {
        console.log(1)
        // 검색결과 초기화
        this.search_list = []
        this.items = []
      
        // 필터제한
        if (this.nationalityCode === '' && this.purposeCode === '')  {
          // 어떻게 표현하지
          console.log("empty")
          return false
        } 

        // if (this.purposeCode === '') {
        //   // 어떻게 표현하지
        //   console.log("pn empty")
        //   return false
        // } 


        // 응답 요청
     

        // 응답 받아오기
        console.log("axios")
        axios({
          method: 'get',
          url : `/openapi/relic/list?serviceKey=${this.serviceKey}&nationalityCode=${this.nationalityCode}&purposeCode=${this.purposeCode}&numOfRows=100&pageNo=1`, 
        })
        .then((res) => {
          if (res.data.totalCount === 0) {
            console.log("결과가 업습니다")
            return false
          }
          console.log(res.data.totalCount)
          this.totalNum = res.data.totalCount
          this.totalPage = parseInt(res.data.totalCount /100) + 2
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
      axios({
              method: 'get',
              url : `/openapi/code?serviceKey=DLuSbLjmCJIDKmhoSB7ELx3eVXXxg9ZBqh9oC8/eFWTcq2gDMqfQA7jrooSkvzWgYv/pd9a6fUJKG40K3VQXHg==&parentCode=PS06001&numOfRows=100`, 
              // url : `/openapi/relic/list?serviceKey=${this.serviceKey}&numOfRows=100&nationalityCode=PS06001009&purposeCode=PS09009`,
})
            .then((res) => {
              console.log(res)
            })
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