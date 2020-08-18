#twittoff/routes/tweet.py

from flask import Blueprint, jsonify, request, render_template , flash, redirect

from twittoff.model import db, Old_Tweet, parse_records

tweet = Blueprint("tweet", __name__)

@tweet.route("/tweets.json")
def list_tweets():
    tweets = [
        {"id": 1, "cory_ken": "Motivate"},
        {"id": 2, "kyle_jen": "New Makeup"}
    ]

    #tweet_records = Tweets.query.all()
    #print(tweet_records)
    #tweets = parse_records(tweet_records)
    return jsonify(tweets)

@tweet.route("/tweets")
def list_tweets_from_twitter():
    tweets = [
        {"id": 1, "cory_ken": "Motivate"},
        {"id": 2, "kyle_jen": "New Makeup"}
    ]
#    tweet_records = Tweets.query.all()
#    tweets = parse_records(tweet_records)
    return render_template("tweets.html", tweets=tweets)


@tweet.route("/tweets/new")
def new_tweet():
    return render_template("new_tweet.html")

@tweet.route("/tweets/create", methods=["POST"])
def create_tweet():
    print("FORM DATA:", dict(request.form)) #>{"tweets": "___", "user_name": "___"}


    new_tweet = Old_Tweet(user=request.form["user_name"], tweet=request.form["tweets"])
    db.session.add(new_tweet)
    db.session.commit()# todo: store in database


    return jsonify({
        "message": "TWEET CREATED OK",
        "tweet": dict(request.form)
    })
    #flash(f"Book '{new_book.title}' created successfully!", "success")
    #return redirect(f"/books")