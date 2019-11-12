#!/usr/bin/env python

# random-strings.py
# Generate n number of words containing m number of letters from a set of characters.

import os
import string
import random

random.seed = (os.urandom(1024))
chars = string.ascii_letters + string.punctuation + string.digits

for i in range(1, 10):
    letters = random.choices(chars, k = 32)
    print("".join(letters))
