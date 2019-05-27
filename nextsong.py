import os, random, tweepy
from os import environ

from phraser import Phraser

# Create a new phrase generator
phraser = Phraser()

# Get the source song titles txt file
dirname = os.path.dirname(os.path.abspath(__file__))
titles = os.path.join(dirname, 'source.txt')

# Read the titles into phraser
phraser.read(titles)

# Sort the read-in phrases into words and phrase strings
phraser.sort()

# Generate a song title from the phraser
songtitle = phraser.generate()

# Get a random intro line
alllines = os.path.join(dirname, 'frontmanlines.txt');
f = open(alllines, 'r')

lines = f.read().split("\n")

line = random.choice(lines)

auth = tweepy.OAuthHandler(environ['CONSUMER_KEY'], environ['CONSUMER_SECRET'])
auth.set_access_token(environ['ACCESS_KEY'], environ['ACCESS_SECRET'])
api = tweepy.API(auth)

api.update_status(line + ' "' + songtitle + '!"')
print('Posted: ' + line + songtitle)