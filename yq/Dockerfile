FROM python:3.8-alpine3.11@sha256:171b0846bd4c72efd87405878ebbb59c42beffb3b36f3a92111ec75a849b94ae
RUN apk add jq && pip install yq
ENTRYPOINT [ "/usr/local/bin/yq" ]