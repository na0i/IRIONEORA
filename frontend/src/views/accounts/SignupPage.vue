<template>
  <div>
    <div class="input-with-button">
      <UserInput class="user-input set"
          id="email" label="이메일" placeholder="이메일을 입력하세요" type="email"
          :input.sync="email" :error="error.email"
          @keyup-enter="moveFocusToPw" ref="email"/>
      <a @click.prevent="checkEmail" v-if="needCheck.email" :class="{disabled: error.email||!email.length}">중복확인</a>
      <a v-else class="success">확인완료</a>
    </div>

    <div class="input-with-button">
      <UserInput class="user-input set"
          id="nickname" label="닉네임" placeholder="닉네임을 입력하세요" type="text"
          :input.sync="nickname" :error="error.nickname" :label-right="needCheck.nickname"
          @keyup-enter="moveFocusToEmail" ref="nickname"/>
      <a @click.prevent="checkNickname" v-if="needCheck.nickname" :class="{disabled: error.nickname||!nickname.length}">중복확인</a>
      <a v-else class="success">확인완료</a>
    </div>


    <UserInput class="user-input"
        id="password" label="비밀번호" placeholder="비밀번호를 입력하세요" type="password"
        :input.sync="password" :error="error.password"
        @keyup-enter="moveFocusToPwConfirm" ref="password"/>

    <UserInput class="user-input"
        id="password-confirm" label="비밀번호<br/>확인" placeholder="비밀번호를 다시 입력하세요" type="password"
        :input.sync="passwordConfirm" :error="error.passwordConfirm"
        @keyup-enter="onSignup" ref="passwordConfirm"/>

    <button class="button" :disabled="isDisabled" @click="onSignup">회 원 가 입</button>
  </div>
</template>

<script>
export default {
  name: "SignupPage"
}
</script>

<style scoped>

</style>