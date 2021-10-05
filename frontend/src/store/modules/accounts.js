import cookies from "vue-cookies";

const state = {
  authToken: cookies.get('user-token'),
  // 프로필
  profileInfo: {
    username: '',
    nickname: '',
    profile_img: '',
    like_artifact: [
      {
        id: '',
        identification_number: '',
        image_uri: '',
      }
    ],
    resemble_artifact: [
      {
        id: '',
        identification_number: '',
        image_uri: '',
      }
    ]
  },
}
const getters = {
  isLoggedIn: state => !!state.authToken,
  config: state => ({ headers: { Authorization: `Token ${state.authToken}` }}),
}
const mutations = {
  SET_PROFILE_INFO(state, profile) {
    state.profileInfo = profile
  },
}
const actions = {
  setProfileInfo({commit}, profile) {
    commit('SET_PROFILE_INFO', profile)
  },

  // 로그인
  // 토큰 저장 & 닮은 유물 저장 요청
  fulfillLogin({commit, state, rootState}, token) {
    // 쿠키에 토큰 저장
    cookies.set('user-token', token, 0)
    // 닮은 유물 저장 요청 -> 앞서 요청 보낸 경우가 있었다면,
    if (rootState.artifacts.results[0].identification) {
      console.log('theres already')
    } else {
      console.log('nothing to save')
    }
  }

}


export default {
  state, getters, mutations, actions
}