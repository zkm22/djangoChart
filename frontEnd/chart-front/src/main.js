import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import vueAxios from 'vue-axios'
import sessionStorage from './assets/js/sessionStorage'

Vue.config.productionTip = false
Vue.use(vueAxios, axios)

Vue.prototype.sessionStorage = sessionStorage

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
