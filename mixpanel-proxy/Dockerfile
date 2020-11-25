FROM node:12-alpine@sha256:a9ee412baa5c130dea5f8483e95890f8d7e499dda196973f4397189b0bb98244
WORKDIR /src
COPY . .
RUN npm ci
CMD ["npm","run","lint"]

FROM node:12-alpine@sha256:a9ee412baa5c130dea5f8483e95890f8d7e499dda196973f4397189b0bb98244
WORKDIR /src
COPY package* ./
ENV NODE_ENV=production
RUN npm ci
COPY . .
EXPOSE 3000
CMD ["node","index.js"]
