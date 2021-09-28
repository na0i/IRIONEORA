<template>
  <div>

    <div class="nav-background">
        <div class="nav-item-start"><router-link to="/search"><span class="material-icons md-18">search</span></router-link></div>
        
        <div class="nav-item-center">
          <router-link to="/">
              <img src="@/assets/images/logo-navbar.png"/>
          </router-link>
        </div>

        <div class="nav-item-end"><router-link to="/profile"><span class="material-icons md-18">person_outline</span></router-link></div>
    </div>

  </div>
</template>

<script>
  export default {
    name: 'Navbar',
  }
</script>

<style lang="scss" scoped>
  @import "../../assets/style/common/NavBar.scss";
</style>