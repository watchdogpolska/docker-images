FROM python:3.8-alpine3.11@sha256:927e4e9ea8182f99b9bd317603a31908f56d90ca82d15498bfc7d0a625220034
RUN apk add jq && pip install yq
ENTRYPOINT [ "/usr/local/bin/yq" ]