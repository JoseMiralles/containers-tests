from flask import Flask, abort

from supertokens_python import init, InputAppInfo, SupertokensConfig, get_all_cors_headers
from supertokens_python.recipe import emailpassword, session, dashboard
from flask_cors import CORS 
from supertokens_python.framework.flask import Middleware
import os



# SETUP AUTH

init(
    app_info=InputAppInfo(
        app_name="api",
        api_domain="localhost",
        website_domain="localhost",
        api_base_path="/auth",
        website_base_path="/auth"
    ),
    # IDP_PORT=tcp://10.102.49.56:3567
    supertokens_config=SupertokensConfig(
        connection_uri=os.getenv("IDP_SERVICE_HOST") + ":" + os.getenv("IDP_SERVICE_PORT"),
    ),
    framework='flask',
    recipe_list=[
        session.init(), # initializes session features
        emailpassword.init(),
        dashboard.init()
    ]
)

app = Flask(__name__)
Middleware(app) # Supertokens middleware



# CORS

CORS(
    app=app,
    origins=[
        "localhost"
    ],
    supports_credentials=True,
    allow_headers=["Content-Type"] + get_all_cors_headers(),
)



@app.route('/', defaults={'u_path': ''})  
@app.route('/<path:u_path>')  
def catch_all(u_path: str):
    abort(404)


@app.route("/")
def hello_world():
    return "<p>Hello, world</p>"
