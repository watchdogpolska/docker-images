FROM node:12-alpine@sha256:1c5f444d75cc3ed4e3dee50f07aa66eba616c45217d6c8600819e4b245b8215e
WORKDIR /src
COPY . .
RUN npm ci
CMD ["npm","run","lint"]

FROM node:12-alpine@sha256:1c5f444d75cc3ed4e3dee50f07aa66eba616c45217d6c8600819e4b245b8215e
WORKDIR /src
COPY package* ./
ENV NODE_ENV=production
RUN npm ci
COPY . .
EXPOSE 3000
CMD ["node","index.js"]
