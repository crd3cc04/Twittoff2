# Twittoff2
Python code to creating a web application using Flask

## Setup
Open anaconda and close out all enviornment: 
```sh
conda deactivate
```

Get directory you want the git repo to be housed: 
```sh
cd Desktop
```

Instruction for git clone:
```sh
Create git repo; copy/paste http link in anaconda: git clone https://github.com/crd3cc04/Twittoff2.git 
```

Go to repo directory: 
```sh
cd Twittoff2
```

Open VS Code: 
```sh
code .
```

Instructions for virtual environment and packages install:
```sh
create enviornment: python -m venv pipenv

install packages: pip install Flask Flask-SQLAlchemy Flask-Migrate

activate envirornment: pipenv\Scripts\activate
```

Instructions to setup database:
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
```

## Usage for Basilica and Tweepy usage
```sh
Import packages Requests, Basilica, and Twitter API access: 
pipenv install python-dotenv requests basilica tweepy
```
```sh
Basilica implementation: 
get API Key from the Basilica website
```
```sh
Twitter implementation:
get API, token, and secret tokens from Twitter Dev website. Note that tokens and sercet keys can be otained from the init file for future reference
```
## Differnt Environments for Flask and Tweepy to work
```sh
To use Flask application you will need to create pip env 

To use Tweepy application you will need to use powershell
```