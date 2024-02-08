
# Non container run:

`. .venv/bin/activate`

# As kubernetes cluster:

`minikube start -p custom`

`skaffold dev`

On a new terminal: `minikube tunnel -p custom`

On another terminal: `minikube dashboard -p custom`
