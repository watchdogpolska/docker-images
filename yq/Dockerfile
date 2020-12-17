FROM python:3.8-alpine3.11@sha256:de030467d42a62229b6284a75a72c2f0f994501f8f6b6771a7d441b985fc1fd6
RUN apk add jq && pip install yq
ENTRYPOINT [ "/usr/local/bin/yq" ]