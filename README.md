# python-docker-app
Python application running within a Docker container.

## Docker image
-  Image Name: python-docker-app

## Docker Hub Image Link
You can find the Docker image on Docker Hub at the following link:
https://hub.docker.com/r/nestallum/python-docker-app

## Docker App run command
To run this Python application in a browser, you can use the following commands:

- **Running the application via Docker image by starting the container :**
    ```bash
    docker run -p 4000:8080 -t python-docker-app
    ```
    Click [here](https://github.com/Nestallum/docker-python-app/blob/main/screenshots/docker_image.png) to view the execution of the application using Docker image.

- **Running the application via a service adress :**
    ```bash
    minikube service myservice --url
    ```
    Click [here](https://github.com/Nestallum/docker-python-app/blob/main/screenshots/service.png) to view the execution of the application using the service.

- **Running the application via Ingress :**
    ```bash
    minikube addons enable ingress-dns
    minikube tunnel
    ```
    Click [here](https://github.com/Nestallum/docker-python-app/blob/main/screenshots/ingress.png) to view the execution of the application using Ingress.

