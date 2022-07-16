# 1. Create and start skaffold project

Start minikube if its not running.

1. Create `flask-api/deployment.yml`
2. Run `skaffold init`
3. Populate `Skaffold.yaml`
4. Run `skaffold dev`
5. Run `kubectl get service` and check that a service named `flask-api`, of type `LoadBalancer` exists.
6. Run `minikube service flask-api` to expose the service and open it on the browser.

## Cretate migrations

Might be better to `skaffold run` instead of `skaffold dev` for this process.

1. Add a model to `flask-api/app/models`.
2. Run cli in pod with `kubectl exec -it <container-name> -- /bin/sh` or using vscode.
3. Create migration `flask db migrate -m "create owners table`
4. In a new terminal copy folder from pod to local file system: `kubectl cp <podname>:/usr/src/app/migrations ./migrations-new`
5. If migration seems correct, remove the existing migrations folder and rename `migrations-new` to `migrations`
6. Apply migration by running `flask db upgrade` from a flask pod.

### Using psql on a postgres:alpine pod

1. Get a pod name using `kubectl get pod`
2. Start terminal on pod `kubectl exec -it <pod-name> /bin/sh`
3. Start psql `psql -U <postgres user> <database name>`

<br>

# 2. Add the app logic

1. Create the models, and migrate.
2. Create the marshmellow schemas
3. Create the api endpoints