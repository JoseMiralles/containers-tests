FROM python:3.7.0-alpine3.8 as base

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP=app.py

FROM base as dev
ENV FLASK_ENV=development
CMD flask run --host=0.0.0.0

