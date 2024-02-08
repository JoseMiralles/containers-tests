from flask import Flask


# if __name__ == "app.app":
#     from app.app_config import config_val
# else:
#     from app_config import config_val

from app_config import config_val

with open("text_files/test_file.txt") as txt:
    file_contents = txt.read()
    print(file_contents)



app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p>{config_val} v0.1</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, ssl_context=("cert/cert.pem", "cert/key.pem"))
