#!/usr/bin/env python

import requests
from random import choice
from string import letters, digits

url = 'https://stupid_blog.tjctf.org/'


s = requests.Session()

username = "".join( [ choice(letters+digits) for _ in range(5) ] )
print username
password = username

r = s.post(url+'/register', data = {"username": username, "password" : password})
r = s.post(url+'/login', data = {"username": username, "password" : password})
print r.text



s.close()