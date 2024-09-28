# Carford App

Python Flask web application with PostgreSQL database to sustain a system where it's possible to save car owners and their cars.

## Table of contents

* [Requirements](#requirements)
    * [Manual Installation](#manual-installation)
    * [Docker and docker-compose](#docker-and-docker-compose)
    * [Flask](#flask)
    * [PostgreSQL](#postgresql)
    * [python-dotenv](#python-dotenv)
    * [Faker](#faker)
* [Run the application](#run-the-application)
    * [Docker installation](#docker-installation)
    * [Environment variables configuration](#environment-variables-configuration)
* [Test the application](#test-the-application)
    * [Scripts](#scripts)
        * [Integration tests](#integration-tests)
        * [Testing everything](#testing-everything)
    * [Manually test](#manually-test)

## Requirements

### Manual Installation

[Installing and setting up the web application with Docker](#docker-installation) will automatically install the Python requirements, but if it is needed to make it by hand, it is possible by using virtualenv, pyenv or any other similar Python virtual environment management tools, using only Pip for the installation.

```bash
cd carford-app/ # Enter the repository root
virtualenv venv # Create local virtualenv
source venv/bin/activate # Acitvate virtualenv
pip install -r reqs.txt # Install the Python requirements
```

### Docker and docker-compose

For the service to run on independent virtualized containers, [Docker CLI](https://docs.docker.com/engine/install/ubuntu/) and [docker-compose](https://docs.docker.com/compose/install/) are required to run the application.

### Flask

Flask was chosen because I am more familiar with it and also it is a really fast and simple web framework, or microframework.

### PostgreSQL

PostgreSQL was chosen as the relational database.

### python-dotenv

To manage project environment variables, python-dotenv allows us to create a simple `.env` file side-by-side with Python's `os.getenv` function, allowing us to use sensitive and/or mutable information inside the code, like API keys, server ports, database location and more.

### Faker

Faker is one of the most famous libraries to create random data like names, emails, numbers and dates, enabling us to use it for testing different user entries and possibilities.

## Run the application

### Docker installation

With the files `Dockerfile` and `docker-compose.yaml` in the repository root folder, it is possible to set up both Python Flask application and PostgreSQL Server by running the following command:

```bash
docker compose up
```

### Environment variables configuration

Environment variables can be configured on `docker-compose.yaml`. Nothing needs to be changed for the application to run, based on the file.

## Test the application

There are two ways of running tests for this application, one of them is through executing scripts and the other is manually testing.

You can run tests both on your machine or on the virtualized container. To run inside the container, when it is running, run the following command to be able to do the testing commands shown in the section below:

```bash
docker exec -it <container_id> bash
```

### Scripts

#### Integration tests

It is possible to run integration tests by entering the already configured virtual environment and running the following command:

```bash
python3 -m unittest tests.integration.all
```

#### Testing everything

It is possible to combine all tests by running the following command:

```bash
python3 -m unittest tests.all
```

### Manually test

One way of manually testing: you can access the application on your browser, create a user at `http://localhost:8080/app/signup`, and then log in at `http://localhost:8080/app/login`, then start using the app, creating owners and cars.

Another way is by using any HTTP request testing tool, such as browsers, Postman, cURL or VSCode "REST Client" extension, where it is possible to manually test the endpoints of this Flask application by following the configurations of `http` files located at the folder `tests/http`.