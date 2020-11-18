FROM node:10@sha256:69c6890c8dc83f1cf0b1e5120a918180ed3c1e08b43c981d595377f3462ffcc8
WORKDIR /src
COPY ./package* ./
RUN npm install
COPY . .
ENV USER_DB=/etc/ftp-srv/user.json
ENV FTP_ROOT=/data
ENV FTP_URL="ftp://0.0.0.0:21"

CMD ["node", "index.js"]
