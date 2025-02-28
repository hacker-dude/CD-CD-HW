# CI/CD Framework Home task

## Setup

1. Dockerfile includes the setup for Jenkins

2. Build and run the container using Podman

3. Setup Jenkins enviromental variables for DB connection

## Pipeline

### Stages:
__1. Checkout SCM:__

Get Latest commits from repos main branch

__2. Build:__
 - activate virtual env
 - install necessary requirements

__3. Checkout SCM:__

 - activate virtual env
 - run tests using python