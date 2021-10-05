<template>
  <div>
    <div class="detail-page">
      <!-- artifact Info -->
      <div>
        <div class="artifact-name">
          {{ detailInfo.artifact_name }}
        </div>
        <div>
          <img :src="imgUrl" class="artifact-image">
        </div>
        <div class="first-tab">
          <div class="second-tab">
            <span class="artifact-title">소장위치</span>
            <span class="artifact-content">{{ detailInfo.museum_name }}</span>
            <button class="museum-button" @click="getMuseumInfo(detailInfo.museum_name)"><span class="museum-button-text">자세히 보기</span></button>
          </div>
          <div v-if="isLike" class="second-tab">
            <img src="@/assets/images/heart.png" class="heart" @click="likeArtifact(detailInfo.identification_number)">
          </div>
          <div v-if="!isLike" class="second-tab">
            <img src="@/assets/images/heart-empty.png" class="heart" @click="likeArtifact(detailInfo.identification_number)">
          </div>
        </div>
        <div>
          <img src="@/assets/images/detailpage-cloud.png" class="detail-bgimg">
        </div>
        <div class="tab">
          <span class="artifact-title">작가</span>
          <span class="artifact-content">{{ detailInfo.artifact_author }}</span>
        </div>
        <div class="tab">
          <span class="artifact-title">시대</span>
          <span class="artifact-content">{{ detailInfo.nationality_name }}</span>
        </div>
        <div class="tab">
          <span class="artifact-title">사이즈</span>
          <span class="artifact-content">{{ detailInfo.artifact_size }}</span>
        </div>
        <div class="tab">
          <span class="artifact-title">색인어</span>
          <span class="artifact-content">{{ detailInfo.index_words }}</span>
        </div>
        <div>
          <div class="artifact-title">설명</div>
          <div class="description">{{ detailInfo.description }}</div>
        </div>
      </div>
      <br>

      <!-- word cloud -->
      <div>
        <div class="wordcloud">
          WORD CLOUD
        </div>
        <div id="wordcloud"></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import API from '@/api/artifacts.js'
import * as echarts from 'echarts'
import 'echarts-wordcloud';


export default {
  name: 'DetailPage',
  components: {},
  props: {},
  data() {
    return {
      detailInfo: [],
      serviceKey: 'SqZskQNLBydKAJrTV5fUn3zRuenH7ELym5KvJWma15ABpxIYBeQK15yeq%2BcLDfiGBiMv8Pt5VFk1H0Sz4lX3yw%3D%3D',
      imgUrl: 'https://',
      isLike: false,
      wordcloudData: '',
    }
  },
  methods: {
    // detail page 전체 정보 받아오기
    fetchDetailInfo() {
      axios({
        url: API.URL + API.ROUTES.detail + `${this.$route.params.artifactId}`,
        method: 'get',
      })
      .then((res) => {
        console.log(res.data)
        this.detailInfo = res.data
        this.imgUrl += res.data.image_uri
      })
      .catch((err) => console.log(err))
    },
    
    // 유물 좋아요
    likeArtifact() {
      axios({
        url: API.URL + API.ROUTES.detail + `${this.$route.params.artifactId}` + '/like',
        method: 'post',
      })
      .then((res) => {
        console.log(res.data)
        this.isLike = !this.isLike
      })
      .catch((err) => console.log(err))
    },

    // 박물관
    getMuseumInfo(museumName) {
      axios({
        url: API.URL + API.ROUTES.museum + `${museumName}` +'/',
        // url: `http://api.data.go.kr/openapi/tn_pubr_public_museum_artgr_info_api?serviceKey=${this.serviceKey}&fcltyNm=${this.detailInfo.museum_name}`, 
        method: 'get'
      })
      .then((res) => {
        console.log(res.data)
      })
      .catch((err) => console.log(err))
    },

    // wordcloud 단어 받아오기
    getWordCloud() {
      axios({
        url: API.URL + API.ROUTES.detail + `${this.$route.params.artifactId}` + '/wordcloud',
        method: 'get',
      })
      .then((res) => {
        this.wordcloudData = res.data
        this.makeWordCloud()
      })
      .catch((err) => console.log(err))
    },

    // wordcloud 그리기
    makeWordCloud() {
      var chart = echarts.init(document.getElementById('wordcloud'));

      // const color_palette = ['#F1E8DB', '#DEC8A4', '#D5D3C3', '#D4AB67', '#B1AFB2', '#848063'];
      // function randomItem(a) {
      //   console.log(a[Math.floor(Math.random() * a.length)])
      //   return a[Math.floor(Math.random() * a.length)]
      // }

      chart.setOption({
          series: [{
              type: 'wordCloud',
              // circle (default),  cardioid (apple or heart shape curve), diamond, triangle-forward, triangle, alias of triangle-upright, pentagon, and star.
              shape: 'diamond',
              // maskImage: maskImage,
              left: 'center',
              top: 'center',
              width: '90%',
              height: '90%',
              right: 'center',
              bottom: 'center',
              sizeRange: [12, 30],
              rotationRange: [-90, 90],
              rotationStep: 45,
              gridSize: 8,
              drawOutOfBound: false,
              layoutAnimation: true,
              textStyle: {
                  fontFamily: 'Noto Serif KR',
                  fontWeight: 500,
                  // color: randomItem(color_palette),
                  // color: function () {
                  //   return 'rgb(' + [
                  //       Math.round(Math.random() * 160),
                  //       Math.round(Math.random() * 160),
                  //       Math.round(Math.random() * 160)
                  //   ].join(',') + ')';
                  // }
                  color: function(a) {
                    const i =  (a.dataIndex)%6;
                    const color_palette = ['#F1E8DB', '#DEC8A4', '#D5D3C3', '#D4AB67', '#B1AFB2', '#848063'];
                    return color_palette[i];
                  }
              },
              emphasis: {
                  focus: 'self',
                  textStyle: {
                      textShadowBlur: 10,
                      textShadowColor: '#333'
                  }
              },
              data: this.wordcloudData
          }]
      });
    }
  },
  computed: {
  },
  created() {
    this.fetchDetailInfo();
    this.getWordCloud();
  }
}

</script>

<style lang="scss" scoped>
  @import "src/assets/style/artifacts/detail.scss";
</style>