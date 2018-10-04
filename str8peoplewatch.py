from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
from config import HANDLE, listenFor, noRT, responses
import tweepy
import random, re

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

class StreamListener(tweepy.StreamListener):
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return True
        else:
            api.send_direct_message(screen_name=rowanlupton, text="str8peoplewatch is down")
    def on_status(self, status):
        if (status.truncated):
            statusText = status._json['extended_tweet']['full_text']
        else:
            statusText = status.text
        if any(mentions['screen_name'] == HANDLE for mentions in status.entities['user_mentions']):
            if hasattr(status, 'quoted_status'):
                try:
                    api.retweet(status.id)
                except: # this should get proper error handling
                    pass
            elif not hasattr(status, 'retweeted_status'):
                # if ('straight' in statusText or 'okay' in statusText):
                if (re.search(r'(([^@]str(8|aight))|([^(str8)]p\S*p(l|s)e?)|(ok))(?mi)', statusText) is not None):
                    try:
                        api.retweet(status.id)
                    except: # this should get proper error handling
                        pass

            # elif (status.user.id in api.followers_ids()):

        if (re.search(r'(\S*r\S*) (str\S*) (p\S*p(l|s)e?) (\S* )?((ok\S*)|(alright))(?mi)', statusText) is None):
            pass
        else:
            api.update_status(random.choice(responses), in_reply_to_status_id=status.id, auto_populate_reply_metadata=True)

streamListener = StreamListener()
stream = tweepy.Stream(auth = api.auth, listener=streamListener)
stream.filter(track=listenFor, async=True)

# api.update_status("no, they're really not")
