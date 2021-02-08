FROM node:10@sha256:033ebaadc711dbfc3b6805c6202e88a2aaf764448dc720a5c4e0396bdf54482e
WORKDIR /src
COPY ./package* ./
RUN npm install
COPY . .
ENV USER_DB=/etc/ftp-srv/user.json
ENV FTP_ROOT=/data
ENV FTP_URL="ftp://0.0.0.0:21"

CMD ["node", "index.js"]
