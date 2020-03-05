<template>
  <div>
    <div class="container-fluid">
      <div class="row">
        <div class="login-buttons col-xs-12 col-md-6 clearfix">
          <button class="btn btn-default" @click="authenticate('facebook')">
            <i class="fa fa-facebook" aria-hidden="true"></i> Login to Facebook</button>
        </div>
        <div class="login-response col-xs-12 col-md-6">
          <h4 class="text-primary">hello(network).getAuthResponse()</h4>
          <div class="well well-lg">{% raw %}{{authRes}}{% endraw %}</div>
          <h4 class="text-primary">hello(network).api('me')</h4>
          <div class="well well-lg">{% raw %}{{profileRes}}{% endraw %}</div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  name: 'SocialLogin',
  data() {
    return {
      authRes: "none",
      profileRes: "none"
    }
  },
  methods: {
    authenticate(network) {
      const _this = this;
      const hello = this.hello;
      hello(network).login().then(() => {
        const authRes = hello(network).getAuthResponse();
        /*
          performs operations using the token from authRes
        */
        let output = JSON.stringify(authRes, undefined, 4);
        _this.authRes = output;
        hello(network).api('me').then(function (profile) {
          /*
            performs operations using the user info from profile
          */
          let output = JSON.stringify(profile, undefined, 4);
          _this.profileRes = output;
        });
      })
    }
  }
}
</script>


<style scoped lang=scss>
.login-buttons {
  button {
    float: right;
    display: block;
    clear: both;
    margin-bottom: 20px;
    i.fa {
      margin-right: 5px;
    }
  }
}

.well {
  white-space: pre;
  overflow-x: scroll;
}
</style>
