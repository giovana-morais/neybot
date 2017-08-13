# Import Tweepy, sleep, credentials.py
import tweepy
from time import sleep
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#api.send_direct_message(screen_name="@sofia_turner",text="vamo se beijar")
for tweet in tweepy.Cursor(api.search,q='#DeusEhTop', lang="pt").items(20):
    try:
        print("respondendo para: @"+ tweet.user.screen_name)
        api.update_status('deus é top memo né, @' +
                          tweet.user.screen_name)
        sleep(20)
    except tweepy.TweepError as e:
        print(e.reason)
        sleep(5)
    except StopIteration:
        break

for tweet in tweepy.Cursos(api.search,q="#refri", lang="pt").items():
    try:
        print("respondendo para: @:" + tweet.user.screen_name)
        api.update_status('To chegando com os refrii rapaziada !!')
        sleep(3600) 
    except tweepy.TweepError as e:
        print(e.reason)
        sleep(10)
    except StopIteration:
        break
