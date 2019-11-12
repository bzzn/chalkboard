#!/usr/bin/env python

# random-words.py
# Generate n number of lists containing m number of words from a list.

import os
import string
import random
import json

filename = 'ogdens-basic-english-words.json'
lines = json.loads(open(filename).read())
random.seed = (os.urandom(1024))

for i in range(1, 10):
    words = random.choices(lines, k = 5)
    print(" ".join(words))
