"""
Charachters project for coding dojo
"""
# pylint: disable=c0103
import random

headscount = 0
tailscount = 0
for x in range(1, 5001):
    flip = random.randint(1, 2)
    if flip > 1:
        attempt = "tail"
        tailscount = tailscount + 1
    elif flip < 2:
        attempt = "head"
        headscount = headscount + 1
    print "Attempt #", str(x) + ":  Throwing a coin... It's a " +  attempt + "!  ..."
    print "Got", str(headscount)+ "head(s) so far and", str(tailscount) + "tail(s) so far"
