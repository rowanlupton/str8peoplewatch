from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
import tweepy
import json

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if status.user.id in api.friends_ids():
            id = status.id
            api.update_status('no', in_reply_to_status_id=id, auto_populate_reply_metadata=True)
streamListener = StreamListener()
stream = tweepy.Stream(auth = api.auth, listener=streamListener)

stream.filter(track=['are straight people okay'])
# tweets = api.home_timeline.search(q="are straight people okay")
# for tweet in tweets:
#     # if "are straight people okay" in tweet.text:
#     print('@'+tweet.user.screen_name + ':', tweet.text)

# api.update_status("no, they're really not")
