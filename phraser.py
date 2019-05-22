import re, random


class Phraser():

    def __init__ (self):
        # Going to keep things simple with these three word types
        self.alltitles = []
        self.adjectives = []
        self.verbs = []
        self.nouns = []
        self.links = ["the", "in", "&", ")", "(", ",", "!", "a", "has", "by", "are", "my", "and", "on", "an", "of", "to", "as", "with",
                      "i", "have"] # linking phrase words, conjunctions, prepositions etc.
        self.phrases = []

    def read(self, filename):

        f = open(filename, 'r')

        # split out each individual song title from the text file
        self.alltitles = f.read().lower().split("\n")

        return self.alltitles

    def sort(self):

        for title in self.alltitles:

            explodedtitle = title.split(" ")
            titlephrase = []

            for word in explodedtitle:

                word = word.replace('.', '')

                if word in self.links:              # is this a linking word?
                    titlephrase.append(word)
                elif word.endswith('ing'):          # put doing words in verbs
                    self.verbs.append(word)
                    titlephrase.append('%v')
                elif word.endswith('ed'):           # put 'ed words in verbs
                    self.verbs.append(word)
                    titlephrase.append('%v')
                elif word.endswith('ly'):           # put 'ly words in adjectives (fuzzy)
                    self.adjectives.append(word)
                    titlephrase.append('%a')
                else:
                    self.nouns.append(word)         # everything else is a noun 'cos that's how english works
                    titlephrase.append('%n')

            if titlephrase not in self.phrases:
                self.phrases.append(' '.join(titlephrase))

    def generate(self):

        phrase = random.choice(self.phrases)

        thephrase = phrase.split(' ')

        for key, word in enumerate(thephrase):

            if word == '%n':
                thephrase[key] = random.choice(self.nouns)
            elif word == '%a':
                thephrase[key] = random.choice(self.adjectives)
            elif word == '%v':
                thephrase[key] = random.choice(self.verbs)
            else:
                thephrase[key] = word

        return ' '.join(thephrase).upper()






