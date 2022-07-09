# Setup

1. Create project folder, and cd into it.
1. `pipenv install flask`
1. create `main.py` as specified below.
1. Set the FLASK_APP enviroment variable `export FLASK_APP=main.py`
1. For development, set `export FLASK_ENV=development`
1. Run Flask `pipenv run flask run`
    - Set Port: add the p flag `-p 5001`

This will start the server.

## Using `.flaskenv` to handle enviroment variables

1. Install dotenv `pipenv install python-dotenv~=0.13`
1. Create `.flaskenv` in the project directory.

```
FLASK_APP=main.py
FLASK_ENV=development
```

## Using `app.config` to configure the app

```
...
app = Flask(__name__)
app.config["greeting"] = "Hey there, humans!"

@app.route("/")
def hello():
    return f"<h1>{app.config["greeting"]}</h1>"
```

A class can be created to define values for app.configure instead.

```
class Config(object):
    GREETING = "SAlutations, superior students!"

app.config.from_object(Config)
```

<br>

# Example Flask app

```
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
    value1: str = request.form["user_id"]  # BODY parameter
    json = request.get_json()   # JSON
    item_id = "GET ITEM ID"
    return redirect(f"/item/{item_id}") # Redirect


# Method runs before every request
@app.before_request
def before_request_function():
    pass
    # There is also after_request, and before_first_request.
```

<br>

# Serving static assets
Flask has a built in special route `/static`. It servers content from the static folder in the root directory of the project.

Ex: `http://localhost:5000/static/styles/main.css`

<br>

# Forms

You can create forms with Flask, Jinja and Flask-WTF.

<br>

# Routing Blueprints

You can separate the login into different files.

## 1. Create the blueprint in the `routes/` folder

`routes/admin.py`
```
from flask import Blueprint

bp = Blueprint("admin", __name__, url_prefix="/admin")

# Handles /admin/dashboard GET and POST requests.
@bp.route("/dashboard", methods=("GET", "POST"))
def admin_dashboard():
    pass
```

## 2. Register the blueprint in the main file

`main.py`
```
import routes

app = Flask()

app.register_blueprint(routes.admin.bp)
```

<br>

# Sessions

1. Add a `SECRET_KEY` to .flaskenv
    - Can use this site to generate it: https://randomkeygen.com/
1. Import and use the `session` dictionary

```
from flask import Flask, session
...
@app.route("/visits-counter/")
def visits():
    if "visits" in session:
        session["visits"] = session.get("visists") + 1
    else:
        session["visits"] = 1
    
    return f"Total visits: {session.get("visits")}"
```
