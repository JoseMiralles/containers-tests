FROM node:10-alpine

WORKDIR /app
COPY . /app
RUN npm install
CMD ["mysql", "sshd", "npm start"]