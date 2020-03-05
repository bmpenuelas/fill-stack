import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'

{% if render_features['vue-socialauth'] %}
const HelloJs = require('hellojs/dist/hello.all.min.js');
const VueHello = require('vue-hellojs');
{% endif %}


Vue.config.productionTip = false

{% if render_features['vue-socialauth'] %}
HelloJs.init({
  facebook: "{{ FS_DJANGO_SOCIALAUTH_FACEBOOK_APP_ID }}",
}, {redirect_uri: 'socialauth_callback'});
Vue.use(VueHello, HelloJs);
{% endif %}

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
