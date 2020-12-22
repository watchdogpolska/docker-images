FROM python:3.8-alpine3.11@sha256:9cf118018dcf5bdc4b3a5632985e0d8516db121d78e06bfd6142ea913cf89152
RUN apk add jq && pip install yq
ENTRYPOINT [ "/usr/local/bin/yq" ]