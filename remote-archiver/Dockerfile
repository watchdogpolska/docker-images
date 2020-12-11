FROM alpine:3.12@sha256:25f5332d060da2c7ea2c8a85d2eac623bd0b5f97d508b165f846c7d172897438
RUN apk add --no-cache postgresql mariadb-client bash && \
adduser user -D && \
mkdir /output && \
chown user:user /output
USER user
VOLUME /output
COPY . .
CMD ./start.sh