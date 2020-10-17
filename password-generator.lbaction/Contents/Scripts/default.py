#!/usr/bin/env python

import sys
import json
from random import seed
from random import randint
from xkcdpass import xkcd_password as xp

try:
    numwords = sys.argv[1]
except IndexError as e:
    sys.exit()

# create a wordlist from the default wordfile
# use words between 5 and 8 letters long
wordfile = xp.locate_wordfile()
mywords = xp.generate_wordlist(wordfile=wordfile, min_length=5, max_length=8)
pswd = xp.generate_xkcdpassword(mywords, numwords=int(numwords), delimiter="-")

# seed random number generator
# seed(1)

uppercased_char = pswd[0].upper()
pswd = uppercased_char + pswd[1:]
pswd = pswd + str(randint(0, 9))

item = {}
item["title"] = pswd
item["subtitle"] = "Length: {}".format(len(pswd))
item["actionRunsInBackground"] = True
item["actionReturnsItems"] = False
item["actionArgument"] = pswd
item["action"] = "paste.sh"
print(json.dumps([item]))
