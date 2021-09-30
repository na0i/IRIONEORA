const state = {
  // 이미지 미리보기
  preview: '',
}
const getters = {
}
const mutations = {
  // 이미지 미리보기
  SET_PREVIEW(state, data) {
    state.preview = data
  }
}
const actions = {
  // 이미지 미리보기
  setPreview({commit}, data) {
    commit('SET_PREVIEW', data)
  }
}

export default {
  state, getters, mutations, actions
}