from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"Hello": "World!"})