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
  }
}
const getters = {
}
const mutations = {
  SET_PROFILE_INFO(state, profile) {
    state.profileInfo = profile
  }
}
const actions = {
  setProfileInfo({commit}, profile) {
    commit('SET_PROFILE_INFO', profile)
  }
}


export default {
  state, getters, mutations, actions
}