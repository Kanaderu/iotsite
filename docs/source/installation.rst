Installation
============

Installation can be performed either using two methods. The two methods are as follows:

- `Docker Installation`_
- `Manual Setup`_

The docker instance allows a user to get setup quickly on a new machine. The docker instance currently sets up the project in development mode.
The manual setup is a bit more involved but allows for a more traditional development setup.

Cloning the Repository
----------------------

Before starting the installation process, the user needs to first obtain the code. The code lives on GitHub and can be obtained `here <https://github.com/Kanaderu/iotsite>`_.

Docker Installation
-------------------

The Docker instance is described primarily by two main files, **Dockerfile** and **docker-compose.yml**.
The **Dockerfile** file contains directives on how to compile a docker image for the current project.
The **docker-compose.yml** file contains directives on how to orchestrate multiple docker images and how they interact with each other.
The **docker-compose.yml** file pulls an image from `Docker-Hub <https://hub.docker.com/>`_, an repository of Docker images,
to instantiate a PostgreSQL database with PostGIS extensions for Geo support. The docker image will download all the required dependencies within its image.

To get the project setup with Docker, navigate to the location of the **docker-compose.yml** and run the following command.
General Docker information can be found at the `Docker's documentation <https://docs.docker.com/>`_.

.. code-block:: bash
   :linenos:

   docker-compose up

Note that the docker container may take a significant amount of time to initially setup the required dependencies and services.
Once the docker containers are up and running, it can be viewed locally at `<http://localhost:8080>`_. To change the default port, modify the ports in the **docker-compose.yml** file.

Manual Setup
------------
