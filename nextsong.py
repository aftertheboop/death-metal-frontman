import os, random

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
songTitle = phraser.generate()

print(songTitle)