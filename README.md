# About the project

Challenge to person CRUD
# Docker and Docker Compose installation

Install Docker:

- `https://docs.docker.com/install/`

After install Docker, proceed to install Docker Compose:

- `https://docs.docker.com/compose/install/`

### Project Structure

The following is the suggested structure to successfully build this project:

```
thinknow-challenge/            # root project
├── src/                       # django project
├── Dockerfile                 # django dockerfile
├── docker-compose-dev.yml     # docker compose definition for dev
└── ...
```

## Project Setup

In the following steps we will cover some basic stuff to setup a development environment for thinknow

### Building the Project for Development Environment

1. Clone the repository using the following command:
```
$ git clone git@github.com:jlmallas160190/thinknow-challenge.git
```
2. Positioned in the root folder execute:
```
# This will clone related repositories and build neccesary docker images.

$ ./pre_setup.sh
```
4. **(Optional)** [Configure PyCharm using Docker-compose file](https://docs.google.com/document/d/19YYeBZ6t88g_AGLCbVejOC5zC-oAL1T0xEyXmX_adXM/edit?usp=sharing)
5. **(Ignore if you followed previous instructions)** Run all services with:
```
$ docker-compose -f docker-compose-dev.yml up -d
```
7. Run post install script to apply migration to related services and load data:


## Install New Dependencies

In order to install new dependencies in the project, you should have Pipenv installed locally.

Please follow these instructions to install it in your local machine: https://pipenv.pypa.io/en/latest/#install-pipenv-today

After installing Pipenv, follow these instructions to perform the installation of a new dependency:
1. Stop all containers `docker-compose -f docker-compose-dev.yml down`.
2. Step to src/ folder: `cd src`.
3. Run `pipenv install <dependency>`.
4. Run `./build_backend` to build a new backend image with the new dependencies.
6. Run `docker-compose -f docker-compose-dev.yml up -d` to start all containers.
7. Remember to commit modified `Pipenv` and `Pipfile.lock` files.

## Project Basic Commands

### Backend
**Build backend image when new dependencies are being installed**:

`$ ./build_backend.sh`

**Apply migrations to the DB:**

`$ ./execute manage migrate`

**Create a super-user:**

`$ ./execute manage createsuperuser`

**Collect static files:**

`$ ./execute manage collectstatic`

**Run Tests:**

`$ ./execute manage test`
