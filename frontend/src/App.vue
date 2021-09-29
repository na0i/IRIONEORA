<template>
  <div id="app">
    <NavBar id="app-nav"/>
    <router-view/>
  </div>
</template>

<script>  
import NavBar from './components/common/NavBar.vue'
  export default {
    components: {
      NavBar,
    }
  }
</script>

<style>
#app {
  max-width: 425px;
  width: 100%;
  /* 가운데 정렬 */
  position: absolute;
  left: 0;
  right: 0;
  margin: 0 auto;

  /* 임시로 구분선 하나 그을게요.. */
  border: 1px solid ivory;

  font-family: 'Noto Serif KR', serif;

}

#app-nav {
  padding: 30px;
}

</style>
