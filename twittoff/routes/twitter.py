#twittoff/routes/twitter.py

from flask import Blueprint, jsonify#, request, render_template #, flash, redirect
from twittoff.services.twitter1 import api as twitter_api
from twittoff.model import db, User, Tweets,  parse_records

twitter = Blueprint("twitter", __name__)

@twitter.route("/users/<screen_name>/fetch")
def fetch_user_data(screen_name):
    print("FETCHING...", screen_name)
    
    # fetch user info
    user = twitter_api.get_user(screen_name)
    
    # store user info in database 
    db_user = User.query.get(user.id) or User(id=user.id)
    db_user.screen_name = user.screen_name
    db_user.name = user.name
    db_user.location = user.location
    db_user.followers_count = user.followers_count
    db.session.add(db_user)
    db.session.commit()

    # fetch their tweets

    statuses = twitter_api.user_timeline(screen_name, tweet_mode="extended", count=35, exclude_replies=True, include_rts=False)
    # TODO: fetch embedding for each tweet


    # store tweets in database (w/ embeddings)

    # counter = 0
    for status in statuses:
        print(status.full_text)
        print("----")
        #print(dir(status))
        # get existing tweet from the db or initialize a new one:
        db_tweet = Tweets.query.get(status.id) or Tweets(id=status.id)
        db_tweet.user_id = status.author.id # or db_user.id
        db_tweet.full_text = status.full_text
        #embedding = basilica_client.embed_sentence(status.full_text, model="twitter") # todo: prefer to make a single request to basilica with all the tweet texts, instead of a request per tweet
        #embedding = embeddings[counter]
        #print(len(embedding))
        #db_tweet.embedding = embedding
        db.session.add(db_tweet)
        #counter+=1

    db.session.commit()


    return f"FETCHED {screen_name} OK"
    #return jsonify({"user": user._json, "num_tweets": len(statuses)})