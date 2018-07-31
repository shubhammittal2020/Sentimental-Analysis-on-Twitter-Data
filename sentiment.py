import tweepy
from textblob import TextBlob

consumer_key='v3yezHywrApvm1hxKL493jDRL'
consumer_secret='reGAy6P4F3erzhOoNXI6BCc2hn5DBlyjuLeOVFYFfjuEyREujI'

access_token='981943034928562177-yYI8alatLNapKMwBXDSFGPEEEBK39cQ'
access_token_secret='UMiAJMz4NHSmbEXgWXSxUEwC53objnJ7of74sdAl484da'

auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api= tweepy.API(auth)

public_tweets= api.search('Trump')

for tweet in public_tweets:
   print(tweet.text)
   analysis= TextBlob(tweet.text)
   print(analysis.sentiment)
   
