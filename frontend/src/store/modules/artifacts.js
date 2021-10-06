const state = {
  // 이미지 미리보기
  preview: '',
  results: [
    {
      identification: 'qwer',
      img_uri: '',
      height: 0,
      width: 0,
      x: 0,
      y: 0,
      w: 0,
      h: 0,
    },
    {
      identification: '',
      img_uri: '',
      height: 0,
      width: 0,
      x: 0,
      y: 0,
      w: 0,
      h: 0,
    },
    {
      identification: '',
      img_uri: '',
      height: 0,
      width: 0,
      x: 0,
      y: 0,
      w: 0,
      h: 0,
    }
  ]
}
const getters = {
}
const mutations = {
  // 이미지 미리보기
  SET_PREVIEW(state, data) {
    state.preview = data
  },

  // 알고리즘 결과 저장
  SET_RESULTS(state, results) {
    state.results = results
  }
}
const actions = {
  // 이미지 미리보기
  setPreview({commit}, data) {
    commit('SET_PREVIEW', data)
  },

  // 알고리즘 결과 저장
  setResults({commit}, results) {
    commit('SET_RESULTS', results)
  }
}

export default {
  state, getters, mutations, actions
}