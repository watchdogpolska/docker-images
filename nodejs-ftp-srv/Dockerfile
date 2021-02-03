FROM node:10@sha256:e7948c8721f6ed5f6c78ead4c3942526c5ddef94f5859c61639bfd55ca751fbb
WORKDIR /src
COPY ./package* ./
RUN npm install
COPY . .
ENV USER_DB=/etc/ftp-srv/user.json
ENV FTP_ROOT=/data
ENV FTP_URL="ftp://0.0.0.0:21"

CMD ["node", "index.js"]
