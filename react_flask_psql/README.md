# TODO app made with Flask and React.

# Start app:
src: https://skaffold.dev/docs/quickstart/

1. `minikube start --profile custom`
2. `skaffold config set --global local-cluster true`
3. `eval $(minikube -p custom docker-env)`
4. On the project directory: `skaffold dev`
5. Open another terminal: `minikube tunnel -p custom`

- Flask API: `http://localhost:6000`

<br>

# Creating and applying migrations

This step is better performed using venv.
1. `cd backend`
2. `source bin/activate`

Creating and seeding db
1. Create migraitons foler and db: `flask db init`
2. Create migraiton: `flask db migrate -m "migration description"`
3. Apply migrations to db: `flask db upgrade`

- Guide: https://flask-migrate.readthedocs.io/en/latest/
- Apply/upgrade the migration from a pod.
