# Using minikube enviroment

1. Install minikube
2. `minikube start`
3. `minikube dashboard` To open the dashboard. Press ctrr + c to exit, dashboard will still be running.
4. Create deployment: `kubectl create deployment hello-node --image=k8s.gcr.io/echoserver:1.4`
    - View deployments: `kubectl get deployments` These can also be seen from the dashboard.
    - View nodes: `kubectl get pods`
    - View events: `kubectl get events`
    - View config: `kubectl config view`
5. Create service: `kubectl expose deployment hello-node --type=LoadBalancer --port=8080`
    - This exposes the pod to the public.
    - The `--type=LoadBalancer` flag indicates that this service should be exposed outside the network.
    - `kubectl get services` To view service.
6. Use `minkube service` to make `LoadBalancer` type services accessible.

## Addons

- `minikube addons list` To view supported addons.
- Enable addon example: `minikube addons enable metrics-server`
    - View new pod and service: `kubectl get pod,svc -n kube-system`
- Disable addon: `minikube addons disable metrics-server`

## Clean up

1. Delete service and deployment for hello-node:
    - `1kubectl delete service hello-node`
    - `kubectl delete deployment hello-node1`
2. Stop minikube `minikube stop`
3. To delete minikube VM: `minikube delete`

# Steps to deployment

1. Create cluster.
2. Create a deployment. The Deployment instructs Kubernetes how to create and update instances of the application. If a node goes down or is deleted, the deployment controller replaces the instance with another EXISTING node in the cluster.
3. 

# Commands

- `kubectl version`: View version.
- `kubectl cluster-info`: View info about the cluster.
- `kubectl get nodes`: Shows all of the nodes.
