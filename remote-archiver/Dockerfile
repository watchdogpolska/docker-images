FROM alpine:3.12
RUN apk add --no-cache postgresql mariadb-client bash && \
adduser user -D && \
mkdir /output && \
chown user:user /output
USER user
VOLUME /output
COPY . .
CMD ./start.sh