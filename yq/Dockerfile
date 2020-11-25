FROM python:3.8-alpine3.11@sha256:2fb38c4143e3b4a234731ee16b84ed8165e945f9aa077e941f7618d0e9c5a127
RUN apk add jq && pip install yq
ENTRYPOINT [ "/usr/local/bin/yq" ]