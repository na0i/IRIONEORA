<template>
  <div>

    <div id="float-clear-div">
        <hr>
        <p class="theme-text">{{theme}}</p>
        <div class="search-filter-div">
          <div class= "search-button" @click="buttonSwitch(ele,sortlist)" v-for="(ele,idx) in sortlist" :key="idx">
            {{ele.name}}
          </div>
        </div>
      </div>

  </div>
</template>

<script>
global.jQuery = require('jquery');
var $ = global.jQuery;
window.$ = $;
  export default {
    name: 'SearchFilter',
    props: {
      theme: {
        type: String,
        required: true
      },
      classname: {
        type: String,
        required: true
      },
      sortlist: {
        type: Array,
        required: true
      }
    },
    
    methods: {
      buttonSwitch: function (ele, sortlist) {
        
        const num = sortlist.length
        const btns = document.getElementsByClassName(this.classname)
        const selectBtns = btns[ele.switch]
        var j
        for (j = 0; j < num; j++) {
          const btn = btns[j]
          $(btn).removeClass('on')
        }
        $(selectBtns).addClass('on')
      return false;
      },
    },

  mounted () {
    const num = this.sortlist.length
    const btns = document.getElementsByClassName("search-button")
    for (var i = 0; i < num; i++) {
      const btn = btns[i]
      $(btn).addClass(this.classname)
    }
   }
  }
</script>

<style lang="scss" scoped>
  @import "src/assets/style/artifacts/_search-filter.scss";
</style>