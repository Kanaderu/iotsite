# IoT Site

The IoT Site repository is used for implementing and testing the use of webhooks for use of publishing and distributing sensor data.

## Repository Setup

Docker can be setup manually or using docker. A docker installation would be the easiest method to get up and running quickly.

### Docker Setup

A `Dockerfile` is written to setup the project and mount the volumes to the container. As a result, any changes reflected on the any of the files will be seen by the container. The `docker-compose.yml` sets up two services, one for the current project as described by the project's `Dockerfile` and another from the Docker-Hub that pulls a postgres database setup with postgis enabled. All database files from the are also mounted as a volume for easy database management purposes. The database files are stored in a folder at `./volumes/db/var/lib/postgres_data` in the project folder. Note that permissions may need to be changed in order to view them with either `chmod` or `chown` (or user added to the proper groups).

To launch docker, navigate to the `docker-compose.yml` file (located in the project root folder) and execute the following code. Note that the first time running the command will take quite a while to set everything up.

```bash
# start up docker container and setup/install all requirements
docker-compose up      # run docker in daemon mode with -d

# close down the docker container, data is persisted
docker-compose down
```

#### Docker Settings

Docker pulls the from the user's environment variables the following: `DARKSKY_KEY` and `SECRET_KEY` to setup the local installation. Additional parameters can be modified in the `docker-compose.yml` file such as the default port and database configurations.

The docker setup can be accessed at http://localhost:8080/

### Manual Setup

Commands to get the server quickly up and running locally.

```
git clone git@github.com:Kanaderu/iotsite.git       # clone the repo

# setup python
cd iotsite/                                         # change directory into repo
pip install -r requirements                         # install python libraries

# install postgres database
sudo apt install postgresql postgresql-contrib libpq-dev

# install postgis support
# refer to https://postgis.net/install/ to install postgis for other distributions
sudo apt-get install python-software-properties
sudo add-apt-repository ppa:ubuntugis/ppa
sudo apt-get update
sudo apt install postgis

# install geospatial libraries
sudo apt install binutils libproj-dev gdal-bin

# setup postgres with user 'geo' with password 'geo' and database 'geodjango'
sudo -u postgres psql -f utils/database/dev.sql

# build database
cd ../
python manage.py makemigrations                     # prepare database commands and check Django ORM
python manage.py migrate                            # build and commit database tables

# build react frontend
python manage.py install_frontend_dependencies
python manage.py build_frontend

# run server
python manage.py runserver                          # run the server locally
```

#### Manual Setup In-Depth Details

Installation follows standard python project setups. Webhooks is implemented using [Thorn by Robinhood](https://github.com/robinhood/thorn).


##### Building the Backend

```
# install python dependencies
pip install -r requirements.txt
```

###### Production Setup

Serving the project in production mode is avaliable but not fully implemented as it varies on the server configuration. ASGI is setup for this project but is not required. The ASGI entrypoint can be found in `iotsite/asgi.py` (Prior setup previously used `iotsite/uwsgi.ini` and `iotsite/wsgi.py` which may still work with some features disabled as uWSGI does not support some features provided by ASGI). Running the server in debug mode should run fine without having use ASGI. Debug mode is the default mode and should be run using regular Django development commands.

#### Setup Environment Variables

Private parameters that are not to be shared publicly are generally loaded in through envionment variables. A template of which variables to set are defined in the file `utils/setup.env.template`. It is best to copy this template (`cp setup.env.template setup.env`) with user only permissions (`chmod 600 setup.env`) for security reasons. To use the `setup.env` parameters, run `source setup.ev` which will make the variables persist for the executing terminal only. Once the terminal has been closed, it will need to be resourced as they will be lost upon reopening.

#### Building the Frontend

React is used to build the frontend dashboard. Using React and Django involves the integration of two separate web development frameworks. Integration is being peformed with the used of webpack and node/yarn. The react app is stored into the `dashboard` folder. To build the `dashboard` app, `npm` and/or `yarn` needs to be installed. Run the following commands to build the `dashboard` react project.

```
cd dashboard/
yarn            # install node_modules/ packages
yarn build      # build the production setup
```

Inplace of `yarn`, `npm` can be used instead using the following commands (these ideally both do the same thing).

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

### Running the server in development mode

To run the server in development mode, the database must first be built from the defined models in Django.
Once the database has been built, the server can be executed in development mode using the following command:

```
python manage.py runserver
```

Node that any changes made to django will invoke the server to be refreshed to encompass the new changes.

## Adding Users

### Super Users

Currently `superuser`s can be added by using the command:

```
python manage.py createsuperuser
```

### Basic Users

Basic users can be added via the registration page from the frontend. Users can also be registered using REST (which is what the frontend uses).

#### Authentication

JSON Web Tokens (JWT) is used for authentication and can be accessed at the following actions and urls:

##### Registration

To register users, send data to `/api/register/`

The following POST format is used to register users:

```json
{
    "username": "user1",
    "password": "password1"
}
```

##### Login

Located at `/api/login/` which will return an `access` token and a `refresh` token if the user login is valid.

The following POST format is used to obtain a JWT token:

```json
{
    "username": "user1",
    "password": "password1"
}
```

A valid response will appear as:

```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU3NDEyNDg0NywianRpIjoiMDhiYjQxYTQ4ZWVhNDE4YWEzOTEwZWU1YWMxYjY2ZjciLCJ1c2VyX2lkIjoyfQ.cg7NQ8YwVbuX2mVEGg6AFkNVQc7PEs72ohDiOnr2ZPg",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc0MDM4NzQ3LCJqdGkiOiIxYzk4NTM2MGQ3NDA0OWFiYmZkNDQzMDliYjAyMzhkMCIsInVzZXJfaWQiOjJ9.Uz_X2sECClBkfT7p1GyCI8L9buJNVvJ2gxq0VJOBqaM"
}
```
 
 
##### Verification

Located at `/api/verify/` which will return a `200` reponse if the provided token is valid.

The following POST format is used for token verification:

```json
{
    "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTczODg2ODQ0LCJqdGkiOiI5ZjI3MzQxZDIyNGQ0YWIwODRmM2YwYTZmYmNlNWQ4YSIsInVzZXJfaWQiOjJ9.wq9C-a1wJDojXUDGo73fhxQylWVgtmOYNhtEl0Up052"
}
```

##### Refresh

To refresh and obtain a new `access` token, a valid `refresh` token must be used. An `access` token with be provided in response to a valid `refresh` token.

The following POST format is used for refreshing an `access` token:

```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU3NDEyNDg0NywianRpIjoiMDhiYjQxYTQ4ZWVhNDE4YWEzOTEwZWU1YWMxYjY2ZjciLCJ1c2VyX2lkIjoyfQ.cg7NQ8YwVbuX2mVEGg6AFkNVQc7PEs72ohDiOnr2ZPg"
}
```

A valid response will appear as:

```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc0MDM4NzY2LCJqdGkiOiJiNTZjYjJjNmZjMzc0OWRlYTZiYmJjYjJhZTM0ZjBjMCIsInVzZXJfaWQiOjJ9.9kKnf0QY1mM41mA-D0Ixl30yofOC78qU-fePWB6WnMM"
}
```

#### Adding Data as a Valid User

Adding/Viewing data which requires a user to be authenticated requires a valid token. To add data as a authenticated user, the header in the POST payload must be defined with the user's token. The header must contain the `access` token in the following format:

```
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc0MDM4NzY2LCJqdGkiOiJiNTZjYjJjNmZjMzc0OWRlYTZiYmJjYjJhZTM0ZjBjMCIsInVzZXJfaWQiOjJ9.9kKnf0QY1mM41mA-D0Ixl30yofOC78qU-fePWB6WnMM
```


An example curl command to POST feather data is shown below:

```
curl -X POST \
-H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc0MDM4NzY2LCJqdGkiOiJiNTZjYjJjNmZjMzc0OWRlYTZiYmJjYjJhZTM0ZjBjMCIsInVzZXJfaWQiOjJ9.9kKnf0QY1mM41mA-D0Ixl30yofOC78qU-fePWB6WnMM" \
-H "Content-Type: application/json" \
-d '{
        "dev_id": 1,
        "metadata": {
              "location": "Apartment",
              "latitude": 39.77710000,
              "longitude": -83.99720000,
              "time": "2019-10-02T19:17:10.067889-04:00"
        },
        "data": [
         {
             "sensor_id": 1,
             "sensor_type": "Temperature",
             "sensor_data": 19.813,
             "sensor_units": "C"
         },
         {
             "sensor_id": 2,
             "sensor_type": "Temperature",
             "sensor_data": 16.188,
             "sensor_units": "C"
         }
         ]
    }' \
http://localhost:8080/api/Feather/
```