# IoT Site

The IoT Site repository is used for implementing and testing the use of webhooks for use of publishing and distributing sensor data.

## Setup Instructions

Installation follows standard python project setups. Webhooks is implemented using [Thorn by Robinhood](https://github.com/robinhood/thorn), however the latest version on pypi is fairly out-of-date. It would be best to install Thorn first, and then the additional required packages using:

```
# install the latest version of thorn via git
pip install git+https://github.com/robinhood/thorn.git

# install the other library requirements
pip install -r requirements
```

Serving the project in production mode is avaliable but not fully implemented as it varies on the server configuration. uWSGI is setup for this project but is not required. To run the server in uWSGI use the `start_server.sh` script to load the server in production mode. The parameters in `iotsite/uwsgi.ini` and `iotsite/wsgi.py` may need to be configured properly. Running the server in debug mode should run fine without having use uWSGI. Debug mode is the default mode and should be run using regular Django development commands.

### Set Up Environment Variables

Private parameters that are not to be shared publicly are generally loaded in through envionment variables. A template of which variables to set are defined in the file `setup.env.template`. It is best to copy this template (`cp setup.env.template setup.env`) with user only permissions (`chmod 600 setup.env`) for security reasons. To use the `setup.env` parameters, run `source setup.ev` which will make the variables persist for the executing terminal only. Once the terminal has been closed, it will need to be resourced as they will be lost upon reopening.

## Running Development Mode

### Setting up the database

To run the server in development mode, the database must first be built from the defined models in Django.

```
python manage.py makemigrations
python manage.py migrate
```

Note that any changes made to the expected database structure requires the previous commands to be executed again to adapt the database to the new changes.

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


# MariaDB Setup

If MariaDB is to be used, install the required libraries using

```
sudo apt-get install libmariadbclient-dev
```
