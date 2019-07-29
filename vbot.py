#!/usr/bin/env python

import pronouncing, random

def syllables(w):
    return pronouncing.syllable_count(pronouncing.phones_for_word(w)[0])

ings = [ w for w in pronouncing.search("IH0 NG$") if syllables(w) == 2  ]
ows = [ w for w in pronouncing.rhymes('now') if syllables(w) == 1 ]

verbs = random.sample(ings, 2)
verb2 = random.choice(pronouncing.rhymes(verbs[0]))

ow = random.choice(ows)

if ow[0] in 'aeoiu':
    ow = ' an ' + ow
else:
    ow = ' a ' + ow

print("You can get it " + verbs[0])
print("You can get it " + verb2)
print("You can get it " + verbs[1] + ow)
print("Matter of fact I've got it now")
