FROM python:3.8-alpine3.11@sha256:4b9149da5d775bdb86463135b2c044d96305623b60503d10e2da84ec5c40cfcf
RUN apk add jq && pip install yq
ENTRYPOINT [ "/usr/local/bin/yq" ]