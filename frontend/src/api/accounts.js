import axios from 'axios'

const URL = 'http://localhost:8000/'
// const URL = 'http://j5a601.p.ssafy.io/'
const ROUTES = {
  profile: 'rest-auth/user/',
  login: 'rest-auth/login/',
  userFace: 'spark/userface/',
}

async function requestProfile () {
  const profilePath = URL + ROUTES.profile
  const headers = {
    'Authorization': 'Token fd241862a1b6cd60b72e5c95692a76e6a1db18e8'
  }
  return await axios.get(profilePath, {headers: headers})
}

async function requestLogin(data) {
  const loginPath = URL + ROUTES.login
  return await axios.post(loginPath, data)
}

// 얼굴 데이터 백 전송
async function requestAnalyze(data) {
  const analyzePath = URL + ROUTES.userFace
  return await axios.post(analyzePath, data)
}


const AccountsApi = {
  URL,
  ROUTES,
  requestProfile: () => requestProfile(),
  requestLogin: (data) => requestLogin(data),
  requestAnalyze: (data) => requestAnalyze(data),
}

export default AccountsApi