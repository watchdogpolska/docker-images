FROM python:3.8-slim@sha256:76ae1f8d27616e0688df6689c2fd1c9a7482eb37984dc0402f6393ac47abfcaa
RUN pip install pyupgrade
WORKDIR /data
COPY ./docker-entrypoint.sh /usr/bin/
ENTRYPOINT [ "docker-entrypoint.sh" ]
CMD ["--py3-plus"]
