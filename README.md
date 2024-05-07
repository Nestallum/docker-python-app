# python-docker-app
Python application running within a Docker container.

## Docker image
-  Image Name: python-docker-app

## Docker Hub Image Link
You can find the Docker image on Docker Hub at the following link:
https://hub.docker.com/r/nestallum/python-docker-app

## Docker run command
To run the Docker container with this Python application, you can use the following command:
     
     docker run -p 4000:8080 -t python-docker-app
     

- Exécution du code via l'image docker :
-      docker run -p 4000:8080 -t python-docker-app
https://github.com/Nestallum/docker-python-app/blob/main/screenshots/docker_image.png

- Exécution du code via un service :
-     minikube service myservice --url
https://github.com/Nestallum/docker-python-app/blob/main/screenshots/service.png

- Exécution du code via ingress :
-     minikube addons enable ingress-dns
-     minikube tunnel 
https://github.com/Nestallum/docker-python-app/blob/main/screenshots/ingress.png


