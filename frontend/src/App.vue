<template>
  <div id="app">
    <NavBar id="app-nav"/>

    <div id="app-content">
      <router-view/>
    </div>

    <LowBar id="low-bar"></LowBar>
  </div>
</template>

<script>  
import NavBar from './components/common/NavBar.vue'
import LowBar from "@/components/common/LowBar";

  export default {
    components: {
      NavBar,
      LowBar
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

#app-content {
  min-height: calc(100vh - 150px);
  /*margin-top: 40px;*/
  margin-bottom: 60px;
}

#app-nav {
  padding: 30px;
}

#low-bar {
  position: absolute;
  bottom: 0;
}

</style>
