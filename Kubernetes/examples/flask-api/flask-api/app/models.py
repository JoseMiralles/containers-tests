from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
app = Flask(__name__)
ma = Marshmallow(app)


class Pony(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(20), nullable=False)
    owners_id = db.Column(db.Integer, db.ForeignKey("owners.id"), nullable=False)

class PonySchema(ma.SQLAlchemySchema): 
    class Meta:
        model = Pony
    id = ma.auto_field()
    color = ma.auto_field()
    owners_id = ma.auto_field()


class Owner(db.Model):
    __tablename__ = "owners"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), nullable=False)

    ponies = db.relationship("Pony", backref="owners", lazy=True)

class OwnerSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Owner
    id = ma.auto_field()
    first_name = ma.auto_field()
    last_name = ma.auto_field()
    email = ma.auto_field()


class schemas:
    owner = OwnerSchema()
    owners = OwnerSchema(many=True)
    pony = PonySchema()
    ponies = PonySchema(many=True)