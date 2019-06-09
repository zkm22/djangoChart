<template>
  <div id="loading" v-if="loading">
    <div class="spin">
      <div class="spin-item item1"></div>
      <div class="spin-item item2"></div>
      <div class="spin-item item3"></div>
      <div class="spin-item item4"></div>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    loading: {
      type: Boolean,
      default: false
    }
  }
}
</script>
<style lang="scss" scoped>
#loading {
  width: 100%;
  height: 100%;
  text-align: center;
  display: inline-block;
  vertical-align: middle;
  position: absolute;
  left: 0;
  top: 0;
  background-color: rgba(51, 51, 51, 0.1);
  opacity: 0.9;
  z-index: 1000;
  .spin {
    // border: 4px solid green;
    // border-radius: 50%;
    position: relative;
    width: 32px;
    height: 32px;
    top: 50%;
    left: 50%;
    background-color: transparent;
    animation: round 3s infinite linear;
    .spin-item {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background-color: #19C0BA;
      position: absolute;
      &.item1 {
        left: 0;
        top: 0;
        animation: spin-inner1 1s infinite cubic-bezier(.23,0,.71,.71) alternate;
      }
      &.item2 {
        right: 0;
        top: 0;
        animation: spin-inner2 1s infinite cubic-bezier(.23,0,.71,.71) alternate;
      }
      &.item3 {
        left: 0;
        bottom: 0;
        animation: spin-inner3 1s infinite cubic-bezier(.23,0,.71,.71) alternate;
      }
      &.item4 {
        right: 0;
        bottom: 0;
        animation: spin-inner4 1s infinite cubic-bezier(.23,0,.71,.71) alternate;
      }
    }
  }
}
@keyframes round {
  0% {
    transform:rotate(0deg)
  }
  100% {
    transform:rotate(720deg)
  }
}
@keyframes spin-inner1 {
  100% {
    left: calc(50% - 8px);
    top: calc(50% - 8px);
  }
}
@keyframes spin-inner2 {
  100% {
    right: calc(50% - 8px);
    top: calc(50% - 8px);
  }
}
@keyframes spin-inner3 {
  100% {
    left: calc(50% - 8px);
    bottom: calc(50% - 8px);
  }
}
@keyframes spin-inner4 {
  100% {
    right: calc(50% - 8px);
    bottom: calc(50% - 8px);
  }
}
</style>
