FROM python:3.8-slim@sha256:06f2b34e0a84cf236c68c11c302b7a5a6a4a89db09ba30284223b82fb6428a2a
RUN pip install mycli
ADD ./entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
