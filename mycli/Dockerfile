FROM python:3.8-slim@sha256:25596dee08bf6fdffeb56f5c48472c5cbe238b6182902481adf4c595cdcc2fa4
RUN pip install mycli
ADD ./entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
