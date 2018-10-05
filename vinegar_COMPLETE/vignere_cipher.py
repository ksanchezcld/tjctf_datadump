#!/usr/bin/env python

import itertools
import string
import collections
from hashlib import sha256


lowercase = collections.deque( string.ascii_lowercase + string.digits ) 

# message = 'uucbx{simbjyaqyvzbzfdatshktkbde}'
# key = 'Kkkkk kkkkKkkkkkkkkKkkkkkkkkKkk'

# I removed the curly braces and spaces in this case
message = 'uucbxsimbjyaqyvzbzfdatshktkbde'
key = 'KkkkkkkkkKkkkkkkkkKkkkkkkkkKkk'



def encrypt( message, key, multipler = -1 ):

	compressed_message = message.lower()

	for punctuation in str(string.punctuation + ' '):
		compressed_message = compressed_message.replace(punctuation, '')
	cycler = itertools.cycle(key.lower())

	long_key = ''.join( [ cycler.next() for _ in range(len(compressed_message))] )

	coded = []
	for number in range(len(long_key)):
		
		cipher_letter = compressed_message[number]
		key_letter = long_key[number]
		key_index = string.ascii_lowercase.index(key_letter)
		cipher_index = string.ascii_lowercase.index(cipher_letter)

		lowercase = collections.deque( string.ascii_lowercase ) 
		lowercase.rotate( multipler * key_index )
		new_alphabet = ''.join(list(lowercase))
		new_character = new_alphabet[cipher_index]
		coded.append( new_character )

	return ''.join(coded)

def decrypt( message, key, multipler = -1 ):

	return encrypt( message, key, 1 )



# message = 'uucbxsimbjyaqyvzbzfdatshktkbde'
# key = 'KkkkkkkkkKkkkkkkkkKkkkkkkkkKkk'

# print decrypt(message, 'blais')

for p in itertools.permutations(string.lowercase, 4):
	key = "".join(p)
	key = "blais" + key
	
	plain = decrypt(message, key)
	
	flag = plain[:5] + '{' + plain[5:] + '}'
	print flag

	s = sha256()
	s.update(flag)
	if s.hexdigest() == '8304c5fa4186bbce7ac030d068fdd485040e65bf824ee70b0bdbac03862bec93':
		print "WE GOT IT!!!",
		print "key", key
		print "flag", flag
		exit()

	# tjctf{rxmtrxpqqdyqzxlziszsszbvm}