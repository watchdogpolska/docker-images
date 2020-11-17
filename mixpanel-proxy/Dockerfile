FROM node:12-alpine@sha256:1a97b805edf24b591ba099be67a2b74f9a156d56805ead8fe58c6da35e59f076
WORKDIR /src
COPY . .
RUN npm ci
CMD ["npm","run","lint"]

FROM node:12-alpine@sha256:1a97b805edf24b591ba099be67a2b74f9a156d56805ead8fe58c6da35e59f076
WORKDIR /src
COPY package* ./
ENV NODE_ENV=production
RUN npm ci
COPY . .
EXPOSE 3000
CMD ["node","index.js"]
