<template>
  <div>
    <input id="image-input" ref="imgInput" type="file" accept="image/jpeg, image/png"
       @change="onImageUploaded" >
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ImageInput",
  data() {
    return {
      selectedFile: null,
      error: '',
    }
  },
  methods: {
    // input창 호출
    onOpen() {
      this.$refs.imgInput.click()
    },

    // 이미지 입력 받음
    onImageUploaded(event) {
      this.selectedFile = event.target.files[0]
      // 이미지 확장자/ 크기 확인
      let extension = this.selectedFile.name.substring(
          this.selectedFile.name.lastIndexOf('.')+1
      ).toLowerCase()

      // 이미지 파일이 아닌 경우
      if (!['jpg', 'jpeg', 'png'].includes(extension)) {
        this.error = '이미지 파일을 선택해 주세요.'
      }
      // 파일의 크기가 너무 큰 경우
      else if (this.selectedFile.size > 2097152) {
        this.error = '2MB 이내의 파일만 선택 가능합니다.'
      }

      // 에러 발생하면 에러메세지 emit
      if (this.error) {
        this.$emit('on-error', this.error)
      }

      // 오류 없는 경우 formData 전송
      else {

        // 서버 전송 데이터
        const imageFile = new FormData()
        imageFile.append('image', this.selectedFile)

        const apiKey = '0e63d9a73b29cb9e1c85f0279f834367'
        const url = "https://dapi.kakao.com/v2/vision/face/detect"
        const headers = {
          "Content-Type": 'multipart/form-data',
          'Authorization': `KakaoAK ${apiKey}`
        }
        axios.post(url, imageFile, {headers: headers})
          .then(res => {
            // 얼굴이 검출되지 않은 경우,
            if (res.data.result.faces.length === 0) {
              this.$emit('on-error', '얼굴이 없거나, 확인이 불가합니다.')
            }
            // 검출완료
            else {
              const url = 'http://localhost:8000/spark/userface/'
              console.log(res.data)
              axios.post(url, res.data)
                .then(res => console.log(res))
                .catch(err => console.log(err))
            }
          })
        .catch(err => console.log(err))
      }
    }

  }

}
</script>

<style scoped>

</style>