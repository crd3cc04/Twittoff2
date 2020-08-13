#twittoff/routes/twitter.py

from flask import Blueprint, jsonify#, request, render_template #, flash, redirect
from twittoff.services.twitter1 import api as twitter_api
from twittoff.model import db, User, Tweets,  parse_records

twitter = Blueprint("twitter", __name__)

@twitter.route("/users/<screen_name>/fetch")
def fetch_user_data(screen_name):
    print("FETCHING...", screen_name)
    
    # TODO: fetch user info
    user = twitter_api.get_user(screen_name)
    
    

    # TODO: store user info in database (w/ embeddings)
    db_user = User.query.get(user.id) or User(id=user.id)
    db_user.screen_name = user.screen_name
    db_user.name = user.name
    db_user.location = user.location
    db_user.followers_count = user.followers_count
    db.session.add(db_user)
    db.session.commit()

    # TODO: fetch their tweets
    statuses = twitter_api.user_timeline(screen_name, tweet_mode="extended", count=35, exclude_replies=True, include_rts=False)
    
    # TODO: fetch embedding for each tweet
    # TODO: store tweets in database (w/ embeddings)


    #return f"FETCHED {screen_name} OK"
    return jsonify({"user": user._json, "num_tweets": len(statuses)})