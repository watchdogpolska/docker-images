FROM python:3.8-slim@sha256:59f664c8f7aa6c3958f440ed73229bf57eb5c2cea15e533a62388a0ea6ac9fe4
RUN pip install mycli
ADD ./entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
