FROM python:3.10-alpine

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

EXPOSE 5000
ENV FLASK_APP=app
ENV FLASK_ENV=development
CMD ["python", "/app/app.py"]