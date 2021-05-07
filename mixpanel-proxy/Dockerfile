FROM node:12-alpine@sha256:9923c9efb13cf7535f67e49b03010f0977a800068e4c8e0e2c93433a6bfa1e77
WORKDIR /src
COPY . .
RUN npm ci
CMD ["npm","run","lint"]

FROM node:12-alpine@sha256:9923c9efb13cf7535f67e49b03010f0977a800068e4c8e0e2c93433a6bfa1e77
WORKDIR /src
COPY package* ./
ENV NODE_ENV=production
RUN npm ci
COPY . .
EXPOSE 3000
CMD ["node","index.js"]
