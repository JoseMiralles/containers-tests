from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
sqlPort = getenv("POSTGRES_SERVICE_PORT") if getenv("POSTGRES_SERVICE_PORT") else 1
connection_string = f'postgresql://postgres:{getenv("POSTGRES_PASSWORD")}@{getenv("POSTGRES_SERVICE_HOST")}:{sqlPort}/{getenv("POSTGRES_DB")}'
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string

db = SQLAlchemy()
migrate = Migrate()
