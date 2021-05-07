FROM alpine:3.12@sha256:36553b10a4947067b9fbb7d532951066293a68eae893beba1d9235f7d11a20ad
RUN apk add --no-cache postgresql mariadb-client bash && \
adduser user -D && \
mkdir /output && \
chown user:user /output
USER user
VOLUME /output
COPY . .
CMD ./start.sh