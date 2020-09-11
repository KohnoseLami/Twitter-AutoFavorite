import tweepy
import re

consumer_key = "3rJOl1ODzm9yZy63FACdg"
consumer_secret = "5jPoQ5kQvMJFDYRNE8bQ4rHuds4xJqhvgNJM4awaE8"
access_key = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
   def on_status(self, status):
       if "@" in status.text:
           pass
       else:
           api.create_favorite(status.id)
           print("ふぁぼったよ！「" + status.text + "」ID:" + status.id_str)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(follow=[""], is_async=True)
