# Kubernetes

It's main features are **high availability**, **scalability**, and **disaster recovery**.

# PODs

The smallest logical units in k8s. They are an abstraction over containers. Pods usually have 1 application/service per pod. Multiple pods can run in a single node.

Each pod get's its own IP address in the virtual network. But because pods are meant to be replaced, a virtual 'service IP' is given to each service and it applies to all of it's pods.

## Ingres

A feature of k8s that receives requests and routes the to the correct service. It makes it possible to use a custom url.

## ConfigMap

An external config for the application. Things like cutom urls can be configured here. Do not use for secrets. Can be used as env variables.

## Secret

Similar to config map, but it stores data encrypted in base64 format. Used for things like passwords and certificates.

<br>

# Volumes

When a db pod goes down, the data shouldn't be lost. Volumes allow engineers to delegate storage of a pod to a separate local or remote drive. K8s does not manage data backup, admins and engineers are responsible for this.

# Deployments and Sateful Sets

The service gives us a permanent ip address and it also serves as a load balancer.

Instead of working with containers or pods directly, we work with **deployments**.

**Stateful Sets** are used to scale stateful pods such as databases. These can be tedious to manage, so it is common to use solutions outside of k8s for data hosting.
