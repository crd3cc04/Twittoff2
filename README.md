# Twittoff2
Python code to creating a web application using Flask

## Setup
Open anaconda and close out all enviornment: conda deactivate
Get directory you want the git repo to be housed: cd Desktop

Instruction for git clone:
Create git repo; copy/paste http link in anaconda: git clone https://github.com/crd3cc04/Twittoff2.git 

Go to repo directory: 
cd Twittoff2

Open VS Code: 
code .

Instructions for virtual environment and packages install:
create enviornment: python -m venv pipenv

install packages: pip install Flask Flask-SQLAlchemy Flask-Migrate

activate envirornment: pipenv\Scripts\activate

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