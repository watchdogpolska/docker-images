FROM alpine:3.14@sha256:234cb88d3020898631af0ccbbcca9a66ae7306ecd30c9720690858c1b007d2a0
RUN apk add --no-cache postgresql mariadb-client bash && \
adduser user -D && \
mkdir /output && \
chown user:user /output
USER user
VOLUME /output
COPY . .
CMD ./start.sh