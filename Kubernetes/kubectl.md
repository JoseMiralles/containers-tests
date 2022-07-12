# Commands

- `kubectl get nodes` Show all nodes and their status.
- `kubectl get pods`
- `kubectl get services`
- `kubectl get all` Show all resources.
- `kubectl logs <PODNAME>` get logs for pod.
    - To get pod names: `kubectl get pods`
- `Kubectl describe pod <PODNAME >` Shows info about the pod.
- `kubectl exec -it <PODNAME> -- <COMMAND>` execute command on pod.
    - Ex: `kubectl exec -it nginx-deployment-85c6d5f6dd-x4zr6 -- bin/bash`
        - This starts lets you access the terminal on that pod.
        - Use `exit` to close session.
- `kubectl delete <resource>/<name>` deletes resource
    - Ex: `kubectl delete deployment/nginx-deployment`

# Deployments and pods

One does not work with pods directly. Instead, one works with deployments.

Format:
```
kubectl create deployment NAME --image=image [--dry-run] [options]
```

# Creating nginx deployment example with CLI:

1. `kubectl create deployment nginx-depl --image=nginx`
    - `kubectl get deployment` should show this deployment now
    - `kubectl get pod` should show this new pod as well
2. `kubectl logs <PODNAME>` should show the logs.
    - Use `kubectl get pod` to get the name of the pods.

# Creating deployments using config file:

This is done using `kubectl apply -f <FILE_PATH>`. The file name is usually `config-file.yaml`.

## Modifying deployment

After editing a deployment yml file, run `kubectl apply -f <FILE_PATH>` again to apply the changes.


# Examples config files:

<br>

## - [Nginx deployment](examples/nginx-deployment.yaml)
A simple deployment of an nginx server.

<br>

## - [MongoDB and Mongo-Express Dashboard](examples/MongoDB-MongoExpress/deployment.yml) with credentials

A MongoDB pod with a Mongo-Express dashboard that uses an external service to receive requests. It also shows how to add env variables.

### 1. Create Secrets.yml

1. Create [`mongo-secret.yml`](examples/MongoDB-MongoExpress/mongo-secret.yaml). This file should contain the secret variables encoded in base64.
    - Run `echo -n "username" | base64` to encode a value and then paste it in the secret yaml file.
2. Run `kubectl apply -f mongo-secret.yaml`
    - `kubectl get secret` should display the secret.

These secrets can now be referenced in the deployment yaml file.

### 2. Create [mongodb-deployment.yml](examples/MongoDB-MongoExpress/mongodb-deployment.yml)

- Fill out and include the secrets.
- Run `kubectl apply -f mongodb-deployment.yml`

At the bottom, you can see the definition of the service which exposes a port to the internal network to connect to.

### 3. Create [configmap.yml](examples/MongoDB-MongoExpress/configmap.yml)

This contains non-secret env variables.

1. Fill out file
2. Run `kubectl apply -f configmap.yml` to add this config map to K8s. 
3. Run `kubectl get configmaps` to view map

### 4. Create [mongoexpress-deployment.yml](examples/MongoDB-MongoExpress/mongoexpress-deployment.yml)

1. Fill out file.
    - Notice how it references configmap.yml
2. Run `kubectl apply -f mongoexpress-deployment.yml`
3. Run `kubectl logs <PODNAME>` to see the logs and make sure that it started.
4. Run `kubectl get service` to see created service.
5. Run `minikube service mongo-express-service` to expose the service and to launch the application in the browser.

<br>

### Requests flow:

External Client -> Mongo Express **external** service -> Mongo Express pod -> MongoDB **internal** service -> MongoDB
