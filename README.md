
# DevOps-Python

This is a DevOps pipeline for a web app displaying Todos list. The purpose of this project is to demonstrate how to create a DevOps pipeline using GitHub Actions.

*	Web app is developed using python and flask 
* Displays Todos list with update (completed or not completed) and delete options 
*	Cloud deployment 
​
## Dependencies

+ Flask
+ html
+ css
+ python
+ GitHub
+ Docker
+ Kubernetes (minikube and kubectl)

## Installation

To install the required software packages to run the web app, use the following command.
* pip3 install -r req.txt

## Usage

Clone the repository:
	git clone https://github.com/RaghuKA/devops-python.git

Open the page http://127.0.0.1:5000/edit. In this page the tasks can be added or updated or deleted.
<p align="center">
  <img src="EditPage.png">
</p>

Open the page http://127.0.0.1:5000/. In this page the added tasks are displayed as a list.
<p align="center">
  <img src="ListPage.png">
</p>

## DevOps workflow

The work flow "Docker push" automatically pushes the new releases to the docker container rkumdocker/devopspython.

## Kubernetes container management

Using the following commands the Docker containers can be managed in Kubernetes.

To create pod
* kubectl create -f pod.yaml


To get pods
* kubectl get pods


To create replicas for high availability, load balancing and self healing of application
* kubectl create -f replica.yaml


To rollout to the new release
* kubectl create -f deployment.yaml