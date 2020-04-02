<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    {% if render_features['vue-socialauth'] %}
    <SocialLogin/>
    {% endif %}
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
{% if render_features['vue-socialauth'] %}
import SocialLogin from '@/components/SocialLogin.vue'
{% endif %}
import { axiosAPI } from '@/config/axios/AxiosInstance.js'


export default {
  name: 'home',
  components: {
    HelloWorld,
    {% if render_features['vue-socialauth'] %}
    SocialLogin,
    {% endif %}
  },
  mounted () {
    // This will prove requests fail unless properly authenticated
    // Get an auth token and send it along the request to make it succeed
    axiosAPI.get('/test')
      // .then(response => {
      //   console.log(response)
      // })
      // .catch((error) => console.log(error))
  }
}
</script>
