FROM node:10@sha256:798efbc0842cf57fbdb9a56ac01a95ad5160eb9d836ce7c9b364103ae1b3a0b7
WORKDIR /src
COPY ./package* ./
RUN npm install
COPY . .
ENV USER_DB=/etc/ftp-srv/user.json
ENV FTP_ROOT=/data
ENV FTP_URL="ftp://0.0.0.0:21"

CMD ["node", "index.js"]
