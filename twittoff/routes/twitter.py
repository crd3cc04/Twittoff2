#twittoff/routes/twitter.py

from flask import Blueprint, jsonify#, request, render_template #, flash, redirect
from twittoff.services.twitter1 import api as twitter_api
from twittoff.model import db, User, Tweets,  parse_records

twitter = Blueprint("twitter", __name__)

@twitter.route("/users/<screen_name>/fetch")
def fetch_user_data(screen_name):
    print(screen_name)
    
    # TODO: fetch user info
    user = twitter_api.get_user(screen_name)
    # TODO: fetch their tweets
    statuses = twitter_api.user_timeline("elonmusk", tweet_mode="extended", count=35, exclude_replies=True, include_rts=False)
    # TODO: fetch embedding for each tweet

    # TODO: store user info in database (w/ embeddings)
    db_user = User("_______________")
    db.session.add(db_user)
    db.session.commit()

    #return f"FETCHED {screen_name} OK"
    return jsonify({"user": user._json, "num_tweets": len(statuses)})