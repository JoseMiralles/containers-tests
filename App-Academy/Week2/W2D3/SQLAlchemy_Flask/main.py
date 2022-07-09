from config import Config
from flask import Flask, abort, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Automatically infers the table name as "free_line_item"
class FreeLineItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(10, 3))
    rate = db.Column(db.Numeric(10, 3))
    description = db.Column(db.Text)

# Query data
@app.route("fee-line-item/<int:id>", method=["GET"])
def show_fee_line_item(id):
    item = FreeLineItem.query.get(id)
    if item is None:
        abort(404)
    return jsonify(item)

# Create item with session
@app.route("/fee-line-item", method=["POST"])
def create_fee_line_item():
    item = FreeLineItem(**request.form)
    db.session.add(item)
    db.session.commit()
    return jsonify(item)

@app.route("/fee-line-item", method=["PUT"])
def update_fee_line_item():
    item = FreeLineItem.query.get(id)
    for key, value in request.form:
        setattr(item, key, value)
    db.session.commit()
    return jsonify(item)

@app.route("/fee-line-item", method=["DELETE"])
def delete_fee_line_item():
    item = FreeLineItem.query.get(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify(item)


