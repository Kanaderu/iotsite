# IoT Site

The IoT Site repository is used for implementing and testing the use of webhooks for use of publishing and distributing sensor data.

## Quick Start

Commands to get the server quickly up and running locally.

```
git clone git@github.com:Kanaderu/iotsite.git       # clone the repo

# setup python
cd iotsite/                                         # change directory into repo
pip install -r requirements                         # install python libraries

# setup react
cd dashboard/                                       # change into frontend react repo
yarn                                                # install node libraries
yarn build                                          # build the react/javascript frontend

# install postgres database
sudo apt install postgresql postgresql-contrib

# refer to https://postgis.net/install/ to install postgis for other distributions
sudo apt-get install python-software-properties
sudo add-apt-repository ppa:ubuntugis/ppa
sudo apt-get update
sudo apt install postgis

# install geospatial libraries
sudo apt install binutils libproj-dev gdal-bin

# setup postgres with user 'geo' with password 'geo' and database 'geodjango'
sudo -u postgres psql -c "CREATE USER geo WITH ENCRYPTED PASSWORD 'geo';"
sudo -u postgres psql -c "CREATE DATABASE geodjango with OWNER geo;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE geodjango TO geo;"
sudo -u postgres psql -d geodjango -c "CREATE EXTENSION postgis;"

# build database
cd ../
python manage.py makemigrations                     # prepare database commands and check Django ORM
python manage.py migrate                            # build and commit database tables

# run server
python manage.py runserver                          # run the server locally
```

## Setup Instructions

Installation follows standard python project setups. Webhooks is implemented using [Thorn by Robinhood](https://github.com/robinhood/thorn).

```
# install python dependencies
pip install -r requirements.txt

cd dashboard/

# install node dependencies
yarn
```

Serving the project in production mode is avaliable but not fully implemented as it varies on the server configuration. uWSGI is setup for this project but is not required. To run the server in uWSGI use the `start_server.sh` script to load the server in production mode. The parameters in `iotsite/uwsgi.ini` and `iotsite/wsgi.py` may need to be configured properly. Running the server in debug mode should run fine without having use uWSGI. Debug mode is the default mode and should be run using regular Django development commands.

### Setup Environment Variables

Private parameters that are not to be shared publicly are generally loaded in through envionment variables. A template of which variables to set are defined in the file `setup.env.template`. It is best to copy this template (`cp setup.env.template setup.env`) with user only permissions (`chmod 600 setup.env`) for security reasons. To use the `setup.env` parameters, run `source setup.ev` which will make the variables persist for the executing terminal only. Once the terminal has been closed, it will need to be resourced as they will be lost upon reopening.

### Building Frontend React

React is used to build the frontend dashboard. Using React and Django involves the integration of two separate web development frameworks. Integration is being peformed with the used of webpack and node/yarn. The react app is stored into the `dashboard` folder. To build the `dashboard` app, `npm` and/or `yarn` needs to be installed. Run the following commands to build the `dashboard` react project.

```
cd dashboard/
yarn            # install node_modules/ packages
yarn build      # build the production setup
```

Inplace of `yarn`, `npm` can be used instead using the following commands.

```
cd dashboard/
npm install     # install node_modules/ packages
npm run build   # build the production setup
```

## Running Development Mode

### Setting up the database

To run the server in development mode, the database must first be built from the defined models in Django.

```
python manage.py makemigrations
python manage.py migrate
```

Note that any changes made to the expected database structure requires the previous commands to be executed again to adapt the database to the new changes.

### Running the frontend with hot-reloading (for development mode)

To run the frontend react with hot-reloading, run the following commands.

```
cd dashboard/
yarn start      # start the react frontend with hotreloading
```

Inplace of `yarn`, `npm` can be used instead using the following commands.

```
cd dashboard/
npm run start      # start the react frontend with hotreloading
```

### Running the server in development mode

To run the server in development mode, the database must first be built from the defined models in Django.
Once the database has been built, the server can be executed in development mode using the following command:

```
python manage.py runserver
```

Node that any changes made to django will invoke the server to be refreshed to encompass the new changes.

### Adding Users

Currently `superuser`s can be added by using the command:

```
python manage.py createsuperuser
```

Basic users have not been impemented yet.

## TODOs:

- [ ] Add documentation for running in Production Mode
- [ ] User authentication
- [ ] Basic user backend setup/configuration
- [ ] Override rest\_framework template
- [ ] Validate sensor model logic
- [ ] Add default landing page (React?)
