import os
from markovbot import MarkovBot

# Initialise a MarkovBot instance
tweetbot = MarkovBot()


# Get the current directory's path
dirname = os.path.dirname(os.path.abspath(__file__))
print (dirname)
# Construct the path to the book
book = os.path.join(dirname, 'hotep_speak.txt')
# Make your bot read the book!
tweetbot.read(book)


my_first_text = tweetbot.generate_text(25, seedword=['black', 'america'])
print("tweetbot says:")
print(my_first_text)


# ALL YOUR SECRET STUFF!
# Consumer Key (API Key)
cons_key = 'K9YqNYb8j6HA0hgBKLZ1aQ918'
# Consumer Secret (API Secret)
cons_secret = 'BFCDji7mF7sfw2PpdQMEcZ90Poht5E6OMff1XEHb3UeLB8K1Fz'
# Access Token
access_token = '988043632828715008-U4kAofzutxFuPx6c3jCwnrRztm3y5lt'
# Access Token Secret
access_token_secret = 'zNxtfZQb9HU3nRN88uJzJ39H2Ttfk7Vno0Qc3WobX0U5J'


# Log in to Twitter
tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)


# Start periodically tweeting
tweetbot.twitter_tweeting_start(days=0, hours=0, minutes=10, keywords=['Greetings', 'pan-African', 'Kemet', 'King', 'My Negus'], prefix=None, suffix='#Ash_e_Hotep')

import time; time.sleep(86400)

# Use the following to stop periodically tweeting
# (Don't do this directly after starting it, or your bot will do nothing!)
# tweetbot.twitter_tweeting_stop()
