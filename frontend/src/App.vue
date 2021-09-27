<template>
  <div id="app">
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
      <h1>안녕안녕</h1>
    
    </div> -->
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

  /* 임시로 가로세로 구분선 하나 그을게요.. */
  border: 1px solid ivory;


  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#app-nav {
  padding: 30px;
}

</style>
