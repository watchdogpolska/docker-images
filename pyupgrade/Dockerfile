FROM python:3.8-slim@sha256:e5000e56eabd767f1a3f01df80fa568d6ecd16cd5110a78ae5d03b7f97a9e00c
RUN pip install pyupgrade
WORKDIR /data
COPY ./docker-entrypoint.sh /usr/bin/
ENTRYPOINT [ "docker-entrypoint.sh" ]
CMD ["--py3-plus"]
