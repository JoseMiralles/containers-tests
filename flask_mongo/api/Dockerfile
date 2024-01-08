FROM python:3.10.5-alpine3.16 as base

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev build-base
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV DB_URL=test
ENV FLASK_APP=app.py

EXPOSE 5000

FROM base as dev
ENV FLASK_ENV=development
RUN echo "DIR:" && ls
RUN touch test.txt
CMD flask run --host=0.0.0.0
# CMD ["sleep", "20000"]  # Sleep for a long time to keep container awake.
