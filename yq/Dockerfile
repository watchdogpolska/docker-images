FROM python:3.8-alpine3.11@sha256:37273c5aaaf064fbd3ce8d76b8a5b15dbf15ba3fb0236495925e9188fda8078f
RUN apk add jq && pip install yq
ENTRYPOINT [ "/usr/local/bin/yq" ]