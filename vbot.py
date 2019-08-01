#!/usr/bin/env python

from botclient import Bot
import pronouncing, random

def syllables(w):
    return pronouncing.syllable_count(pronouncing.phones_for_word(w)[0])

def syllfilt(words, n):
    return [ w for w in words if syllables(w) == n ]


class VictoriaBotter(Bot):

    def render(self):
        participles = syllfilt(pronouncing.search("IH0 NG$"), 2)
        nouns = syllfilt(pronouncing.rhymes('now'), 1)

        rhymes = []
        p1 = None
        p3 = None
        while not rhymes:
            ps = random.sample(participles, 2)
            rhymes = syllfilt(pronouncing.rhymes(ps[0]), 2)

        p1 = ps[0]
        p2 = random.choice(rhymes)
        p3 = ps[1]

        noun = random.choice(nouns)

        if noun[0] in 'aeoiu':
            noun = ' an ' + noun
        else:
            noun = ' a ' + noun

        text = "You can get it " + p1 + "\n"
        text += "You can get it " + p2 + "\n"
        text += "You can get it " + p3 + noun + "\n"
        text += "Matter of fact I've got it now"

        return text

        
if __name__ == '__main__':
    vb = VictoriaBotter()
    vb.configure()
    toot = vb.render()
    vb.post(toot)





