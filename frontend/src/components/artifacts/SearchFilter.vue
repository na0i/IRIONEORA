<template>
  <div>

    <div id="float-clear-div">
        <hr>
        <p class="theme-text">{{theme}}</p>
        <div class="search-filter-div">
          <div class= "search-button" @click="buttonSwitch($event)" v-for="(ele,idx) in sortlist" :key="idx">
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
      startnum: {
        type: Number,
        required: true
      },
      sortlist: {
        type: Array,
        required: true
      }
    },
    
    methods: {
      buttonSwitch: function ($event) {
        console.log($event.target.classList)
        if ($event.target.classList[1] === "on") {
          console.log("already on")
        } else {
          var j = this.startnum
          var num = j+this.sortlist.length
          const btns = document.getElementsByClassName("search-button")
          // console.log(j)
          for (j ; j < num; j++) {
            const btn = btns[j]
            $(btn).removeClass('on')
          }
          $event.target.classList.add("on")
        }
      return false;
      },
    },
  }
</script>

<style lang="scss" scoped>
  @import "src/assets/style/artifacts/_search-filter.scss";
</style>