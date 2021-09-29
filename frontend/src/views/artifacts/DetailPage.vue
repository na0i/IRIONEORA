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
            <button class="museum-button"><span class="museum-button-text">자세히 보기</span></button>
          </div>
          <div class="second-tab">
            <img src="@/assets/images/heart.png" class="heart">
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
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import API from '@/api/artifacts.js'

export default {
  name: 'DetailPage',
  components: {},
  props: {},
  data() {
    return {
      detailInfo: [],
      imgUrl: 'https://'
    }
  },
  methods: {
    fetchDetailInfo() {
      axios({
        url: API.URL + API.ROUTES.detail + `${this.$route.params.artifactId}`,
        method: 'get',
      })
      .then((res) => {
        this.detailInfo = res.data
        this.imgUrl += res.data.image_uri
      })
      .catch((err) => console.log(err))
    },
  },
  computed: {
  },
  created() {
    this.fetchDetailInfo();
  }
}

</script>

<style lang="scss">
  @import "src/assets/style/artifacts/detail.scss";
</style>