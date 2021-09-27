 import axios from 'axios'

 const URL = 'http://localhost:8000/'
 const ROUTES = {
  profile: 'rest-auth/user/'
 }

 async function requestProfile () {
  const profilePath = URL + ROUTES.profile
  const headers = {
   'Authorization': 'Token fd241862a1b6cd60b72e5c95692a76e6a1db18e8'
  }
  const result = await axios.get(profilePath, {headers: headers})
  return result
 }

 const accountsApi = {
   URL,
   ROUTES,
   requestProfile: () => requestProfile(),
 }

 export default accountsApi