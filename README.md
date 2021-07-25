# FluToDo application
It is a web service that show a list of TODO items and functionalities to add more items and modify them.
It also provides a REST API with the same functionalities.
It is written in python3 using the django rest framework and uses a PostgreSQL database. 
Support for docker is also provided to facilitate deploying on production.

## Environment
Env variables are read from an .env file on the root directory. 
You can use the file .env_sample as a reference of which variables must be setup.
Create an .env file with the required variables.

## Running the server with docker
To run it with docker just follow this steps:

1. Install [docker](https://docs.docker.com/engine/installation/)
2. Install [docker-compose](https://docs.docker.com/compose/install/)
3. Run the following command:
```
    docker-compose up
```
Then go to [localhost:8000](http://localhost:8000) on your browser

## REST API documentation
You can access the documentation of the REST API on [/api/docs](http://localhost:8000/api/docs)
