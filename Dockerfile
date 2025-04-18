ARG DOCKER_REGISTRY="docker.io"
FROM ${DOCKER_REGISTRY}/python:3.13.2

EXPOSE 8000

WORKDIR /opt/app
VOLUME ["/opt/app/public", "/opt/app/log"]
COPY . .

ARG PIP_INDEX_URL
ARG PIP_TRUSTED_HOST

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.gunicorn.txt --default-timeout=100

RUN chgrp -R 0 /opt/app/ && chmod -R g=u /opt/app/
RUN ["chmod", "+x", "/opt/app/docker-entrypoint.sh"]
RUN ["chmod", "+x", "/opt/app/wait-for-it.sh"]

RUN mkdir /var/log/web_app/ && \
    chgrp -R 0 /var/log/web_app/ && chmod -R g=u /var/log/web_app/

ENTRYPOINT ["/opt/app/docker-entrypoint.sh"]