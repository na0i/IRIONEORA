import axios from "axios";

const URL = 'http://localhost:8000/'
const ROUTES = {
  detail: 'artifacts/',
  today: 'pages/recommend',
}
const SERVICE_KEY = 'SrLLfGdZjGbS5OmPmSlewYvcR6tXPmpk11SduYlvFr7r6CA7L9vjF7JRSx7rhrTEvOdAlUDtqkY9HJAg8%2BY6ww%3D%3D'


async function requestToday() {
  const todayPath = URL + ROUTES.today
  return await axios.get(todayPath)
}



const ArtifactsApi = {
  URL,
  ROUTES,
  SERVICE_KEY,
  requestToday: () => requestToday()
}

export default ArtifactsApi