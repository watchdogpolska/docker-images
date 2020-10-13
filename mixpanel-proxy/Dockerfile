FROM node:12-alpine@sha256:c29fba1f3ea0c23ca3ab59367dc644a594c8186fe28067ea4ac7e51b4a0956a1
WORKDIR /src
COPY . .
RUN npm ci
CMD ["npm","run","lint"]

FROM node:12-alpine@sha256:c29fba1f3ea0c23ca3ab59367dc644a594c8186fe28067ea4ac7e51b4a0956a1
WORKDIR /src
COPY package* ./
ENV NODE_ENV=production
RUN npm ci
COPY . .
EXPOSE 3000
CMD ["node","index.js"]
