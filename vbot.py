#!/usr/bin/env python

from botclient import Bot
import re, pronouncing, random




class VictoriaBotter(Bot):
    def syllables(self, w):
        return pronouncing.syllable_count(pronouncing.phones_for_word(w)[0])

    def syllfilt(self, words, n):
        if self.hose:
            return [ w for w in words if self.syllables(w) == n and not self.hose.search(w) ]
        else:
            return [ w for w in words if self.syllables(w) == n ]
 
    def render(self):
        if self.cf['hose']:
            self.hose = re.compile(self.cf['hose'])
        else:
            self.hose = None
        participles = self.syllfilt(pronouncing.search("IH0 NG$"), 2)
        nouns = self.syllfilt(pronouncing.rhymes('now'), 1)

        rhymes = []
        p1 = None
        p3 = None
        while not rhymes:
            ps = random.sample(participles, 2)
            rhymes = self.syllfilt(pronouncing.rhymes(ps[0]), 2)

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
    options = {}
    if 'content_warning' in vb.cf:
    	options['spoiler_text'] = vb.cf['content_warning']
    if 'visibility' in vb.cf:
        options['visibility'] = vb.cf['visibility']
    toot = vb.render()
    vb.post(toot, options)





