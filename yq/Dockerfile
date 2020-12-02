FROM python:3.8-alpine3.11@sha256:8a92fb73a63be8e206a1ba8b4c7da0e827ef4270e21021764d66d08cef6899ab
RUN apk add jq && pip install yq
ENTRYPOINT [ "/usr/local/bin/yq" ]