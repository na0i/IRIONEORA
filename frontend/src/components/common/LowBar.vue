<template>
  <div class="low-bar">
    <div class="name">
      이리오너라(IRIONEORA)
    </div>
    <a
        class="notion"
        href="https://equatorial-skirt-01e.notion.site/A601-3bc429ffa68d48c2a81a5a77d6d1a132"
        target="_blank"
    >
      Copyrightⓒ2021 by 오이려좋아
    </a>
  </div>
</template>

<script>
export default {
  name: "LowBar"
}
</script>

<style scoped>
.low-bar {
  width: 100%;
  height: 50px;
  max-width: 425px;
  background: rgba(222, 200, 164, 0.2);
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.name {
  color: #FFFFFF;
  font-weight: 400;
  font-size: 10px;
  align-self: center;
}

.notion {
  color: #848063;
  font-weight: 300;
  font-size: 8px;
  align-self: center;
}

</style>