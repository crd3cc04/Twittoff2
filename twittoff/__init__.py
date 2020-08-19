from flask import Flask

from twittoff.model import db, migrate
from twittoff.routes.welcome import welcome 
from twittoff.routes.tweet import tweet
from twittoff.routes.twitter import twitter
from twittoff.routes.admin_routes import admin_routes #registering admin functions to create or delete tables and/or database....
from twittoff.routes.stats1 import stats1 #registering admin functions to create or delete tables and/or database....


#DATABASE_URI = "sqlite:///twitoff2.db" # using relative filepath
#DATABASE_URI = "sqlite:////Users/Username/Desktop/your-repo-name/web_app_99.db" # using absolute filepath on Mac (recommended)
DATABASE_URI = "sqlite:///C:\\Users\\Lola\\Desktop\\Twittoff2\\twittoff\\twitoff2.db" # using absolute filepath on Windows (recommended) h/t: https://stackoverflow.com/a/19262231/670433

def create_app():
    app = Flask(__name__)
    app.secret_key = "him1203"

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(welcome)
    app.register_blueprint(tweet)
    app.register_blueprint(twitter)
    app.register_blueprint(admin_routes)
    app.register_blueprint(stats1)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)