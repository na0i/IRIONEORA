import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/common/Home.vue'
import SearchPage from '../views/artifacts/SearchPage.vue'
import ProfilePage from "../views/accounts/ProfilePage";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/search',
    name: 'SearchPage',
    component: SearchPage
  },
  {
    path: '/profile',
    component: ProfilePage,

  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
