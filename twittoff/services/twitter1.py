#twittoff/services/twitter1.py

import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
print(type(auth))

api = tweepy.API(auth)
print(type(api))
# import pprint from pprint to get a single column list of what the directory has...

#user = api.get_user("elonmusk")
#print(type(user)) #<class 'tweepy.models.User'>


if __name__ == "__main__":

    screen_name = input("Flease choose a screen_name")
    # For example on a user in Twitter....
    print("------------------")
    print("USER")
    user = api.get_user("elonmusk")
    print(type(user))
    print(user.screen_name)
    print(user.id)
    print(user.statuses_count)

    print("-------------------")
    print("STATUSES")
    # Actual code to retrieve users tweets
    #statuses = api.user_timeline("elonmusk", count=25) #how ever many tweets you want to pull
    #for status in statuses:
    #    print("---")
    #    print(status.text)

    # If you are needing to add more parameters and are narrowing down linespace.....
    statuses = api.user_timeline("elonmusk", tweet_mode="extended", count=35, exclude_replies=True, include_rts=False) #Make sure that watch out for parameters; they will filter out how many tweets you are trying to call for.....
    for status in statuses:
        print("-----")
        print(status.full_text)

    status = statuses[0]
    print(type(status)) #<class 'tweepy.models.Status'>

    print(status.id)
    print(status.full_text)
    #breakpoint()

    #To get the json file for the statuses use this code....
    #from pprint import pprint
    #pprint(status._json)
