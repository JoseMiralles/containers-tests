from app.config import app, db, migrate
from app.auth import authorize

db.init_app(app)
migrate.init_app(app, db)


@app.cli.command()
def seed():
    from app.seed import start_seed
    start_seed(db)

@authorize("admin")
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/connection_string")
def get_connection_string():
    from app.config import connection_string
    return connection_string
