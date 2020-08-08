#twittoff/model.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()

class Old_Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True, extend_existing=True)
    user = db.Column(db.String(128))
    tweet = db.Column(db.String(128))

#    def __repr__(self):
#        return f"<Old_Tweet {self.id} {self.user} {self.tweet}>"

#class User(db.Model):
#    id = db.Column(db.BigInteger, primary_key=True)
#    screen_name = db.Column(db.String(128), nullable=False)
#    name = db.Column(db.String)
#    location = db.Column(db.String)
#    followers_count = db.Column(db.Integer)
    #latest_tweet_id = db.Column(db.BigInteger)

#class Tweets(db.Model):
#    id = db.Column(db.BigInteger, primary_key=True)
#    user_id = db.Column(db.BigInteger, db.ForeignKey("user.id"))
#    full_text = db.Column(db.String(500))
    #embedding = db.Column(db.PickleType)

    #user = db.relationship("User", backref=db.backref("tweets", lazy=True))


def parse_records(database_records):
    parsed_records = []
    for record in database_records:
        print(record)

    parsed_record = record.__dict__
    del parsed_record["_sa_instance_state"]
    parsed_records.append(parsed_record)
    return parsed_records