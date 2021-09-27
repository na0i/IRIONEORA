<template>
  <div>
    <SearchBox />
  </div>
</template>

<script>
import SearchBox from "@/components/artifacts/SearchBox.vue";
import axios from'axios'
global.jQuery = require('jquery');
var $ = global.jQuery;
window.$ = $;
  export default {
    name: 'SearchIndexPage',
    components: {
      SearchBox
    },
    data: function() {
      return {
        //setting const
        serviceKey: "DLuSbLjmCJIDKmhoSB7ELx3eVXXxg9ZBqh9oC8/eFWTcq2gDMqfQA7jrooSkvzWgYv/pd9a6fUJKG40K3VQXHg==",

        // data
        indexWord: '',
      }
    },
    methods: {
      // index case: search of name
      searchKeyWord: function() {
        axios({
        method: 'get',
        url: `http://www.emuseum.go.kr/openapi/relic/list?serviceKey=${this.serviceKey}&indexWord=${this.indexWord}&numOfRows=1&pageNo=1`,
        // headers: 
      })
        .then((res) => {
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
      },
    }
  }
// @api_view(['GET'])
// def artifact_search_index_word(request, index_word):
//     # 전체 검색수 파악 및 변수 설정
//     url = f'http://www.emuseum.go.kr/openapi/relic/list?serviceKey={service_key}&indexWord={index_word}&numOfRows=1&pageNo=1'
//     response = requests.get(url).content
//     response_dict = xmltodict.parse(response)
//     total_count = int(response_dict["result"]["totalCount"]) // 100

//     # 이름에 해당 키워드가 들어간 유물 찾기
//     search_list = []
//     image_uri = ""
//     id_num = ""
//     name = ""
//     for i in range(1,total_count+2):
//         url = f'http://www.emuseum.go.kr/openapi/relic/list?serviceKey={service_key}&indexWord={index_word}&numOfRows=100&pageNo={i}'
//         response = requests.get(url)
//         response_dict = bs4.BeautifulSoup(response.content, 'html.parser')

//         for data in response_dict.findAll('data'):
//             for item in data.findAll('item'):
//                 if item['key'] == 'id':
//                     id_num = item['value']
//                 elif item['key'] == 'nameKr':
//                     name = item['value']
//                 elif item['key'] == 'imgUri':
//                     image_uri = item['value']
//             search_list.append([image_uri,id_num,name])

//     return Response(search_list)
</script>

<style lang="scss" scoped>
  @import "src/assets/style/artifacts/_search-box.scss";
</style>

