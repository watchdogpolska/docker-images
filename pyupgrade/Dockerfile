FROM python:3.8-slim@sha256:8dab48a48334878a58fd7898e636eb1f964b8bba1ca79f29f9c9ceddd9b3d198
RUN pip install pyupgrade
WORKDIR /data
COPY ./docker-entrypoint.sh /usr/bin/
ENTRYPOINT [ "docker-entrypoint.sh" ]
CMD ["--py3-plus"]
