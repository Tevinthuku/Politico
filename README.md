[![Build Status](https://travis-ci.org/Tevinthuku/Politico.svg?branch=develop)](https://travis-ci.org/Tevinthuku/Politico)
[![Maintainability](https://api.codeclimate.com/v1/badges/65cb6a9e0fc4d16df8ce/maintainability)](https://codeclimate.com/github/Tevinthuku/Politico/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/Tevinthuku/Politico/badge.svg?branch=Ch-setup-code-coverage-163674818)](https://coveralls.io/github/Tevinthuku/Politico?branch=Ch-setup-code-coverage-163674818)

![](https://img.shields.io/github/last-commit/Tevinthuku/Politico/develop.svg?style=for-the-badge)
![](https://img.shields.io/pypi/pyversions/flask.svg?style=for-the-badge)
# Politico

A Platform for driving political change and engagement

## Setup and installation

1. Set up virtualenv

   ```bash
        virtualenv venv
   ```

2. Activate virtualenv

   ```bash
        source venv/bin/activate
   ```

3. Install dependencies

   ```bash
        pip install -r requirements.txt
   ```

4. Setup env variables
    - export FLASK_APP=run.py
    - export FLASK_DEBUG=1
    - export FLASK_ENV=development

5. Running tests
      ```
         python -m pytest --cov=app/api
      ```
##Politico Endpoints

| Method | Endpoint          | Description                           |
| ------ | ----------------- | ------------------------------------- |
| `GET`  | `/api/v1/offices` | View All offices created by the ADMIN |



### Author: TevinThuku

### Credits: Andela
