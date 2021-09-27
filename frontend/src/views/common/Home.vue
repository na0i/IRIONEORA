<template>
  <div class="home">
    <input type="text" placeholder="아이디">
    <input type="password" placeholder="비밀번호">
    <button>로그인하기</button>
  </div>
</template>

<script>

export default {
  name: 'Home',
}
</script>

<style scoped>
  div {
    position: absolute;
    top: 0;
    z-index: 100;
    background: #081420;
  }
  div input {
    height: 50px;
    display: block;
    width: 100vw;
    max-width: 425px;
    margin: 10px 0;
  }
</style>