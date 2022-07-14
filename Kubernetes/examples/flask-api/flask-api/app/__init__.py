from app.models import Owner, db
from flask import Flask, jsonify
from flask_migrate import Migrate
import os

_DATABASE_URL = os.environ.get("DB_URL").replace(" ", "")

app = Flask(__name__)
app.config.from_mapping({
    "SQLALCHEMY_DATABASE_URI": _DATABASE_URL,
    "SQLALCHEMY_TRACK_MODIFICATIONS": False
})

db.init_app(app)
Migrate(app, db)

@app.route('/')
def index():
    if _DATABASE_URL:
        return _DATABASE_URL
    return "Val was null"

@app.route("/owners")
def get_owners():
    return Owner.query.all()
