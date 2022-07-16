from app.models import Owner, Pony, db, app, schemas
from flask import Flask, jsonify, request
from flask_migrate import Migrate
import os

_DATABASE_URL = os.environ.get("DB_URL").replace(" ", "")
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

@app.route("/owners", methods=["GET"])
def get_owners():
    return jsonify(schemas.owners.dump(Owner.query.all()))

@app.route("/owners", methods=["POST"])
def add_owner():
    new_owner = Owner(
        first_name=request.form["first_name"],
        last_name=request.form["last_name"],
        email=request.form["email"]
    )
    db.session.add(new_owner)
    db.session.commit()
    return jsonify(schemas.owner.dump(new_owner))

@app.route("/owners/<int:owner_id>/ponies", methods=["GET"])
def get_owner_ponies(owner_id):
    ponies = Owner.query.filter_by(id=owner_id).join(Pony).all()
    return(jsonify(schemas.ponies.dump(ponies)))

@app.route("/ponies", methods=["POST"])
def add_pony():
    new_pony = Pony(
        color=request.form["color"],
        owners_id=request.form["owners_id"]
    )
    db.session.add(new_pony)
    db.session.commit()
    return jsonify(schemas.pony.dump(new_pony))

