FROM node:12-alpine@sha256:41ae2b38e38e387517c59ca50498eac0537a2ff2316552c3df3b406d31414d78
WORKDIR /src
COPY . .
RUN npm ci
CMD ["npm","run","lint"]

FROM node:12-alpine@sha256:41ae2b38e38e387517c59ca50498eac0537a2ff2316552c3df3b406d31414d78
WORKDIR /src
COPY package* ./
ENV NODE_ENV=production
RUN npm ci
COPY . .
EXPOSE 3000
CMD ["node","index.js"]
