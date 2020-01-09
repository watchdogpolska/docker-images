FROM python:3.8-alpine3.11
RUN apk add jq && pip install yq
ENTRYPOINT [ "/usr/local/bin/yq" ]