#twittoff/routes/welcome.py
from flask import Blueprint

welcome = Blueprint("welcome", __name__)

@welcome.route("/")
def index():
    return f"Index Page"

@welcome.route("/welcome")
def about():
    return "Welcome to Twitoff Challenge"