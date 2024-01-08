# Create New Microservice

Follow these steps: https://skaffold.dev/docs/quickstart/

- Remember to add `type: LoadBalancer` to services that need to be accessed externally.
- Run `minikube tunnel -p custom` to expose services.

# Access Dev Services

Mongo express: http://127.0.0.1:8081/
API: http://127.0.0.1:5000/
IDP: http://127.0.0.1:3567/
