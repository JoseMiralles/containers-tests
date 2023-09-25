from app.models.users_model import User
from app.models.items_model import Item
from app.config import app

@app.route("/")
def hello_world():
    from app.config import connection_string
    return connection_string
