<template>
  <div id="login">

    <div class="login-input">

    <UserInput class="user-input"
        id="username" label="아이디" placeholder="아이디를 입력하세요" type="text"
        :input.sync="username" :error="error.username"
        @keyup-enter="moveFocusToPw" @on-focus="onFocus" ref="username"/>

    <UserInput class="user-input"
        id="password" label="비밀번호" placeholder="비밀번호를 입력하세요" type="password"
        :input.sync="password" :error="error.password"
        @keyup-enter="onLogin" @on-focus="onFocus" ref="password"/>
    </div>

    <div v-if="loginError.isFailed" class="error-message">
      {{ loginError.message }}
    </div>

    <button class="button" :disabled="!isSubmit" @click="onLogin">로 그 인</button>

    <KakaoLogin></KakaoLogin>



  </div>
</template>

<script>
import cookies from "vue-cookies";
import PV from "password-validator"
import AccountsApi from "@/api/accounts";
import UserInput from "@/components/accounts/UserInput";
import KakaoLogin from "@/components/accounts/KakaoLogin";

export default {
  name: "Login",
  // components
  components: {
    UserInput,
    KakaoLogin
  },
  // props
  // data
  data() {
   return {
     username: "",
     password: "",
     passwordSchema: new PV(),
     autoLogin: false,
     error: {
       username: false,
       password: false
     },
     isSubmit: false,
     loginError: {
       isFailed: false,
       message: "입력하신 정보와 일치하는 아이디 혹은 비밀번호가 존재하지 않습니다."
     },
   }
  },
  // methods
  methods: {
    // 형식 검증
    checkForm() {
      // 아이디, 비밀번호 입력됐으면 버튼 활성화
      if (this.password && this.username)
        this.isSubmit = true

    },

    // 로그인
    onLogin() {
      if (this.isSubmit) {
        let {username, password} = this
        let data = {
          username,
          password,
        }

        // 버튼 비활성화
        this.isSubmit = false

        AccountsApi.requestLogin(data)
          // 로그인 성공
          .then(res => {
            const token = res.data.key
              // 회원 프로필 저장
              AccountsApi.requestProfile(token)
                .then(res =>
                  this.$store.dispatch('setProfileInfo', res.data)
                )

              // 쿠키에 유저 토큰 저장
              cookies.set('user-token', token, 0)
              this.$router.back()
            })

          // 로그인 실패
          .catch(() => {
            this.loginError.isFailed = true
            this.$refs.username.onReset()
            this.$refs.password.onReset()
          })
      }
    },

    // 로그인 실패 에러메시지가 노출되어 있을 때,
    // 새로 로그인을 시도하는 경우, 해당 메시지 사라지도록
    onFocus() {
      this.loginError.isFailed = false
    },

    // 입력 칸 포커스 이동
    moveFocusToPw() {
      document.getElementById('username').blur()
      document.getElementById('password').focus()
    },
  },
  // computed
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn
    }
  },
  // watch
  watch: {
    username: function () {
      // 대문자 입력 방지
      this.username = this.username.toLowerCase()
    },
    password: function () {
      this.checkForm()
    },
    isLoggedIn() {
      // 이전에 거쳐온 히스토리 기록이 없으면 메인 페이지로 -> 새로고침으로 인한 현상
      if (Object.keys(this.$route.params).length === 0) {
        this.$router.back()
        // 프로필 페이지에서 넘어왔음
      } else
        if (this.$route.params.history === '/user/profile/undefined') {
        const nickname = this.$store.state.user.loginUser.nickname
        this.$router.push(`/user/profile/${nickname}`)
      // 이전에 왔던 곳으로
      } else {
        this.$router.push(this.$route.params.history)
      }
    }
  },
  // lifecycle hook
  //navigation guard
}
</script>

<style scoped>

#login {
  margin-top: 40px;
  display: flex;
  flex-direction: column;
  /*position: absolute;*/
  /*width: 90%;*/
  /*top: 60px;*/
}

#login .back-button {
  /*position: absolute;*/
  /*top: 10px;*/
  display: flex;
  margin-top: 10px;
}

#login #title {
  color: #183a1d;
  margin: 30px 0 40px;
  padding: 10px 0;
  font-size: 1.4em;
}

.user-input {
  width: 90%;
  margin-left: 5%;
}

.error-message {
  color: #cd4e3e;
  margin-bottom: 20px;
  font-size: 0.8em;
  font-weight: bold;
  width: 65%;
  align-self: center;
}

/* 자동로그인 */
.login-duration {
  width: 80%;
  margin: auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.8em;
}

.switch {
    display: inline-block;
    height: 25px;
    position: relative;
    width: 50px;
}

.switch > input {
    height: 0px;
    opacity: 0;
    width: 0px;
}

.switch > .switch-slider {
    -webkit-transition: .4s;
    background-color: #ccc;
    border-radius: 20px;
    bottom: 0;
    cursor: pointer;
    left: 0;
    position: absolute;
    right: 0;
    top: 0;
    transition: .4s;
}

.switch > .switch-slider:before {
    -webkit-transition: .4s;
    background-color: white;
    border-radius: 50%;
    bottom: 4px;
    content: "";
    height: 18px;
    left: 4px;
    position: absolute;
    transition: .4s;
    width: 18px;
}

.switch > input:checked + .switch-slider:before {
    -ms-transform: translateX(24px);
    -webkit-transform: translateX(24px);
    transform: translateX(24px);
}

.switch.switch-off-primary > input + .switch-slider {
  background-color: #183a1d;
}

.switch.switch-primary > input:checked + .switch-slider {
  background-color: #183a1d;
  box-shadow: 0 0 3px #183a1d;
}

.switch-sm > .switch-slider:before {
    height: 18px;
    width: 18px;
}
.switch-sm > input:checked + .switch-slider:before {
    -ms-transform: translateX(22px);
    -webkit-transform: translateX(22px);
    transform: translateX(22px);
}




.button {
  width: 90%;
  margin-left: 5%;
  margin-top: 20px;
  height: 50px;
  background-color: #183a1d;
  color: #e1eedd;
  border-radius:25px;
  box-shadow: 0 0 15px -8px rgba(0, 0, 0, 0.55);
  font-size: 1em;
  cursor: pointer;
}
.button:disabled {
  opacity: 0.6;
  cursor: default;
}

/* 소셜로그인, 회원가입 */
.login-description{
  width: 90%;
  margin-left: 5%;
  font-family: GongGothicLight;
  font-size: 0.9em;
  color: #183a1d;
}

hr {
  display: inline-block;
  width: calc((100% - 200px) / 2)
}

#login-social {
  display: flex;
  align-items: center;
  justify-items: start;
  justify-content: space-between;
  margin-top: 40px;
}

.kakao-login {
  height: 40px;
}

.kakao-login-long {
  height: 50px;
  width: 90%;
  margin: auto;
  /*margin-left: 5%;*/
  /*margin-top: 10px;*/
}


#login-to-signup .login-description{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 80px;
  margin-bottom: 30px;
}


#to-signup-button {
  width: 90%;
  margin: auto;
}
</style>


<!--<style lang="scss" scoped>-->
<!--  @import "src/assets/style/accounts/Login";-->
<!--</style>-->