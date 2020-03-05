{% if render_features['vue'] %}
# build stage
FROM node:lts-alpine as build-stage
WORKDIR /vue_app
COPY ./vue/{{ FS_VUE_PROJECT_NAME }}/package*.json ./
RUN npm install
COPY ./vue/{{ FS_VUE_PROJECT_NAME }}/ /vue_app
RUN npm run build
{% endif %}

# production stage
FROM nginx:stable-alpine as production-stage

WORKDIR /
RUN rm /etc/nginx/nginx.conf
RUN rm /etc/nginx/conf.d/default.conf
COPY /nginx/nginx.conf /etc/nginx/nginx.conf
COPY /nginx/sites-enabled /etc/nginx/sites-enabled

{% if render_features['vue'] %}
COPY --from=build-stage /vue_app/dist /usr/share/nginx/html
{% endif %}
