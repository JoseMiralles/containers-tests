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


```
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

```
