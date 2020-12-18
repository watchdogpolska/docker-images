FROM node:10@sha256:fb7f794d41831f7e00fb5a1cbda9f7db4b317e677bbf316c4c2f69063f44c078
WORKDIR /src
COPY ./package* ./
RUN npm install
COPY . .
ENV USER_DB=/etc/ftp-srv/user.json
ENV FTP_ROOT=/data
ENV FTP_URL="ftp://0.0.0.0:21"

CMD ["node", "index.js"]
