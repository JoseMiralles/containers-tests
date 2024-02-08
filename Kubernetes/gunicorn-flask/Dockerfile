FROM python:3.7.3-slim

COPY requirements.txt /

RUN pip3 install --upgrade pip

RUN pip3 install -r /requirements.txt



COPY . .

EXPOSE 5000

RUN echo "V0.1"


# CMD ["gunicorn","--config", "gunicorn_config.py", "wsgi:app"]
ENTRYPOINT [ "python3" ]
CMD ["app/app.py"]