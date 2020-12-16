FROM python:3.8-slim@sha256:3a7b2ec271aa68b4718021b0c9137d2945d4103bbb24705eeebb6669d4b6b0d7
RUN pip install mycli
ADD ./entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
