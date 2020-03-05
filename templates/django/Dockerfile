# use base python image with python 3
FROM python:3

# add sources
RUN mkdir /django
COPY . /django

# install python dependencies
RUN pip install -r /django/requirements.txt

# create unprivileged user
RUN adduser --disabled-password --gecos '' {{ FS_DOCKER_USERNAME }}
