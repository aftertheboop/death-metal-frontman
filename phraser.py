import re, random


class Phraser():

    def __init__ (self):
        # Going to keep things simple with these three word types
        self.alltitles = []
        self.adjectives = []
        self.verbsing = []
        self.verbsed = []
        self.nouns = []
        # linking phrase words, conjunctions, prepositions etc.
        self.shorts = ["!", "&", "(", ")", ",", "101", "69", "a", "ain't", "aint", "all", "am", "an", "and", "another",
                       "are", "as", "at", "be", "before", "but", "by", "come", "don't", "dont", "down", "for", "from",
                       "had", "has", "have", "he", "her", "hers", "his", "i", "i'm", "i've", "im", "in", "inside",
                       "into", "is", "it", "it's", "its", "itself", "ive", "let", "many", "me", "must", "my", "no",
                       "of", "on", "or", "our", "ov", "own", "put", "shall", "she", "so", "that", "the", "their",
                       "them", "they", "this", "through", "thus", "thy", "till", "to", "too", "under", "up", "upon",
                       "us", "was", "we", "what", "when", "where", "which", "who", "will", "with", "within", "you",
                       "you", "your"]
        self.phrases = []

    def read(self, filename):

        f = open(filename, 'r')

        # split out each individual song title from the text file
        self.alltitles = f.read().lower().split("\n")

        return self.alltitles

    def sort(self):

        for title in self.alltitles:

            explodedtitle = title.split(" ")

            if len(explodedtitle) > 1:

                titlephrase = []

                for word in explodedtitle:

                    # word = word.replace('.', '')
                    word = re.sub(r'\W+', '', word)

                    if word in self.shorts:              # is this a linking word?
                        titlephrase.append(word)
                    elif word.endswith('ing'):          # put doing words in verbs
                        self.verbsing.append(word)
                        titlephrase.append('%ving')
                    elif word.endswith('ed'):           # put 'ed words in verbs
                        self.verbsed.append(word)
                        titlephrase.append('%ved')
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
            # put everything back together randomly, woo
            if word == '%n':
                thephrase[key] = random.choice(self.nouns)
            elif word == '%a':
                thephrase[key] = random.choice(self.adjectives)
            elif word == '%ving':
                thephrase[key] = random.choice(self.verbsing)
            elif word == '%ved':
                thephrase[key] = random.choice(self.verbsed)
            else:
                thephrase[key] = word

        return ' '.join(thephrase).upper()

