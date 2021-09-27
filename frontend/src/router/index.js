import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/common/Home.vue'
import SearchPage from '../views/artifacts/SearchPage.vue'
import ProfilePage from "../views/accounts/ProfilePage";
import ProfileLikePage from "@/views/accounts/ProfileLikePage";
import ProfileResemblePage from "@/views/accounts/ProfileResemblePage";
import DetailPage from '@/views/artifacts/DetailPage.vue'

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
    children: [
      {path: '', name: 'ProfileLikePage', component: ProfileLikePage},
      {path: 'resemble', name: 'ProfileResemblePage', component: ProfileResemblePage}
    ]

  },
  {
    path: '/detail/:artifactId',
    name: 'DetailPage',
    component: DetailPage,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
