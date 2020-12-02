FROM python:3.8-slim@sha256:036e81d215d304457316e228e4b294a3c6ca6a81ed8145b1319e477de35ed07f
RUN pip install pyupgrade
WORKDIR /data
COPY ./docker-entrypoint.sh /usr/bin/
ENTRYPOINT [ "docker-entrypoint.sh" ]
CMD ["--py3-plus"]
