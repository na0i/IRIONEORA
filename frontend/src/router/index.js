import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/common/Home.vue'
import SearchPage from '../views/artifacts/SearchPage.vue'
import ProfilePage from "../views/accounts/ProfilePage";
import ProfileLikePage from "@/views/accounts/ProfileLikePage";
import ProfileResemblePage from "@/views/accounts/ProfileResemblePage";
import DetailPage from '@/views/artifacts/DetailPage.vue'
import SearchIndexPage from '@/views/artifacts/SearchIndexPage.vue'
import SearchFilterPage from '@/views/artifacts/SearchFilterPage.vue'
import LoadingPage from '../views/common/LoadingPage.vue'

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
    component: SearchPage,
    children: [
      {path: '', name: 'SearchIndexPage', component: SearchIndexPage},
      {path: 'filter', name: 'SearchFilterPage', component: SearchFilterPage},
    ]
    
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
    path: '/loading',
    name: 'LoadingPage',
    component: LoadingPage,
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
