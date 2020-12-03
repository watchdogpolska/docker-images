FROM python:3.8-slim@sha256:1da93917f765c29a35eb0212980a0e398a620ab66fd5e7fdade12d37d1d39975
RUN pip install mycli
ADD ./entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
