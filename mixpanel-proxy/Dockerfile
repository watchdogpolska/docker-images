FROM node:12-alpine
WORKDIR /src
COPY . .
RUN npm ci
CMD ["npm","run","lint"]

FROM node:12-alpine
WORKDIR /src
COPY package* ./
ENV NODE_ENV=production
RUN npm ci
COPY . .
EXPOSE 3000
CMD ["node","index.js"]
