<template>
  <div>
    <SearchFilter theme="유물종류1" :sortlist="nationalityName" classname="search1" />
    <SearchFilter theme="유물종류1" :sortlist="nationalityName" classname="search2" />
  </div>
</template>

<script>
import SearchFilter from "@/components/artifacts/SearchFilter.vue";
  export default {
    name: 'SearchFilterPage',
    components : {
      SearchFilter
    },
    data () {
      return {
        nationalityName:[
          {name: '고조선', switch:0},
          {name: '고구려', switch:1},
          {name: '신라', switch:2},
          {name: '백제', switch:3},
          {name: '고려', switch:4},
          {name: '조선', switch:5},
          {name: '근현대', switch:6}
        ],
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "src/assets/style/artifacts/_search-box.scss";
</style>