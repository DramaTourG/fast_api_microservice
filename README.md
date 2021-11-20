# FastAPIService

## Run server with database in docker
run command in terminal or Git bash (optional)
   
 ```bash
    docker-compose up --build
 ```
server is available at the following address:

 ```
 bash localhost:8000
 ```

## Prerequisites

- We use Python 3
- Install pipenv `pip install pipenv`
- Spawns a shell within the virtualenv: `pipenv shell`
- Install all dependencies `pipenv install`


### Run server

If you want to run a backend API:
1. create .env file or set environment variables
2. run your database and set DATABASE_URL
3. for migrations run `alembic upgrade head`
4. run server:
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```
    or `python main.py`


## Tests

In order to run tests:

- Install all dependencies `pipenv install --dev`
- Run pytest `python -m pytest`

## Migration

- create new migration `alembic revision -m "Add a column"`
- run migration `alembic upgrade head`

## Documentation API

API documentation is available at ```.../docs```
For example: 
The server is running locally the path is: ```http://localhost:8000/docs/```
