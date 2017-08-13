# Import Tweepy, sleep, credentials.py
import tweepy
from time import sleep
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# For loop to iterate over tweets with #ocean, limit to 10
for tweet in tweepy.Cursor(api.search,q='#DeusEhTop', lang="pt").items(10):
    try:
    # Print out usernames of the last 10 people to use #DeusEhTop
        print('Tweet by: @' + tweet.user.screen_name)
        tweet.retweet()
        tweet.favorite()
        if not tweet.user.follow():
            tweet.user.follow()
#        sleep(20)
        sleep(1800)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
