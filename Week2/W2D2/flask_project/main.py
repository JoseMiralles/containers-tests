from flask import Flask

app = Flask(__name__) # __name__ = file name

@app.route("/")
def hello():
    return "<h1>Hello, world!</h1>"

@app.route("/jose")
def hello_jose():
    return "<h1>Hello Jose!</h1>"

@app.route("/test")
def test():
    return "test"

