from flask import Flask

#from twittoff.models import db, migrate
from twittoff.routes.welcome import welcome 
#from app_dev.routes.tweet_routes import tweet_routes
#from app_dev.routes.twitter_routes import twitter_routes


#DATABASE_URI = "sqlite:///twitoff_dev_app.db" # using relative filepath
#DATABASE_URI = "sqlite:////Users/Username/Desktop/your-repo-name/web_app_99.db" # using absolute filepath on Mac (recommended)
#DATABASE_URI = "sqlite:///C:\\Users\\Username\\Desktop\\your-repo-name\\web_app_99.db" # using absolute filepath on Windows (recommended) h/t: https://stackoverflow.com/a/19262231/670433

def create_app():
    app = Flask(__name__)

    #app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    #db.init_app(app)
    #migrate.init_app(app, db)

    app.register_blueprint(welcome)
    #app.register_blueprint(tweet_routes)
    #app.register_blueprint(twitter_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)