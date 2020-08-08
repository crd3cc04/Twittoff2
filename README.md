# Twittoff2
Python code to creating a web application using Flask

## Setup
Instruction for git clone

Instructions for virtual environment

Instructions to setup database

```sh
flask db init #> generate app/migrations dir. will not need to run again once already ran

#run both when changing the schema:
flask db migrate #> create the db (with "alembic_version" table)
flask db upgrade
```


## Usage

```sh
Deploy Flask App Itself: FLASK_APP_twittoff.py
Run Flask App: flask run