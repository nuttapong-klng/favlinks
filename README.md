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

## Web page

1. Sign Up: http://localhost:8000/accounts/signup/
1. Login: http://localhost:8000/accounts/login/
1. Favorited Links: http://localhost:8000/favorite_urls/list/
1. Categories: http://localhost:8000/favorite_urls/category/list/
1. Tags: http://localhost:8000/favorite_urls/tag/list/

## API
1. Token auth: http://localhost:8000/api/token/
1. Favorited Links: http://localhost:8000/api/favorite_urls/
1. Categories: http://localhost:8000/api/categories/
1. Tags: http://localhost:8000/api/tags/
