FROM python:3.8-alpine3.11@sha256:83c0e3d83c345cc01ff4ccacffcc48a39267fa3304173dd2c7a9683924735107
RUN apk add jq && pip install yq
ENTRYPOINT [ "/usr/local/bin/yq" ]