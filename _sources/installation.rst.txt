Installation
============

Installation can be performed either using two methods. The two methods are as follows:

- `Docker Installation`_
- `Manual Setup`_

The docker instance allows a user to get setup quickly on a new machine. The docker instance currently sets up the project in development mode. The manual setup is a bit more involved but allows for a more traditional development setup.

Cloning the Repository
----------------------

Before starting the installation process, the user needs to first obtain the code. The code lives on GitHub and can be obtained `here <https://github.com/Kanaderu/iotsite>`_. The repository can be downloaded using `git` or by download directly from the `GitHub Project Page <https://github.com/Kanaderu/iotsite/archive/master.zip>`_.

.. code-block:: bash

   git clone https://github.com/Kanaderu/iotsite.git

Docker Installation
-------------------

The Docker instance is described primarily by two main files, **Dockerfile** and **docker-compose.yml**. The **Dockerfile** file contains directives on how to compile a docker image for the current project. The **docker-compose.yml** file contains directives on how to orchestrate multiple docker images and how they interact with each other. The **docker-compose.yml** file pulls an image from `Docker-Hub <https://hub.docker.com/>`_, an repository of Docker images, to instantiate a PostgreSQL database with PostGIS extensions for Geo support. The docker image will download all the required dependencies within its image.

To get the project setup with Docker, navigate to the location of the **docker-compose.yml** and run the following command. General Docker information can be found at the `Docker's documentation <https://docs.docker.com/>`_.

.. code-block:: bash

   docker-compose up

Note that the docker container may take a significant amount of time to initially setup the required dependencies and services. Once the docker containers are up and running, it can be viewed locally at `<http://localhost:8080>`_. To change the default port, modify the ports in the **docker-compose.yml** file.

Manual Setup
------------

The manual setup is a bit more involved requiring the developer to setup the dependencies for their system. This setup will document how to setup the project on an Ubuntu/Debian based machine. Dependencies and requirements may slightly differ from different flavors of Linux but the packages should not be dependent to a specific flavor of Linux.

A quick overview of the manual setup is below followed by details for each specific step.

.. code-block:: bash
   :linenos:

   # install postgis support
   # refer to https://postgis.net/install/ to install postgis for other distributions
   sudo apt-get install python-software-properties
   sudo add-apt-repository ppa:ubuntugis/ppa
   sudo apt-get update

   # install postgres database
   sudo apt-get install postgresql postgresql-contrib libpq-dev

   # install geospatial libraries
   sudo apt-get install binutils libproj-dev gdal-bin postgis

   # setup postgres with user 'geo' with password 'geo' and database 'geodjango'
   sudo -u postgres psql -f utils/database/dev.sql

   # setup python
   pip install -r requirements                         # install python libraries

   # build database
   python manage.py makemigrations                     # prepare database commands and check Django ORM
   python manage.py migrate                            # build and commit database tables

   # build react frontend
   python manage.py install_frontend_dependencies
   python manage.py build_frontend

   # run server
   python manage.py runserver                          # run the server locally

Prerequisites and Dependencies
******************************

The main development libraries are as follows:

.. code-block:: md

   Python >= 3.5
   PostgreSQL with PostGIS extensions
   Node and NPM

To setup an python environment, it is recommended to either use `virtualenv <https://virtualenv.pypa.io/en/latest/>`_ or `Anaconda <https://www.anaconda.com/distribution/>`_. The python environment will separate the development environment for this project from other python projects on your system. PostGIS and PostgreSQL are left to be installed which will vary based on the system the user is running. Refer to `PostGIS <https://postgis.net/>`_ to determine how to install PostGIS capabilities for other operating systems. After python has been installed, download the additional required programs by running the following commands:


.. code-block:: bash
   :linenos:

   # install ppa for postgis
   sudo apt-get install python-software-properties
   sudo add-apt-repository ppa:ubuntugis/ppa
   sudo apt-get update

   # install postgres
   sudo apt-get install postgresql postgresql-contrib libpq-dev

   # install geospatial libraries
   sudo apt-get install binutils libproj-dev gdal-bin postgis

Once the appropriate libraries have been installed, the python dependencies can be added. It's recommended to first create a virtual environment as mentioned before. Install the python packages by running the following on the `requirements.txt` file:

.. code-block:: bash

   pip install -r requirements.txt

The frontend is built with javascript and `React <https://reactjs.org/>`_. Installation of node may vary from platform to platform so viewing the documentation and installation instructions specific to the target platform. Node and npm/yarn can be downloaded from the `Node website <https://nodejs.org/en/download/>`_ (the latest LTS is being used for stability).

Once node and npm/yarn have been setup, the frontend dependencies can be installed. Navigate to the frontend in *dashboard/* where **package.json** is located. **package.json** defines the frontend project. Run the following commands to download the dependencies:

.. code-block:: bash

   yarn

Alternatively, a Django management command is written in the *setup* app which does the same thing. To invoke this alternative, run the following:

.. code-block:: bash

   python manage.py install_frontend_dependencies

Setting up the Database
***********************

The database first needs to be created before it can be populated. The first step involves building the database with a username and password. After a user has been created, a database is created specifically for the project and PostGIS extensions are enabled for the database.

Once the database has been setup properly, Django can begin populating the database with its appropriate ORM tables.

Building the Database
#####################

The database at this point is currently empty. To begin populating and setting up the database, a user will be created and a database table will be created with PostGIS extensions enabled. For convenience, a `.sql` script is available to create the user and database. To run the script run the following:

.. code-block:: bash

   sudo -u postgres psql -f utils/database/dev.sql

The script can be examined. In summary, it will:

- Create a user named **geo** with password **geo**
- Create a database **geodjango**
- Enable PostGIS extensions for the **geodjango** database

The database and user information is used for the project installation located in the project's settings file (*iotsite/settings/dev.py*). A separate settings file (*iotsite/settings/production.py*) is used for a production environment and is highly recommended to change the default username/password/database for security reasons.

Populating the Database
#######################

Populating the database, once it's been created can be done using Django's *./manage.py* script. Populate the database by running the following commands:

.. code-block:: bash

   python manage.py makemigrations
   python manage.py migrate

Note that these two steps are required every time the Django ORM model has been modified. Specifically, the *makemigrations* directive specifies how the current instance of the database will be altered and *migrate* with commit those changes to the database. If code changes are not made to any ORM models (any *models.py* changes), then migrations to the database do not need to be made. Refer to the `Django documentation <https://docs.djangoproject.com/>`_ for additional details.

Running the Backend
*******************

Once the database has been built, the backend can be launched. To run the backend server, run the following command:

.. code-block:: bash

   python manage.py runserver 8080       # optional port 8080 is specified, otherwise defaults to 8000


Building the Frontend
*********************

At this point, viewing the website at http://localhost:8080 does not show the frontend. This is particularly due to the frontend hasn't been built. To build the frontend, navigate to the `dashboard/` app and run the following commands to build the frontend:

.. code-block:: bash

   yarn build


Alternatively, a Django management command is written in the *setup* app which does the same thing. To invoke this alternative, run the following:

.. code-block:: bash

   python manage.py build_frontend

Once the frontend has been built, the backend is setup to automatically setup the routes to render it. The page at http://localhost:8080 from before should now render the project.
