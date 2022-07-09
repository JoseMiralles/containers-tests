# Base

FROM node:12-alpine as base
EXPOSE 8081
ENV NODE_ENV=production
WORKDIR /app
# Copy package.json and package-lock.json
COPY package*.json ./
RUN npm ci && npm cache clean --force
# Add node_modules/.nin to path to be able to execute node commands without path.
ENV PATH=/app/node_modules/.bin:$PATH

# Development

FROM base as dev
ENV NODE_ENV=development
WORKDIR /app
RUN npm install --only=development
RUN ls
CMD ["nodemon", "./app.js"]

# Production

FROM base as prod
WORKDIR /app
COPY . .
CMD ["node", "./app.js"]
