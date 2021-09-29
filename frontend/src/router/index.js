import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/common/Home.vue'
import MainPage from "@/views/common/MainPage";
import SearchPage from '../views/artifacts/SearchPage.vue'
import ProfilePage from "../views/accounts/ProfilePage";
import ProfileLikePage from "@/views/accounts/ProfileLikePage";
import ProfileResemblePage from "@/views/accounts/ProfileResemblePage";
import DetailPage from '@/views/artifacts/DetailPage.vue'
import SearchIndexPage from '@/views/artifacts/SearchIndexPage.vue'
import SearchFilterPage from '@/views/artifacts/SearchFilterPage.vue'
import LoadingPage from '../views/common/LoadingPage.vue'
import ResultPage from "@/views/artifacts/ResultPage";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/main',
    name: 'MainPage',
    component: MainPage
  },
  {
    path: '/search',
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
  },
  {
    path: '/result',
    name: 'ResultPage',
    component: ResultPage
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
