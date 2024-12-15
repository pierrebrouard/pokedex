# Frontend Dockerfile
FROM node:23-alpine

WORKDIR /

COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

COPY . .

EXPOSE 3000
CMD ["yarn", "dev"]