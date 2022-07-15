FROM python:3.7.0-alpine3.8 as base

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev build-base
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV DB_URL=
ENV FLASK_APP=app.py

FROM base as dev
ENV FLASK_ENV=development
RUN echo "DIR:" && ls
RUN touch test.txt
RUN flask db upgrade
CMD flask run --host=0.0.0.0
# CMD ["sleep", "20000"]  # Sleep for a long time to keep container awake.
