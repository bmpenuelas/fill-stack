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

export default {
  name: 'home',
  components: {
    HelloWorld,
    {% if render_features['vue-socialauth'] %}
    SocialLogin,
    {% endif %}
  }
}
</script>
