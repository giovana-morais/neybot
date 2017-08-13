import tweepy
from time import sleep
from credentials import *

# faz acesso
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# operações com arquivo dos tweets
arquivo = open('ney.txt', 'r')
linhas = arquivo.readlines()
arquivo.close()

def tweet():
    for linha in linhas:
        try:
            print(linha)
            if linha != "\n":
                api.update_status(linha)
                # espera 1 dia antes da próxima postagem
                sleep(86400)
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
            # espera 1 hora antes de tentar a próxima linha
            sleep(3600)

tweet()
