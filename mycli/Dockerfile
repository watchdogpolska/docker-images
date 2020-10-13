FROM python:3.8-slim@sha256:3a751ba465936180c83904df83436e835b9a919a6331062ae764deefbd3f3b47
RUN pip install mycli
ADD ./entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
