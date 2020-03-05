# {{ FS_PRODUCT_NAME }}


## SECRETS!

The file `.env` in the root directory contains all your production secrets. Make sure you handle that file properly:

    * **Do not use default values in production.** Set your passwords making sure that they are strong enough.
    * **Store it properly.** Most times it's best to avoid including it in your repository. If possible, keep it in a separate safe storage.



{% if render_features['aws-docker-machine'] %}
## Django-REST
### Django + REST framework

Secrets example:
```
    ENV_DJANGO_DEBUG=True
    ENV_DJANGO_SECRET_KEY=useAveryL0ngK3yWith$ymbolS
    ENV_DJANGO_ADMIN_USER=your_admin
    ENV_DJANGO_ADMIN_EMAIL=your_email
    ENV_DJANGO_ADMIN_PASSWORD=aStrongPassw0rd
```



{% endif %}
{% if render_features['django-socialauth'] %}
## Social Authentication
### Provide the ability to login with Facebook, Google, ... etc.

Setup all the providers you want, and get the API secret tokens. Store those in your `.env` file.

Example, for *login with Facebook*

- Choose ENV_DJANGO_SOCIALAUTH_CLIENT_ID (*recommended 40 characters long*) and ENV_DJANGO_SOCIALAUTH_CLIENT_SECRET (*recommended 128 characters long*)

- Create an app at [developers.facebook](https://developers.facebook.com/apps/). There, you get:
    - DJANGO_SOCIALAUTH_FACEBOOK_APP_ID
    - ENV_DJANGO_SOCIALAUTH_FACEBOOK_APP_SECRET

- For testing, you can get a debug [User Token](https://developers.facebook.com/tools/accesstoken/)


Request an *access_token* from your backend in exchange for a **Facebook** *user_token* with:

```
curl -X POST -d "grant_type=convert_token&client_id=**<your-ENV_DJANGO_SOCIALAUTH_CLIENT_ID>**&client_secret=**<your-ENV_DJANGO_SOCIALAUTH_CLIENT_SECRET>**&backend=facebook&token=**<your-User-Token>**" http://0.0.0.0/{{ FS_API_PATH }}/auth-social/convert-token
```

The returned `access_token` is the one you can use from this moment on to authenticate requests directly with your backend, without needing to ask Facebook every time. To request an authentication-protected view, add the `access_token` to the request headers as:

| Header | Content |
|---|---|
Authorization | Bearer <your_access_token> |


Now you can try requesting the included `/test` endpoint, which by default requires authentication:
```
curl -H "Authorization: Bearer <your_access_token>" -X POST http://0.0.0.0/{{ FS_API_PATH }}/test
```



{% endif %}
{% if render_features['django-jwt'] %}
## django-jwt
### JSON Web Token Authentication support for Django REST framework.

More info on how to customize your settings at [github.io/django-rest-framework-jwt](http://jpadilla.github.io/django-rest-framework-jwt/)



{% endif %}
{% if render_features['aws-docker-machine'] %}
## AWS
### Steps to deploy to EC2 using docker-machine

* Install [Docker Machine](https://docs.docker.com/machine/install-machine/).

* Install [AWS cli](https://docs.aws.amazon.com/cli/latest/userguide/install-linux-al2017.html).

* [Create a user](https://console.aws.amazon.com/iam/home?#users) and assign it a group with enough permissions.

* Enter the created credentials and desired [zone](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) in:

    `aws configure`


* Start the new instance:

    `docker-machine create --driver amazonec2 <machine_name>`

    (for additional parameters run: `docker-machine -D create --driver amazonec2 --help`)


* Open the ports that you need (i.e HTTP, HTTPS...):

    *[EC2 dashboard](https://console.aws.amazon.com/ec2) > Security Groups > YourGroupName > Inbound / Outbound tabs*


* Activate it:

    `eval $(docker-machine env <machine_name>)`

* Now you can use docker-compose on the AWS ec2 as if you were running it locally:

    `docker-compose up` ...



### Useful commands

* List available machines

    `docker-machine ls`


* Start / Stop EC2 instances

    `docker-machine [start|stop] <machine_name>`


* Get the public IP of an instance

    `docker-machine ip <machine_name>`


* SSH into an instance

    `docker-machine ssh <machine_name>`


* Stop and rebuild all / a service

    `docker-compose up -d --no-deps --build <service_name>`


* Remove the EC2 instance

    `docker-machine rm <machine_name>`


* You can add the previous commands to your `~/.bashrc` as more handy aliases:
    ```
    alias dcu='docker-compose up'
    alias dcd='docker-compose down'
    alias dcr='docker-compose up -d --no-deps --build'

    alias dmc='docker-machine create --driver amazonec2'
    alias dmls='docker-machine ls'
    alias dmstart='docker-machine start'
    alias dmstop='docker-machine stop'
    alias dmip='docker-machine ip'
    alias dmssh='docker-machine ssh'
    alias dmrm='docker-machine rm'

    function dmenv {
        eval $(docker-machine env $1)
    }
    function dmenvrm {
        eval $(docker-machine env -u)
    }
    ```



{% endif %}
{% if render_features['noip'] %}
## No-IP
### Configuration for noip dynamic DNS auto-update

Enter your [noip](https://my.noip.com) username, password and desired update rate in the `.env` file.

Secrets example:
```
    ENV_NOIP_USER=myusername
    ENV_NOIP_PASSWORD=mypassword
    ENV_NOIP_INTERVAL=15m
```

Make sure you have *only one host* in that account, **all the hosts in the account will be updated** to the IP of the machine that runs this docker container.



{% endif %}
{% if render_features['https-portal'] %}
## https support
### Via https-portal reverse proxy with LetsEncrypt

You will have out-of-the-box https certicates issued, installed and renewed automatically.

Just pay attention to the rate limits of LetsEncrypt, set your `.env` to `local` (*default*) or `staging` in order to not extinguish the limit. `staging` is great for developing once your project is online, but you are just testing, the certificate will be flagged as non-valid by the browser but you can accept it and continue to your site. Set it to `production` to get real certificates (*caution, the limit is quite low if you keep bringing up and down the container*). Find more details in the [docs](https://github.com/SteveLTN/https-portal).

Example:
```
ENV_HTTPS_PORTAL_STAGE=staging
```



{% endif %}
{% if render_features['dev-hosts'] %}
## development hosts file
### redirect requests to {{ FS_DOMAIN }} to your machine

In order to test locally using **real URLs**, you can run `sudo python3 dev/set_dev_hosts.py` and any request sent to *{{ FS_DOMAIN }}*, or opening the page in your browser, will be redirected to your local machine, not the real online server. Instead of *0.0.0.0* or *localhost*, you can use your real domain without putting your changes online.

When you are done testing, you can revert it with `sudo python3 dev/set_dev_hosts.py -u`



{% endif %}
