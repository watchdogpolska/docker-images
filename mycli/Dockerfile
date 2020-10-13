FROM python:3.8-slim@sha256:064c43de1bdf0e29192c7e8f75af94dd6981f7412b252546730efc7e22fa274a
RUN pip install mycli
ADD ./entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
