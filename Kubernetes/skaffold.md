
A tool created by Google to facilitate development using Kubernetes.

# Setup

```
minikube start --profile custom
skaffold config set --global local-cluster true
eval $(minikube -p custom docker-env)git clone --depth 1 https://github.com/GoogleContainerTools/skaffold
```

