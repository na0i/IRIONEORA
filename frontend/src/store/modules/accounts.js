const state = {
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
  afterLoginPath: '',
}
const getters = {
}
const mutations = {
  SET_PROFILE_INFO(state, profile) {
    state.profileInfo = profile
  },
  SET_LOGIN_PATH(state, path) {
    state.afterLoginPath = path
  }
}
const actions = {
  setProfileInfo({commit}, profile) {
    commit('SET_PROFILE_INFO', profile)
  },
  setLoginPath({commit}, path) {
    commit('SET_LOGIN_PATH', path)
  }
}


export default {
  state, getters, mutations, actions
}