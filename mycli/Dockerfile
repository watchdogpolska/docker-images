FROM python:3.8-slim@sha256:6a6a4c1f2b2813b2745868469afb3177501dd97afa91153295130bdb90f7e4dd
RUN pip install mycli
ADD ./entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
