import re, random


class Phraser():

    def __init__ (self):
        # Going to keep things simple with these three word types
        self.allwords = []
        self.adjectives = []
        self.verbs = []
        self.nouns = []
        self.other = [] # just in case

    def read(self, filename):

        f = open(filename, 'r')

        self.allwords = re.sub("\n", " \n", f.read()).lower().replace("\n", "").split(' ')
        # no idea why i suddenly need to replace \n

        return self.allwords

    def sort(self):

        for word in self.allwords:
            word = word.replace('.', '')

            # this is a hyper simple approach, need more logic here
            if word.endswith('ing'):
                self.verbs.append(word)
            elif word.endswith('ed'):
                self.verbs.append(word)
            elif word.endswith('ly'):
                self.adjectives.append(word)
            elif word in ["the", "in", "a", "by", "my", "and", "on", "an", "of", "to", "as", "with", "i"]:
                word
            else:
                self.nouns.append(word)

    def generate(self):

        phrases = [
            "%v by %n",
            "%v in the %n",
            "%v %n",
            "%v %a by %n",
            "%v with %n",
            "%n %v",
            "the %a %n",
            "a %n"
        ]
        phrase = random.choice(phrases)

        phrase = phrase.replace("%v", random.choice(self.verbs))\
                       .replace("%n", random.choice(self.nouns))\
                       .replace("%a", random.choice(self.adjectives))

        return phrase.upper()






