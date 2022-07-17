FROM node:18-alpine3.15 AS base
WORKDIR /app
COPY package*.json ./
COPY . .
# ENV PATH /app/node_modules/.bin:$PATH
EXPOSE 8080


FROM base AS dev
RUN npm ci --only=development
RUN npm run tsc
CMD ["node", "dist/app.js"]


FROM base AS production
RUN npm ci --only=production
RUN npm run tsc
CMD ["node", "dist/app.js"]