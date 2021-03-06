import os
from dotenv import load_dotenv
load_dotenv()

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_KEY = os.getenv("ACCESS_KEY")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
HANDLE = 'str8peoplewatch'

listenFor = [
    '@'+HANDLE,
    'straight people',
    'str8 people',
    'straight ppl',
    'str8 ppl'
    'straight folks',
    'str8 folks'
]
noRT = [
    'no retweet',
    'no rt',
    'don\'t retweet',
    'don\'t rt'
]
responses = [
    'no',
    'nope',
    'obviously not',
    'so not okay',
    'nooooooooope',
    'nah',
    'oh, honey, if only',
    'lol, no',
    'absolutely not',
    '200% no',
    'heterNo',
    'does it even matter?'
]
