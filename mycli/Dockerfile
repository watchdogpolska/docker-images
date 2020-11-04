FROM python:3.8-slim@sha256:9d274288c74f943a7ee9a8b529f9d37e3457787118276417fbe572c767ff796d
RUN pip install mycli
ADD ./entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
