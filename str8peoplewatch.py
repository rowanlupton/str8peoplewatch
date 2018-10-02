from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
import tweepy
import json

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

class StreamListener(tweepy.StreamListener):
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return True
    def on_status(self, status):
        if any(mentions['screen_name'] == 'str8peoplewatch' for mentions in status.entities['user_mentions']):
            try:
                api.retweet(status.id)
            except: # this should get proper error handling
                pass

        elif status.user.id in api.followers_ids():
            id = status.id
            api.update_status('no', in_reply_to_status_id=id, auto_populate_reply_metadata=True)

streamListener = StreamListener()
stream = tweepy.Stream(auth = api.auth, listener=streamListener)
stream.filter(track=['are straight people okay', '@str8peoplewatch'], async=True)

# api.update_status("no, they're really not")
