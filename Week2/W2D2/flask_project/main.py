from typing import Text, Tuple
from flask import Flask, redirect, render_template, request

app = Flask(__name__) # __name__ = file name

@app.route("/")
def hello():
    return "<h1>Hello, world!</h1>"

# Take in parameters
@app.route("/item/<int:id>")
def get_item_by_id(id: int) -> str:
    _item: str = "Item is aquired here"
    return _item

# Render Jinja template
# Loads from the /templates folder.
@app.route("/template-page")
def get_template_page() -> Text:
    return render_template(
        "index.html",
        page="my page",
        sitename="my site",
        logged_in=True
    )

@app.route("/item", methods=['POST'])
def create_item() -> Tuple[str,str]:
    arg1: str = request.args["name"]    # URL parameter
    value1: str = request.form["user_id"]   # BODY parameter
    json = request.get_json()   # JSON
    item_id = "GET ITEM ID"
    return redirect(f"/item/{item_id}")     # Redirect


# Method runs before every request
@app.before_request
def before_request_function():
    pass
    # There is also after_request, and before_first_request.


