import axios from "axios";

// const URL = 'http://localhost:8000/'
const URL = 'http://j5a601.p.ssafy.io/'

const ROUTES = {
  detail: 'artifacts/',
  today: 'pages/recommend',
}
const SERVICE_KEY = 'SrLLfGdZjGbS5OmPmSlewYvcR6tXPmpk11SduYlvFr7r6CA7L9vjF7JRSx7rhrTEvOdAlUDtqkY9HJAg8%2BY6ww%3D%3D'

// 오늘의 문화재 요청
async function requestToday() {
  const todayPath = URL + ROUTES.today
  return await axios.get(todayPath)
}

// 유물 상세정보 요청
async function requestDetail(id) {
  const detailPath = URL + ROUTES.detail + id
  return await axios.get(detailPath)
}



const ArtifactsApi = {
  URL,
  ROUTES,
  SERVICE_KEY,
  requestToday: () => requestToday(),
  requestDetail: (id) => requestDetail(id),
}

export default ArtifactsApi