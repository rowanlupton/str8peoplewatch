# str8peoplewatch
Are straight people okay? Stay tuned.

## about
This is a (currently twitter-only) bot that listens for anybody asking if straight people are okay, and responds that, no, they are not. There's some allowance for different spellings and an option to add an extra word between "straight" and "okay", e.g. "are straight people doing okay?". There could definitely be some more sophisticated regexing going on here.
It will also probably retweet @mentions that say some variation on "straight" or "people" (e.g. "str8" will work, as will "ppl" or "peeps").

## how to use
To use this bot, you will need to:
* make an API key on [dev.twitter.com](https://dev.twitter.com)
* plug the keys into a `.env` file on your computer (or use another method of setting environment variables)
* decide whether you want to continually run it
  * if not, you can run it from your computer
  * if yes, you'll probably want to throw it up on something that's always connected to the internet, be that a vps, heroku, local raspberry pi, whatever
