from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
connection_string = f'postgresql://postgres:{getenv("POSTGRES_PASSWORD")}@{getenv("POSTGRES_SERVICE_HOST")}:{getenv("POSTGRES_SERVICE_PORT")}/{getenv("POSTGRES_DB")}'
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.cli.command()
def seed():
    from app.seed import start_seed
    start_seed(db)