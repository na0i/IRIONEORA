<template>
  <div>
    <div class="input-with-button">
      <UserInput class="user-input set"
          id="username" label="아이디" placeholder="아이디를 입력하세요" type="text"
          :input.sync="username" :error="error.username"
          @keyup-enter="moveFocusToNickname" ref="username"/>
      <a @click.prevent="checkUsername" v-if="needCheck.username" :class="{disabled: error.username||!username.length}">중복확인</a>
      <a v-else class="success">확인완료</a>
    </div>

    <UserInput class="user-input"
        id="nickname" label="닉네임" placeholder="닉네임을 입력하세요" type="text"
        :input.sync="nickname" :error="error.nickname" :label-right="needCheck.nickname"
        @keyup-enter="moveFocusToPw" ref="nickname"/>


    <UserInput class="user-input"
        id="password1" label="비밀번호" placeholder="비밀번호를 입력하세요" type="password"
        :input.sync="password1" :error="error.password1"
        @keyup-enter="moveFocusToPwConfirm" ref="password1"/>

    <UserInput class="user-input"
        id="password2" label="비밀번호<br/>확인" placeholder="비밀번호를 다시 입력하세요" type="password"
        :input.sync="password2" :error="error.password2"
        @keyup-enter="onSignup" ref="password2"/>

    <button class="button" :disabled="isDisabled" @click="onSignup">회 원 가 입</button>
  </div>
</template>

<script>
import PV from "password-validator";
import UserInput from "@/components/accounts/UserInput";
import AccountsApi from "@/api/accounts";

export default {
  name: "SignupPage",
  components: {
    UserInput
  },
  data() {
    return {
      username: '',
      nickname: '',
      password1: '',
      password2: '',
      passwordSchema: new PV(),
      error: {
        username: false,
        nickname: false,
        password1: false,
        password2: false,
      },
      needCheck: {
        username: true
      },
      isSubmit: false
    }
  },
  methods: {
    // validation
    checkForm() {
      if (this.username.length > 8)
        this.error.username = "최대 8자까지 입력 가능합니다."
      else this.error.username = false

      if (this.nickname.length > 8)
        this.error.nickname = "최대 8자까지 입력 가능합니다."
      else this.error.nickname = false

      if (this.password1.length > 0 && !this.passwordSchema.validate(this.password1))
        this.error.password1 = "영문,숫자 포함 8~16자리를 입력해주세요.";
      else this.error.password1 = false;

      if (this.password2.length > 0 && this.password1 !== this.password2)
        this.error.password2 = "비밀번호가 일치하지 않습니다."
      else this.error.password2 = false

      let isSubmit = true;
      Object.values(this.error).map(v => {
        if (v) isSubmit = false;
      });
      this.isSubmit = isSubmit;
    },

    // 중복확인
    checkUsername() {
      console.log('clicked')
      // GET /user/nickname?nickname="kimssafy"
      let params = {username: this.username}
      console.log(params)
      AccountsApi.requestUsernameCheck(params)
        .then(res => {
          // 중복된 아이디
          if (res.data.error) {
            this.error.username = res.data.result
            this.$refs.username.onReset()
          }
          // 중복확인 완료
          else {
            this.needCheck.username = false
            this.moveFocusToNickname
          }
        })
      .catch(err => console.log(err))
    },

    // 회원가입
    onSignup() {
      if (this.isSubmit) {
        let { username, nickname, password1, password2 } = this
        let data = {
          username,
          nickname,
          password1,
          password2
        }

        this.isSubmit = false;

        AccountsApi.requestSignup(data)
        .then(res => {
          const token = res.data.key
          

        })
      }
    },

    // enter 입력시 다음 칸으로 포커스 이동
    moveFocusToNickname() {
      document.getElementById('username').blur()
      document.getElementById('nickname').focus()
    },
    moveFocusToPw() {
      document.getElementById('nickname').blur()
      document.getElementById('password1').focus()
    },
    moveFocusToPwConfirm() {
      document.getElementById('password1').blur()
      document.getElementById('password2').focus()
    },
  },
  computed: {
    // 버튼 비활성화
    isDisabled() {
      return !(this.nickname.length && this.username.length && this.password1.length && this.password2.length
          && !this.needCheck.username && this.isSubmit)
    }
  },
  watch: {
    // 형식 검증
    username: function (v) {
      this.checkForm()
      // 중복확인이 끝난 후 데이터 값에 변화가 있는 경우, 중복확인 버튼을 다시 살려주기
      if (!this.needCheck.username)
        this.needCheck.username = true
    },
    nickname: function (v) {
      this.checkForm()
    },
    password1: function (v) {
      this.checkForm()
    },
    password2: function (v) {
      this.checkForm()
    }
  },
  // lifecycle hook
  created() {
    this.passwordSchema
      // 영문, 숫자 포함 8~16자리
      .is().min(8)
      .is().max(16)
      .has().digits()
      .has().letters()
  },
}
</script>

<style scoped>

#signup{
  margin-top: 40px;
}


#signup .back-button {
  display: flex;
  margin-top: 10px;
}

#signup #title {
  color: #183a1d;
  margin: 30px 0 40px;
  padding: 10px 0;
  font-size: 1.4em;
}

.user-input {
  width: 90%;
  margin-left: 5%;
}

.user-input.set {
  margin-left: 0;
  width: 76%;
}

.input-with-button {
  display: flex;
  justify-content: space-between;
  margin-left: 5%;
  width: 90%;
}

.input-with-button a {
  width: 21%;
  margin-bottom: 25px;
  margin-left: 3%;
  align-self: center;
  color: #cd4e3e;
  font-size: 0.8em;
  cursor: pointer;
  border: 1px solid #cd4e3e;
  padding: 5px 3px;
  border-radius: 5px;
  box-shadow: 0 0 15px -8px rgba(0, 0, 0, 0.55);
  text-decoration: none;
}

.input-with-button a.disabled {
  /*color: lightgray;*/
  opacity: 0.5;
  /*text-decoration: none;*/
  pointer-events: none;
  cursor: default;
}

.input-with-button a.success {
  color: #6cb9a2;
  /*text-decoration: none;*/
  pointer-events: none;
  cursor: default;
  border: none;
  box-shadow: none;
}

.button {
  width: 90%;
  height: 50px;
  border-radius:25px;
  box-shadow: 0 0 15px -8px rgba(0, 0, 0, 0.55);
  font-size: 1em;
  /*font-weight: bold;*/
  background-color: #183a1d;
  color: #e1eedd;
  cursor: pointer;
}
.button:disabled {
  opacity: 0.6;
  cursor: default;
}
</style>