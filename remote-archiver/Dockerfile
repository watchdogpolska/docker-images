FROM alpine:3.12@sha256:3c7497bf0c7af93428242d6176e8f7905f2201d8fc5861f45be7a346b5f23436
RUN apk add --no-cache postgresql mariadb-client bash && \
adduser user -D && \
mkdir /output && \
chown user:user /output
USER user
VOLUME /output
COPY . .
CMD ./start.sh