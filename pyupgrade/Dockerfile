FROM python:3.9-slim@sha256:655f71f243ee31eea6774e0b923b990cd400a0689eff049facd2703e57892447
RUN pip install pyupgrade
WORKDIR /data
COPY ./docker-entrypoint.sh /usr/bin/
ENTRYPOINT [ "docker-entrypoint.sh" ]
CMD ["--py3-plus"]
