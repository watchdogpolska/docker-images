FROM python:3.8-alpine3.11@sha256:bbf35c62b5713a2ed62633046b9fe2d369abcbc4cfd53dd3085abd9f4ac9aeb2
RUN apk add jq && pip install yq
ENTRYPOINT [ "/usr/local/bin/yq" ]