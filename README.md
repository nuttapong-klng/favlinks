# FavLinks

FavLinks Web Application

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: MIT

## Run Local

1. Builld and up the services
    ```bash
    docker compose -f docker-compose.local.yml build
    docker compose -f docker-compose.local.yml up -d
    ```
1. Wait a minute for the service to be ready
1. Go to http://localhost:8000/ to access the web page
1. Or use http://localhost:8000/api/ to access the APIs
