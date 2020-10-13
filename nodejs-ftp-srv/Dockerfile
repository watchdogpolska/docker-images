FROM node:10@sha256:a72ca257ecfe43c1945a63ff4dfe298452ac8ffd11202f933062960aadba3e31
WORKDIR /src
COPY ./package* ./
RUN npm install
COPY . .
ENV USER_DB=/etc/ftp-srv/user.json
ENV FTP_ROOT=/data
ENV FTP_URL="ftp://0.0.0.0:21"

CMD ["node", "index.js"]
