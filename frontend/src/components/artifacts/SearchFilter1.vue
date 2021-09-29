<template>
  <div>
    <div id="float-clear-div">
        <hr>
        <p id="sort-p">유물 종류</p>
        <div class="search-filter-div">
          <div class= "search-button" @click="buttonSwitch(purpose,purposeName)" v-for="(purpose,idx) in purposeName" :key="idx">
            {{ purpose.name }}
          </div>
        </div>
      </div>
     
      <div id="float-clear-div">
        <hr>
        <p id="sort-p">시대 구분</p>
        <div class="search-filter-div">
          <div class= "era-button" @click="buttonSwitch2(era,nationalityName)" v-for="(era,idx) in nationalityName" :key="idx">
            {{ era.name }}
          </div>
        </div>
      </div>

      <div class="search-button-div">
        <Button class="seach-button" value="검색"/>
      </div>

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
import Button from "@/components/common/Button";
global.jQuery = require('jquery');
var $ = global.jQuery;
window.$ = $;
export default {
  name: 'SearchFilter',
  components: {
    Button
  },
  data: function() {
    return {
      //setting values
      serviceKey: "DLuSbLjmCJIDKmhoSB7ELx3eVXXxg9ZBqh9oC8/eFWTcq2gDMqfQA7jrooSkvzWgYv/pd9a6fUJKG40K3VQXHg==",

      // filter case
      purposeName:[
        {name: '네임1', switch:0},
        {name: '네임2', switch:1},
        {name: '네임3', switch:2},
        {name: '네임4', switch:3},
        {name: '네임5', switch:4},
        {name: '네임6', switch:5},
        {name: '네임7', switch:6}
      ],   

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
  },
  
  methods: {
    buttonSwitch: function (item, listName) {
      const num = listName.length
      const btns = document.getElementsByClassName("search-button")
      const selectBtns = btns[item.switch]
      var i
      for (i = 0; i < num; i++) {
        const btn = btns[i]
        $(btn).removeClass('on')
      }
      $(selectBtns).addClass('on')
    return false;
  },

    buttonSwitch2: function (item, listName) {
        const num = listName.length
        const btns = document.getElementsByClassName("era-button")
        const selectBtns = btns[item.switch]
        var i
        for (i = 0; i < num; i++) {
          const btn = btns[i]
          $(btn).removeClass('on')
        }
        $(selectBtns).addClass('on')
      return false;
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "src/assets/style/artifacts/_search-filter.scss";
</style>