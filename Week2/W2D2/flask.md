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

```
from flask import Flask

app = Flask(__name__) # __name__ = file name

@app.route("/")
def hello():
    return "<h1>Hello, world!</h1>"

@app.route("/jose")
def hello_jose():
    return "<h1>Hello Jose!</h1>"

```
