FROM python:3.8-slim@sha256:3a751ba465936180c83904df83436e835b9a919a6331062ae764deefbd3f3b47
RUN pip install pyupgrade
WORKDIR /data
COPY ./docker-entrypoint.sh /usr/bin/
ENTRYPOINT [ "docker-entrypoint.sh" ]
CMD ["--py3-only"]