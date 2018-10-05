#!/usr/bin/env python

from requests import *

s = Session()
print s.get('https://cookie_monster.tjctf.org/').text
print s.cookies