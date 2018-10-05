#!/usr/bin/env python

import string
import itertools


# flag length is 28
encrypted = '473c23192d4737025b3b2d34175f66421631250711461a7905342a3e365d08190215152f1f1e3d5c550c12521f55217e500a3714787b6554'

message = "tjctf{" + 'x'*21 + "}"
# key = "3V@mK<"
# message = "tj"
key = "3V@mK<"
# first_part_of_key = '3V@mK<'

def encrypt(message,key):

    length_of_key = len(key);
    segments = [ message[i::length_of_key] for i in range(length_of_key) ]
 
    for i in range(length_of_key):
  
        a = 0
        encrypted = ""

        for c in segments[i]:

            a = ord(c) ^ ord(key[i])^(a>>2)
            encrypted += chr(a)

        segments[i]=encrypted

    return "".join(hex((256)+ord(f))[3:] for f in "".join( "".join(y) for y in zip(*segments) ) )

def decrypt(ciphertext, key):
    pass

it = list('3V@mK<')
for i in string.printable:
    # new = encrypt(message,''.join(i))
    new = encrypt(message, ''.join(it)+ i)
    if encrypted.startswith(new):
        print new, ''.join(it)+ i



print(encrypt(message,key))


# 473c23192d4737025b3b2d34175f66421631250711461a7905342a3e365d08190215152f1f1e3d5c550c12521f55217e500a3714787b6554