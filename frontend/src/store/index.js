import Vue from "vue";
import Vuex from "vuex";
import accounts from "@/store/modules/accounts";
import artifacts from "@/store/modules/artifacts";
Vue.use(Vuex);
export default new Vuex.Store({
  modules: { accounts, artifacts},
});
