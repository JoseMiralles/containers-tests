# Images

A collection of app binaries and dependencies.

## Image Commands

- `sudo docker image ls` Lists all images
- `sudo docker image tag <image> <user>/<image>` Tags an image
- `sudo docker inspect <image>` Shows metadata for image
- `sudo docker image history <image>` Shows a list of changes
- `sudo docker image rm <image>` Remove image

<br>

- `sudo docker image push <account>/<image>` Pushed image to docker hub
- `sudo docker build . -t <account>/<image>` Creates an image using the current directory's Dockerfile. It also assigns it a name.

# Example, create Docker Image:

1. Create a folder, and cd into it.
2. Create `app.py`

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def serve():
    return "<h1>Hi!!!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
```
3. Create `requirements.txt`
```
flask
```
4. 