from flask import Flask

app = Flask(__name__) # __name__ = file name

@app.route("/")
def hello():
    return "<h1>Hello, world!</h1>"

# Take in parameters
@app.route("/item/<int:id>")
def get_item_by_id(id: int) -> str:
    _item: str = "Item is aquired here"
    return _item

# Method runs before every request
@app.before_request
def before_request_function():
    pass
    # There is also after_request, and before_first_request.


