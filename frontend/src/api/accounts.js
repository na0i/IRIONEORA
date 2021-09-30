import axios from 'axios'

const URL = 'http://localhost:8000/'
// const URL = 'http://j5a601.p.ssafy.io/'
const ROUTES = {
  profile: 'rest-auth/user/',
  login: 'rest-auth/login/',
  kakao: 'accounts/kakao/login/',
  userFace: 'spark/userface/',
}

async function requestProfile (token) {
  const profilePath = URL + ROUTES.profile
  const headers = {
    'Authorization': `Token ${token}`
  }
  return await axios.get(profilePath, {headers: headers})
}

async function requestLogin(data) {
  const loginPath = URL + ROUTES.login
  return await axios.post(loginPath, data)
}

// 카카오 로그인
async function requestKakaoLogin(code) {
  const kakaoPath = URL + ROUTES.kakao
  const data = {
    'code': code
  }
  return await axios.post(kakaoPath, data)
}


// 얼굴 데이터 백 전송
async function requestAnalyze(data) {
  const analyzePath = URL + ROUTES.userFace
  return await axios.post(analyzePath, data)
}



const AccountsApi = {
  URL,
  ROUTES,
  requestProfile: (token) => requestProfile(token),
  requestLogin: (data) => requestLogin(data),
  requestAnalyze: (data) => requestAnalyze(data),
  requestKakaoLogin: (code) => requestKakaoLogin(code),
}

export default AccountsApi