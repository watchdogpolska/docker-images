FROM node:10@sha256:59531d2835edd5161c8f9512f9e095b1836f7a1fcb0ab73e005ec46047384911
WORKDIR /src
COPY ./package* ./
RUN npm install
COPY . .
ENV USER_DB=/etc/ftp-srv/user.json
ENV FTP_ROOT=/data
ENV FTP_URL="ftp://0.0.0.0:21"

CMD ["node", "index.js"]
