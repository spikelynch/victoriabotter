#!/usr/bin/env python

import pronouncing, random

def syllables(w):
    return pronouncing.syllable_count(pronouncing.phones_for_word(w)[0])

def syllfilt(words, n):
    return [ w for w in words if syllables(w) == n ]

ings = syllfilt(pronouncing.search("IH0 NG$"), 2)
ows = syllfilt(pronouncing.rhymes('now'), 1)


rhymes = []
while not rhymes:
    verbs = random.sample(ings, 2)
    rhymes = syllfilt(pronouncing.rhymes(verbs[0]), 2)


verb2 = random.choice(rhymes)

ow = random.choice(ows)

if ow[0] in 'aeoiu':
    ow = ' an ' + ow
else:
    ow = ' a ' + ow

print("You can get it " + verbs[0])
print("You can get it " + verb2)
print("You can get it " + verbs[1] + ow)
print("Matter of fact I've got it now")

