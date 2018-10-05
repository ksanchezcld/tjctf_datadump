#!/usr/bin/env python

# nc problem1.tjctf.org 8001

from pwn import *

s = remote('problem1.tjctf.org', 8001)

print s.recv()
while 1:
    print s.recv()
    s.sendline('1'*100)

s.close()